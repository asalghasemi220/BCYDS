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
    const ts = [1.4, 3.0, 6.8, 9.6, 14.6, 17.8, 22.8, 26.4, 30.5];
    for (const t of ts) { await p.evaluate(t => renderAt(t), t); await p.screenshot({ path: `test-${t}.jpg`, type: 'jpeg', quality: 80 }); }
  } else {
    fs.mkdirSync('frames', { recursive: true });
    const fps = 30, dur = 31;
    for (let f = 0; f < fps * dur; f++) {
      await p.evaluate(t => renderAt(t), f / fps);
      await p.screenshot({ path: `frames/${String(f).padStart(5, '0')}.jpg`, type: 'jpeg', quality: 92 });
    }
  }
  await b.close();
})();
