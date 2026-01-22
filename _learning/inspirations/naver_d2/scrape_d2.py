import asyncio
import json
import os
import re
from datetime import datetime
from pathlib import Path
from playwright.async_api import async_playwright
import httpx

BASE_DIR = Path(__file__).parent
IMAGES_DIR = BASE_DIR / "images"
IMAGES_DIR.mkdir(exist_ok=True)

URL = "https://d2.naver.com/helloworld/3344073"
BASE_URL = "https://d2.naver.com"


async def download_image(url: str, filename: str):
    """이미지 다운로드"""
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, follow_redirects=True)
            if response.status_code == 200:
                filepath = IMAGES_DIR / filename
                filepath.write_bytes(response.content)
                print(f"  Downloaded: {filename}")
                return True
    except Exception as e:
        print(f"  Failed to download {url}: {e}")
    return False


async def scrape_d2():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print(f"Navigating to {URL}...")
        await page.goto(URL, wait_until="networkidle")
        await page.wait_for_timeout(3000)

        # HTML 저장
        html_content = await page.content()
        (BASE_DIR / "article.html").write_text(html_content, encoding="utf-8")
        print("Saved article.html")

        # D2 특화 셀렉터로 메타 정보 추출
        meta_info = await page.evaluate("""
            () => {
                const result = {
                    title: '',
                    author: '',
                    date: '',
                    views: ''
                };

                // 제목: .posting_tit
                const titleEl = document.querySelector('.posting_tit, h1.posting_tit');
                if (titleEl) result.title = titleEl.innerText.trim();

                // 날짜: .post_info dd (첫번째)
                const dateEl = document.querySelector('.post_info dd');
                if (dateEl) result.date = dateEl.innerText.trim();

                // 조회수
                const infoItems = document.querySelectorAll('.post_info dd');
                if (infoItems.length >= 3) {
                    result.views = infoItems[2].innerText.trim();
                }

                return result;
            }
        """)

        print(f"Title: {meta_info['title']}")
        print(f"Date: {meta_info['date']}")

        # 이미지 정보 추출 (con_view 내부)
        images = await page.evaluate("""
            () => {
                const imgs = document.querySelectorAll('.con_view img');
                return Array.from(imgs).map((img, i) => ({
                    index: i + 1,
                    src: img.src,
                    alt: img.alt || ''
                }));
            }
        """)

        # 링크 정보 추출
        links = await page.evaluate("""
            () => {
                const anchors = document.querySelectorAll('.con_view a');
                return Array.from(anchors).map(a => ({
                    text: a.innerText.trim(),
                    href: a.href
                })).filter(l => l.text && l.href && !l.href.startsWith('javascript'));
            }
        """)

        # 마크다운 변환
        markdown_content = await page.evaluate("""
            () => {
                const conView = document.querySelector('.con_view');
                if (!conView) return '';

                let md = '';

                function processNode(node, depth = 0) {
                    if (node.nodeType === Node.TEXT_NODE) {
                        return node.textContent;
                    }

                    if (node.nodeType !== Node.ELEMENT_NODE) return '';

                    const tag = node.tagName.toLowerCase();
                    let content = '';

                    // 재귀적으로 자식 노드 처리
                    for (const child of node.childNodes) {
                        content += processNode(child, depth);
                    }

                    switch(tag) {
                        case 'h1': return '\\n# ' + content.trim() + '\\n\\n';
                        case 'h2': return '\\n## ' + content.trim() + '\\n\\n';
                        case 'h3': return '\\n### ' + content.trim() + '\\n\\n';
                        case 'h4': return '\\n#### ' + content.trim() + '\\n\\n';
                        case 'h5': return '\\n##### ' + content.trim() + '\\n\\n';
                        case 'h6': return '\\n###### ' + content.trim() + '\\n\\n';
                        case 'p': return content.trim() + '\\n\\n';
                        case 'br': return '\\n';
                        case 'strong':
                        case 'b': return '**' + content.trim() + '**';
                        case 'em':
                        case 'i': return '*' + content.trim() + '*';
                        case 'code':
                            if (node.parentElement && node.parentElement.tagName.toLowerCase() === 'pre') {
                                return content;
                            }
                            return '`' + content.trim() + '`';
                        case 'pre': return '\\n```\\n' + content.trim() + '\\n```\\n\\n';
                        case 'blockquote': return '\\n> ' + content.trim().replace(/\\n/g, '\\n> ') + '\\n\\n';
                        case 'ul': return '\\n' + content + '\\n';
                        case 'ol': return '\\n' + content + '\\n';
                        case 'li':
                            const parent = node.parentElement;
                            if (parent && parent.tagName.toLowerCase() === 'ol') {
                                const index = Array.from(parent.children).indexOf(node) + 1;
                                return index + '. ' + content.trim() + '\\n';
                            }
                            return '- ' + content.trim() + '\\n';
                        case 'a':
                            const href = node.getAttribute('href');
                            return '[' + content.trim() + '](' + href + ')';
                        case 'img':
                            const src = node.getAttribute('src');
                            const alt = node.getAttribute('alt') || 'image';
                            return '\\n![' + alt + '](' + src + ')\\n\\n';
                        default:
                            return content;
                    }
                }

                return processNode(conView);
            }
        """)

        # 이미지 다운로드
        print(f"\nDownloading {len(images)} images...")
        for img in images:
            src = img['src']
            # 상대 경로면 절대 경로로 변환
            if src.startswith('/'):
                src = BASE_URL + src

            ext = src.split('.')[-1].split('?')[0]
            if ext not in ['png', 'jpg', 'jpeg', 'gif', 'webp', 'svg']:
                ext = 'png'
            filename = f"img_{img['index']:02d}.{ext}"
            img['filename'] = filename
            img['original_src'] = img['src']
            img['src'] = src
            await download_image(src, filename)

        # 메타데이터 저장
        metadata = {
            "url": URL,
            "scraped_at": datetime.now().isoformat(),
            "title": meta_info.get('title', ''),
            "date": meta_info.get('date', ''),
            "author": "박슬기",
            "team": "네이버 Business Analytics",
            "views": meta_info.get('views', ''),
            "images": images,
            "links": links,
            "image_count": len(images),
            "link_count": len(links)
        }

        (BASE_DIR / "metadata.json").write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )
        print("Saved metadata.json")

        # 이미지 경로를 로컬 경로로 변환한 마크다운
        md_local = markdown_content
        for img in images:
            if img.get('original_src'):
                md_local = md_local.replace(img['original_src'], f"./images/{img['filename']}")
            if img.get('src'):
                md_local = md_local.replace(img['src'], f"./images/{img['filename']}")

        # 마크다운 파일 저장
        md_content = f"""# {metadata['title']}

> **Source:** {URL}
> **Author:** {metadata['author']} | {metadata['team']}
> **Date:** {metadata['date']}
> **Views:** {metadata['views']}

---

{md_local}
"""

        (BASE_DIR / "article.md").write_text(md_content, encoding="utf-8")
        print("Saved article.md")

        await browser.close()
        print(f"\nScraping completed! {len(images)} images, {len(links)} links")


if __name__ == "__main__":
    asyncio.run(scrape_d2())
