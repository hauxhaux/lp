# WLFW Grasslands & Savannas Sub-site Style Guide

**Source URL:** https://dev.landscapepartnership.org/networks/working-lands-for-wildlife/landscapes-wildlife/landscapes/grasslands-and-savannas
**CSS file:** `wlfw-grassland.css` (sub-site specific, loaded last)
**Body class:** `site-grasslands-and-savannas`

---

## Page Inventory

| # | Page | URL Path (relative to base) | File |
|---|------|---------------------------|------|
| 1 | Home | `/` (east-and-central-grasslands-and-savannas default view) | `01-home.html` |
| 2 | About | `/about` | `02-about.html` |
| 3 | Framework | `/framework` | `03-framework.html` |
| 4 | Wildlife | `/wildlife` | `04-wildlife.html` |
| 5 | Resources | `/resources` | `05-resources.html` |
| 6 | Training | `/training` | `06-training.html` |
| 7 | Stories | `/stories` | `07-stories.html` |
| 8 | News | `/news` | `08-news.html` |
| 9 | Workspace | `/workspace` | `09-workspace.html` |

Base URL: `https://dev.landscapepartnership.org/networks/working-lands-for-wildlife/landscapes-wildlife/landscapes/grasslands-and-savannas`

---

## Color Palette

### CSS Custom Properties (from `wlfw-grassland.css :root`)

| Variable | Hex | Usage |
|----------|-----|-------|
| `--darkgrey` | `#262626` | Return-to-WLFW bar background |
| `--darkblue` | `#25334f` | **Header background**, site actions bar, overlay blocks |
| `--heading` | `#425a84` | All headings (h1-h6), nav tree portlet header, tile headlines |
| `--gold` | `#dcc464` | Nav selected/hover text, h1 underline bar, subheadings, nav portlet header link |
| `--ltgold` | `#ebdc9e` | Light gold background variant |
| `--darkgold` | `#bca647` | Footer background (`#portal-footer-wlfw`) |
| `--grey` | `#f8f5ef` | Grey background blocks |
| `--orange` | `#f88630` | Return-bar hover, companion-select hover |
| `--yellow` | `#fbd84d` | Blue-block h4, black-70-block subhead |
| `--white` | `#ffffff` | Body background, nav link text |
| `--brown` | `#846b0a` | `.subheading-2` text |

### Additional Colors Used Inline

| Hex | Usage |
|-----|-------|
| `#3b3b3b` | Body paragraph text |
| `#3c4d6a` | Intro text, pullquote text |
| `#4a4a4a` | Submenu link text |
| `#d3bd64` | Pullquote border-left, callout border-left |
| `#f2e6b5` | Callout background |
| `#D0F7FF` | Blue-block subhead text, dark-block-75 subhead |
| `#f1d215` | Black-overlay-block subhead |
| `#E86128` | Submenu hover text (orange) |
| `#efefef` | Submenu hover background |
| `#d8c468` | Mobile nav background (opened), gold text |
| `#29457b` | EEO statement hover |
| `#a9e1f3` | Personal tools visited link |
| `#f8903e` | Dark-block-75 h4 color, also btn-orange in ploneCustom |
| `rgba(0 0 0 / 35%)` | Nav hover/selected background overlay |
| `rgba(37 50 75 / 90%)` | Blue-block background |
| `rgba(8 7 7 / 80%)` | Black-overlay-block background |
| `rgba(0 0 0 / 50%)` | Black-50-block background |
| `rgba(0 0 0 / 70%)` | Black-70-block background |
| `rgba(0 0 0 / 75%)` | Dark-block-75 background |

---

## Typography

### Google Fonts Loaded

```html
<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,400i,600|Source+Sans+Pro:400,700&display=swap">
<link href="https://fonts.googleapis.com/css?family=Merriweather:400,400i,700|Montserrat:400,500,600&display=swap">
<link href="https://fonts.googleapis.com/icon?family=Material+Icons">
<link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:ital,wght@0,400;0,700;1,400&display=swap">
<link href="https://fonts.googleapis.com/css2?family=Public+Sans:ital,wght@0,300;0,400;0,700;1,300;1,400&display=swap">
```

Also: Font Awesome 4.2.0 via `//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css`

### Font Families

