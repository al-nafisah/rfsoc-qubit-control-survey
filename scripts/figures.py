#!/usr/bin/env python3
"""Draw the survey's own figures into figures/*.svg.

Every figure here is drawn from scratch from the sources cited in the
README, never traced from a paper's figure. Standard library only.

    python3 scripts/figures.py

Text is set in a monospace stack, so a label's width is predictable:
about 0.6 of the font size per character.
"""

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent.parent / "figures"

PAPER = "#FFFFFF"
INK = "#16150F"
MUTED = "#6B6358"
FAINT = "#DDD7C9"
FILL = "#F4F1EA"
ACCENT = "#9A5B00"
FONT = "ui-monospace, 'SF Mono', Menlo, Consolas, 'DejaVu Sans Mono', monospace"


class Svg:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.parts = []

    def add(self, s):
        self.parts.append(s)

    def text(self, x, y, s, size=14, color=INK, anchor="start", weight="normal", style="normal"):
        self.add(
            f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" '
            f'font-weight="{weight}" font-style="{style}">{escape(s)}</text>'
        )

    def lines(self, x, y, rows, size=14, color=INK, anchor="start", leading=1.3, weight="normal"):
        for i, row in enumerate(rows):
            self.text(x, y + i * size * leading, row, size, color, anchor, weight)

    def rect(self, x, y, w, h, fill=FILL, stroke=INK, width=1.5, dash=None, radius=3):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{width}"{d}/>'
        )

    def box(self, x, y, w, h, rows, size=13, fill=FILL, stroke=INK, color=INK, dash=None):
        self.rect(x, y, w, h, fill, stroke, dash=dash)
        top = y + h / 2 - (len(rows) - 1) * size * 0.65 + size * 0.35
        self.lines(x + w / 2, top, rows, size, color, "middle")

    def path(self, d, color=INK, width=1.5, dash=None, arrow=True):
        marker = f' marker-end="url(#head-{color[1:]})"' if arrow else ""
        dd = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}"{dd}{marker}/>')

    def circle(self, x, y, r, fill, stroke):
        self.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')

    def save(self, name, title, desc):
        heads = "".join(
            f'<marker id="head-{c[1:]}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" '
            f'markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
            for c in (INK, MUTED, ACCENT)
        )
        svg = (
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" '
            f'viewBox="0 0 {self.width} {self.height}" font-family="{FONT}" role="img">\n'
            f"<title>{escape(title)}</title>\n<desc>{escape(desc)}</desc>\n"
            f"<defs>{heads}</defs>\n"
            f'<rect width="{self.width}" height="{self.height}" fill="{PAPER}"/>\n'
            + "\n".join(self.parts)
            + "\n</svg>\n"
        )
        OUT.mkdir(exist_ok=True)
        (OUT / name).write_text(svg, encoding="utf-8")


# ---------------------------------------------------------------------------
# Figure 1. Where the real-time control lives
# ---------------------------------------------------------------------------

def dac(s, x, y):
    """A converter drawn as a right-pointing pentagon, 46 by 30."""
    s.add(
        f'<path d="M{x},{y} h30 l16,15 l-16,15 h-30 z" fill="{PAPER}" stroke="{INK}" stroke-width="1.5"/>'
    )
    s.text(x + 18, y + 20, "DAC", 11, INK, "middle")


def adc(s, x, y):
    s.add(
        f'<path d="M{x + 46},{y} h-30 l-16,15 l16,15 h30 z" fill="{PAPER}" stroke="{INK}" stroke-width="1.5"/>'
    )
    s.text(x + 28, y + 20, "ADC", 11, INK, "middle")


def fridge(s, x, y, h):
    s.rect(x, y, 70, h, PAPER, MUTED, 1.2, "5 4")
    s.lines(x + 35, y + h / 2 - 6, ["qubits"], 12, MUTED, "middle")


def panel_frame(s, ox, oy, w, h, letter, heading, systems):
    s.rect(ox, oy, w, h, PAPER, FAINT, 1.5, radius=4)
    s.text(ox + 18, oy + 30, f"({letter}) {heading}", 16, INK, weight="bold")
    s.text(ox + 18, oy + 52, systems, 13, ACCENT)


