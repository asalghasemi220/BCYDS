// Renders brand/guide/index.html to BCYDS-Brand-Guidelines.pdf (1600 x 1131 px pages, A4 proportions).
// Needs: cd ../../video-source && npm install   (local copy of the brand font)
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const fonts = path.resolve(__dirname, '../../video-source/node_modules/@fontsource/plus-jakarta-sans/files');
  const css = [500, 600, 700, 800].map(w => `@font-face{font-family:"Plus Jakarta Sans";font-weight:${w};src:url(file://${fonts}/plus-jakarta-sans-latin-${w}-normal.woff2)}`).join('');
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1600, height: 1131 } });
  await p.goto('file://' + __dirname + '/index.html', { waitUntil: 'load' });
  await p.addStyleTag({ content: css });
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
  await p.pdf({ path: path.join(__dirname, 'BCYDS-Brand-Guidelines.pdf'), width: '1600px', height: '1131px', printBackground: true });
  // screenshots for review
  if (process.argv[2]) {
    for (const [name, w] of [['g-desk', 1366], ['g-phone', 390]]) {
      const q = await b.newPage({ viewport: { width: w, height: 900 } });
      await q.goto('file://' + __dirname + '/index.html', { waitUntil: 'load' });
      await q.addStyleTag({ content: css }); await q.waitForTimeout(500);
      console.log(name, 'overflow', await q.evaluate(() => document.documentElement.scrollWidth - innerWidth));
      await q.screenshot({ path: path.join(process.argv[2], name + '.png'), fullPage: true });
    }
  }
  await b.close();
})();
