import { createRequire } from "node:module"; import { homedir } from "node:os"; import { join } from "node:path"; import { writeFileSync } from "node:fs";
const require = createRequire(join(homedir(), "work/company/qa-lab/package.json")); const { chromium } = require("playwright-core");
const CHROME = join(homedir(), "work/company/video-lab/browsers/chrome-headless-shell/mac-150.0.7871.125/chrome-headless-shell-mac-x64/chrome-headless-shell");
const b = await chromium.launch({ executablePath: CHROME, headless: true });
const p = await b.newPage({ viewport: { width: +(process.argv[4]||1280), height: 900 } });
await p.goto(process.argv[2]); await p.waitForTimeout(500);
writeFileSync(process.argv[3], await p.screenshot({ fullPage: true })); await b.close();
