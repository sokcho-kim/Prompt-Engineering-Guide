"""
The Prompt Test 사이트 스크래핑
https://test.the-prompt.me/test

스크린샷 + 페이지 구조 분석
"""

import asyncio
from playwright.async_api import async_playwright
from pathlib import Path
import json
from datetime import datetime

OUTPUT_DIR = Path(__file__).parent
SCREENSHOTS_DIR = OUTPUT_DIR / "screenshots"


async def scrape_the_prompt_test():
    """메인 스크래핑 함수"""
    SCREENSHOTS_DIR.mkdir(exist_ok=True)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # headless=False로 브라우저 보이게
        context = await browser.new_context(
            viewport={"width": 1920, "height": 1080},
            locale="ko-KR"
        )
        page = await context.new_page()

        results = {
            "url": "https://test.the-prompt.me/test",
            "scraped_at": datetime.now().isoformat(),
            "screenshots": [],
            "page_structure": {},
            "ui_elements": []
        }

        # 1. 메인 페이지 접속
        print("1. 메인 페이지 접속...")
        await page.goto("https://test.the-prompt.me/test", wait_until="networkidle")
        await page.wait_for_timeout(2000)  # 로딩 대기

        # 전체 페이지 스크린샷
        screenshot_path = SCREENSHOTS_DIR / "01_main_page.png"
        await page.screenshot(path=str(screenshot_path), full_page=True)
        results["screenshots"].append(str(screenshot_path))
        print(f"   스크린샷 저장: {screenshot_path}")

        # 2. 페이지 구조 분석
        print("2. 페이지 구조 분석...")

        # 네비게이션 메뉴 추출
        nav_items = await page.query_selector_all("nav a, header a")
        nav_texts = []
        for item in nav_items:
            text = await item.inner_text()
            href = await item.get_attribute("href")
            if text.strip():
                nav_texts.append({"text": text.strip(), "href": href})
        results["page_structure"]["navigation"] = nav_texts

        # 버튼 추출
        buttons = await page.query_selector_all("button")
        button_texts = []
        for btn in buttons:
            text = await btn.inner_text()
            if text.strip():
                button_texts.append(text.strip())
        results["ui_elements"].append({"type": "buttons", "items": button_texts})

        # 입력 필드 추출
        inputs = await page.query_selector_all("input, textarea, select")
        input_info = []
        for inp in inputs:
            tag = await inp.evaluate("el => el.tagName")
            placeholder = await inp.get_attribute("placeholder") or ""
            name = await inp.get_attribute("name") or ""
            input_type = await inp.get_attribute("type") or ""
            input_info.append({
                "tag": tag,
                "type": input_type,
                "name": name,
                "placeholder": placeholder
            })
        results["ui_elements"].append({"type": "inputs", "items": input_info})

        # 3. 주요 섹션별 스크린샷
        print("3. 주요 섹션 스크린샷...")

        # 모델 선택 영역 찾기
        try:
            model_selector = await page.query_selector("[class*='model'], [class*='select']")
            if model_selector:
                await model_selector.screenshot(path=str(SCREENSHOTS_DIR / "02_model_selector.png"))
                results["screenshots"].append(str(SCREENSHOTS_DIR / "02_model_selector.png"))
        except Exception as e:
            print(f"   모델 선택 영역 캡처 실패: {e}")

        # 4. 인터랙티브 요소 테스트
        print("4. 인터랙티브 요소 탐색...")

        # 드롭다운/셀렉트 박스 옵션 추출
        selects = await page.query_selector_all("select")
        select_options = []
        for sel in selects:
            options = await sel.query_selector_all("option")
            opts = []
            for opt in options:
                text = await opt.inner_text()
                value = await opt.get_attribute("value")
                opts.append({"text": text, "value": value})
            if opts:
                select_options.append(opts)
        results["ui_elements"].append({"type": "select_options", "items": select_options})

        # 5. 텍스트 콘텐츠 추출
        print("5. 텍스트 콘텐츠 추출...")

        # 라벨, 헤딩 추출
        headings = await page.query_selector_all("h1, h2, h3, h4, label")
        heading_texts = []
        for h in headings:
            text = await h.inner_text()
            tag = await h.evaluate("el => el.tagName")
            if text.strip():
                heading_texts.append({"tag": tag, "text": text.strip()})
        results["page_structure"]["headings"] = heading_texts

        # 6. 스크롤하면서 추가 스크린샷
        print("6. 스크롤 스크린샷...")

        # 페이지 높이 확인
        page_height = await page.evaluate("document.body.scrollHeight")
        viewport_height = 1080

        scroll_count = 0
        current_scroll = 0
        while current_scroll < page_height and scroll_count < 5:
            current_scroll += viewport_height
            await page.evaluate(f"window.scrollTo(0, {current_scroll})")
            await page.wait_for_timeout(500)

            screenshot_path = SCREENSHOTS_DIR / f"scroll_{scroll_count + 1}.png"
            await page.screenshot(path=str(screenshot_path))
            results["screenshots"].append(str(screenshot_path))
            scroll_count += 1

        # 맨 위로 스크롤
        await page.evaluate("window.scrollTo(0, 0)")

        # 7. 결과 저장
        print("7. 결과 저장...")

        with open(OUTPUT_DIR / "analysis_result.json", "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)

        # 요약 마크다운 생성
        summary = generate_summary(results)
        with open(OUTPUT_DIR / "ANALYSIS_SUMMARY.md", "w", encoding="utf-8") as f:
            f.write(summary)

        print(f"\n완료! 결과 저장됨:")
        print(f"  - {OUTPUT_DIR / 'analysis_result.json'}")
        print(f"  - {OUTPUT_DIR / 'ANALYSIS_SUMMARY.md'}")
        print(f"  - 스크린샷: {SCREENSHOTS_DIR}")

        await browser.close()

        return results


def generate_summary(results: dict) -> str:
    """분석 결과를 마크다운으로 정리"""
    md = f"""# The Prompt Test 사이트 분석

> 스크래핑 일시: {results['scraped_at']}
> URL: {results['url']}

## 1. 네비게이션 구조

| 메뉴 | 링크 |
|------|------|
"""
    for nav in results.get("page_structure", {}).get("navigation", []):
        md += f"| {nav['text']} | {nav['href']} |\n"

    md += """
## 2. 주요 UI 요소

### 버튼
"""
    for elem in results.get("ui_elements", []):
        if elem["type"] == "buttons":
            for btn in elem["items"]:
                md += f"- {btn}\n"

    md += """
### 입력 필드
"""
    for elem in results.get("ui_elements", []):
        if elem["type"] == "inputs":
            for inp in elem["items"]:
                md += f"- `{inp['tag']}` (type: {inp['type']}, name: {inp['name']})\n"

    md += """
### 헤딩/라벨
"""
    for h in results.get("page_structure", {}).get("headings", []):
        md += f"- **{h['tag']}**: {h['text']}\n"

    md += f"""
## 3. 스크린샷

총 {len(results.get('screenshots', []))}개 캡처됨

"""
    for ss in results.get("screenshots", []):
        md += f"- `{Path(ss).name}`\n"

    md += """
## 4. 기능 분석

(스크린샷 확인 후 수동 분석 필요)

### 추정 기능
1. 프롬프트 작성 및 테스트
2. 다중 모델 비교
3. 파라미터 조정 (Temperature, Max Tokens 등)
4. 템플릿 관리
5. 실행 로그 확인
"""

    return md


if __name__ == "__main__":
    asyncio.run(scrape_the_prompt_test())