| Font | Usage |
|------|-------|
| **Public Sans** | Body text, nav links, list items, subheadings, document description |
| **Merriweather** | All headings (h1-h6), intro text, pullquotes, quotes |
| **Montserrat** | `.heading-white`, dark-block-75 subhead/h4 |
| **Material Icons** | Icon font (various sizes: 40px, 48px, 60px, 68px, 90px) |
| **Open Sans** | Base body font from ploneCustom.css (overridden by sub-site) |
| **Source Sans Pro** | Base nav font from ploneCustom.css (overridden by sub-site) |

### Heading Styles

| Element | Font | Size | Weight | Color | Line Height | Notes |
|---------|------|------|--------|-------|-------------|-------|
| h1-h6 | Merriweather, serif | varies | 600 | `#425a84` (--heading) | 1.5em | letter-spacing: -0.025em |
| h1 / h1.documentFirstHeading | Merriweather | 2.8rem (mobile: 2.3rem) | 600 | `#425a84` | 3.2rem (mobile: 2.6rem) | Gold underline bar after (80px wide, 5px tall, `--gold`) |
| h2 | Merriweather | 2.3rem | 600 | `#425a84` | 2.8rem | |
| h2.large | Merriweather | 2.8rem (mobile: 2rem) | 600 | `#425a84` | | |
| h3 | Merriweather | 1.7rem | 600 | `#425a84` | | |
| h4 | Merriweather | 1.5rem | 600 | `#425a84` | | |

### Body Text

| Element | Font | Size | Color | Line Height |
|---------|------|------|-------|-------------|
| body | Public Sans, sans-serif | default | -- | -- |
| p | Public Sans | 1.1rem | `#3b3b3b` | 1.65rem |
| #content li | Public Sans | 1rem | `#262626` (--darkgrey) | -- |
| .intro | Merriweather, serif | 18px | `#3c4d6a` | 1.6em |
| .documentDescription | Public Sans | 1.35em | -- | 1.5em |
| .subheading | Public Sans | 1.1rem | `#dcc464` (--gold) | -- |
| .subheading-2 | Public Sans | 1.3rem | `#846b0a` (--brown) | uppercase |

### Special Text

| Class | Font | Size | Style | Color |
|-------|------|------|-------|-------|
| .pullquote | Merriweather, serif | 1.5rem | letter-spacing: -0.05em | `#3c4d6a` |
| .quote | Merriweather | 20px | italic | -- |
| .cite | -- | 0.9rem | text-align: center | -- |
| .heading-white | Montserrat, sans-serif | 2.7em | 600, uppercase | `#fff` |

---

## Layout & Structure

### Page Width

| Element | Width | Notes |
|---------|-------|-------|
| `#visual-portal-wrapper` | `max-width: 100%` | `border-radius: 0`, `margin: 0 auto` |
| `#content` | `width: 80%` | `margin: 1em auto`; below 1530px: `width: 100%; padding: 0 2em` |
| `.template-atct_edit #visual-portal-wrapper` | `width: 1170px` | Edit mode only |
| `#portal-columns` | -- | `padding: 0 2em`; mobile: `padding: 0` |

### Header

| Property | Value |
|----------|-------|
| Height | **150px** desktop, **100px** mobile |
| Background | `#25334f` (--darkblue) |
| Logo width | 560px desktop, 335px mobile |
| Logo position | `top: 15px; left: 35px` desktop, `top: -15px; left: 5px` mobile |

### Return-to-WLFW Bar (`.wlfw-biome-nav-bar`)

| Property | Value |
|----------|-------|
| Background | `#262626` (--darkgrey) |
| Padding | `10px 30px` (mobile: `10px 15px`) |
| Font | 600 weight, 12px (mobile: 11px), letter-spacing: 1px |
| Link color | `#fff`, uppercase |
| Link hover | `--orange` (`#f88630`) |

### Banner (`#portal-banner`)

| Property | Value |
|----------|-------|
| Height | **450px** desktop, **195px** mobile |
| Default background | `working-lands/restored-prairie-in-ohio.jpg`, cover, centered |
| Per-section backgrounds | About: `ocala-iStock-597928044.jpg`, Resources: `longleaf-pine.jpg`, Training: `longleaf-FB-group.jpg`, Workspace: `wlfw-grassland-header.jpg` |

### Search Box (`.LSBox`)

| Property | Value |
|----------|-------|
| Position | `top: 430px; right: 5%` (relative positioned) |
| Background | `#ffffff`, `padding: 10px 13px`, `border-radius: 6px` |
| Mobile | `top: 100px; position: absolute; left: 90px; width: 100px; background: transparent` |

