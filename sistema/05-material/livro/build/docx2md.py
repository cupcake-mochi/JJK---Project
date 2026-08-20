#!/usr/bin/env python3
"""Extrai um .docx pra Markdown razoável, sem depender de python-docx."""
import sys
import zipfile
from xml.etree import ElementTree as ET

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def qn(tag):
    return W + tag


def get_style(p):
    pPr = p.find(qn("pPr"))
    if pPr is None:
        return None
    pStyle = pPr.find(qn("pStyle"))
    return None if pStyle is None else pStyle.get(qn("val"))


def run_text(r):
    rPr = r.find(qn("rPr"))
    bold = italic = False
    if rPr is not None:
        b, i = rPr.find(qn("b")), rPr.find(qn("i"))
        if b is not None and b.get(qn("val")) != "0":
            bold = True
        if i is not None and i.get(qn("val")) != "0":
            italic = True
    parts = [t.text or "" for t in r.findall(qn("t"))]
    parts += ["\n" for _ in r.findall(qn("br"))]
    s = "".join(parts)
    if not s.strip():
        return s
    if bold:
        s = f"**{s}**"
    if italic:
        s = f"*{s}*"
    return s


def para_text(p):
    return "".join(run_text(r) for r in p.findall(qn("r")))


def cell_text(tc):
    return " ".join(t for t in (para_text(p) for p in tc.findall(qn("p"))) if t.strip())


def table_to_md(tbl):
    rows = [[cell_text(tc) for tc in tr.findall(qn("tc"))] for tr in tbl.findall(qn("tr"))]
    if not rows:
        return ""
    header = rows[0]
    out = ["| " + " | ".join(c.replace("|", "\\|") for c in header) + " |",
           "|" + "|".join(["---"] * len(header)) + "|"]
    for row in rows[1:]:
        row = (row + [""] * len(header))[: len(header)]
        out.append("| " + " | ".join(c.replace("|", "\\|") for c in row) + " |")
    return "\n".join(out)


HEADING = {"Heading1": "#", "Heading2": "##", "Heading3": "###",
           "Heading4": "####", "Heading5": "#####", "Title": "#", "Subtitle": "##"}


def main(path, out_path):
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read("word/document.xml"))
    lines = []
    for child in root.find(qn("body")):
        tag = child.tag.replace(W, "")
        if tag == "p":
            text = para_text(child).strip()
            if not text:
                lines.append("")
                continue
            pre = HEADING.get(get_style(child))
            lines.append(f"\n{pre} {text}\n" if pre else text)
        elif tag == "tbl":
            lines.append("\n" + table_to_md(child) + "\n")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Escrito {out_path}, {len(lines)} blocos.")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
