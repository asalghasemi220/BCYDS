# Social media starter kit

Everything needed to open the society's accounts and post for the first month. Visual rules live in the brand guide (`../brand/guide/`).

## Ready-made assets (`assets/`)
| File | Use | Size |
|---|---|---|
| `avatar-pilot.png` | Profile picture for Instagram, TikTok, YouTube (shows Pilot in the round crop) | 1080 × 1080 |
| `avatar-logo.png` | Profile picture for Facebook and LinkedIn (full logo) | 1080 × 1080 |
| `highlight-about.png`, `-support`, `-robotics`, `-steam`, `-contact` | Instagram story highlight covers | 1080 × 1920 |
| `post-01-hello.png` … `post-09-get-started.png` | The nine launch posts | 1080 × 1350 |
| `story-hello.png` | First story ("Hi, I'm Pilot!") | 1080 × 1920 |
| `cover-facebook.png` | Facebook page cover | 1640 × 624 |
| `cover-linkedin.png` | LinkedIn page cover (text sits right of the logo overlap area) | 1584 × 396 |

`grid-preview.jpg` shows how the profile grid looks after all nine posts. To change any design, edit `templates.html` and run `node render.js` (needs `npm install` in `../video-source` once, for the font).

## Before you open accounts
1. **Name.** The society name is provisional. Either wait for approval, or reserve the handles now and rename later (Instagram, Facebook and LinkedIn all allow renaming).
2. **Shared email.** Create a society email (for example a new Gmail or, later, an address on your domain). Never use a personal email or phone as the only login.
3. **Two admins.** At least two board-approved people should have admin access, so the society never loses its accounts.
4. **Password manager and two-factor authentication** on every account.

## Handles (check availability; use the same one everywhere)
1. `@bcyouthdiscovery` (recommended)
2. `@bcyds`
3. `@bcyouthdiscoverysociety`

## Bios
**Instagram** (≤150 characters)
```
Helping B.C. kids thrive 💙
Consulting & support for kids, families and schools
Hands-on robotics + STEAM
B.C. not-for-profit
```
Name field: `BC Youth Discovery Society` · Category: Nonprofit organization · Link: website once live.

**Facebook** (short description)
> BC Youth Discovery Society is a B.C. not-for-profit helping kids thrive. We offer consulting and support for kids, families and schools, including students with ADHD, autism and other needs, plus hands-on robotics and STEAM.

**LinkedIn** tagline (≤120 characters)
> Helping B.C. kids thrive through consulting, support and hands-on robotics and STEAM.

## Step-by-step setup
**Instagram**
1. Sign up with the society email and the chosen handle.
2. Settings → Account type and tools → Switch to professional account → Business → Category "Nonprofit organization".
3. Add `avatar-pilot.png`, the name, the bio, the society email as the contact button.
4. Settings → Privacy: turn on Hidden Words and comment filtering. Turn off location tagging when posting.
5. Settings → Accounts Center: two-factor authentication on; add the second admin through Meta Business Suite.
6. Post `story-hello.png`, save it to a highlight, and use the highlight covers as you add more.

**Facebook page**
1. From Meta Business Suite, create a Page named "BC Youth Discovery Society", category Nonprofit Organization.
2. Profile `avatar-logo.png`, cover `cover-facebook.png`, the short description, the society email.
3. Link the Instagram account to the Page in Business Suite so you can schedule posts for both.

**LinkedIn page** (for schools, partners and funders)
1. An admin signs in with their own LinkedIn profile → For Business → Create a Company Page → Company → Nonprofit.
2. Logo `avatar-logo.png`, cover `cover-linkedin.png`, the tagline, and the boilerplate from the brand guide as "About".

Optional later: YouTube (upload the intro video), TikTok only once there is a clear plan for safe, consented video content.

## Launch posts: order and captions
Post them in this order, so post 9 sits top-left of the grid. A good rhythm is three a week (Mon / Wed / Fri) for three weeks.

