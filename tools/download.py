"""Download the dataset: python tools/download.py urls.txt."""

import csv
import hashlib
import os
import sys
import time
from datetime import date
from pathlib import Path
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser

import requests

RAW = Path("data/raw")
MANIFEST = Path("data/manifest.csv")
HEADERS = {
    "User-Agent": (
        "WardWiseDataCollector/1.0 "
        "(+https://github.com/janarthanan2006v/WardWise)"
    )
}
DELAY_SECONDS = 2
ROBOTS: dict[str, RobotFileParser | None] = {}


def entries(list_file: str):
    """Yield (filename, URL); a bare URL keeps its server filename."""
    for raw_line in Path(list_file).read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "|" in line:
            filename, url = (part.strip() for part in line.split("|", 1))
        else:
            url = line
            filename = Path(urlparse(url).path).name or "download"
        if Path(filename).name != filename or urlparse(url).scheme not in {"http", "https"}:
            raise ValueError(f"Invalid entry: {raw_line}")
        yield filename, url


def allowed(session: requests.Session, url: str) -> bool:
    """Check robots.txt; continue carefully when the file is unavailable."""
    parsed = urlparse(url)
    root = f"{parsed.scheme}://{parsed.netloc}"
    if root in ROBOTS:
        parser = ROBOTS[root]
        return parser is None or parser.can_fetch(HEADERS["User-Agent"], url)

    robots_url = f"{root}/robots.txt"
    try:
        response = session.get(robots_url, timeout=15)
        if response.status_code != 200:
            print(f"robots.txt unavailable ({response.status_code}); proceeding carefully")
            ROBOTS[root] = None
            return True
        parser = RobotFileParser()
        parser.set_url(robots_url)
        parser.parse(response.text.splitlines())
        ROBOTS[root] = parser
        return parser.can_fetch(HEADERS["User-Agent"], url)
    except requests.RequestException as exc:
        print(f"robots.txt unavailable ({exc.__class__.__name__}); proceeding carefully")
        ROBOTS[root] = None
        return True


def download(session: requests.Session, filename: str, url: str):
    path = RAW / filename
    if path.exists():
        print("skip (already have)", path)
        return None
    if not allowed(session, url):
        print("BLOCKED by robots.txt, not downloading:", url)
        return None

    temporary = path.with_suffix(path.suffix + ".part")
    digest = hashlib.sha256()
    size = 0
    try:
        with session.get(url, timeout=120, stream=True) as response:
            response.raise_for_status()
            with temporary.open("wb") as output:
                for chunk in response.iter_content(1024 * 1024):
                    if chunk:
                        output.write(chunk)
                        digest.update(chunk)
                        size += len(chunk)
        with temporary.open("rb") as downloaded:
            if downloaded.read(5) != b"%PDF-":
                raise ValueError(f"Downloaded content is not a PDF: {url}")
        os.replace(temporary, path)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise

    print("saved", path, size, "bytes")
    return [str(path), url, date.today().isoformat(), size, digest.hexdigest()]


def main(list_file: str):
    RAW.mkdir(parents=True, exist_ok=True)
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    new_manifest = not MANIFEST.exists()
    with requests.Session() as session, MANIFEST.open("a", newline="", encoding="utf-8") as file:
        session.headers.update(HEADERS)
        log = csv.writer(file, lineterminator="\n")
        if new_manifest:
            log.writerow(["file", "source_url", "downloaded_on", "bytes", "sha256"])
        for filename, url in entries(list_file):
            row = download(session, filename, url)
            if row:
                log.writerow(row)
                file.flush()
                time.sleep(DELAY_SECONDS)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: python tools/download.py urls.txt")
    main(sys.argv[1])