def channel_out(s, ox, y, x_from, label_rows=("gen",)):
    """Generator, DAC, line into the fridge, starting at x_from."""
    s.path(f"M{ox + x_from},{y + 15} H{ox + 228}")
    s.box(ox + 232, y, 64, 30, list(label_rows), 12)
    s.path(f"M{ox + 296},{y + 15} H{ox + 318}")
    dac(s, ox + 322, y)
    s.path(f"M{ox + 368},{y + 15} H{ox + 440}")


def readout_in(s, ox, y):
    """Fridge, ADC, readout DSP, returning the x of the readout box's left edge."""
    s.path(f"M{ox + 440},{y + 15} H{ox + 372}")
    adc(s, ox + 322, y)
    s.path(f"M{ox + 322},{y + 15} H{ox + 300}")
    s.box(ox + 222, y, 76, 30, ["readout"], 12)
    return ox + 222


def figure_sequencers():
    W, H = 1200, 890
    s = Svg(W, H)
    s.text(40, 48, "Where the real-time control lives", 24, INK, weight="bold")
    s.lines(
        40, 76,
        [
            "Six open RFSoC qubit controllers, four ways of deciding what plays when. Boxes are roles,",
            "not floorplans; each panel is drawn from the papers cited in the README.",
        ],
        14, MUTED,
    )
    pw, ph = 545, 340
    origins = [(40, 120), (615, 120), (40, 485), (615, 485)]

    # (a) one processor for every channel
    ox, oy = origins[0]
    panel_frame(s, ox, oy, pw, ph, "a", "One processor, every channel", "QICK (tProcessor v1 and v2)")
    s.box(ox + 20, oy + 82, 110, 150, ["one", "processor"], 13)
    ys = [oy + 84, oy + 124, oy + 164, oy + 204]
    for y in ys:
        s.path(f"M{ox + 130},{y + 15} H{ox + 146}")
        for k in range(3):
            s.rect(ox + 150 + k * 9, y + 6, 8, 18, PAPER, MUTED, 1.2, radius=1)
        channel_out(s, ox, y, 178)
    s.text(ox + 164, oy + 76, "timed queues", 11, MUTED, "middle")
    fridge(s, ox + 444, oy + 76, 240)
    yr = oy + 270
    left = readout_in(s, ox, yr)
    s.path(f"M{left},{yr + 15} H{ox + 75} V{oy + 236}", ACCENT, 2)
    s.text(ox + 20, oy + 318, "the readout feeds the processor, which branches", 12, ACCENT)

    # (b) one processor per qubit
    ox, oy = origins[1]
    panel_frame(s, ox, oy, pw, ph, "b", "One processor per qubit", "QubiC, QiController, RISC-Q as built for QEC")
    ys = [oy + 84, oy + 128, oy + 172]
    for i, y in enumerate(ys):
        s.box(ox + 20, y, 110, 30, [f"core q{i}"], 12)
        channel_out(s, ox, y, 130)
    s.text(ox + 75, oy + 228, "...", 14, MUTED, "middle")
    fridge(s, ox + 444, oy + 76, 240)
    yr = oy + 270
    left = readout_in(s, ox, yr)
    s.box(ox + 20, yr, 110, 30, ["result hub"], 12, stroke=ACCENT)
    s.path(f"M{left},{yr + 15} H{ox + 134}", ACCENT, 2)
    s.path(f"M{ox + 150},{yr} V{oy + 99}", ACCENT, 2, arrow=False)
    s.path(f"M{ox + 130},{yr + 15} H{ox + 150}", ACCENT, 2, arrow=False)
    for y in ys:
        s.path(f"M{ox + 150},{y + 22} H{ox + 134}", ACCENT, 2)
    s.text(ox + 20, oy + 318, "a hub hands each core the results it waits on", 12, ACCENT)

    # (c) an event table, no processor
    ox, oy = origins[2]
    panel_frame(s, ox, oy, pw, ph, "c", "An event table, no processor", "FIREQ")
    s.rect(ox + 20, oy + 82, 110, 150, FILL, INK)
    for k in range(1, 8):
        s.add(
            f'<line x1="{ox + 28}" y1="{oy + 82 + k * 17}" x2="{ox + 122}" y2="{oy + 82 + k * 17}" '
            f'stroke="{MUTED}" stroke-width="1"/>'
        )
    s.text(ox + 75, oy + 250, "trigger table", 12, INK, "middle")
    ys = [oy + 84, oy + 124, oy + 164, oy + 204]
    for y in ys:
        channel_out(s, ox, y, 130)
    fridge(s, ox + 444, oy + 76, 240)
    yr = oy + 270
    left = readout_in(s, ox, yr)
    s.path(f"M{left},{yr + 15} H{ox + 134}", MUTED, 1.5, "5 4")
    s.box(ox + 20, yr, 110, 30, ["to the ARM"], 12, fill=PAPER, stroke=MUTED, color=MUTED)
    s.text(ox + 20, oy + 318, "no conditional path is reported", 12, MUTED)

    # (d) a fixed state machine
    ox, oy = origins[3]
    panel_frame(s, ox, oy, pw, ph, "d", "A fixed state machine", "SQ-CARS")
    s.box(ox + 20, oy + 82, 110, 150, ["state", "machine,", "fixed loops"], 13)
    ys = [oy + 84, oy + 124, oy + 164, oy + 204]
    for y in ys:
        channel_out(s, ox, y, 130)
    fridge(s, ox + 444, oy + 76, 240)
    yr = oy + 270
    left = readout_in(s, ox, yr)
    s.path(f"M{left},{yr + 15} H{ox + 134}", MUTED, 1.5, "5 4")
    s.box(ox + 20, yr, 110, 30, ["DMA to ARM"], 12, fill=PAPER, stroke=MUTED, color=MUTED)
    s.text(ox + 20, oy + 318, "feedback is claimed, not demonstrated", 12, MUTED)

    s.lines(
        40, 860,
        [
            "Common to all six: ARM cores on the same chip run Linux (PYNQ on five of them) and talk to a host PC.",
        ],
        13, MUTED,
    )
    s.save(
        "sequencer-models.svg",
        "Where the real-time control lives",
        "Four panels. (a) QICK: one processor feeds timed queues for every channel, and the readout feeds "
        "back into it. (b) QubiC, QiController and RISC-Q as built for QEC: one core per qubit, with a "
        "result hub returning measurements to the cores. (c) FIREQ: a trigger table with no processor and "
        "no reported conditional path. (d) SQ-CARS: a fixed state machine; readout data goes by DMA to the "
        "ARM, and feedback is claimed but not demonstrated.",
    )


