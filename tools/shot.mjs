// Screenshot helper for article images (RES-1480). Usage:
//   node tools/shot.mjs check <site> <out.png|.webp>          real run of the live free check, result card only
//   node tools/shot.mjs svg <in.svg> <out.png> [w h]          rasterise an SVG (OG images)
import { createRequire } from "node:module";
import { homedir } from "node:os";
import { join } from "node:path";
import { readFileSync, writeFileSync } from "node:fs";
const require = createRequire(join(homedir(), "work/company/qa-lab/package.json"));
const { chromium } = require("playwright-core");
const CHROME = process.env.CHROME || join(homedir(), "work/company/video-lab/browsers/chrome-headless-shell/mac-150.0.7871.125/chrome-headless-shell-mac-x64/chrome-headless-shell");
const [mode, a, out, W, H] = process.argv.slice(2);
const b = await chromium.launch({ executablePath: CHROME, headless: true });
const toWebp = async (p, buf) => out.endsWith(".webp") ? Buffer.from(await p.evaluate(async (b64) => { const img = new Image(); img.src = "data:image/png;base64," + b64; await img.decode(); const c = document.createElement("canvas"); c.width = img.width; c.height = img.height; c.getContext("2d").drawImage(img, 0, 0); return c.toDataURL("image/webp", 0.85).split(",")[1]; }, buf.toString("base64")), "base64") : buf;
if (mode === "check") {
  const p = await b.newPage({ viewport: { width: 1100, height: 900 }, deviceScaleFactor: 1 });
  await p.goto("https://citedby.eu/check?internal=1"); await p.fill("#f-url", a); await p.click("#f-go");
  await p.waitForSelector("#result:not([hidden]) ul.cl, .status.err", { timeout: 40000 }); const er = await p.$(".status.err"); if (er && (await er.textContent())) { if (process.env.KEEP_ERR) { await p.waitForTimeout(600); const f = await (await p.$("#cf")).boundingBox(), t = await (await p.$("#status")).boundingBox(); writeFileSync(out, await toWebp(p, await p.screenshot({ fullPage: true, clip: { x: f.x - 8, y: f.y - 8, width: f.width + 16, height: t.y + t.height - f.y + 24 } }))); console.log("wrote error card", out); await b.close(); process.exit(0); } throw new Error("check failed: " + await er.textContent()); }
  const el = await p.$("#result .col"); const buf = await el.screenshot();
  writeFileSync(out, await toWebp(p, buf)); console.log("wrote", out, await p.evaluate(() => document.querySelector("#result .sum").textContent));
} else {
  const p = await b.newPage({ viewport: { width: +(W || 1200), height: +(H || 630) } });
  await p.setContent(`<body style="margin:0">${readFileSync(a, "utf8")}</body>`);
  writeFileSync(out, await p.screenshot({ clip: { x: 0, y: 0, width: +(W || 1200), height: +(H || 630) } })); console.log("wrote", out);
}
await b.close();
