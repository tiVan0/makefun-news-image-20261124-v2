#!/usr/bin/env python3
"""Render news-image-20261124 v2 (Builder B): DENSE BROADSHEET, picture-led.
50 distinct stories of Tuesday 24 November 2026, 9 regions, 14 numbered map pins.
Drawn fresh in this session. PIL only at build time; main.py is stdlib-only.
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
FD = "/usr/share/fonts/truetype/dejavu"

def font(name, size):
    return ImageFont.truetype(f"{FD}/{name}", size)

F_SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
F_SANS = lambda s: font("DejaVuSans.ttf", s)
F_SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)

INK = (18, 18, 18)
NAVY = (16, 42, 90)
RED = (178, 34, 34)
PAPER = (250, 248, 243)
GREY = (110, 110, 110)
LGREY = (228, 226, 220)
BLUE = (30, 90, 160)
GREEN = (28, 110, 60)

# (num, region, headline, deck-or-"")
STORIES = [
 (1, "NORTH AMERICA", "HUANG BACK AT NVIDIA; SHARES +31%, THEN -6%",
  "Board reinstated Jensen Huang as CEO on Monday after Trump intervened; "
  "shares jumped 31% to $165.05, then fell 6% on Tuesday as the rally faded."),
 (2, "NORTH AMERICA", "US BLACKLISTS 7 FIRMS, ALIBABA UNIT AMONG THEM",
  "Megaspeed, at the heart of the Nvidia scandal, joins the list on security grounds."),
 (3, "NORTH AMERICA", "COURT CLEARS ARMY TO DETONATE IOWA EXPLOSIVES",
  "Toxic lead azide to be blown up on Wednesday despite a last-minute order from Trump."),
 (4, "NORTH AMERICA", "81.5M TO TRAVEL FOR THANKSGIVING; STORMS HIT BOTH COASTS",
  "AAA counts 81.5 million travellers; flights held at O'Hare as millions set off."),
 (5, "BUSINESS", "SANOFI TO BUY INSMED FOR $41 BILLION",
  "French drugmaker offers $175 a share in cash, a 17% premium, for respiratory drugs."),
 (6, "NORTH AMERICA", "TRUMP SET TO UNVEIL NEW TARIFFS AFTER PROBE",
  "Findings target excess factory capacity in 16 trading partners, sources say."),
 (7, "NORTH AMERICA", "US CONSUMER CONFIDENCE AT NEAR 2-YEAR HIGH",
  "Confidence jumps to its highest level in nearly two years, Reuters reports."),
 (8, "TECH", "MICROSOFT DECLARES 'CODE RED' AFTER OUTAGE",
  "Internal memos show a historic outage put the cloud giant on alert."),
 (9, "NORTH AMERICA", "FBI DEPUTY TO RETIRE IN DECEMBER",
  "Christopher Raia steps down, the Washington Post reported."),
 (10, "TECH", "AMAZON TO BUY DECART AI TECH IN $7.5BN DEAL",
  "Amazon agrees to acquire the AI firm's technology and hire its founders."),
 (11, "SOUTH AMERICA", "MEXICO TO TRY 'EL CHAPO ISIDRO' AT HOME",
  "The cartel leader faces trial in Mexico despite a US extradition request."),
 (12, "SOUTH AMERICA", "ARGENTINA INFLATION QUICKENS TO 2.2%",
  "Prices rose 2.2% in October, the fastest since April."),
 (13, "SOUTH AMERICA", "COLOMBIAN PESO BIGGEST G10 FALLER, -3%",
  "The peso leads decliners as the dollar steadies, Reuters reports."),
 (14, "EUROPE", "ZAPORIZHZHIA STRIKE KILLS 2, WOUNDS 22",
  "An overnight Russian strike hit homes; two children are among the wounded."),
 (15, "EUROPE", "ZELENSKY URGES FOUR-WAY TALKS 'SOON'",
  "Kyiv is ready to meet 'literally tomorrow'; he will turn to the US Congress "
  "if Trump fails to win a deal by year-end."),
 (16, "EUROPE", "EU WEIGHS SPORTS BAN IN RUSSIA SANCTIONS",
  "A draft package would bar Russian athletes in Europe and ban visas for combatants."),
 (17, "EUROPE", "UK DESTITUTION HITS NEAR 4 MILLION",
  "Almost four million people in destitution, a new study finds."),
 (18, "EUROPE", "BURNHAM'S 10-YEAR PLAN UNDER SCRUTINY",
  "No 10 North faces closer watch as the plan looms."),
 (19, "EUROPE", "FRENCH FAR LEFT: 'DESTROY CAPITALISM'",
  "The BBC meets protesters Macron says threaten the Republic."),
 (20, "EUROPE", "NEW MUSEUM OF LONDON OPENS",
  "The 437-million-pound museum opens its doors to the public."),
 (21, "EUROPE", "BELLINGHAM IN REAL MADRID TALKS",
  "Jude Bellingham nears a new five-year deal."),
 (22, "EUROPE", "UK TARGETS HOUTHIS WITH NEW SANCTIONS",
  "Britain designates the group and four senior figures under its Yemen regime."),
 (23, "MIDDLE EAST", "GAZA NOW A 'TOXIC WASTELAND', OXFAM SAYS",
  "Israeli attacks have left Gaza toxic, the aid group said."),
 (24, "MIDDLE EAST", "IRAN VOWS TO END US BLOCKADE 'BY ALL MEANS'",
  "Tehran calls the naval blockade an act of aggression."),
 (25, "MIDDLE EAST", "FLYDUBAI CLEARED TO RETURN TO TEL AVIV",
  "Israel approves resumption of Dubai-Tel Aviv flights."),
 (26, "MIDDLE EAST", "OIL SLIDES ~3% AS FLOWS RISE",
  "Middle East supply and a Libyan restart push crude down."),
 (27, "MIDDLE EAST", "UKRAINE SINKS RUSSIAN WARSHIP OFF LIBYA",
  "A rare strike far beyond the Black Sea, Reuters reports on Tuesday."),
 (28, "MIDDLE EAST", "IRAQ PM ORDERS TAKEOVER OF KURDISH CROSSINGS",
  "Baghdad to run border crossings and oil fields after a smuggling probe."),
 (29, "MIDDLE EAST", "EISENKOT CLINCHES FIRST COALITION PACT",
  "Yashar agrees a deal with Lieberman's party in the bid to form a government."),
 (30, "MIDDLE EAST", "HOUTHIS 'WON'T SEIZE ADEN', ARMY SAYS",
  "Yemeni forces say the Houthis, 60 km from the city, will not capture it."),
 (31, "MIDDLE EAST", "RIYADH TOWER TARGETED, COALITION SAYS",
  "A skyscraper in the finance district was hit in a 'terrorist attack'."),
 (32, "AFRICA", "NIGERIA BOAT TOLL REACHES 24",
  "Search goes on in Bayelsa after a funeral boat capsized."),
 (33, "AFRICA", "DRONES HIT HOMES, UN BUILDING IN KHARTOUM",
  "Strikes kill civilians and damage a UN building in Khartoum."),
 (34, "AFRICA", "CONGO HALTS COBALT EXPORTS",
  "The top producer suspends exports from 30 Nov to fight a glut."),
 (35, "AFRICA", "KENYA, DR CONGO RESTORE TIES",
  "Full diplomatic ties agreed after years of tension."),
 (36, "AFRICA", "JOHANNESBURG: NEW COALITION TO RUN CITY",
  "Major parties seal a deal to govern the metros."),
 (37, "AFRICA", "TINUBU ASKS TO TRIM 2026 BUDGET TO $48BN",
  "Nigeria's president seeks a cut to 65.2 trillion naira from 68.3 trillion."),
 (38, "AFRICA", "~175 MIGRANTS UNACCOUNTED FOR OFF SENEGAL",
  "Contact lost with a Europe-bound boat that left Dakar about two weeks ago."),
 (39, "EAST ASIA", "JAPAN FACTORY GROWTH QUICKENS",
  "Flash PMI rises to 53.7 in November on chip demand."),
 (40, "EAST ASIA", "KOREA RATE RISE EXPECTED ON THURSDAY",
  "The central bank is seen lifting its rate to 3.25%."),
 (41, "EAST ASIA", "CHINA SENTENCES OFFICIAL TO DEATH FOR SPYING",
  "A court hands down a death sentence in an espionage case."),
 (42, "EAST ASIA", "TAIWAN COUNTS 24 PLA AIRCRAFT",
  "Seventeen crossed the median line; 11 warships also tracked."),
 (43, "EAST ASIA", "CHINA PROBES POLITBURO MEMBER CHEN JINING",
  "Shanghai's party chief is under investigation, Xinhua said on Tuesday."),
 (44, "EAST ASIA", "JAPAN STOCKS +4% AS ASIA RALLIES",
  "Tokyo leads gains while China holds steady, Reuters reports."),
 (45, "SOUTH ASIA", "HASINA PLANS RETURN ON 16 DECEMBER",
  "The ousted prime minister will fly home from exile in India, her aide told Reuters."),
 (46, "SOUTH ASIA", "INDIA PLEDGES $1.6BN TO NEPAL",
  "New Delhi offers aid in a reset of ties with its neighbour."),
 (47, "SOUTH ASIA", "BANGLADESH GARMENT WORKERS CLASH WITH POLICE",
  "Pay protests shut factories; workers demand the wage more than double to 30,000 taka."),
 (48, "SOUTH-EAST ASIA", "SINGAPORE, AUSTRALIA SIGN TWO PACTS",
  "PM Wong hails a 'trusted partnership' as leaders meet."),
 (49, "OCEANIA", "AUSTRALIA WARNS ON AI MISUSE",
  "Foreign actors will exploit AI, Canberra warns."),
 (50, "WORLD", "COP31 ENDS WITHOUT AGREEMENT",
  "Climate talks end with no deal after fossil-fuel language split the summit; "
  "the UNFCCC counts 198 Parties."),
]

# 14 numbered map pins: (story num, place label, lon, lat)
PINS = [
 (15, "KYIV", 30.5, 50.4), (14, "ZAPORIZHZHIA", 35.2, 47.8),
 (23, "GAZA", 34.5, 31.5), (24, "TEHRAN", 51.4, 35.7),
 (31, "RIYADH", 46.7, 24.7), (28, "BAGHDAD", 44.4, 33.3),
 (30, "ADEN", 45.0, 12.8), (33, "KHARTOUM", 32.6, 15.6),
 (34, "KINSHASA", 15.3, -4.3), (32, "BAYELSA", 6.3, 4.8),
 (43, "SHANGHAI", 121.5, 31.2), (41, "BEIJING", 116.4, 39.9),
 (42, "TAIPEI", 121.6, 25.0), (47, "DHAKA", 90.4, 23.8),
]

REGION_COLOR = {
 "NORTH AMERICA": NAVY, "SOUTH AMERICA": (120, 60, 20), "EUROPE": (90, 30, 90),
 "MIDDLE EAST": RED, "AFRICA": (150, 100, 0), "EAST ASIA": (0, 110, 110),
 "SOUTH ASIA": (160, 40, 90), "SOUTH-EAST ASIA": GREEN, "OCEANIA": (60, 90, 40),
 "BUSINESS": (90, 90, 90), "TECH": (40, 80, 160), "WORLD": (60, 60, 60),
}

def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_text(d, xy, text, fnt, fill=INK):
    d.text(xy, text, font=fnt, fill=fill)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------- MASTHEAD (0..96) ----------
d.rectangle([0, 0, W, 96], fill=NAVY)
draw_text(d, (24, 10), "THE WORLD IN ONE DAY", F_SERIF_B(34), (255, 255, 255))
draw_text(d, (24, 52), "TUESDAY  24  NOVEMBER  2026", F_SANS_B(24), (255, 210, 90))
draw_text(d, (700, 16), "50 STORIES", F_SANS_B(20), (255, 255, 255))
draw_text(d, (700, 44), "9 REGIONS  ·  14 MAP PINS", F_SANS_B(13), (200, 210, 230))
draw_text(d, (700, 64), "WIRES CUT 23:59 UTC", F_SANS_B(13), (255, 210, 90))

# ---------- LEAD BAND (96..264): 3 picture-led leads ----------
LEADS = [1, 27, 5]
lx = [24, 356, 688]
lw = [316, 316, 312]
d.rectangle([0, 96, W, 264], fill=(255, 255, 255))
for i, num in enumerate(LEADS):
    x, w = lx[i], lw[i]
    _, region, head, deck = STORIES[num - 1]
    d.rectangle([x, 104, x + w, 256], outline=LGREY, width=1)
    d.rectangle([x, 104, x + w, 128], fill=REGION_COLOR[region])
    draw_text(d, (x + 8, 110), f"LEAD {i+1}  ·  {region}", F_SANS_B(11), (255, 255, 255))
    # picture strip: drawn illustration per lead
    py = 132
    if num == 1:  # bar chart: +31% then -6%
        d.rectangle([x + 10, py, x + w - 10, py + 34], fill=(238, 240, 245))
        d.rectangle([x + 40, py + 6, x + 90, py + 30], fill=GREEN)
        d.rectangle([x + 110, py + 20, x + 160, py + 30], fill=RED)
        draw_text(d, (x + 175, py + 8), "+31% MON", F_SANS_B(11), GREEN)
        draw_text(d, (x + 175, py + 20), "-6% TUE", F_SANS_B(11), RED)
    elif num == 27:  # ship + blast at sea
        d.rectangle([x + 10, py, x + w - 10, py + 34], fill=(210, 228, 245))
        d.rectangle([x + 30, py + 18, x + 130, py + 28], fill=NAVY)
        d.rectangle([x + 60, py + 6, x + 70, py + 18], fill=NAVY)
        d.polygon([(x + 170, py + 8), (x + 178, py + 16), (x + 162, py + 16)], fill=RED)
        d.polygon([(x + 190, py + 20), (x + 198, py + 28), (x + 182, py + 28)], fill=RED)
        draw_text(d, (x + 215, py + 10), "OFF LIBYA", F_SANS_B(11), NAVY)
    else:  # pill / pharma
        d.rectangle([x + 10, py, x + w - 10, py + 34], fill=(240, 235, 245))
        d.ellipse([x + 40, py + 6, x + 120, py + 28], fill=(120, 40, 120))
        d.rectangle([x + 40, py + 6, x + 80, py + 28], fill=(200, 120, 200))
        draw_text(d, (x + 140, py + 8), "$41 BN", F_SANS_B(14), (120, 40, 120))
        draw_text(d, (x + 140, py + 22), "$175 / SHARE", F_SANS_B(10), INK)
    hl = wrap(d, head, F_SANS_B(15), w - 16)
    y = 172
    for ln in hl[:2]:
        draw_text(d, (x + 8, y), ln, F_SANS_B(15))
        y += 18
    dl = wrap(d, deck, F_SANS(11), w - 16)
    for ln in dl[:3]:
        draw_text(d, (x + 8, y), ln, F_SANS(11), (60, 60, 60))
        y += 13

# ---------- MAP BAND (264..432) ----------
d.rectangle([0, 264, W, 432], fill=(235, 240, 246))
draw_text(d, (24, 270), "THE DAY ON THE MAP  —  numbered pins match the story numbers below",
          F_SANS_B(12), NAVY)
MAP_X0, MAP_Y0, MAP_W, MAP_H = 24, 292, 620, 132

def project(lon, lat):
    x = MAP_X0 + (lon + 180.0) / 360.0 * MAP_W
    y = MAP_Y0 + (90.0 - lat) / 180.0 * MAP_H
    return x, y

# clean, smooth continent blobs (rounded shapes, not sketchy polygons)
def blob(cx, cy, rx, ry, fill):
    d.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=fill)
LAND = (196, 208, 190)
_cx, _cy = project(-100, 45); blob(_cx, _cy, 72, 24, LAND)   # N America
_cx, _cy = project(-105, 30); blob(_cx, _cy, 34, 14, LAND)
_cx, _cy = project(-60, -15); blob(_cx, _cy, 26, 26, LAND)   # S America
_cx, _cy = project(20, 5); blob(_cx, _cy, 38, 30, LAND)      # Africa
_cx, _cy = project(80, 50); blob(_cx, _cy, 120, 20, LAND)    # Eurasia
_cx, _cy = project(100, 35); blob(_cx, _cy, 55, 15, LAND)
_cx, _cy = project(134, -25); blob(_cx, _cy, 26, 12, LAND)   # Australia
_cx, _cy = project(0, 54); blob(_cx, _cy, 6, 5, LAND)        # UK
_cx, _cy = project(139, 37); blob(_cx, _cy, 6, 7, LAND)      # Japan
d.rectangle([MAP_X0, MAP_Y0, MAP_X0 + MAP_W, MAP_Y0 + MAP_H], outline=(160, 170, 180), width=1)
# pins: small dot at the true spot + numbered badge offset where the
# Europe / Middle East cluster would collide (leader line joins them)
PIN_OFF = {14: (-16, -12), 15: (12, -14), 23: (-18, 8), 24: (16, -8),
           28: (14, 10), 30: (-12, 12), 31: (18, 2)}
for num, place, lon, lat in PINS:
    x, y = project(lon, lat)
    ox, oy = PIN_OFF.get(num, (0, 0))
    bx, by = x + ox, y + oy
    d.ellipse([x - 3, y - 3, x + 3, y + 3], fill=RED)
    if (ox, oy) != (0, 0):
        d.line([x, y, bx, by], fill=RED, width=1)
    d.ellipse([bx - 8, by - 8, bx + 8, by + 8], fill=RED, outline=(255, 255, 255), width=2)
    t = str(num)
    tw = d.textlength(t, font=F_SANS_B(9))
    draw_text(d, (bx - tw / 2, by - 6), t, F_SANS_B(9), (255, 255, 255))

# legend: pin number + place, 2 columns x 7 rows
lx0, ly0 = 668, 292
for i, (num, place, lon, lat) in enumerate(PINS):
    col, row = divmod(i, 7)
    x = lx0 + col * 170
    y = ly0 + row * 17
    d.ellipse([x, y, x + 14, y + 14], fill=RED)
    t = str(num)
    tw = d.textlength(t, font=F_SANS_B(9))
    draw_text(d, (x + 7 - tw / 2, y + 2), t, F_SANS_B(9), (255, 255, 255))
    draw_text(d, (x + 19, y + 2), place, F_SANS_B(10))
draw_text(d, (668, 414), "Numbered pins — no labels on the map.", F_SANS(10), GREY)

# ---------- STORY GRID (432..912): 5 columns x 10 rows = 50 stories ----------
GRID_Y0, GRID_H = 432, 480
CELL_W, CELL_H = 195, 48
GX0 = 24
d.rectangle([0, GRID_Y0, W, GRID_Y0 + GRID_H], fill=(255, 255, 255))
draw_text(d, (24, GRID_Y0 + 4), "ALL 50 STORIES  —  BY REGION", F_SANS_B(11), NAVY)
for idx, (num, region, head, deck) in enumerate(STORIES):
    col, row = divmod(idx, 10)
    x = GX0 + col * CELL_W
    y = GRID_Y0 + 22 + row * 46
    # thin divider
    if row > 0:
        d.line([x + 4, y - 3, x + CELL_W - 10, y - 3], fill=LGREY)
    rc = REGION_COLOR[region]
    draw_text(d, (x, y), f"{num:02d} {region}", F_SANS_B(8), rc)
    hl = wrap(d, head, F_SANS_B(10), CELL_W - 12)
    yy = y + 11
    for ln in hl[:2]:
        draw_text(d, (x, yy), ln, F_SANS_B(10))
        yy += 12

# ---------- BY THE NUMBERS (912..968) — labelled ----------
d.rectangle([0, 912, W, 968], fill=(245, 240, 225))
draw_text(d, (24, 918), "BY THE NUMBERS  —  Tuesday's figures, as reported", F_SANS_B(12), RED)
draw_text(d, (24, 936),
  "Nvidia +31% Mon to $165.05, then -6% Tue  ·  Nasdaq -1.5%, S&P 500 -0.5%, Dow +0.9% Tue  ·  81.5m Thanksgiving travellers",
  F_SANS(11))
draw_text(d, (24, 951),
  "Zaporizhzhia: 2 killed, 22 wounded  ·  Sanofi-Insmed $41bn  ·  COP31: 198 Parties  ·  Japan PMI 53.7  ·  ~175 migrants unaccounted for",
  F_SANS(11))

# ---------- DATE CHECK (968..1024) — 3 mandatory lines ----------
d.rectangle([0, 968, W, 1024], fill=NAVY)
draw_text(d, (24, 972),
  "DATE CHECK — Wires cut 23:59 UTC, Tue 24 Nov 2026. Every story was reported on Tue 24 Nov 2026 (any time zone),",
  F_SANS_B(10), (255, 210, 90))
draw_text(d, (24, 984),
  "or is a dated Tuesday development of it. Dated otherwise: Nvidia +31% and CrowdStrike-Zscaler ($43.9bn) announced Mon 23 Nov;",
  F_SANS(10), (255, 255, 255))
draw_text(d, (24, 996),
  "Zelenskyy interview late Mon, published Tue; Hasina returns 16 Dec; Congo halt starts 30 Nov. Left out: Gaza meningitis warning +",
  F_SANS(10), (255, 255, 255))
draw_text(d, (24, 1008),
  "Solomon Islands pact switch (both single-source, 24 Nov). Sources: Reuters, BBC, Bloomberg, WSJ, Investopedia.",
  F_SANS(10), (200, 210, 230))

img.save("entry.png", optimize=True)
print("saved entry.png", img.size, img.mode)
