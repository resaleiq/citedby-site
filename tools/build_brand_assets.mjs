// Renders favicon PNG/ICO, touch icons and the OG image from public/favicon.svg and public/brand/*v4*.svg (RES-1335 S2).
// Run: node tools/build_brand_assets.mjs   (needs playwright-core and chrome-headless-shell, same pins as company/bin/qa-lib.mjs)
import { createRequire } from "node:module";
import { homedir } from "node:os";
import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";
import { readFileSync, writeFileSync, unlinkSync } from "node:fs";
const require = createRequire(join(homedir(), "work/company/qa-lab/package.json"));
const { chromium } = require("playwright-core");
const CHROME = process.env.CHROME || join(homedir(), "Library/Caches/ms-playwright/chromium_headless_shell-1217/chrome-headless-shell-mac-x64/chrome-headless-shell");
const PUB = join(dirname(fileURLToPath(import.meta.url)), "..", "public");
const fav = readFileSync(join(PUB, "favicon.svg"), "utf8");
const lock = readFileSync(join(PUB, "brand/citedby-lockup-v4-reverse.svg"), "utf8").replace(/ width="\d+" height="\d+"/, ' width="440" height="92"');
const b = await chromium.launch({ executablePath: CHROME, headless: true });
async function png(html, w, h, out, transparent = false) {
  const p = await b.newPage({ viewport: { width: w, height: h } });
  await p.setContent(html); await p.evaluate(() => document.fonts.ready);
  const buf = await p.screenshot({ omitBackground: transparent, clip: { x: 0, y: 0, width: w, height: h } });
  writeFileSync(join(PUB, out), buf); await p.close(); return buf;
}
const icon = (s, pad, bg) => `<body style="margin:0;background:${bg};width:${s}px;height:${s}px;display:grid;place-items:center"><div style="width:${s - 2 * pad}px;height:${s - 2 * pad}px">${fav.replace(/ width="32" height="32"/, ' width="100%" height="100%"')}</div></body>`;
const b16 = await png(icon(16, 0, "transparent"), 16, 16, "favicon-16.png", true);
const b32 = await png(icon(32, 0, "transparent"), 32, 32, "favicon-32.png", true);
const b48 = await png(icon(48, 0, "transparent"), 48, 48, "favicon-48.png", true);
await png(icon(180, 22, "#0F1B2D"), 180, 180, "apple-touch-icon.png");
await png(icon(192, 24, "#0F1B2D"), 192, 192, "icon-192.png");
// ICO with embedded PNGs (16, 32, 48)
const imgs = [[16, b16], [32, b32], [48, b48]];
const head = Buffer.alloc(6 + 16 * imgs.length); head.writeUInt16LE(0, 0); head.writeUInt16LE(1, 2); head.writeUInt16LE(imgs.length, 4);
let off = head.length; imgs.forEach(([s, buf], i) => { const o = 6 + 16 * i; head[o] = s; head[o + 1] = s; head.writeUInt16LE(1, o + 4); head.writeUInt16LE(32, o + 6); head.writeUInt32LE(buf.length, o + 8); head.writeUInt32LE(off, o + 12); off += buf.length; });
writeFileSync(join(PUB, "favicon.ico"), Buffer.concat([head, ...imgs.map(i => i[1])]));
const ff = (n, w) => `@font-face{font-family:Newsreader;font-weight:${w};src:url(file://${PUB}/fonts/${n}.woff2)}`;
const og = `<style>${ff("newsreader-latin-600-normal", 600)}${ff("newsreader-latin-400-normal", 400)}@font-face{font-family:Plex;font-weight:400;src:url(file://${PUB}/fonts/ibm-plex-sans-latin-400-normal.woff2)}@font-face{font-family:Plex;font-weight:600;src:url(file://${PUB}/fonts/ibm-plex-sans-latin-600-normal.woff2)}
body{margin:0;width:1200px;height:630px;background:#0F1B2D;color:#E8EDF4;position:relative;overflow:hidden}
.l{position:absolute;left:72px;top:56px}.u{position:absolute;right:72px;top:76px;font:400 26px Plex,sans-serif;color:#C9D2DF}
.k{position:absolute;left:72px;top:176px;font:600 20px Plex,sans-serif;letter-spacing:.14em;color:#9AA6B8}
.h{position:absolute;left:72px;top:212px;width:1056px;font:600 72px/1.06 Newsreader,Georgia,serif;letter-spacing:-.02em}
.h u{text-decoration:none;box-shadow:inset 0 -.2em 0 #4FD1C5}
.rows{position:absolute;left:72px;right:72px;top:420px}.r{height:22px;border-radius:4px;background:#2A374D;margin-bottom:12px}
.f{height:64px;border-radius:6px;background:#4FD1C5;color:#0F1B2D;display:flex;align-items:center;padding:0 24px;font:600 26px Plex,sans-serif;margin-bottom:12px}
.f b{font-size:18px;letter-spacing:.14em;margin-right:22px}.f i{margin-left:auto;font-style:normal}
.n{position:absolute;left:72px;bottom:16px;font:400 18px Plex,sans-serif;color:#9AA6B8}</style><body><div class="l">${lock}</div><div class="u">citedby.eu</div>
<div class="k">WEBSITE AUDIT · THE FIX, WRITTEN FOR YOUR PAGE</div><div class="h">300 errors. Here is <u>the one</u> to fix first.</div>
<div class="rows"><div class="r" style="width:92%"></div><div class="f"><b>FIX THIS FIRST</b>Pages return an error status<i>85 pages</i></div><div class="r" style="width:78%"></div><div class="r" style="width:64%"></div></div>
<div class="n">Real crawl of plausible.io, 21 Oct 2026. Not a customer.</div></body>`;
const ogBuf = await png(og, 1200, 630, "og-v2.png"); writeFileSync(join(PUB, "og.png"), ogBuf); // og.png still sold the retired product (READINESS gap 2)
unlinkSync(join(PUB, "favicon-48.png")); // only inside the ICO
await b.close();
console.log("brand assets written to", PUB);