# ---------------------------------------------------------------------------
# Figure 2. What is public
# ---------------------------------------------------------------------------

YES, PART, NO, UNKNOWN = "yes", "part", "no", "unknown"


def glyph(s, x, y, kind):
    if kind == YES:
        s.circle(x, y, 8, INK, INK)
    elif kind == PART:
        s.circle(x, y, 8, PAPER, INK)
        s.add(f'<path d="M{x},{y - 8} A8,8 0 0,0 {x},{y + 8} z" fill="{INK}"/>')
    elif kind == NO:
        s.circle(x, y, 8, PAPER, INK)
    else:
        s.text(x, y + 5, "?", 15, MUTED, "middle")


def figure_openness():
    cols = [
        ("Gateware", "source"),
        ("Build", "scripts"),
        ("Bitstreams", ""),
        ("Host", "software"),
        ("Board", "designs"),
    ]
    rows = [
        ("QubiC", [YES, YES, YES, YES, YES], "BSD-3 (LBNL)", "1"),
        ("QICK", [YES, YES, YES, YES, PART], "MIT", "2"),
        ("FIREQ", [NO, NO, YES, YES, "AMD cards"], "AGPL-3.0", ""),
        ("RISC-Q", [YES, YES, NO, YES, "QubiC's"], "none", "3"),
        ("SQ-CARS", [PART, PART, YES, YES, "AMD cards"], "none", "4"),
        ("QiController", [NO, NO, NO, YES, NO], "GPL-3.0 (client)", "5"),
    ]
    W, H = 1200, 700
    s = Svg(W, H)
    s.text(40, 48, "What each project publishes", 24, INK, weight="bold")
    s.lines(40, 76, ["Read from each project's public repositories on 2026-10-01."], 14, MUTED)
    x0, cw = 260, 128
    head_y = 130
    for i, (a, b) in enumerate(cols):
        cx = x0 + i * cw + cw / 2
        s.lines(cx, head_y, [a, b] if b else [a], 14, INK, "middle")
    s.text(x0 + len(cols) * cw + 20, head_y, "Licence", 14, INK)
    row_h = 56
    top = 170
    for r, (name, cells, licence, note) in enumerate(rows):
        y = top + r * row_h
        s.add(f'<line x1="40" y1="{y - 18}" x2="{W - 40}" y2="{y - 18}" stroke="{FAINT}" stroke-width="1"/>')
        s.text(40, y + 15, name, 16, INK, weight="bold")
        if note:
            s.text(40 + len(name) * 9.6 + 6, y + 8, note, 11, ACCENT)
        for c, kind in enumerate(cells):
            cx = x0 + c * cw + cw / 2
            if kind not in (YES, PART, NO, UNKNOWN):
                s.text(cx, y + 15, kind, 12, MUTED, "middle")
            else:
                glyph(s, cx, y + 10, kind)
        s.text(x0 + len(cols) * cw + 20, y + 15, licence, 14, INK if licence != "none" else ACCENT)
    yl = top + len(rows) * row_h - 4
    s.add(f'<line x1="40" y1="{yl - 14}" x2="{W - 40}" y2="{yl - 14}" stroke="{FAINT}" stroke-width="1"/>')
    glyph(s, 48, yl + 12, YES)
    s.text(62, yl + 17, "public", 13, MUTED)
    glyph(s, 150, yl + 12, PART)
    s.text(164, yl + 17, "partly", 13, MUTED)
    glyph(s, 252, yl + 12, NO)
    s.text(266, yl + 17, "not public", 13, MUTED)
    s.text(386, yl + 17, "Text: the project runs on boards it did not design (AMD evaluation cards, or QubiC's)", 13, MUTED)
    notes = [
        "1  Hardware randomized compiling and parameterized circuit execution: HDL not found in any public branch.",
        "2  tProcessor v2 bitstreams are served from a SLAC web directory, not the repository. Board files: ZCU111 only.",
        "3  No licence file, so the code is visible but no right to reuse it is granted.",
        "4  The block design is public; the custom RTL modules it instantiates are not in the repository.",
        "5  The Python client is GPL-3.0; its README says development happens on an internal KIT GitLab.",
        "All six instantiate AMD's RF Data Converter and Zynq IP, which Vivado generates and which is not open.",
    ]
    s.lines(40, yl + 58, notes, 13, MUTED, leading=1.55)
    s.save(
        "openness.svg",
        "What each project publishes",
        "A table of six projects against gateware source, build scripts, bitstreams, host software, board "
        "designs and licence. QubiC: all public, BSD-3 (LBNL). QICK: all public except partial board files, "
        "MIT. FIREQ: bitstreams and software only, AGPL-3.0. RISC-Q: source and scripts, no bitstreams, no "
        "licence. SQ-CARS: partial gateware, bitstreams and software, no licence. QiController: client "
        "software only, GPL-3.0.",
    )


