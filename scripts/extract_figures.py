#!/usr/bin/env python3
"""Pull the figures listed in references/figures.tsv out of the papers.

For each listed figure, downloads the paper's arXiv source once (cached in
papers/src/), finds the figure environments in document order, and writes
the figure's image files to extracted/<key>-fig<N>[a-z].png. Both folders
are gitignored: these are for reading and drafting, not for publishing.

A figure may be copied into figures/reused/ only when its paper is CC BY
(scripts/fetch_papers.py lists licences), and then with its credit.

    python3 scripts/extract_figures.py

Needs pdftoppm (poppler) for PDF figures and ImageMagick's `magick` for EPS.
"""

import csv
import gzip
import io
import re
import shutil
import subprocess
import tarfile
import time
from pathlib import Path

from fetch_papers import BIB, ENTRY, EPRINT, get

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "papers" / "src"
OUT = ROOT / "extracted"
LIST = ROOT / "references" / "figures.tsv"

FIGURE = re.compile(r"\\begin\{figure\*?\}(.*?)\\end\{figure\*?\}", re.S)
GRAPHIC = re.compile(r"\\includegraphics\s*(?:\[[^\]]*\])?\s*\{([^}]+)\}")
INPUT = re.compile(r"\\(?:input|include|subfile)\s*\{([^}]+)\}")
COMMENT = re.compile(r"(?<!\\)%.*")
EXTENSIONS = ("", ".pdf", ".png", ".jpg", ".jpeg", ".eps", ".ps")


def eprints():
    text = BIB.read_text(encoding="utf-8")
    found = {}
    for match in ENTRY.finditer(text):
        key, body = match.groups()
        eprint = EPRINT.search(body)
        if eprint:
            found[key] = eprint.group(1).strip()
    return found


def unpack(key, arxiv_id):
    target = SRC / key
    if target.exists():
        return target
    blob = get(f"https://arxiv.org/e-print/{arxiv_id}")
    time.sleep(3)
    target.mkdir(parents=True)
    try:
        with tarfile.open(fileobj=io.BytesIO(blob)) as tar:
            tar.extractall(target, filter="data")
    except tarfile.ReadError:
        (target / "main.tex").write_bytes(gzip.decompress(blob))
    return target


def expand(path, root, seen):
    if path in seen or not path.exists():
        return ""
    seen.add(path)
    text = COMMENT.sub("", path.read_text(encoding="utf-8", errors="replace"))

    def include(match):
        name = match.group(1).strip()
        candidate = root / name
        if not candidate.suffix:
            candidate = candidate.with_suffix(".tex")
        return expand(candidate, root, seen)

    return INPUT.sub(include, text)


def figures_in(root):
    mains = [p for p in root.rglob("*.tex") if "\\documentclass" in p.read_text(errors="replace")]
    if not mains:
        return []
    main = max(mains, key=lambda p: p.stat().st_size)
    text = expand(main, main.parent, set())
    paths = re.findall(r"\\graphicspath\s*\{((?:\{[^}]*\})+)\}", text)
    search = [main.parent] + [main.parent / p for group in paths for p in re.findall(r"\{([^}]*)\}", group)]
    found = []
    for env in FIGURE.finditer(text):
        files = []
        for name in GRAPHIC.findall(env.group(1)):
            for base in search:
                for ext in EXTENSIONS:
                    candidate = base / (name.strip() + ext)
                    if candidate.is_file():
                        files.append(candidate)
                        break
                else:
                    continue
                break
        found.append(files)
    return found


def render(source, target):
    suffix = source.suffix.lower()
    if suffix == ".pdf":
        subprocess.run(
            ["pdftoppm", "-png", "-r", "200", "-singlefile", str(source), str(target.with_suffix(""))],
            check=True,
        )
    elif suffix in (".eps", ".ps"):
        subprocess.run(["magick", "-density", "200", str(source), str(target)], check=True)
    elif suffix == ".png":
        shutil.copyfile(source, target)
    else:
        subprocess.run(["magick", str(source), str(target)], check=True)


def main():
    known = eprints()
    rows = list(csv.DictReader(LIST.open(encoding="utf-8"), delimiter="\t"))
    OUT.mkdir(exist_ok=True)
    cache = {}
    for row in rows:
        key, number = row["key"], int(row["figure"])
        if key not in known:
            print(f"skip  {key}: no arXiv source")
            continue
        if key not in cache:
            try:
                cache[key] = figures_in(unpack(key, known[key]))
            except Exception as error:
                print(f"fail  {key}: {error}")
                cache[key] = []
        figures = cache[key]
        if number > len(figures) or not figures[number - 1]:
            print(f"miss  {key} figure {number}: {len(figures)} figure environments found")
            continue
        files = figures[number - 1]
        for i, source in enumerate(files):
            letter = "" if len(files) == 1 else "abcdefghijklmnopqrstuvwxyz"[i]
            target = OUT / f"{key}-fig{number}{letter}.png"
            try:
                render(source, target)
                print(f"ok    {target.name}  <- {source.name}")
            except Exception as error:
                print(f"fail  {target.name}: {error}")


if __name__ == "__main__":
    main()
