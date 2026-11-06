import os, subprocess, sys, html
sys.path.insert(0, os.path.dirname(__file__))
import importlib; POSTS = importlib.import_module(os.environ.get("POSTS_MODULE", "posts")).POSTS

OUT = os.environ.get("OUT_DIR", "/tmp/ig-out")
TMP = os.environ.get("TMP_DIR", "/tmp/ig-tmp")
os.makedirs(TMP, exist_ok=True); os.makedirs(OUT, exist_ok=True)

NAVY = "#0A1A33"; NAVY2 = "#10264A"; BLUE = "#2F7BFF"; LIGHT = "#F3F6FB"; INK = "#0A1A33"; MUTED = "#5B6B85"

CSS = f"""
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:1080px;height:1350px;overflow:hidden}}
body{{font-family:'Inter Display','Inter',sans-serif;-webkit-font-smoothing:antialiased}}
.s{{position:relative;width:1080px;height:1350px;padding:84px 90px;display:flex;flex-direction:column}}
.dark{{background:{NAVY};color:#fff}}
.dark::before{{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:54px 54px}}
.dark::after{{content:"";position:absolute;width:900px;height:900px;right:-380px;top:-380px;background:radial-gradient(circle,rgba(47,123,255,.34),transparent 62%)}}
.light{{background:{LIGHT};color:{INK}}}
.light::after{{content:"";position:absolute;left:0;bottom:0;width:100%;height:10px;background:{BLUE}}}
.s>*{{position:relative;z-index:2}}
.hd{{display:flex;justify-content:space-between;align-items:center}}
.wm{{font-weight:700;font-size:38px;letter-spacing:-.02em}}
.wm span{{color:{BLUE}}}
.cnt{{font-family:'DejaVu Sans Mono',monospace;font-size:24px;opacity:.55;letter-spacing:.05em}}
.body{{flex:1;display:flex;flex-direction:column;justify-content:center}}
.kick{{font-family:'DejaVu Sans Mono',monospace;font-size:26px;letter-spacing:.14em;text-transform:uppercase;color:{BLUE};margin-bottom:34px;display:flex;align-items:center;gap:18px}}
.kick::before{{content:"";width:46px;height:3px;background:{BLUE}}}
h1{{font-size:104px;line-height:1.02;font-weight:700;letter-spacing:-.035em}}
h2{{font-size:78px;line-height:1.06;font-weight:700;letter-spacing:-.03em}}
h1 b,h2 b{{color:{BLUE};font-weight:700}}
.sub{{font-size:40px;line-height:1.35;margin-top:44px;opacity:.72;font-weight:400;max-width:860px}}
.ft{{display:flex;justify-content:space-between;align-items:center;font-size:28px;font-weight:500}}
.ft .h{{opacity:.6}}
.ft .sw{{display:flex;align-items:center;gap:14px;color:{BLUE};font-weight:600}}
.num{{font-family:'DejaVu Sans Mono',monospace;font-size:200px;font-weight:700;color:{BLUE};line-height:1;letter-spacing:-.04em;margin-bottom:40px}}
.pbody{{font-size:44px;line-height:1.4;color:{MUTED};margin-top:40px;max-width:880px}}
.dark .pbody{{color:rgba(255,255,255,.72)}}
ul.li{{list-style:none;margin-top:56px}}
ul.li li{{font-size:42px;line-height:1.3;padding:26px 0;border-top:2px solid rgba(10,26,51,.1);display:flex;gap:28px;align-items:baseline;font-weight:500}}
.dark ul.li li{{border-top-color:rgba(255,255,255,.12)}}
ul.li li::before{{content:"";flex:0 0 18px;height:18px;background:{BLUE};border-radius:4px;transform:translateY(-4px)}}
.cta{{display:inline-flex;align-self:flex-start;margin-top:64px;background:{BLUE};color:#fff;font-size:44px;font-weight:700;padding:30px 52px;border-radius:999px;letter-spacing:-.01em}}
.big .pre{{font-size:40px;color:{MUTED};line-height:1.35}}
.dark.big .pre{{color:rgba(255,255,255,.7)}}
.big .n{{font-size:190px;font-weight:800;letter-spacing:-.05em;line-height:1;margin:36px 0 26px;color:{BLUE}}}
.big .post{{font-size:52px;font-weight:600}}
.note{{font-size:26px;opacity:.5;margin-top:60px}}
.opt{{display:flex;align-items:center;gap:36px;background:#fff;border-radius:28px;padding:34px 40px;margin-top:26px;font-size:42px;font-weight:600;box-shadow:0 2px 0 rgba(10,26,51,.06)}}
.dark .opt{{background:rgba(255,255,255,.06);border:2px solid rgba(255,255,255,.1)}}
.opt .l{{flex:0 0 84px;height:84px;border-radius:22px;background:{BLUE};color:#fff;display:flex;align-items:center;justify-content:center;font-size:44px;font-weight:800}}
.chat{{background:#0E2245;border-radius:40px;padding:50px 44px;margin-top:10px;border:2px solid rgba(255,255,255,.08)}}
.chat .top{{display:flex;align-items:center;gap:22px;padding-bottom:30px;border-bottom:2px solid rgba(255,255,255,.08);margin-bottom:24px}}
.chat .av{{width:76px;height:76px;border-radius:50%;background:{BLUE};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:34px}}
.chat .nm{{font-size:34px;font-weight:700}} .chat .st{{font-size:24px;color:#5BE38C}}
.m{{max-width:78%;padding:24px 30px;border-radius:30px;font-size:34px;line-height:1.35;margin-top:22px}}
.m small{{display:block;font-size:22px;opacity:.55;margin-top:10px;font-family:'DejaVu Sans Mono',monospace}}
.m.in{{background:rgba(255,255,255,.1);border-bottom-left-radius:8px}}
.m.out{{background:{BLUE};margin-left:auto;border-bottom-right-radius:8px;text-align:left}}
.cfoot{{font-size:40px;font-weight:600;margin-top:48px}}
.cmp li::before{{content:"✕" !important;background:none !important;color:#E5484D;font-weight:800;font-size:40px;flex:0 0 40px !important;height:auto !important;transform:none !important}}
.cmp.good li::before{{content:"✓" !important;color:{BLUE}}}
"""

