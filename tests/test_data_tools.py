from pathlib import Path

import pytest

from tools.download import entries


def test_entries_support_named_and_bare_urls(tmp_path: Path):
    urls = tmp_path / "urls.txt"
    urls.write_text(
        "# source list\n"
        "who_2025_guide.pdf | https://example.org/source.pdf\n"
        "https://example.org/another.pdf\n",
        encoding="utf-8",
    )

    assert list(entries(str(urls))) == [
        ("who_2025_guide.pdf", "https://example.org/source.pdf"),
        ("another.pdf", "https://example.org/another.pdf"),
    ]


def test_entries_reject_path_traversal(tmp_path: Path):
    urls = tmp_path / "urls.txt"
    urls.write_text("../outside.pdf | https://example.org/source.pdf\n", encoding="utf-8")

    with pytest.raises(ValueError, match="Invalid entry"):
        list(entries(str(urls)))
