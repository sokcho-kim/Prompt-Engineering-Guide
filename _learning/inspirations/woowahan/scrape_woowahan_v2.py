"""
우아한형제들 기술블로그 스크래핑 v2
https://techblog.woowahan.com/22839/

이미지, 링크, 구조 개선 버전
"""

import asyncio
from playwright.async_api import async_playwright
from pathlib import Path
import json
from datetime import datetime
import re

OUTPUT_DIR = Path(__file__).parent
SCREENSHOTS_DIR = OUTPUT_DIR / "screenshots"
IMAGES_DIR = OUTPUT_DIR / "images"


async def scrape_woowahan_blog_v2():
    """우아한형제들 블로그 스크래핑 v2"""
    SCREENSHOTS_DIR.mkdir(exist_ok=True)
    IMAGES_DIR.mkdir(exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            locale="ko-KR",
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = await context.new_page()

        url = "https://techblog.woowahan.com/22839/"
        print(f"1. 페이지 접속: {url}")

        await page.goto(url, wait_until="networkidle")
        await page.wait_for_timeout(3000)

        # 스크린샷
        await page.screenshot(path=str(SCREENSHOTS_DIR / "full_page.png"), full_page=True)

        # 2. 메타 정보
        print("2. 메타 정보 추출...")

        title = await page.locator("h1").first.inner_text()

        # 날짜와 작성자 추출
        date_author = await page.locator(".date, .author, time, .post-meta").all_inner_texts()
        date_text = ""
        author_text = ""
        for item in date_author:
            if re.search(r'\d{4}', item):
                date_text = item.strip()
            elif item.strip() and not re.search(r'\d{4}', item):
                author_text = item.strip()

        # 본문에서 날짜/작성자 찾기
        body_text = await page.locator("article, .post-content, .entry-content").first.inner_text()
        date_match = re.search(r'(\d{4}\.\s*\d{2}\.\s*\d{2}\.?)', body_text)
        if date_match:
            date_text = date_match.group(1)

        # 작성자 (보통 날짜 다음 줄)
        lines = body_text.split('\n')
        for i, line in enumerate(lines):
            if date_text and date_text.replace(' ', '') in line.replace(' ', ''):
                if i + 1 < len(lines) and len(lines[i+1].strip()) < 20:
                    author_text = lines[i+1].strip()
                    break

        print(f"   제목: {title}")
        print(f"   날짜: {date_text}")
        print(f"   작성자: {author_text}")

        # 3. 이미지 다운로드
        print("3. 이미지 추출...")

        images = await page.locator("article img, .post-content img, .entry-content img").all()
        image_list = []

        for i, img in enumerate(images):
            try:
                src = await img.get_attribute("src")
                alt = await img.get_attribute("alt") or ""

                if src and not src.startswith("data:"):
                    # 상대 경로 처리
                    if src.startswith("/"):
                        src = f"https://techblog.woowahan.com{src}"

                    image_list.append({
                        "index": i + 1,
                        "src": src,
                        "alt": alt,
                        "filename": f"img_{i+1:02d}.png"
                    })
                    print(f"   이미지 {i+1}: {alt or src[:50]}")
            except:
                continue

        # 4. 링크 추출
        print("4. 링크 추출...")

        links = await page.locator("article a, .post-content a").all()
        link_list = []
        seen_hrefs = set()

        for link in links:
            try:
                href = await link.get_attribute("href")
                text = await link.inner_text()

                if href and text.strip() and href not in seen_hrefs:
                    if not href.startswith("#") and not href.startswith("javascript"):
                        seen_hrefs.add(href)
                        link_list.append({
                            "text": text.strip()[:100],
                            "href": href
                        })
            except:
                continue

        print(f"   링크 {len(link_list)}개 추출")

        # 5. 본문 구조화
        print("5. 본문 구조화...")

        # 섹션별로 분리
        content_html = await page.locator("article, .post-content, .entry-content").first.inner_html()

        # 마크다운 생성
        markdown = await generate_clean_markdown(
            page=page,
            title=title,
            date=date_text,
            author=author_text,
            url=url,
            images=image_list,
            links=link_list
        )

        # 6. 저장
        print("6. 저장...")

        # 마크다운
        with open(OUTPUT_DIR / "article.md", "w", encoding="utf-8") as f:
            f.write(markdown)

        # JSON
        result = {
            "url": url,
            "scraped_at": datetime.now().isoformat(),
            "title": title,
            "date": date_text,
            "author": author_text,
            "images": image_list,
            "links": link_list,
            "image_count": len(image_list),
            "link_count": len(link_list)
        }

        with open(OUTPUT_DIR / "metadata.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        print(f"\n완료!")
        print(f"  - article.md (본문)")
        print(f"  - metadata.json (메타데이터)")
        print(f"  - 이미지 {len(image_list)}개")
        print(f"  - 링크 {len(link_list)}개")

        await browser.close()
        return result


async def generate_clean_markdown(page, title, date, author, url, images, links):
    """깔끔한 마크다운 생성"""

    # 본문의 각 섹션 추출
    sections = []

    # 헤딩들 추출
    headings = await page.locator("article h2, article h3, article h4").all()

    for h in headings:
        tag = await h.evaluate("el => el.tagName")
        text = await h.inner_text()
        level = int(tag[1])  # H2 -> 2
        sections.append({"level": level, "text": text.strip()})

    # 본문 텍스트
    body = await page.locator("article, .post-content").first.inner_text()

    # 불필요한 부분 제거
    body = re.sub(r'^.*?AI 기술은 빠르게 진화하고 있습니다\.', 'AI 기술은 빠르게 진화하고 있습니다.', body, flags=re.DOTALL)

    # 하단 네비게이션 제거
    body = re.sub(r'목록으로 돌아가기.*$', '', body, flags=re.DOTALL)

    md = f"""# {title}

> **원문**: {url}
> **작성일**: {date}
> **작성자**: {author}
> **스크래핑**: {datetime.now().strftime('%Y-%m-%d')}

---

## 목차

"""

    # 목차 생성
    for sec in sections:
        indent = "  " * (sec["level"] - 2)
        md += f"{indent}- [{sec['text']}](#{sec['text'].lower().replace(' ', '-').replace('.', '')})\n"

    md += f"""
---

## 본문

{body}

---

## 이미지 목록 ({len(images)}개)

| # | 설명 | URL |
|---|------|-----|
"""

    for img in images:
        alt = img['alt'][:50] if img['alt'] else '(설명 없음)'
        md += f"| {img['index']} | {alt} | [링크]({img['src']}) |\n"

    md += f"""
---

## 참조 링크 ({len(links)}개)

"""

    for link in links:
        md += f"- [{link['text']}]({link['href']})\n"

    return md


if __name__ == "__main__":
    asyncio.run(scrape_woowahan_blog_v2())