def wm():
    return '<div class="wm">Launch<span>code</span></div>'

def slide_html(p, s, i, total):
    t = s["t"]
    dark = t in ("cover", "cta", "chat") or (t == "big" and i == 2) or (t == "compare" and not s.get("bad"))
    if t == "poll": dark = False
    cls = "dark" if dark else "light"
    last = i == total
    hd = f'<div class="hd">{wm()}<div class="cnt">{i:02d} / {total:02d}</div></div>' if total > 1 else f'<div class="hd">{wm()}<div class="cnt">@launchcod</div></div>'
    sw = '' if last else '<div class="sw">Arrasta <span style="font-size:34px">→</span></div>'
    ft = f'<div class="ft"><div class="h">@launchcod</div>{sw}</div>' if total > 1 else '<div class="ft"><div class="h">launchcode.com.br</div></div>'
    k = lambda: f'<div class="kick">{s["kick"] if "kick" in s else s.get("kicker","")}</div>' if s.get("kicker") else ''
    if t == "cover":
        body = f'{k()}<h1>{s["title"]}</h1><div class="sub">{s["sub"]}</div>'
    elif t == "point":
        body = f'<div class="num">{s["n"]}</div><h2>{s["title"]}</h2><div class="pbody">{s["body"]}</div>'
    elif t == "list":
        items = "".join(f"<li>{x}</li>" for x in s["items"])
        body = f'{k()}<h2>{s["title"]}</h2><ul class="li">{items}</ul>'
    elif t == "compare":
        items = "".join(f"<li>{x}</li>" for x in s["items"])
        good = "" if s["bad"] else " good"
        body = f'{k()}<h2>{"O problema" if s["bad"] else "A solução"}</h2><ul class="li cmp{good}">{items}</ul>'
    elif t == "big":
        cls += " big"
        note = f'<div class="note">{s["note"]}</div>' if s.get("note") else ''
        body = f'{k()}<div class="pre">{s["pre"]}</div><div class="n">{s["num"]}</div><div class="post">{s["post"]}</div>{note}'
    elif t == "cta":
        body = f'<h1 style="font-size:96px">{s["title"]}</h1><div class="sub">{s["body"]}</div><div class="cta">{s["action"]}</div>'
    elif t == "poll":
        opts = "".join(f'<div class="opt"><div class="l">{a}</div>{b}</div>' for a, b in s["options"])
        body = f'{k()}<h2 style="font-size:72px;margin-bottom:30px">{s["title"]}</h2>{opts}<div class="cfoot" style="color:{BLUE}">{s["action"]} ↓</div>'
    elif t == "chat":
        ms = "".join(f'<div class="m {d}">{html.escape(txt)}<small>{tm}</small></div>' for d, tm, txt in s["msgs"])
        body = f'<div class="chat"><div class="top"><div class="av">N</div><div><div class="nm">NeXo · Atendimento</div><div class="st">● online agora</div></div></div>{ms}</div><div class="cfoot">{s["foot"]}</div>'
    return f'<!DOCTYPE html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="s {cls}">{hd}<div class="body">{body}</div>{ft}</div></body></html>'

def render():
    files = []
    for p in POSTS:
        total = len(p["slides"])
        for i, s in enumerate(p["slides"], 1):
            name = f'{p["slug"]}-{i:02d}'
            hp = f"{TMP}/{name}.html"; png = f"{TMP}/{name}.png"; jpg = f"{OUT}/{name}.jpg"
            open(hp, "w").write(slide_html(p, s, i, total))
            subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                            "--force-device-scale-factor=1", f"--screenshot={png}", "--window-size=1080,1350", f"file://{hp}"],
                           check=True, capture_output=True)
            subprocess.run(["convert", png, "-quality", "92", jpg], check=True)
            files.append(jpg)
    print(len(files), "imagens")

if __name__ == "__main__":
    render()
