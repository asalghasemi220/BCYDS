# BCYDS website (test version)

A single static page: `index.html` plus `images/` and `video/`. No build step. Open `index.html` in a browser, or upload the folder to any static host. Hosting and domain come later.

## Content
Focus: consulting and support for B.C. kids, families and schools, including students with ADHD, autism and other needs. Robotics and hands-on STEAM are the activities. Sections: hero with video, What we do, Hands-on STEAM, promise line, Getting started, Partners, Get in touch.

## Design
- Minimal product-page style (Apple / Square): centred hero, app-style icons, bento blocks, colour letter tiles, short copy.
- Logo: `../brand/logo-original.png` as supplied; web cut-outs in `images/brand/`.
- Colours: navy `#002E5D` and blue `#1D64D8` only (plus light blue `#4C8DF6`, sky `#BFD9FF`, ice `#EEF5FF`), on white. The logo's teal trail stays inside the logo artwork only.
- Mascot: Pilot (`images/mascot/`), in the hero, the contact block and the footer.
- Type: Plus Jakarta Sans.
- Motion is light: hero fade-in, hover lifts, and the video (muted, pauses when scrolled away). Everything stops for "reduce motion".

## Photos
All photos are the society's own (supplied Nov 2026), resized, with phone metadata removed:
`cat-mask.jpg`, `build-swing.jpg`, `build-creature.jpg`, `robotics-team.jpg`, and `event-banner.jpg` (not used on the page yet).
Before publishing, confirm written consent: from the parents of the child in `cat-mask.jpg`, and from the people in `robotics-team.jpg`.

## Video
`video/bcyds-intro.mp4` (+ `.webm`, `poster.jpg`): 32 seconds, silent with on-screen text, made from the photos above. Re-render steps are in `../video-source/`.

## Before going live
- [ ] Partner logos: add `images/partners/kavosh.png` and `images/partners/paradise.png` and swap them in where the comments in `index.html` say.
- [ ] Confirm both partners approve how they are named and described, and that Kavosh is happy with the team photo.
- [ ] Society name is provisional. It is in the logo files, the video, `<title>`, alt text and the copyright line.
- [ ] Replace `[society email]` (search for `TODO`).
- [ ] Only describe services as psychology, therapy, counselling or assessment if a registered professional delivers them.
- [ ] Domain and a social sharing image. Vector logo files from the designer.