---

## Navigation

### Main Nav (`#portal-globalnav`)

| Property | Value |
|----------|-------|
| Display | `flex`, `justify-content: right` |
| Margin | `margin-right: 2.5%` |
| Background | transparent |

### Nav Wrapper (`#globalnav-wrapper`)

| Property | Value |
|----------|-------|
| Background | transparent |
| Position | `top: 100px` (positioned absolute from ploneCustom) |
| Mobile | `width: 100%; top: 105px; left: 0` |

### Nav Link Styles (`#portal-globalnav li a`)

| Property | Value |
|----------|-------|
| Font | Public Sans, 1rem (16px at 1024px breakpoint), 600 weight |
| Text transform | uppercase |
| Padding | `10px 20px` (15px at 1024px) |
| Border | `3px solid transparent` |
| Color | `#fff` |

### Nav States

| State | Background | Text Color |
|-------|-----------|------------|
| Default | transparent | `#fff` |
| Hover | `rgba(0 0 0 / 35%)` | `#dcc464` (--gold) |
| Selected | `rgba(0 0 0 / 35%)` | `#dcc464` (--gold) |
| Visited | -- | `#fff` |

### Home Tab (`#portaltab-home`)

| Property | Value |
|----------|-------|
| Default | Shows text "Home" (not icon — overrides base home icon) |
| Hover | `rgba(0 0 0 / 35%)` bg, gold text |
| Submenu | Hidden (`display: none`) |

### Submenu (`#portal-globalnav ul.submenu`)

| Property | Value |
|----------|-------|
| Text | Not uppercase, 15px |
| Link color | `#4a4a4a` |
| Hover background | `#efefef` |
| Hover text | `#E86128` (orange) |

### Mobile Nav (below 767px)

| Property | Value |
|----------|-------|
| `#portal-globalnav` | `display: none` (shown via `.opened` class) |
| `#portal-globalnav li` | `width: 100%; background: #d8c468` |
| `.menu-toggle` | `font-weight: 600; font-size: 13px; padding: 12px 0 12px 35px` |

### Landscape Biome Menu (`.landscape-biome-menu`)

| Property | Value |
|----------|-------|
| Position | `absolute; top: 2px; right: 20px; z-index: 25` |
| Font size | 13px |
| First link | Gold text (`#d8c468`), uppercase, arrow background image |
| Dropdown (`.companion-select`) | `background: #f3f3f3; box-shadow: 0 0 10px rgba(0,0,0,.25); min-width: 200px` |
| Dropdown links | `color: #3390aa`, not uppercase |
| Mobile | `position: absolute; top: 304px` |

---

## Buttons (from ploneCustom.css, shared across sub-sites)

| Class | Background | Text | Padding | Border | Hover BG |
|-------|-----------|------|---------|--------|----------|
| `.cta-button` | `#f7bd4f` | `#fff`, Montserrat 600 | `15px 25px` | `1px solid #fff`, 5px radius | `#f38b1a` |
| `.btn-orange` | `#f8903e` | `#fff` | `10px 15px` | `1px solid #fff`, 5px radius | `#F7700D` |
| `.btn-orange-large` | `#f8903e` | `#fff` | `10px 15px` | `1px solid #fff`, 5px radius | `#F7700D` |
| `.btn-red` | `#FF6633` | `#fff` | `10px 15px` | 5px radius | -- |
| `.btn-blue` | `#0e71eb` | `#fff` | `8px 15px` | 8px radius | `#1a5cbb` |
| `.btn-tan` | `#d4d5c6` | `#797979` | `10px` | 6px radius | `#C1C1B5` |
| `.btn-grey` | (in ploneCustom) | -- | -- | -- | -- |
| `a.overlay-btn` | `rgba(0,0,0,0.5)` | `#fafafa`, 20px 600 | `10px` | `0 0 5px 5px` radius | `rgba(0,0,0,0.6)` |
| `a.overlay-btn-2` | `rgba(0,0,0,0.5)` | `#fff`, 1.3em | `15px` | `1px solid #fff`, 6px radius | `rgba(255,255,255,1)` bg, `#222` text |
| `a.overlay-btn-3` | `rgba(0,0,0,0.35)` | `#fff`, 1.3em | `15px` | `0 0 6px 6px` radius | `rgba(0,0,0,0.75)` bg, `#f7c60e` text |

