const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const mode = process.argv[2] || 'test';
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1 });
  await p.goto('file://' + __dirname + '/scene.html', { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  if (mode === 'test') {
    const ts = [1.6, 6.5, 10.5, 15.0, 19.5, 23.6, 27.2, 30.8, 0.4];
    for (const t of ts) { await p.evaluate(t => renderAt(t), t); await p.screenshot({ path: `test-${t}.jpg`, type: 'jpeg', quality: 80 }); }
  } else {
    fs.mkdirSync('frames', { recursive: true });
    const fps = 30, dur = 32;
    for (let f = 0; f < fps * dur; f++) {
      await p.evaluate(t => renderAt(t), f / fps);
      await p.screenshot({ path: `frames/${String(f).padStart(5, '0')}.jpg`, type: 'jpeg', quality: 92 });
    }
  }
  await b.close();
})();
