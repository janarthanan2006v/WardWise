"""Measure the local dataset: python tools/count_pages.py."""

from pathlib import Path

from pypdf import PdfReader

RAW = Path("data/raw")
CODE_SUFFIXES = {
    ".c",
    ".go",
    ".h",
    ".java",
    ".js",
    ".kt",
    ".py",
    ".rs",
    ".ts",
    ".yaml",
    ".yml",
}


def main():
    pdf_pages = html_pages = code_files = broken_files = scanned_pdfs = 0
    for path in sorted(RAW.rglob("*")):
        if not path.is_file():
            continue
        suffix = path.suffix.lower()
        if suffix == ".pdf":
            try:
                reader = PdfReader(path)
                pages = len(reader.pages)
                pdf_pages += pages
                has_text = any((page.extract_text() or "").strip() for page in reader.pages)
                scanned_pdfs += not has_text
                print(f"{pages:5d} pages  {path}")
            except Exception as exc:
                broken_files += 1
                print(f"BROKEN       {path} ({exc.__class__.__name__})")
        elif suffix in {".html", ".htm"}:
            html_pages += 1
        elif suffix in CODE_SUFFIXES:
            code_files += 1

    print(
        f"\nPDF pages: {pdf_pages} | HTML pages: {html_pages} | "
        f"code files: {code_files} | broken files: {broken_files} | "
        f"scanned PDFs: {scanned_pdfs}"
    )
    print(f"TOTAL pages for DATASET.md: {pdf_pages + html_pages}")


if __name__ == "__main__":
    main()
