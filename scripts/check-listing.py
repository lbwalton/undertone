#!/usr/bin/env python3
"""Verify docs/appstore-listing.md fields against App Store Connect limits.

ASC rejects over-limit fields at paste time; catching it here keeps the
listing doc trustworthy. Sections are located by their exact headings.
"""
import re
import sys
from pathlib import Path

DOC = Path(__file__).resolve().parent.parent / "docs" / "appstore-listing.md"

LIMITS = {
    "Name": 30,
    "Subtitle": 30,
    "Promotional text": 170,
    "Description": 4000,
    "Keywords": 100,
    "What's New for 0.1.1": 4000,
}


def section(body: str, title_prefix: str) -> str:
    pattern = rf"^## {re.escape(title_prefix)}.*?$\n(.*?)(?=^## |\Z)"
    m = re.search(pattern, body, re.M | re.S)
    if not m:
        sys.exit(f"FAIL: section not found: {title_prefix}")
    return m.group(1).strip()


def main() -> None:
    body = DOC.read_text()
    failures = []
    for title, limit in LIMITS.items():
        text = section(body, title)
        # Multi-paragraph fields are pasted as-is; single-line fields are one line.
        n = len(text)
        status = "ok" if n <= limit else "OVER"
        print(f"{title}: {n}/{limit} {status}")
        if n > limit:
            failures.append(title)
    if failures:
        sys.exit(f"FAIL: over limit: {', '.join(failures)}")
    print("All fields within App Store Connect limits.")


if __name__ == "__main__":
    main()
