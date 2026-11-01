#!/usr/bin/env python3
"""Builds assets/hero-dark.svg and assets/hero-light.svg, the animated profile banner.

GitHub shows README SVGs as <img>: no scripts and no external fonts. So both fonts are subset to
the glyphs actually used and inlined as base64 WOFF2, and all motion is CSS, which also lets
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
FONTS = ROOT / "assets" / "fonts"
DISPLAY, MONO = FONTS / "SpaceGrotesk[wght].ttf", FONTS / "JetBrainsMono[wght].ttf"
W, H = 1000, 360
X0, X1 = 48, 952

PALETTES = {
    "dark": dict(bg="#0C0E0D", tile="#131614", grid="#262B28", ink="#ECEAE3", muted="#8E938F", faint="#2E3330", accent="#FF6B2C"),
    "light": dict(bg="#F6F4EE", tile="#EFECE4", grid="#DDD9CE", ink="#151716", muted="#5B5F5C", faint="#D4D0C4", accent="#C2410C"),
}

CAPTION_L, CAPTION_R = "FULL-STACK PRODUCT ENGINEER", "SDE II AT AWIROS · EX-FOUNDING ENGINEER"
NAME = "Aryan Teng"
ROLE = ("I build products from zero to production,", "from Figma to the customer site.")
STACK = "React · TypeScript · React Native · Node.js · Go · Kafka"
# Impact lines, one per product; every figure is on the published resume.
TICKER = [
    "Founding engineer at Enveave · 0-to-1 MVP with the founders",
    "UVIP · React 19 rebuild, 31 modules, 300+ typed APIs",
    "CV apps · per-app images, deploys 90%+ faster",
    "Developer Mode · live-mounted source, alerts in real time",
    "Seek · search at 33 Indian airports, 51 s → 4.7 s",
    "Delhi IGI · 9,189 e-challans filed with Delhi Traffic Police",
    "ClickHouse · 20M+ events a day",
]
# Things built and shipped at Awiros, product first.
CHIPS = [
    "UVIP platform rebuild", "CV app delivery",
    "Developer Mode", "Seek vector search",
    "Enterprise SSO", "IGI airport ops suite",
    "Two mobile apps", "Event pipeline",
]
STAGES = ["idea", "figma", "react", "api", "data", "deploy", "on-site"]
CHIP_X, CHIP_Y, CHIP_W, CHIP_H, GAP = 572, 110, 184, 30, 8
STEP = 3  # seconds each ticker line stays up


def font_face(path: Path, family: str, weight: int, text: str) -> str:
    font = instantiateVariableFont(TTFont(path), {"wght": weight})
    opts = subset.Options()
    opts.flavor, opts.layout_features, opts.name_IDs = "woff2", ["kern"], []
    sub = subset.Subsetter(opts)
    sub.populate(text=text)
    sub.subset(font)
    buf = io.BytesIO()
    font.flavor = "woff2"
    font.save(buf)
    b64 = base64.b64encode(buf.getvalue()).decode()
    return f"@font-face{{font-family:{family};font-weight:{weight};src:url(data:font/woff2;base64,{b64}) format('woff2')}}"


def body(p: dict) -> str:
    chips = [f'<text class="cap" x="{CHIP_X}" y="{CHIP_Y - 14}">BUILT AND SHIPPED</text>']
    for i, name in enumerate(CHIPS):
        x = CHIP_X + (i % 2) * (CHIP_W + GAP)
        y = CHIP_Y + (i // 2) * (CHIP_H + GAP)
        chips.append(
            f'<g class="chip" style="animation-delay:{0.15 + i * 0.08:.2f}s">'
            f'<rect x="{x}" y="{y}" width="{CHIP_W}" height="{CHIP_H}" rx="8" fill="{p["tile"]}" stroke="{p["faint"]}"/>'
            f'<circle cx="{x + 14}" cy="{y + CHIP_H / 2}" r="3" fill="{p["accent"]}"/>'
            f'<text class="chipt" x="{x + 26}" y="{y + 20}">{name}</text></g>'
        )
    ticks = "\n".join(
        f'<text class="tick{" t0" if i == 0 else ""}" x="{X0 + 24}" y="276" style="animation-delay:{i * STEP}s">{t}</text>'
        for i, t in enumerate(TICKER)
    )
    step = (X1 - X0) / (len(STAGES) - 1)
    nodes, labels = [], []
    for i, s in enumerate(STAGES):
        x = X0 + i * step
        anchor = "start" if i == 0 else "end" if i == len(STAGES) - 1 else "middle"
        nodes.append(f'<rect x="{x - 3.5:.1f}" y="{310 - 3.5}" width="7" height="7" fill="{p["ink"]}"/>')
        labels.append(f'<text class="lab" x="{x:.1f}" y="338" text-anchor="{anchor}">{s}</text>')
    pulses = "".join(
        f'<g class="pulse" style="animation-delay:{-i * 4 / 3:.2f}s"><circle cx="{X0}" cy="310" r="9" fill="{p["accent"]}" opacity=".18"/>'
        f'<circle cx="{X0}" cy="310" r="3.5" fill="{p["accent"]}"/></g>'
        for i in range(3)
    )
    return f"""
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="16" fill="{p['bg']}" stroke="{p['faint']}"/>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="16" fill="url(#dots)" mask="url(#fade)"/>
<text class="cap" x="{X0}" y="56">{CAPTION_L}</text>
<text class="cap" x="{X1}" y="56" text-anchor="end">{CAPTION_R}</text>
<text class="name" x="{X0 - 3}" y="136">{NAME}<tspan class="dot">.</tspan></text>
<text class="role" x="{X0}" y="178">{ROLE[0]}</text>
<text class="role dim" x="{X0}" y="206">{ROLE[1]}</text>
<text class="stack" x="{X0}" y="240">{STACK}</text>
<text class="prompt" x="{X0}" y="276">▸</text>
{ticks}
{"".join(chips)}
<line x1="{X0}" y1="310" x2="{X1}" y2="310" stroke="{p['faint']}" stroke-width="1.5"/>
{"".join(nodes)}{pulses}{"".join(labels)}"""


def svg(theme: str, faces: str) -> str:
    p = PALETTES[theme]
    n = len(TICKER)
    on = 100 / n  # share of the cycle each ticker line is visible
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-labelledby="t d">
<title id="t">Aryan Teng: full-stack product engineer, ex-founding engineer</title>
<desc id="d">I build products from zero to production, from Figma to the customer site. Built and shipped at Awiros: the UVIP platform rebuild, CV app delivery, Developer Mode, Seek vector search, enterprise SSO, the Delhi IGI airport operations suite, two mobile apps and a ClickHouse event pipeline. Previously founding engineer at Enveave.</desc>
<defs>
<pattern id="dots" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="12" cy="12" r="1" fill="{p['grid']}"/></pattern>
<linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity=".05"/><stop offset="1" stop-color="#fff" stop-opacity=".9"/></linearGradient>
<mask id="fade"><rect width="{W}" height="{H}" fill="url(#g)"/></mask>
<style>{faces}
text{{font-family:S,system-ui,sans-serif;fill:{p['ink']}}}
.cap,.stack,.lab,.prompt{{font-family:J,ui-monospace,monospace}}
.cap{{font-size:13px;letter-spacing:2.5px;fill:{p['muted']}}}
.name{{font-size:74px;font-weight:700;letter-spacing:-2.5px}}
.dot{{fill:{p['accent']}}}
.role{{font-size:23px;font-weight:500;letter-spacing:-.2px}}
.dim{{fill:{p['muted']}}}
.stack{{font-size:13.5px;fill:{p['muted']}}}
.prompt{{font-size:17px;fill:{p['accent']}}}
.tick{{font-size:18px;font-weight:500;opacity:0;animation:tick {n * STEP}s linear infinite backwards}}
.t0{{opacity:1}}
.chipt{{font-size:13.5px;font-weight:500}}
.lab{{font-size:11.5px;fill:{p['muted']}}}
.chip{{animation:rise .6s cubic-bezier(.2,.8,.2,1) both}}
.pulse{{animation:flow 4s linear infinite}}
@keyframes tick{{0%{{opacity:0;transform:translateY(8px)}}{on * .1:.2f}%,{on * .9:.2f}%{{opacity:1;transform:none}}{on:.2f}%,100%{{opacity:0;transform:translateY(-8px)}}}}
@keyframes rise{{from{{opacity:0;transform:translateY(10px)}}to{{opacity:1;transform:none}}}}
@keyframes flow{{from{{transform:translateX(0)}}to{{transform:translateX({X1 - X0}px)}}}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}.pulse{{display:none}}}}
</style>
</defs>{body(p)}
</svg>
"""


def main() -> None:
    display_text = NAME + "." + "".join(ROLE) + "".join(TICKER) + "".join(CHIPS)
    mono_text = CAPTION_L + CAPTION_R + "BUILT AND SHIPPED" + STACK + "".join(STAGES) + "▸"
    faces = "".join(
        [font_face(DISPLAY, "S", w, display_text) for w in (500, 700)]
        + [font_face(MONO, "J", 400, mono_text)]
    )
    for theme in PALETTES:
        out = ROOT / "assets" / f"hero-{theme}.svg"
        out.write_text(svg(theme, faces))
        print(f"{out.relative_to(ROOT)}: {out.stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