**1 · post-01-hello**
> Hello, B.C.! 💙 We're BC Youth Discovery Society, a new not-for-profit helping kids thrive. We offer consulting and support for kids, families and schools, with hands-on robotics and STEAM. Follow along!
> #BCYouthDiscovery #HelpingBCKidsThrive #BCkids #BCEducation #Nonprofit

**2 · post-02-meet-pilot**
> Meet Pilot, our robot sidekick. Curious, kind, and always cheering for effort. You'll see Pilot around here a lot. Say hi in the comments! 👋
> #BCYouthDiscovery #MeetPilot #KidsRobotics #HandsOnLearning

**3 · post-03-consulting**
> Every child is different, so we start by listening. We help kids, families and schools find the right support, together.
> #BCYouthDiscovery #FamilySupport #BCEducation #EveryChild

**4 · post-04-belong**
> Every child belongs. We support students with ADHD, autism and other needs, with our partner Paradise Life Academy.
> #BCYouthDiscovery #InclusiveEducation #Neurodiversity #EveryChildBelongs

**5 · post-05-built-in-class**
> Built in class: big eyes, a rainbow tower and an umbrella. Robotics gives kids a hands-on way to focus, create and work together. 🤖
> #BCYouthDiscovery #KidsRobotics #STEAMeducation #LearnByDoing

**6 · post-06-steam**
> Science, Technology, Engineering, Arts and Math. Five subjects, one big build. That's hands-on STEAM.
> #BCYouthDiscovery #STEAMeducation #HandsOnLearning #BCkids

**7 · post-07-big-ideas**
> Small builds. Big ideas. A swing set, two tiny friends, and a lot of problem-solving.
> #BCYouthDiscovery #KidsRobotics #CreativeKids #LearnByDoing

**8 · post-08-partners**
> Better together. Thank you to our partners: Kavosh AI and Robotics Academy for robotics instruction and kits, and Paradise Life Academy for consulting and intake interviews for students with special needs.
> #BCYouthDiscovery #Partnership #BCEducation
> *(Tag the partners only after they approve the post.)*

**9 · post-09-get-started**
> Getting started is simple: 1. Reach out. 2. We listen. 3. We grow together. Send us a message or tap the link in our bio. 💙
> #BCYouthDiscovery #HelpingBCKidsThrive #BCkids

## After launch: content plan
**Pillars** (rough monthly mix)
- Support and belonging: tips and encouragement for families and teachers (35%)
- Built in class: projects and builds, hands and models only (30%)
- Pilot and behind the scenes (15%)
- Partners and community (10%)
- How to get started and announcements (10%)

**Cadence:** 2–3 posts a week, stories 2–3 times a week, reply to comments and messages within two working days.

**Month 1 after the launch posts (example)**
| Week | Mon | Wed | Fri |
|---|---|---|---|
| 4 | Tip: three ways to celebrate effort | Build of the week (photo) | Pilot asks: what should we build next? (story poll) |
| 5 | What happens in a first conversation | STEAM letter spotlight: S for Science | Thank-you to a school or partner (with approval) |
| 6 | Tip: making a calm start to a busy day | Build of the week | Reminder: how to get in touch |
| 7 | Myth vs fact about robotics for young kids | STEAM spotlight: T for Technology | Pilot's weekend challenge |

## Child safety rules (non-negotiable)
1. **No identifiable child** (face, name tag, distinctive clothing) without **written parental consent** for that specific use. Prefer hands, builds and backs of heads.
2. **Never** name a child, their school, their class or an exact location. No geotags. No tagging minors.
3. **Check backgrounds** for names on whiteboards, cubbies, lanyards or school logos.
4. **Remove metadata** from photos before posting (the website photos already are), and take down any photo immediately if a family asks.
5. **Don't message minors.** Talk with parents, guardians or school staff only.
6. **Partners:** get approval before posting partner photos, logos or tags.
7. **Wording:** only describe services as psychology, therapy, counselling, assessment or diagnosis if a registered professional delivers them. Otherwise say "consulting" and "support".
8. Moderate comments daily; hide or delete anything unkind, and never argue in public.
