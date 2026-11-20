// Exports every .asset in templates.html to assets/<id>.png at its exact size.
// Needs: cd ../video-source && npm install   (for the brand font files)
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1800, height: 1200 }, deviceScaleFactor: 1 });
  await p.goto('file://' + __dirname + '/templates.html', { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
  const ids = await p.$$eval('.asset', els => els.map(e => e.id));
  for (const id of ids) await p.locator('#' + id).screenshot({ path: `${__dirname}/assets/${id}.png` });
  console.log('exported', ids.length, 'assets');
  await b.close();
})();
