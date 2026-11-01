#!/usr/bin/env python3
"""Builds assets/hero-dark.svg and assets/hero-light.svg, the animated profile banner.

GitHub shows README SVGs as <img>: no scripts and no external fonts. So the font is subset to the
glyphs actually used and inlined as base64 WOFF2, and all motion is CSS, which also lets
prefers-reduced-motion freeze it on its final frame.

Usage: .venv/bin/python scripts/build_hero.py
"""
import base64
import io
from pathlib import Path

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / "assets" / "fonts" / "JetBrainsMono[wght].ttf"
W, H = 1000, 360
X0, X1 = 48, 952

PALETTES = {
    "dark": dict(bg="#0C0E0D", grid="#262B28", ink="#ECEAE3", muted="#8E938F", faint="#2E3330", accent="#FF6B2C"),
    "light": dict(bg="#F6F4EE", grid="#DDD9CE", ink="#151716", muted="#5B5F5C", faint="#D4D0C4", accent="#C2410C"),
}

TICKER = [
    "Seek · vector search used at 33 Indian airports",
    "650K alerts and 1.3M embeddings a day",
    "UVIP · React 19 rebuild, 300+ typed endpoints",
    "ClickHouse pipeline · 20M+ events a day",
]
STAGES = ["events", "kafka", "embed", "milvus", "grpc", "react"]
BAR_X, BAR_W = 668, 284
BEFORE = 0.58  # share of alerts searchable before Seek (after: all of them), drawn to scale


def font_face(weight: int, text: str) -> str:
    font = instantiateVariableFont(TTFont(FONT), {"wght": weight})
    opts = subset.Options()
    opts.flavor, opts.layout_features, opts.name_IDs = "woff2", ["kern"], []
    sub = subset.Subsetter(opts)
    sub.populate(text=text)
    sub.subset(font)
    buf = io.BytesIO()
    font.flavor = "woff2"
    font.save(buf)
    b64 = base64.b64encode(buf.getvalue()).decode()
    return f"@font-face{{font-family:J;font-weight:{weight};src:url(data:font/woff2;base64,{b64}) format('woff2')}}"


def body(p: dict) -> str:
    lines = "\n".join(
        f'<text class="tick t{i}" x="{X0 + 26}" y="258">{t}</text>' for i, t in enumerate(TICKER)
    )
    step = (X1 - X0) / (len(STAGES) - 1)
    nodes, labels = [], []
    for i, s in enumerate(STAGES):
        x = X0 + i * step
        anchor = "start" if i == 0 else "end" if i == len(STAGES) - 1 else "middle"
        nodes.append(f'<rect x="{x - 3.5:.1f}" y="{306 - 3.5}" width="7" height="7" fill="{p["ink"]}"/>')
        labels.append(f'<text class="lab" x="{x:.1f}" y="334" text-anchor="{anchor}">{s}</text>')
    pulses = "\n".join(
        f'<g class="pulse" style="animation-delay:{-i * 4 / 3:.2f}s"><circle cx="{X0}" cy="306" r="9" fill="{p["accent"]}" opacity=".18"/>'
        f'<circle cx="{X0}" cy="306" r="3.5" fill="{p["accent"]}"/></g>'
        for i in range(3)
    )
    return f"""
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="16" fill="{p['bg']}" stroke="{p['faint']}"/>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="16" fill="url(#dots)" mask="url(#fade)"/>
<text class="cap" x="{X0}" y="58">SYSTEMS + PRODUCT ENGINEER</text>
<text class="cap" x="{X1}" y="58" text-anchor="end">SDE II · AWIROS · NEW DELHI</text>
<text class="name" x="{X0 - 3}" y="146">Aryan Teng</text>
<rect class="cursor" x="478" y="92" width="22" height="60" fill="{p['accent']}"/>
<text class="role" x="{X0}" y="190">Real-time AI systems, end to end.</text>
<text class="stack" x="{X0}" y="220">Go · Kafka · Milvus · ClickHouse · React</text>
<text class="prompt" x="{X0}" y="258">▸</text>
{lines}
<text class="cap" x="600" y="110">ALERTS SEARCHABLE · SEEK</text>
<text class="val v0" x="600" y="148">58%</text>
<rect x="{BAR_X}" y="134" width="{BAR_W * BEFORE:.1f}" height="16" fill="{p['faint']}"/>
<text class="val v1" x="600" y="182">100%</text>
<rect class="bar" x="{BAR_X}" y="168" width="{BAR_W}" height="16" fill="{p['accent']}"/>
<text class="lab" x="600" y="214">natural-language search over every alert</text>
<line x1="{X0}" y1="306" x2="{X1}" y2="306" stroke="{p['faint']}" stroke-width="1.5"/>
{"".join(nodes)}
{pulses}
{"".join(labels)}"""