---

## Content Blocks

### Background Blocks (from `wlfw-grassland.css`)

| Class | Background | Padding | Min-Height | Border Radius | Notes |
|-------|-----------|---------|------------|---------------|-------|
| `.bg-dark` | `#25334f` | -- | -- | -- | |
| `.bg-blue` | `#425a84` | -- | -- | -- | |
| `.bg-grey` | `#f8f5ef` | -- | -- | -- | |
| `.bg-gold` | `#dcc464` | -- | -- | -- | `border-top: none` |
| `.bg-drk-gold` | `#bca647` | -- | -- | -- | |
| `.bg-lt-gold` | `#ebdc9e` | -- | -- | -- | |
| `.bg-orange` | `#f88630` | -- | -- | -- | |

### Overlay Blocks

| Class | Background | Padding | Min-Height | Border Radius |
|-------|-----------|---------|------------|---------------|
| `.blue-block` | `rgba(37 50 75 / 90%)` | `40px 30px` | 400px | 10px |
| `.black-overlay-block` | `rgba(8 7 7 / 80%)` | `40px 30px` | 400px | 10px |
| `.black-50-block` | `rgba(0 0 0 / 50%)` | `40px` | -- | -- |
| `.black-70-block` | `rgba(0 0 0 / 70%)` | `40px` | -- | 10px |
| `.dark-block-75` | `rgba(0 0 0 / 75%)` | `40px` | -- | -- |

### Blue Block Typography

| Element | Size | Color |
|---------|------|-------|
| h2 | 40px (mobile: 30px) | -- |
| h4 | 22px | `#fbd84d` (--yellow) |
| .subhead | 14px, uppercase, letter-spacing: 3px, 600 weight | `#D0F7FF` |

### Black-70 Block

- `display: flex; gap: 20px` (column on mobile)
- `.subhead`: letter-spacing 2px, 600 weight, `#fbd84d` (--yellow), 14px

### Special Content

| Class | Style |
|-------|-------|
| `.callout` | bg: `#f2e6b5`, padding: 1em, border-left: 1em solid `#d3bd64` |
| `.pullquote` | border-left: 6px solid `#d3bd64`, margin-left: 30px, padding: `10px 0 10px 30px` |
| `.mapviewer-block` | background image, cover, min-height: 400px |
| `.turf-block` | background image (`rich-turf.jpg`), cover |

### Spacing Utilities

| Class | Value |
|-------|-------|
| `.pad80` | `padding: 80px 0` |
| `.pad60` | `padding: 60px 0` |
| `.pad40` | `padding: 40px` |
| `.pad20` | `padding: 20px` |

---

## Breadcrumbs

| Property | Value |
|----------|-------|
| Padding | `15px 35px` |
| Font size | 0.9rem |
| "You are here" label | Hidden (`display: none`) |
| Home section | Hidden on home section (`section-east-and-central-grasslands-and-savannas`) |

---

## Grid Layouts (from ploneCustom.css, shared)

| Class | Columns | Gap |
|-------|---------|-----|
| `.grid-container-2col` | `1fr 1fr` | -- |
| `.grid-container-2col-no-gap` | `1fr 1fr` | 0 |
| `.grid-container-3col` | `1fr 1fr 1fr` | -- |
| `.grid-container-4col` | `1fr 1fr 1fr 1fr` | -- |
| `.grid-container-5col` | `repeat(5, 1fr)` | -- |
| `.grid-container-6col` | `repeat(6, 1fr)` | -- |
| `.grid-container-50-25-25` | `50% 25% 25%` | -- |
| `.grid-container-25-50-25` | `25% 50% 25%` | -- |
| `.grid-container-15-70-15` | `15% 70% 15%` | -- |
| `.grid-container-20-80` | `20% 80%` | -- |
| `.grid-container-30-70` | `30% 70%` | -- |
| `.grid-container-70-30` | `70% 30%` | -- |
| `.grid-container-40-60` | `40% 60%` | -- |
| `.grid-container-65-35` | `65% 35%` | -- |

All multi-column grids collapse to single column on mobile (767px or 768px breakpoints).

---

## Footer

### WLFW Footer (`#portal-footer-wlfw`)

| Property | Value |
|----------|-------|
| Display | `block` (default is `display: none` in ploneCustom; sub-site shows it) |
| Background | `#bca647` (--darkgold) |
| Text color | `#fff` |
| Padding | `1.5em` |

