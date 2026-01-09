"""
PyMuPDF vs pdfplumber 비교 테스트
"""
import sys
from pathlib import Path
import time

import fitz  # PyMuPDF
import pdfplumber


def test_pymupdf(pdf_path: Path) -> tuple[list[str], float]:
    """PyMuPDF로 텍스트 추출"""
    start = time.time()
    doc = fitz.open(pdf_path)
    pages = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        pages.append(text.strip())
    doc.close()
    elapsed = time.time() - start
    return pages, elapsed


def test_pdfplumber(pdf_path: Path) -> tuple[list[str], float]:
    """pdfplumber로 텍스트 추출"""
    start = time.time()
    pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text() or ""
            pages.append(text.strip())
    elapsed = time.time() - start
    return pages, elapsed


def compare_quality(text1: str, text2: str) -> dict:
    """두 텍스트 품질 비교"""
    return {
        "len_1": len(text1),
        "len_2": len(text2),
        "words_1": len(text1.split()),
        "words_2": len(text2.split()),
        "diff_ratio": len(text1) / len(text2) if text2 else float('inf') if text1 else 1.0
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python compare_parsers.py <pdf_path>")
        sys.exit(1)

    pdf_path = Path(sys.argv[1])
    print(f"테스트 파일: {pdf_path.name}\n")

    # PyMuPDF 테스트
    print("=" * 60)
    print("PyMuPDF 테스트")
    print("=" * 60)
    pymupdf_pages, pymupdf_time = test_pymupdf(pdf_path)
    print(f"추출 시간: {pymupdf_time:.3f}초")
    print(f"총 페이지: {len(pymupdf_pages)}")

    # pdfplumber 테스트
    print("\n" + "=" * 60)
    print("pdfplumber 테스트")
    print("=" * 60)
    plumber_pages, plumber_time = test_pdfplumber(pdf_path)
    print(f"추출 시간: {plumber_time:.3f}초")
    print(f"총 페이지: {len(plumber_pages)}")

    # 속도 비교
    print("\n" + "=" * 60)
    print("속도 비교")
    print("=" * 60)
    print(f"PyMuPDF: {pymupdf_time:.3f}초")
    print(f"pdfplumber: {plumber_time:.3f}초")
    print(f"PyMuPDF가 {plumber_time/pymupdf_time:.1f}배 빠름" if pymupdf_time < plumber_time else f"pdfplumber가 {pymupdf_time/plumber_time:.1f}배 빠름")

    # 페이지별 품질 비교
    print("\n" + "=" * 60)
    print("페이지별 텍스트 추출 품질 비교")
    print("=" * 60)
    print(f"{'Page':<6} {'PyMuPDF (chars)':<16} {'pdfplumber (chars)':<18} {'Winner':<10}")
    print("-" * 60)

    pymupdf_total = 0
    plumber_total = 0
    pymupdf_wins = 0
    plumber_wins = 0
    ties = 0

    for i, (p1, p2) in enumerate(zip(pymupdf_pages, plumber_pages), 1):
        len1 = len(p1)
        len2 = len(p2)
        pymupdf_total += len1
        plumber_total += len2

        if len1 > len2 * 1.1:  # 10% 이상 차이
            winner = "PyMuPDF"
            pymupdf_wins += 1
        elif len2 > len1 * 1.1:
            winner = "pdfplumber"
            plumber_wins += 1
        else:
            winner = "Similar"
            ties += 1

        print(f"{i:<6} {len1:<16} {len2:<18} {winner:<10}")

    print("-" * 60)
    print(f"{'Total':<6} {pymupdf_total:<16} {plumber_total:<18}")
    print(f"\nPyMuPDF 승: {pymupdf_wins}, pdfplumber 승: {plumber_wins}, 비슷: {ties}")

    # 샘플 텍스트 출력
    print("\n" + "=" * 60)
    print("샘플 텍스트 비교 (첫 페이지)")
    print("=" * 60)
    print("\n[PyMuPDF 결과]")
    print(pymupdf_pages[0][:500] if pymupdf_pages[0] else "(빈 페이지)")
    print("\n[pdfplumber 결과]")
    print(plumber_pages[0][:500] if plumber_pages[0] else "(빈 페이지)")

    # 텍스트가 거의 없는 페이지 (OCR 필요)
    print("\n" + "=" * 60)
    print("OCR 필요 페이지 (50자 미만)")
    print("=" * 60)
    for i, (p1, p2) in enumerate(zip(pymupdf_pages, plumber_pages), 1):
        if len(p1) < 50 or len(p2) < 50:
            print(f"Page {i}: PyMuPDF={len(p1)}자, pdfplumber={len(p2)}자")


if __name__ == "__main__":
    main()