def svg(theme: str, faces: str) -> str:
    p = PALETTES[theme]
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
<title id="t">Aryan Teng: systems and product engineer</title>
<desc id="d">Real-time AI systems, end to end. Seek vector search, used at 33 Indian airports, made every alert searchable (up from 58%) at 650K alerts and 1.3M embeddings a day.</desc>
<defs>
<pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="12" cy="12" r="1" fill="{p['grid']}"/></pattern>
<linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity=".05"/><stop offset="1" stop-color="#fff" stop-opacity=".9"/></linearGradient>
<mask id="fade"><rect width="{W}" height="{H}" fill="url(#g)"/></mask>
<style>{faces}
text{{font-family:J,ui-monospace,monospace;fill:{p['ink']}}}
.cap{{font-size:13px;font-weight:400;letter-spacing:2.5px;fill:{p['muted']}}}
.name{{font-size:76px;font-weight:800;letter-spacing:-3px}}
.role{{font-size:22px;font-weight:400}}
.stack{{font-size:17px;fill:{p['muted']}}}
.prompt{{font-size:19px;fill:{p['accent']}}}
.tick{{font-size:19px;opacity:0;animation:tick 12s linear infinite backwards}}
.t0{{opacity:1}}.t1{{animation-delay:3s}}.t2{{animation-delay:6s}}.t3{{animation-delay:9s}}
.val{{font-size:18px;font-weight:700}}.v0{{fill:{p['muted']}}}.v1{{fill:{p['accent']}}}
.lab{{font-size:13px;fill:{p['muted']}}}
.bar{{transform-box:fill-box;transform-origin:left;animation:grow 7s cubic-bezier(.2,.8,.2,1) infinite}}
.cursor{{animation:blink 1.1s steps(1) infinite}}
.pulse{{animation:flow 4s linear infinite}}
@keyframes tick{{0%{{opacity:0;transform:translateY(8px)}}2%,23%{{opacity:1;transform:none}}25%,100%{{opacity:0;transform:translateY(-8px)}}}}
@keyframes grow{{0%,10%{{transform:scaleX({BEFORE})}}34%,92%{{transform:scaleX(1);opacity:1}}96%{{opacity:0}}100%{{transform:scaleX({BEFORE});opacity:0}}}}
@keyframes blink{{50%{{opacity:0}}}}
@keyframes flow{{from{{transform:translateX(0)}}to{{transform:translateX({X1 - X0}px)}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}.pulse{{display:none}}}}
</style>
</defs>{body(p)}
</svg>
"""


def main() -> None:
    glyphs = "".join(sorted(set(body(PALETTES["dark"]) + "ui-monospace"))) + "ASDEIWRONLHYTPUC"
    faces = "".join(font_face(w, glyphs) for w in (400, 700, 800))
    for theme in PALETTES:
        out = ROOT / "assets" / f"hero-{theme}.svg"
        out.write_text(svg(theme, faces))
        print(f"{out.relative_to(ROOT)}: {out.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