### Footer Structure

- `.bottom-nav`: `display: flex; justify-content: space-between; align-items: center` (column on mobile)
- `.ft-menu`: links `#fff`, 15px, line-height 1.8em; hover: `border-bottom: 1px solid #fff`
- `h3`: `#fff`, `border-bottom: 1px solid #ebebeb`, letter-spacing: 2px, 1.5rem
- `.eeo-statement`: 0.75rem, line-height: 1.4em
- `.sitecredit`: 13px, uppercase, letter-spacing: 0.05em, margin: `25px auto 5px`

### Default LP Footer (`#portal-footer`)

Hidden (`display: none`) in this sub-site.

### Site Actions (`#portal-siteactions`)

Background: `#25324b` (dark blue, matches header)

---

## Navigation Tree Portlet

| Property | Value |
|----------|-------|
| `.portletHeader` background | `#425a84` (--heading) |
| `.portletHeader` border-radius | `6px 6px 0 0` |
| `.portletHeader` text | uppercase, padding: 15px |
| `.portletHeader a` color | `#dcc464` (--gold), 600 weight |

---

## Responsive Breakpoints

| Breakpoint | Selectors Affected |
|-----------|-------------------|
| `max-width: 1530px` | `#content` width: 100%, padding: 0 2em |
| `max-width: 1024px` | Nav links: 16px, padding: 10px 15px |
| `max-width: 768px` | Header height: 100px; banner: 195px; search box mobile; nav wrapper; biome menu position; blue-block/black-overlay margins; flex padding; portal-columns padding; LSBox; wlfw-biome-nav-bar; black-70-block column |
| `max-width: 767px` | Nav hidden (toggle); nav items full-width gold bg; h1 sizes; h2.large: 2rem; fire-block bg; footer bottom-nav column |

---

## CSS Load Order

1. `reset.css` — CSS reset
2. `base.css` — Plone base styles (70KB)
3. `jquery.css` — jQuery UI styles (@import)
4. `dropdown-menu.css` — Nav dropdown mechanics (@import)
5. `tinymce.css` — TinyMCE editor styles
6. `print.css` — Print styles
7. `mobile.css` — Mobile overrides (480px handheld)
8. `dateinput.css` — Date input widget (@import)
9. `fullcalendar.css` — Calendar widget (@import)
10. `contentleadimage.css` — Lead image styles
11. `truegallery.css` — Gallery portlet (@import)
12. `ploneboard.css` — Forum styles (@import)
13. `ploneCustom.css` — **Main site-wide custom styles** (130KB, all shared rules)
14. `font-awesome.min.css` — Font Awesome 4.2.0
15. Google Fonts (5 link tags)
16. **`wlfw-grassland.css`** — **Sub-site specific overrides** (863 lines, loaded last = highest priority)

---

## Key Differences from Aquatics Sub-site

| Feature | Aquatics | Grasslands |
|---------|----------|------------|
| Header bg | `#278e95` (teal) | `#25334f` (dark blue) |
| Heading color | (teal-based) | `#425a84` (muted blue) |
| Heading font | -- | Merriweather, serif |
| Body font | Public Sans | Public Sans |
| Gold accent | `#dcc464` | `#dcc464` (same) |
| Footer bg | -- | `#bca647` (dark gold) |
| Banner height | -- | 450px desktop, 195px mobile |
| Nav hover/selected | same pattern | same pattern |

---

## Image Assets Referenced

- `working-lands/WLFW-grassland-logo.png` — Header logo
- `working-lands/restored-prairie-in-ohio.jpg` — Default banner
- `working-lands/ocala-iStock-597928044.jpg` — About banner
- `working-lands/longleaf-pine.jpg` — Resources banner
- `working-lands/fire-images/longleaf-FB-group.jpg` — Training banner
- `working-lands/wlfw-grassland-header.jpg` — Workspace banner
- `working-lands/rich-turf.jpg` — Turf block background
- `working-lands/working-lands-logo.png` — Footer WLFW logo
- `landscape-images/lp-logo-white.svg` — Footer LP logo
- `magnifier-white.png` — Mobile search icon
- `fire-images/mapviewer-bg.jpg` — Map viewer block bg
- `fire-images/sefiremap-2-bg.jpg` — Map viewer block 2 bg
