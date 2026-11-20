# BCYDS website (test version)

A single static page: `index.html` plus `images/` and `video/`. No build step. Open `index.html` in a browser, or upload the folder to any static host. Hosting and domain come later.

## Design
- **Style:** minimal product-page layout (Apple / Square style): centred hero, app-style icons, bento grid, short copy only.
- **Logo:** `../brand/logo-original.png` as supplied; web cut-outs in `images/brand/`.
- **Colours:** brand navy `#002E5D` and teal `#00B79F` (from the logo), on white and light grey `#F5F5F7`. Each activity has one bright colour: robotics blue `#0A84FF`, science teal `#00B79F`, arts rose `#FF375F`, outdoor green `#2DB84D`, life skills amber `#FFB020`, hands-on projects violet `#6E4BE0`.
- **Type:** Plus Jakarta Sans only.
- **Motion:** the logo's plane flies in and draws its trail; the icon row floats; sections fade in; the video plays muted while on screen. All of it stops for visitors who set "reduce motion".

## Video
`video/bcyds-intro.mp4` (+ `.webm` fallback, `poster.jpg`): a 31-second silent explainer with on-screen text, made from the site's photos and logo. The source and re-render steps are in `../video-source/`. Replace it with real classroom footage once you have it (with consent).

## Before going live
- [ ] **Partner logos:** add `images/partners/kavosh.png` and `images/partners/paradise.png` (PNG or SVG, transparent background) and swap them in where the comments in `index.html` say. The page shows the partner names until then.
- [ ] Confirm both partners are happy with how they are named and described.
- [ ] **Society name is provisional.** It is in the logo files, the video, `<title>`, alt text and the copyright line.
- [ ] Replace `[school inquiry email]` (search for `TODO`).
- [ ] Domain, and a social sharing image.
- [ ] Ask the logo designer for vector files (SVG or PDF).
- [ ] Program status: robotics says "First program"; the others say "Coming soon". Update as programs launch.
- [ ] Replace the illustrative photos with the society's own, with written media consent.

## Photo credits (openly licensed; also in the page footer under "Photo credits")
| File | Creator | Source | Licence |
|---|---|---|---|
| `images/students-building-robots.jpg` | International Gemini Observatory/NOIRLab/NSF/AURA/J. Pollard | https://commons.wikimedia.org/w/index.php?curid=146174718 | CC BY 4.0 |
| `images/robot-car-sensor.jpg` (video) | forumbildig | https://www.flickr.com/photos/160200532@N02/40802364221 | CC BY 2.0 |
| `images/science-lab.jpg` (video) | TimBlackman93 | https://commons.wikimedia.org/w/index.php?curid=101299227 | CC BY-SA 4.0 |
| `images/classroom-experiment.jpg` (video) | Gulliver Schools | https://commons.wikimedia.org/w/index.php?curid=17227599 | CC BY 2.5 |
| `images/painting-outdoors.jpg` | Virginia State Parks staff | https://commons.wikimedia.org/w/index.php?curid=29261775 | CC BY 2.0 |
| `images/outdoor-forest.jpg` | Sharpe2021 | https://commons.wikimedia.org/w/index.php?curid=108682240 | CC BY-SA 4.0 |