# ---------------------------------------------------------------------------
# Figure 3. What each feedback-latency number counts
# ---------------------------------------------------------------------------

def figure_feedback():
    segs = [
        ("A", ["readout", "integration"]),
        ("B", ["ADC and", "readout DSP"]),
        ("C", ["state", "decision"]),
        ("D", ["branch in", "sequencer"]),
        ("E", ["pulse out", "and DAC"]),
        ("F", ["cables and", "fridge"]),
    ]
    I, O, Q = "in", "out", "?"
    rows = [
        ("QICK, tProc v1, ZCU111", "184 to 211 ns", "Stefanazzi 2022, Table II", [O, I, I, I, I, O]),
        ("QubiC 2.0", "150 ns, total less readout", "Hashim 2025, App. C", [O, I, I, I, I, Q]),
        ("QubiC, third-party", "205 ns, one branch", "Giortamis 2026, Table II", [O, I, I, I, I, Q]),
        ("QiController, ZCU111", "428 ns", "Gebauer 2020", [O, I, I, I, I, O]),
        ("SQ-CARS, loopback only", "250 ns, no decision", "Singhal 2023, Sec. III", [O, I, O, O, I, O]),
        ("RISC-Q, 3 boards", "446 ns, adds a decoder", "Liu 2026, Fig. 8", [O, Q, Q, I, Q, O]),
        ("FIREQ", "not reported", "La Capra 2026", None),
    ]
    W, H = 1200, 860
    s = Svg(W, H)
    s.text(40, 48, "What each feedback-latency number counts", 24, INK, weight="bold")
    s.lines(
        40, 76,
        [
            "A measurement-conditioned pulse passes through six stages. Each published number covers a",
            "different subset, so they cannot be ranked against one another.",
        ],
        14, MUTED,
    )
    x0, cw = 470, 112
    ys = 120
    for i, (letter, label) in enumerate(segs):
        x = x0 + i * cw
        s.rect(x + 4, ys, cw - 8, 92, FILL, INK)
        s.text(x + cw / 2, ys + 28, letter, 20, ACCENT, "middle", "bold")
        s.lines(x + cw / 2, ys + 54, label, 12, INK, "middle")
        if i < len(segs) - 1:
            s.path(f"M{x + cw - 4},{ys + 46} H{x + cw + 3}", INK, 1.5)
    s.path(
        f"M{x0 + 6 * cw - 4},{ys + 80} h14 V{ys + 112} H{x0 - 10} V{ys + 80} h12",
        MUTED, 1.2, "5 4",
    )
    s.text(x0 - 20, ys + 132, "the next pulse reaches the qubit", 12, MUTED, "start")
    s.lines(
        40, ys + 22,
        ["Stages", "A: the measurement itself", "B to E: the controller", "F: the wiring"],
        13, MUTED, leading=1.5,
    )
    top = 300
    row_h = 62
    for r, (name, value, source, cells) in enumerate(rows):
        y = top + r * row_h
        s.add(f'<line x1="40" y1="{y - 22}" x2="{W - 40}" y2="{y - 22}" stroke="{FAINT}" stroke-width="1"/>')
        s.text(40, y, name, 15, INK, weight="bold")
        s.text(40, y + 21, f"{value}  ({source})", 12, MUTED)
        if cells is None:
            s.text(x0 + 3 * cw, y + 8, "no feedback latency reported", 13, MUTED, "middle", style="italic")
            continue
        for c, kind in enumerate(cells):
            cx = x0 + c * cw + cw / 2
            if kind == I:
                s.circle(cx, y + 4, 9, ACCENT, ACCENT)
            elif kind == O:
                s.circle(cx, y + 4, 9, PAPER, INK)
            else:
                s.text(cx, y + 10, "?", 17, MUTED, "middle")
    yl = top + len(rows) * row_h - 12
    s.add(f'<line x1="40" y1="{yl - 10}" x2="{W - 40}" y2="{yl - 10}" stroke="{FAINT}" stroke-width="1"/>')
    s.circle(50, yl + 16, 9, ACCENT, ACCENT)
    s.text(66, yl + 21, "counted", 13, MUTED)
    s.circle(160, yl + 16, 9, PAPER, INK)
    s.text(176, yl + 21, "not counted", 13, MUTED)
    s.text(300, yl + 22, "?", 17, MUTED, "middle")
    s.text(316, yl + 21, "the source does not say", 13, MUTED)
    s.lines(
        40, yl + 58,
        [
            "Loopback measurements (QICK, SQ-CARS, RISC-Q) run a short cable from DAC to ADC in place of fridge wiring.",
            "RISC-Q's number is decoding feedback for a distance-3 surface code across three boards, two network hops included.",
            "Each row is the source's own definition; the README gives the wording.",
        ],
        13, MUTED, leading=1.55,
    )
    s.save(
        "feedback-latency.svg",
        "What each feedback-latency number counts",
        "Six stages of a feedback loop, A readout integration, B ADC and readout DSP, C state decision, "
        "D branch in the sequencer, E pulse out and DAC, F cables and fridge, against seven published "
        "numbers. None counts the readout integration. QICK 184 to 211 ns counts B to E. QubiC 150 ns "
        "counts B to E and does not say about F. A third-party QubiC measurement, 205 ns, counts B to E. "
        "QiController 428 ns counts B to E. SQ-CARS 250 ns counts only B and E, with no decision. RISC-Q "
        "446 ns counts the branch and adds a decoder, with B, C and E not stated. FIREQ reports none.",
    )


if __name__ == "__main__":
    figure_sequencers()
    figure_openness()
    figure_feedback()
    for name in sorted(OUT.glob("*.svg")):
        print(name.relative_to(OUT.parent))
