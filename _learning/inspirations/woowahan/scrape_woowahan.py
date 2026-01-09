"""
우아한형제들 기술블로그 스크래핑
https://techblog.woowahan.com/22839/

블로그 글 전체 내용 수집
"""

import asyncio
from playwright.async_api import async_playwright
from pathlib import Path
import json
from datetime import datetime
import re

OUTPUT_DIR = Path(__file__).parent
SCREENSHOTS_DIR = OUTPUT_DIR / "screenshots"


async def scrape_woowahan_blog():
    """우아한형제들 블로그 스크래핑"""
    SCREENSHOTS_DIR.mkdir(exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            locale="ko-KR",
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = await context.new_page()

        url = "https://techblog.woowahan.com/22839/"
        print(f"1. 페이지 접속: {url}")

        await page.goto(url, wait_until="networkidle")
        await page.wait_for_timeout(3000)

        # 전체 페이지 스크린샷
        await page.screenshot(path=str(SCREENSHOTS_DIR / "full_page.png"), full_page=True)
        print("   스크린샷 저장 완료")

        # 2. 메타 정보 추출
        print("2. 메타 정보 추출...")

        # 제목
        title = await page.query_selector("h1.post-title, h1.entry-title, article h1, .post-header h1")
        title_text = await title.inner_text() if title else "제목 없음"

        # 날짜
        date_elem = await page.query_selector("time, .post-date, .entry-date, .date")
        date_text = ""
        if date_elem:
            date_text = await date_elem.get_attribute("datetime") or await date_elem.inner_text()

        # 작성자
        author_elem = await page.query_selector(".author, .post-author, .writer, .byline")
        author_text = await author_elem.inner_text() if author_elem else ""

        # 카테고리/태그
        tags = await page.query_selector_all(".tag, .category, .post-tag, .entry-tag a")
        tag_texts = [await tag.inner_text() for tag in tags]

        print(f"   제목: {title_text}")
        print(f"   날짜: {date_text}")
        print(f"   작성자: {author_text}")

        # 3. 본문 추출
        print("3. 본문 추출...")

        # 본문 컨테이너 찾기
        content_selectors = [
            "article .post-content",
            "article .entry-content",
            ".post-body",
            ".article-content",
            "article",
            ".content"
        ]

        content_elem = None
        for selector in content_selectors:
            content_elem = await page.query_selector(selector)
            if content_elem:
                break

        # HTML 본문
        content_html = await content_elem.inner_html() if content_elem else ""

        # 텍스트 본문 (구조 유지)
        content_text = await content_elem.inner_text() if content_elem else ""

        # 4. 구조화된 콘텐츠 추출
        print("4. 구조화된 콘텐츠 추출...")

        sections = []

        # 헤딩 추출
        headings = await page.query_selector_all("article h1, article h2, article h3, article h4")
        for h in headings:
            tag = await h.evaluate("el => el.tagName")
            text = await h.inner_text()
            sections.append({"type": "heading", "level": tag, "text": text.strip()})

        # 코드 블록 추출
        code_blocks = await page.query_selector_all("pre, code, .highlight")
        codes = []
        for i, code in enumerate(code_blocks):
            code_text = await code.inner_text()
            # 언어 감지 시도
            class_attr = await code.get_attribute("class") or ""
            lang_match = re.search(r'language-(\w+)', class_attr)
            lang = lang_match.group(1) if lang_match else ""
            if code_text.strip():
                codes.append({"index": i, "language": lang, "code": code_text.strip()})

        # 이미지 추출
        images = await page.query_selector_all("article img")
        image_list = []
        for i, img in enumerate(images):
            src = await img.get_attribute("src") or ""
            alt = await img.get_attribute("alt") or ""
            if src:
                image_list.append({"index": i, "src": src, "alt": alt})

        # 링크 추출
        links = await page.query_selector_all("article a")
        link_list = []
        for link in links:
            href = await link.get_attribute("href") or ""
            text = await link.inner_text()
            if href and text.strip():
                link_list.append({"text": text.strip(), "href": href})

        # 5. 마크다운 변환
        print("5. 마크다운 생성...")

        markdown = generate_markdown(
            title=title_text,
            date=date_text,
            author=author_text,
            tags=tag_texts,
            content_text=content_text,
            codes=codes,
            images=image_list,
            links=link_list
        )

        # 6. 결과 저장
        print("6. 결과 저장...")

        # JSON 저장
        result = {
            "url": url,
            "scraped_at": datetime.now().isoformat(),
            "title": title_text,
            "date": date_text,
            "author": author_text,
            "tags": tag_texts,
            "content_text": content_text,
            "content_html": content_html,
            "code_blocks": codes,
            "images": image_list,
            "links": link_list
        }

        with open(OUTPUT_DIR / "raw_data.json", "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)

        # 마크다운 저장
        with open(OUTPUT_DIR / "article.md", "w", encoding="utf-8") as f:
            f.write(markdown)

        # HTML 저장 (원본)
        with open(OUTPUT_DIR / "article.html", "w", encoding="utf-8") as f:
            f.write(content_html)

        print(f"\n완료!")
        print(f"  - {OUTPUT_DIR / 'article.md'}")
        print(f"  - {OUTPUT_DIR / 'raw_data.json'}")
        print(f"  - {OUTPUT_DIR / 'article.html'}")
        print(f"  - {SCREENSHOTS_DIR / 'full_page.png'}")

        await browser.close()
        return result


def generate_markdown(title, date, author, tags, content_text, codes, images, links):
    """수집된 데이터를 마크다운으로 변환"""

    md = f"""# {title}

> **원문**: https://techblog.woowahan.com/22839/
> **작성일**: {date}
> **작성자**: {author}
> **태그**: {', '.join(tags) if tags else '없음'}

---

## 본문

{content_text}

---

## 코드 블록 목록

"""

    for code in codes:
        lang = code.get('language', '')
        md += f"""
### 코드 #{code['index'] + 1} {f'({lang})' if lang else ''}

```{lang}
{code['code']}
```

"""

    md += """
---

## 이미지 목록

"""
    for img in images:
        md += f"- ![{img['alt']}]({img['src']})\n"
        if img['alt']:
            md += f"  - 설명: {img['alt']}\n"

    md += """
---

## 참조 링크

"""
    for link in links:
        md += f"- [{link['text']}]({link['href']})\n"

    return md


if __name__ == "__main__":
    asyncio.run(scrape_woowahan_blog())
