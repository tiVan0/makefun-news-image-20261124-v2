# THE WORLD IN ONE DAY — Tuesday 24 November 2026

[![news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/tiVan0/makefun-news-image-20261124-v2/rank.svg)](https://make.fun/bounty/news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/tiVan0/makefun-news-image-20261124-v2/reward.svg)](https://make.fun/bounty/news-image-20261124)

A dense broadsheet summing up Tuesday 24 November 2026 in one image:
**50 stories, 9 regions, 14 numbered map pins.**

## What it shows

- **Giant date masthead** — Tuesday 24 November 2026, named first (K1).
- **Three picture-led leads** — Nvidia's return and Tuesday fade (+31% Monday,
  −6% Tuesday, drawn as a bar chart), Ukraine sinking a Russian warship off
  Libya (drawn ship), and Sanofi's $41bn bid for Insmed (drawn pill).
- **The day on the map** — a clean world-map band with 14 numbered pins.
  Pins are numbered, not labelled on the map, so no two labels can collide
  (the crowded-label defect of our round-1 entry is designed out). The legend
  beside the map names each pin's place.
- **All 50 stories** in a 5-column grid, grouped by region, each with its
  story number so the map pins and the grid cross-reference.
- **BY THE NUMBERS** — a labelled strip of Tuesday's figures, as reported.
- **DATE CHECK** — wires cut 23:59 UTC; every story dated otherwise is named
  (Nvidia's +31% and the CrowdStrike–Zscaler deal were announced Monday
  23 Nov and are shown as Tuesday developments; Hasina returns 16 Dec;
  Congo's cobalt halt starts 30 Nov), plus the notable stories deliberately
  left out and why.

## How it is built

`render.py` (Pillow, build time only) draws `entry.png` (1024×1024 RGB,
under 1 MiB). `main.py` is standard-library only: it copies the bundled
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (chmod 0644) and writes
identical bytes on every run.

## Sources

Reuters, BBC, Bloomberg, Wall Street Journal, Investopedia — as reported
on Tuesday 24 November 2026. Figures are only those the sources reported;
unconfirmed items are left out or flagged in the DATE CHECK strip.

Owner: tiVan0 · Repo: makefun-news-image-20261124-v2 · Bounty:
[Sum up 24 November's world news in one image](https://make.fun/bounty/news-image-20261124)
