# Intro video source

`scene.html` is a scripted 31-second animation built from the site's photos and logo files. `render.js` captures it frame by frame with Playwright.

To re-render (for example after the society name or photos change):

```
cd video-source
npm install
node render.js full          # writes frames/00000.jpg ... frames/00929.jpg
ffmpeg -y -framerate 30 -i frames/%05d.jpg -c:v libx264 -preset slow -crf 23 -pix_fmt yuv420p -movflags +faststart -an ../website/video/bcyds-intro.mp4
ffmpeg -y -i frames/00204.jpg -q:v 3 ../website/video/poster.jpg
rm -rf frames
```

`node render.js test` writes a few still frames instead, for a quick check. The video is silent with on-screen text; it can be replaced with real classroom footage later.
