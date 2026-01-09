"""
지능형 PDF 파서 (pdfplumber 기반)
=================================
1단계: pdfplumber로 텍스트 추출 (한글 띄어쓰기 유지)
2단계: OCR 필요 페이지 기록
3단계: Upstage Document AI로 OCR (선택적)

사용법:
    # 분석만
    python intelligent_pdf_parser.py --input <pdf_path_or_dir> --output <output_dir> --analyze-only

    # 무료 파싱만 (OCR 없이)
    python intelligent_pdf_parser.py --input <pdf_path_or_dir> --output <output_dir>

    # OCR 포함 파싱
    python intelligent_pdf_parser.py --input <pdf_path_or_dir> --output <output_dir> --with-ocr
"""

import os
import sys
import json
import argparse
import re
from pathlib import Path
from datetime import datetime
from typing import Optional
from dataclasses import dataclass, asdict, field

import pdfplumber
import fitz  # PyMuPDF - 이미지 변환용

# .env 파일 로드
try:
    from dotenv import load_dotenv
    # 스크립트 위치 기준으로 .env 찾기
    script_dir = Path(__file__).parent.parent
    env_path = script_dir / "experiments" / ".env"
    if env_path.exists():
        load_dotenv(env_path)
except ImportError:
    pass  # dotenv 없으면 환경변수만 사용

# Upstage는 필요할 때만 import
try:
    import httpx
    HTTPX_AVAILABLE = True
except ImportError:
    HTTPX_AVAILABLE = False


@dataclass
class PageResult:
    """페이지 파싱 결과"""
    page_num: int
    text: str
    char_count: int
    word_count: int
    needs_ocr: bool
    ocr_status: str = "not_needed"  # not_needed | pending | success | failed


@dataclass
class PDFResult:
    """PDF 파싱 결과"""
    filename: str
    total_pages: int
    pages_with_text: int
    pages_needing_ocr: int
    ocr_page_numbers: list
    pages: list = field(default_factory=list)


# 설정
MIN_CHARS_THRESHOLD = 50  # 이 이하면 OCR 필요로 판단
MIN_WORDS_THRESHOLD = 10  # 단어 수 기준


def parse_pdf_with_pdfplumber(pdf_path: Path) -> PDFResult:
    """pdfplumber로 PDF 파싱 (1단계: 무료 추출)"""
    pages = []
    pages_with_text = 0
    ocr_needed = []

    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages, 1):
            text = page.extract_text() or ""
            text = text.strip()

            # 공백 정리 (여러 공백 → 단일 공백)
            clean_text = re.sub(r'\s+', ' ', text).strip()
            char_count = len(clean_text)
            word_count = len(clean_text.split()) if clean_text else 0

            # OCR 필요 여부 판단
            needs_ocr = char_count < MIN_CHARS_THRESHOLD or word_count < MIN_WORDS_THRESHOLD

            if not needs_ocr:
                pages_with_text += 1
                ocr_status = "not_needed"
            else:
                ocr_needed.append(i)
                ocr_status = "pending"

            pages.append(PageResult(
                page_num=i,
                text=text,
                char_count=char_count,
                word_count=word_count,
                needs_ocr=needs_ocr,
                ocr_status=ocr_status
            ))

    return PDFResult(
        filename=pdf_path.name,
        total_pages=len(pages),
        pages_with_text=pages_with_text,
        pages_needing_ocr=len(ocr_needed),
        ocr_page_numbers=ocr_needed,
        pages=pages
    )


def extract_page_as_image(pdf_path: Path, page_num: int) -> bytes:
    """특정 페이지를 이미지로 변환 (PyMuPDF 사용)"""
    doc = fitz.open(pdf_path)
    page = doc[page_num - 1]  # 0-based

    # 고해상도 이미지로 변환
    mat = fitz.Matrix(2, 2)  # 2x 스케일
    pix = page.get_pixmap(matrix=mat)
    img_bytes = pix.tobytes("png")

    doc.close()
    return img_bytes


