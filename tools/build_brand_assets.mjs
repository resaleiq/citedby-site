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
const og = `<style>${ff("newsreader-latin-600-normal", 600)}${ff("newsreader-latin-400-normal", 400)}@font-face{font-family:Plex;font-weight:400;src:url(file://${PUB}/fonts/ibm-plex-sans-latin-400-normal.woff2)}
body{margin:0;width:1200px;height:630px;background:#0F1B2D;color:#E8EDF4;position:relative;overflow:hidden}
.l{position:absolute;left:72px;top:64px}.h{position:absolute;left:72px;top:200px;width:1040px;font:600 66px/1.08 Newsreader,Georgia,serif;letter-spacing:-.02em}
.s{position:absolute;left:72px;top:430px;font:400 28px/1.45 Plex,sans-serif;color:#C9D2DF;width:900px}.bar{position:absolute;left:0;right:0;bottom:0;height:14px;background:#FFB400}
.u{position:absolute;right:72px;top:84px;font:400 26px Plex,sans-serif;color:#C9D2DF}</style><body><div class="l">${lock}</div><div class="u">citedby.eu</div>
<div class="h">Is an AI assistant sending your customers to a competitor?</div><div class="s">Paste your site address. We ask nine AI assistants what your buyers ask and show who they name instead of you.</div><div class="bar"></div></body>`;
await png(og, 1200, 630, "og.png");
unlinkSync(join(PUB, "favicon-48.png")); // only inside the ICO
await b.close();
console.log("brand assets written to", PUB);
