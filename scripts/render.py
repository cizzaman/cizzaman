#!/usr/bin/env python3
"""Build self-contained profile SVGs with Python's standard library."""
import base64
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "profile.json").read_text())
PORTRAIT = base64.b64encode((ROOT / "assets/portrait.png").read_bytes()).decode()
BG, FG, MUTED, BLUE, GREEN, GOLD = "#10151d", "#dce4ed", "#8b9bae", "#8bc6eb", "#a5cfad", "#d9ba8c"


def text(x, y, value, size=18, color=FG, **attrs):
    extra = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in attrs.items())
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" {extra}>{html.escape(value)}</text>'


def line(x1, y, x2, color="#293342", dash=""):
    return f'<path d="M{x1} {y} H{x2}" fill="none" stroke="{color}" stroke-dasharray="{dash}"/>'


def portrait(x, y, w, h):
    return f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="data:image/png;base64,{PORTRAIT}" preserveAspectRatio="xMidYMid meet"/>'


def begin(width, height):
    return [f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
<title id="title">{DATA['name']} — @{DATA['handle']}</title>
<desc id="desc">A terminal-style profile with an ASCII portrait. Software, AI automation, and HYROX. Featured project: terminaltheme, matching themes for Terminal.app and Ghostty.</desc>
<defs><clipPath id="card"><rect width="{width}" height="{height}" rx="16"/></clipPath></defs>
<g clip-path="url(#card)" font-family="'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace">
<rect width="{width}" height="{height}" fill="{BG}"/>
<rect width="{width}" height="56" fill="#171f29"/>
<circle cx="27" cy="28" r="5" fill="#e28a88"/><circle cx="47" cy="28" r="5" fill="{GOLD}"/><circle cx="67" cy="28" r="5" fill="{GREEN}"/>
''', text(94, 34, "cizzaman@github: ~", 16, MUTED), line(0, 56, width)]


def section(x, y, label, end):
    return [text(x, y, label, 17, GREEN), line(x + len(label) * 10.2 + 18, y - 6, end)]


def rows(x, y, values, width, step=29, size=18):
    parts = []
    for label, value in values:
        parts.append(text(x, y, label, size, GOLD))
        parts.append(line(x + len(label) * size * .6 + 14, y - 4,
                          x + width - len(value) * size * .6 - 12,
                          "#354153", "1 6"))
        parts.append(text(x + width, y, value, size, BLUE, text_anchor="end"))
        y += step
    return parts


def footer(parts, width, height):
    parts.append(line(28, height - 63, width - 28))
    palette = ["#354153", "#e28a88", GOLD, GREEN, BLUE, "#b8a4d5", "#85c4bf", FG]
    for i, color in enumerate(palette):
        parts.append(f'<rect x="{28 + i * 22}" y="{height - 39}" width="22" height="13" fill="{color}"/>')
    parts.append(text(width - 29, height - 27, f"github since {DATA['since']}", 14, MUTED, text_anchor="end"))
    parts.extend(['</g>', f'<rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="16" fill="none" stroke="#303b4a"/>', '</svg>'])


def desktop():
    p = begin(1200, 744)
    p += [portrait(24, 101, 396, 528), text(222, 654, "@cizzaman", 17, MUTED, text_anchor="middle"),
          '<path d="M448 91 V650" stroke="#293342"/>',
          text(483, 106, "$ whoami", 17, GREEN),
          text(483, 148, DATA['name'], 30, FG, font_weight="600"),
          text(483, 179, DATA['focus'], 18, BLUE)]
    p += section(483, 227, "System", 1167)
    p += rows(483, 258, DATA['system'], 684)
    p += section(483, 387, "Interests", 1167)
    p += rows(483, 419, DATA['interests'], 684)
    p += section(483, 519, "Featured project", 1167)
    p += [text(483, 552, DATA['project']['name'], 22, BLUE, font_weight="600"),
          text(483, 581, DATA['project']['description'], 17, FG),
          text(483, 609, DATA['project']['stack'], 16, MUTED),
          text(483, 654, "$ build; automate; train", 17, GREEN),
          '<rect x="741" y="640" width="9" height="18" fill="#a5cfad"/>']
    footer(p, 1200, 744)
    return "\n".join(p)


def mobile():
    p = begin(600, 960)
    p += [portrait(22, 78, 174, 232),
          text(224, 120, "$ whoami", 17, GREEN),
          text(224, 163, "Christian", 28, FG, font_weight="600"),
          text(224, 198, "Landsnes", 28, FG, font_weight="600"),
          text(224, 235, "@cizzaman", 19, BLUE),
          text(224, 274, "Software / AI / HYROX", 16, MUTED)]
    p += section(28, 347, "System", 572)
    p += rows(28, 383, DATA['system'], 544, step=32, size=19)
    p += section(28, 532, "Interests", 572)
    p += rows(28, 570, DATA['interests'], 544, step=32, size=18)
    p += section(28, 686, "Featured project", 572)
    p += [text(28, 724, DATA['project']['name'], 25, BLUE, font_weight="600"),
          text(28, 758, "Matching themes for", 19),
          text(28, 786, "Terminal.app + Ghostty", 19),
          text(28, 822, DATA['project']['stack'], 17, MUTED),
          text(28, 869, "$ build; automate; train", 17, GREEN)]
    footer(p, 600, 960)
    return "\n".join(p)


for name, render in [("profile.svg", desktop), ("profile-mobile.svg", mobile)]:
    (ROOT / "assets" / name).write_text(render())
    print(f"Rendered assets/{name}")