def ocr_with_upstage(image_bytes: bytes, api_key: str) -> str:
    """Upstage Document AI로 OCR 수행"""
    if not HTTPX_AVAILABLE:
        raise ImportError("httpx 라이브러리가 필요합니다: pip install httpx")

    url = "https://api.upstage.ai/v1/document-ai/ocr"
    headers = {"Authorization": f"Bearer {api_key}"}

    files = {"document": ("page.png", image_bytes, "image/png")}

    with httpx.Client(timeout=60.0) as client:
        response = client.post(url, headers=headers, files=files)
        response.raise_for_status()
        result = response.json()

    # 텍스트 추출
    if "text" in result:
        return result["text"]
    elif "pages" in result:
        texts = []
        for page in result["pages"]:
            if "text" in page:
                texts.append(page["text"])
        return "\n".join(texts)

    return ""


def save_to_markdown(result: PDFResult, output_dir: Path) -> Path:
    """파싱 결과를 마크다운으로 저장"""
    output_dir.mkdir(parents=True, exist_ok=True)

    # 파일명 정리
    safe_name = re.sub(r'[^\w가-힣\s\-]', '', Path(result.filename).stem)
    safe_name = re.sub(r'\s+', '_', safe_name).strip('_')

    md_path = output_dir / f"{safe_name}.md"

    # 마크다운 작성
    lines = [
        f"# {Path(result.filename).stem}",
        "",
        f"> 파싱 일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"> 총 페이지: {result.total_pages}",
        f"> 텍스트 추출 성공: {result.pages_with_text}",
        f"> OCR 필요: {result.pages_needing_ocr}",
        "",
        "---",
        ""
    ]

    for page in result.pages:
        if page.text and not page.needs_ocr:
            lines.append(f"## 페이지 {page.page_num}")
            lines.append("")
            lines.append(page.text)
            lines.append("")
            lines.append("---")
            lines.append("")
        elif page.needs_ocr:
            if page.ocr_status == "success":
                lines.append(f"## 페이지 {page.page_num} (OCR)")
                lines.append("")
                lines.append(page.text)
                lines.append("")
                lines.append("---")
                lines.append("")
            else:
                lines.append(f"## 페이지 {page.page_num}")
                lines.append("")
                lines.append(f"*[OCR 필요 - 상태: {page.ocr_status}]*")
                lines.append("")
                lines.append("---")
                lines.append("")

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

    return md_path


def save_metadata(result: PDFResult, output_dir: Path) -> Path:
    """메타데이터 저장"""
    safe_name = re.sub(r'[^\w가-힣\s\-]', '', Path(result.filename).stem)
    safe_name = re.sub(r'\s+', '_', safe_name).strip('_')

    meta_path = output_dir / f"{safe_name}_meta.json"

    meta = {
        "source": result.filename,
        "parsed_at": datetime.now().isoformat(),
        "total_pages": result.total_pages,
        "pages_with_text": result.pages_with_text,
        "pages_needing_ocr": result.pages_needing_ocr,
        "ocr_page_numbers": result.ocr_page_numbers,
        "pages": [asdict(p) for p in result.pages]
    }

    with open(meta_path, 'w', encoding='utf-8') as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    return meta_path


def run_ocr_on_pending_pages(
    pdf_path: Path,
    result: PDFResult,
    api_key: str
) -> int:
    """OCR 필요한 페이지에 대해 Upstage OCR 실행"""
    success_count = 0

    for page in result.pages:
        if page.needs_ocr and page.ocr_status == "pending":
            try:
                print(f"  OCR 페이지 {page.page_num}...", end=" ", flush=True)
                img_bytes = extract_page_as_image(pdf_path, page.page_num)
                ocr_text = ocr_with_upstage(img_bytes, api_key)
                page.text = ocr_text
                page.char_count = len(ocr_text)
                page.word_count = len(ocr_text.split())
                page.ocr_status = "success"
                success_count += 1
                print("OK")
            except Exception as e:
                page.ocr_status = f"failed: {str(e)}"
                print(f"FAIL: {e}")

    return success_count


