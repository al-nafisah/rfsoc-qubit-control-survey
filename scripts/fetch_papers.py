#!/usr/bin/env python3
"""Rebuild the local paper library from references/papers.bib.

Every entry with an `eprint` field is an arXiv preprint. This script
downloads each one to papers/<key>.pdf, skipping files already there, and
prints the licence arXiv records for it. The licence decides whether any of
its figures may be reused in this repository: only CC BY may (see README).

    python3 scripts/fetch_papers.py            # download and list licences
    python3 scripts/fetch_papers.py --licences # list licences only

Standard library only. arXiv asks for no more than one request every three
seconds, and the script keeps to that.
"""

import re
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BIB = ROOT / "references" / "papers.bib"
OUT = ROOT / "papers"
DELAY = 3.0
AGENT = "rfsoc-qubit-control-survey/1.0 (https://github.com/al-nafisah/rfsoc-qubit-control-survey)"

ENTRY = re.compile(r"@\w+\{([^,\s]+),(.*?)\n\}", re.S)
EPRINT = re.compile(r"\beprint\s*=\s*\{([^}]+)\}")
OAI = "{http://www.openarchives.org/OAI/2.0/}"
ARXIV = "{http://arxiv.org/OAI/arXiv/}"


def entries():
    text = BIB.read_text(encoding="utf-8")
    for match in ENTRY.finditer(text):
        key, body = match.groups()
        eprint = EPRINT.search(body)
        if eprint:
            yield key, eprint.group(1).strip()


def get(url):
    request = urllib.request.Request(url, headers={"User-Agent": AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()


def licence(arxiv_id):
    url = (
        "https://export.arxiv.org/oai2?verb=GetRecord&metadataPrefix=arXiv"
        f"&identifier=oai:arXiv.org:{arxiv_id}"
    )
    root = ET.fromstring(get(url))
    node = root.find(f".//{OAI}metadata/{ARXIV}arXiv/{ARXIV}license")
    if node is None or not node.text:
        return "arXiv default (non-exclusive distribution licence)"
    return node.text.strip()


def short(url):
    for name, marker in (
        ("CC BY", "/by/"),
        ("CC BY-SA", "/by-sa/"),
        ("CC BY-NC-SA", "/by-nc-sa/"),
        ("CC BY-NC-ND", "/by-nc-nd/"),
        ("CC0", "/zero/"),
        ("arXiv only", "nonexclusive-distrib"),
    ):
        if marker in url:
            return name
    return url


def main():
    licences_only = "--licences" in sys.argv[1:]
    OUT.mkdir(exist_ok=True)
    rows = []
    for key, arxiv_id in entries():
        if not licences_only:
            target = OUT / f"{key}.pdf"
            if not target.exists():
                target.write_bytes(get(f"https://arxiv.org/pdf/{arxiv_id}"))
                time.sleep(DELAY)
        rows.append((key, arxiv_id, short(licence(arxiv_id))))
        time.sleep(DELAY)
    width = max(len(key) for key, _, _ in rows)
    for key, arxiv_id, name in rows:
        reusable = "figures reusable" if name in ("CC BY", "CC0") else ""
        print(f"{key:<{width}}  {arxiv_id:<12}  {name:<12}  {reusable}")


if __name__ == "__main__":
    main()
