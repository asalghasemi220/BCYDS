# Generates the "Pilot" mascot SVGs (one source of truth for every pose).
NAVY, DEEP, BLUE, BLUE4, SKY, ICE, WHITE = "#002E5D", "#001F40", "#1D64D8", "#4C8DF6", "#BFD9FF", "#EEF5FF", "#FFFFFF"

def head(x=0, y=0):
    return f'''
  <g transform="translate({x},{y})">
    <path d="M130 66 C130 50 126 42 133 34 C141 25 156 30 152 42 C148 53 131 49 132 34 C133 24 139 16 147 13" fill="none" stroke="{NAVY}" stroke-width="5" stroke-linecap="round"/>
    <circle cx="149" cy="12" r="9" fill="{BLUE}"/><circle cx="146" cy="9" r="3" fill="{WHITE}" opacity=".8"/>
    <rect x="44" y="104" width="16" height="38" rx="8" fill="{BLUE}"/>
    <rect x="200" y="104" width="16" height="38" rx="8" fill="{BLUE}"/>
    <rect x="54" y="62" width="152" height="120" rx="36" fill="{NAVY}"/>
    <rect x="70" y="84" width="120" height="82" rx="26" fill="url(#screen)"/>
    <ellipse cx="106" cy="120" rx="13" ry="16" fill="{WHITE}"/>
    <ellipse cx="154" cy="120" rx="13" ry="16" fill="{WHITE}"/>
    <circle cx="108" cy="123" r="6.5" fill="{NAVY}"/><circle cx="156" cy="123" r="6.5" fill="{NAVY}"/>
    <circle cx="110.5" cy="120" r="2.2" fill="{WHITE}"/><circle cx="158.5" cy="120" r="2.2" fill="{WHITE}"/>
    <path d="M117 145 Q130 156 143 145" fill="none" stroke="{WHITE}" stroke-width="5" stroke-linecap="round"/>
    <circle cx="86" cy="143" r="6" fill="{SKY}" opacity=".55"/><circle cx="174" cy="143" r="6" fill="{SKY}" opacity=".55"/>
    <rect x="66" y="64" width="128" height="9" rx="4.5" fill="{DEEP}"/>
    <circle cx="108" cy="68" r="15" fill="{SKY}" stroke="{DEEP}" stroke-width="5"/>
    <circle cx="152" cy="68" r="15" fill="{SKY}" stroke="{DEEP}" stroke-width="5"/>
    <path d="M101 62 l7 -4" stroke="{WHITE}" stroke-width="3" stroke-linecap="round" opacity=".9"/>
    <path d="M145 62 l7 -4" stroke="{WHITE}" stroke-width="3" stroke-linecap="round" opacity=".9"/>
  </g>'''

DEFS = f'''<defs>
    <linearGradient id="screen" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{BLUE}"/><stop offset="1" stop-color="#114A9E"/></linearGradient>
    <linearGradient id="bodyg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{BLUE4}"/><stop offset="1" stop-color="{BLUE}"/></linearGradient>
  </defs>'''

def body():
    return f'''
  <rect x="118" y="178" width="24" height="14" rx="4" fill="{DEEP}"/>
  <rect x="98" y="270" width="26" height="26" rx="10" fill="{NAVY}"/>
  <rect x="136" y="270" width="26" height="26" rx="10" fill="{NAVY}"/>
  <rect x="90" y="288" width="38" height="14" rx="7" fill="{DEEP}"/>
  <rect x="132" y="288" width="38" height="14" rx="7" fill="{DEEP}"/>
  <rect x="72" y="186" width="116" height="94" rx="30" fill="url(#bodyg)"/>
  <rect x="100" y="206" width="60" height="48" rx="16" fill="{WHITE}"/>
  <path d="M130 245 C130 245 114 235 114 224 A8 8 0 0 1 130 220 A8 8 0 0 1 146 224 C146 235 130 245 130 245 Z" fill="{BLUE}"/>'''

def arm_down_left():
    return f'''<rect x="50" y="196" width="26" height="62" rx="13" fill="{NAVY}" transform="rotate(12 63 200)"/>
  <circle cx="57" cy="262" r="14" fill="{NAVY}"/>'''

def arm_wave_right():
    return f'''<g transform="rotate(38 192 204)"><rect x="179" y="142" width="26" height="66" rx="13" fill="{NAVY}"/><circle cx="192" cy="138" r="15" fill="{NAVY}"/></g>'''

def arm_wave_left():
    return f'''<g transform="rotate(-38 68 204)"><rect x="55" y="142" width="26" height="66" rx="13" fill="{NAVY}"/><circle cx="68" cy="138" r="15" fill="{NAVY}"/></g>'''

def arm_hold_right():
    # arm forward holding a paper plane
    return f'''<rect x="184" y="198" width="26" height="56" rx="13" fill="{NAVY}" transform="rotate(-62 197 202)"/>
  <circle cx="238" cy="186" r="14" fill="{NAVY}"/>
  <path d="M222 172 L276 150 L250 194 L242 180 Z" fill="{WHITE}" stroke="{NAVY}" stroke-width="4" stroke-linejoin="round"/>
  <path d="M242 180 L276 150" stroke="{NAVY}" stroke-width="3" stroke-linecap="round"/>'''

def svg(content, vb="0 0 260 320", title="Pilot, the BC Youth Discovery Society mascot"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" role="img" aria-label="{title}">\n  {DEFS}\n  <ellipse cx="130" cy="306" rx="70" ry="8" fill="{NAVY}" opacity=".12"/>{content}\n</svg>\n'

poses = {
    'pilot-wave.svg': svg(arm_down_left() + body() + arm_wave_right() + head(), vb="0 0 270 320"),
    'pilot-cheer.svg': svg(arm_wave_left() + body() + arm_wave_right() + head(), vb="-10 0 280 320"),
}
# avatar: head only, centred in a square
poses['pilot-head.svg'] = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="34 -6 192 196" role="img" aria-label="Pilot">\n  {DEFS}{head()}\n</svg>\n'
for name, s in poses.items():
    open(name, 'w').write(s)
print('wrote', list(poses))