def main():
    parser = argparse.ArgumentParser(description="지능형 PDF 파서 (pdfplumber 기반)")
    parser.add_argument("--input", "-i", required=True, help="PDF 파일 또는 디렉토리")
    parser.add_argument("--output", "-o", required=True, help="출력 디렉토리")
    parser.add_argument("--analyze-only", action="store_true", help="분석만 수행")
    parser.add_argument("--with-ocr", action="store_true", help="OCR도 함께 수행")
    parser.add_argument("--upstage-key", help="Upstage API 키 (또는 UPSTAGE_API_KEY 환경변수)")

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output)

    # API 키
    upstage_key = args.upstage_key or os.environ.get("UPSTAGE_API_KEY")

    # PDF 수집
    if input_path.is_file():
        pdf_files = [input_path]
    else:
        pdf_files = sorted(input_path.glob("*.pdf"))

    if not pdf_files:
        print("PDF 파일을 찾을 수 없습니다.")
        sys.exit(1)

    print(f"PDF 파일: {len(pdf_files)}개")
    print(f"출력 디렉토리: {output_path}")
    print(f"OCR 모드: {'ON' if args.with_ocr else 'OFF'}")
    print()

    all_results = []
    total_pages = 0
    total_ocr_needed = 0
    total_ocr_success = 0

    for pdf_path in pdf_files:
        print(f"{'='*60}")
        print(f"처리 중: {pdf_path.name}")
        print(f"{'='*60}")

        # 1단계: pdfplumber로 파싱
        result = parse_pdf_with_pdfplumber(pdf_path)
        total_pages += result.total_pages
        total_ocr_needed += result.pages_needing_ocr

        print(f"  총 페이지: {result.total_pages}")
        print(f"  텍스트 추출: {result.pages_with_text}")
        print(f"  OCR 필요: {result.pages_needing_ocr}")

        if result.ocr_page_numbers:
            print(f"  OCR 필요 페이지: {result.ocr_page_numbers}")

        # 2단계: OCR (선택적)
        if args.with_ocr and result.pages_needing_ocr > 0:
            if upstage_key:
                print(f"\n  OCR 수행 중...")
                success = run_ocr_on_pending_pages(pdf_path, result, upstage_key)
                total_ocr_success += success
                print(f"  OCR 완료: {success}/{result.pages_needing_ocr}")
            else:
                print(f"  [경고] Upstage API 키 없음 - OCR 건너뜀")

        # 분석만 모드가 아니면 저장
        if not args.analyze_only:
            md_path = save_to_markdown(result, output_path)
            meta_path = save_metadata(result, output_path)
            print(f"\n  저장: {md_path.name}")

        all_results.append(result)
        print()

    # 요약
    print("=" * 60)
    print("요약")
    print("=" * 60)
    print(f"총 PDF: {len(pdf_files)}개")
    print(f"총 페이지: {total_pages}")
    print(f"OCR 필요 페이지: {total_ocr_needed}")
    if args.with_ocr:
        print(f"OCR 성공: {total_ocr_success}")
        print(f"OCR 미처리: {total_ocr_needed - total_ocr_success}")

    # 전체 OCR 필요 페이지 목록 저장
    ocr_summary = {
        "created_at": datetime.now().isoformat(),
        "total_files": len(pdf_files),
        "total_pages": total_pages,
        "total_ocr_needed": total_ocr_needed,
        "ocr_completed": total_ocr_success if args.with_ocr else 0,
        "files": []
    }

    for result in all_results:
        if result.ocr_page_numbers:
            ocr_summary["files"].append({
                "filename": result.filename,
                "ocr_pages": result.ocr_page_numbers,
                "status": [p.ocr_status for p in result.pages if p.needs_ocr]
            })

    output_path.mkdir(parents=True, exist_ok=True)
    summary_path = output_path / "ocr_summary.json"
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump(ocr_summary, f, ensure_ascii=False, indent=2)

    print(f"\nOCR 요약 저장: {summary_path}")


if __name__ == "__main__":
    main()
