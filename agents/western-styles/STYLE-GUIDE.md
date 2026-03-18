# Western Landscapes Sub-site Style Guide

**Source URL:** https://dev.landscapepartnership.org/networks/working-lands-for-wildlife/landscapes-wildlife/landscapes/western-landscapes
**Sub-site CSS:** `wlfw-western.css` (16 KB)
**Shared CSS:** `ploneCustom.css` (130 KB)
**Date captured:** 2025-03-18

---

## Page Inventory

| # | Page | URL Path (relative to sub-site root) | Body Classes |
|---|------|--------------------------------------|--------------|
| 1 | Home | `/` (western-wlfw) | `site-western-landscapes section-western-wlfw` |
| 2 | About | `/about` | `site-western-landscapes section-about` |
| 3 | Wildlife | `/wildlife` | `site-western-landscapes section-wildlife` |
| 4 | Resources | `/resources` | `site-western-landscapes section-resources` |
| 5 | Training | `/training` | `site-western-landscapes section-training` |
| 6 | Workspace | `/workspace` | `site-western-landscapes section-workspace` |
| 7 | Partners | `/about/partners` | `site-western-landscapes section-partners` |
| 8 | Great Plains Grassland Biome Framework | `/resources/great-plains-grassland-biome-framework` | `site-western-landscapes section-great-plains-grassland-biome-framework` |
| 9 | Sagebrush Biome Framework | `/resources/sagebrush-biome-framework` | `site-western-landscapes section-sagebrush-biome-framework` |
| 10 | Apps, Maps, and Data | `/resources/maps` | `site-western-landscapes section-maps` |

### Navigation Structure (Primary)
- Home
- About (sub: Partners)
- Wildlife (sub: Sage Grouse [ext], Lesser Prairie-Chicken [ext], Southwestern Willow Flycatcher [ext], Hawaiian Nene [ext], Kenai Peninsula Salmon [ext])
- Resources (sub: Great Plains Grassland Biome Framework, Sagebrush Biome Framework, Apps Maps and Data)
- Training
- Workspace

---

## Color Palette

### CSS Custom Properties (defined in `wlfw-western.css :root`)

| Variable | Hex | Usage |
|----------|-----|-------|
| `--darkgrey` | `#262626` | Return-to bar background |
| `--purple` | `#486182` | Header background, bg-dark, bg-purple, submenu hover text |
| `--heading` | `#5a6e88` | All headings (h1-h6), tile headlines, nav tree header bg |
| `--gold` | `#dcc464` | Nav selected/hover text, h1 underline bar, subheading text, nav tree header link, callout border |
| `--ltgold` | `#ebdc9e` | bg-lt-gold blocks |
| `--darkgold` | `#bca647` | Footer background (`#portal-footer-wlfw`) |
| `--brown` | `#8b7b34` | Site actions bar background |
| `--grey` | `#f8f5ef` | bg-grey blocks |
| `--orange` | `#f88630` | bg-orange, return-bar hover, companion-select hover |
| `--yellow` | `#fbd84d` | Blue-block h4, black-70-block subhead |
| `--white` | `#ffffff` | Body background, nav link text |

### Additional Colors (hard-coded)

| Hex | Usage |
|-----|-------|
| `#d8c468` | `.gold-text`, mobile nav bg for opened nav items |
| `#3b3b3b` | Body paragraph text |
| `#3c4d6a` | `.intro` text, pullquote text |
| `#666666` | Submenu link text |
| `#E86128` | Submenu link hover text |
| `#efefef` | Submenu link hover background |
| `#f2e6b5` | `.callout` background |
| `#d3bd64` | Pullquote border-left, callout border-left |
| `#D0F7FF` | Blue-block `.subhead` text |
| `#f1d215` | Black-overlay-block `.subhead` text |
| `#29457b` | EEO statement link hover |
| `rgba(0 0 0 / 35%)` | Nav hover/selected background, banner caption background |
| `rgba(37 50 75 / 90%)` | `.blue-block` background |
| `rgba(8 7 7 / 80%)` | `.black-overlay-block` background |
| `rgb(0 0 0 / 50%)` | `.black-50-block` background |
| `rgb(0 0 0 / 70%)` | `.black-70-block` background |

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

### Font Usage

| Element | Font Family | Weight | Size | Line-height | Color | Notes |
|---------|-------------|--------|------|-------------|-------|-------|
| `body` | Public Sans, sans-serif | 400 | - | - | - | `-webkit-font-smoothing: antialiased` |
| `h1-h6` | Merriweather, serif | 600 | varies | 1.5em | `--heading` (#5a6e88) | `letter-spacing: -0.025em` |
| `h1.documentFirstHeading` | Merriweather | 600 | 2.8rem | 3.4rem | `--heading` | Gold underline bar (80px x 5px) after |
| `h1` (in `#content`) | Merriweather | 600 | 2.8rem | 3.4rem | `--heading` | Gold underline bar after |
| `h2` | Merriweather | 600 | 2.3rem | 2.8rem | `--heading` | |
| `h2.large` | Merriweather | 600 | 2.8rem | - | `--heading` | Mobile: 2rem |
| `h3` | Merriweather | 600 | 1.7rem | 1.5em | `--heading` | |
| `h4` | Merriweather | 600 | 1.5rem | 1.5em | `--heading` | |
| `p` | Public Sans | 400 | 1.1rem | 1.65rem | `#3b3b3b` | |
| `.intro` | Merriweather, serif | 400 | 18px | 1.6em | `#3c4d6a` | |
| `.subheading` | Public Sans | 400 | 1.1rem | - | `--gold` | `display: block` |
| `.heading-white` | Montserrat, sans-serif | 600 | 2.7em | - | `#fff` | `text-transform: uppercase; letter-spacing: -0.025em` |
| `#content li` | Public Sans, sans-serif | 400 | 1rem | - | `--darkgrey` | `letter-spacing: 0.01em; margin-bottom: 10px` |
| `.documentDescription` | Public Sans, sans-serif | 500 | 1.35em | 1.5em | - | |
| Nav links | Public Sans | 600 | 1rem | - | `#fff` | `text-transform: uppercase` |
| Submenu links | (inherited) | - | 15px | - | `#666666` | `text-transform: none` |
| `.pullquote` | Merriweather, serif | 400 | 1.5rem | 1.5em | `#3c4d6a` | `letter-spacing: -0.05em; border-left: 6px solid #d3bd64` |
| `.quote` | Merriweather | italic | 20px | - | - | |
| `.cite` | - | - | 0.9rem | - | - | `text-align: center` |
| Breadcrumbs | - | - | 0.9rem | - | - | `padding: 15px 35px` |

### Mobile Typography

| Element | Size | Line-height |
|---------|------|-------------|
| `h1.documentFirstHeading` | 2.1rem | 2.5rem |
| `#content h1` | 2.3rem | 2.6rem |
| `h2.large` | 2rem | - |

---

## Layout & Structure

### Page Width
- `#visual-portal-wrapper`: `max-width: 100%; margin: 0 auto`
- `#content`: `width: 1170px; margin: 1em auto`
- `#content` (below 1530px): `width: 100%; padding: 0 2em`
- `.narrow`: `width: 1170px; margin: 0 auto` (mobile: `max-width: 100%; padding: 0 1rem`)
- `.template-atct_edit #visual-portal-wrapper`: `width: 1170px`

### Header
- `#portal-header`: `width: 100%; height: 150px; background-color: var(--purple)` (#486182)
- Mobile (max-width: 768px): `height: 100px`
- Logo: `width: 465px; top: 15px; left: 35px` (relative positioned)
- Mobile logo: `width: 320px; top: -18px; left: 5px`

### Return-to Bar
- `.wlfw-biome-nav-bar`: Dark grey (#262626) background, `padding: 10px 30px`, `font-weight: 600`, `font-size: 12px`, `letter-spacing: 1px`, white uppercase text
- Hover: orange text (`--orange`)
- Mobile: `padding: 10px 15px`, `font-size: 11px`, `letter-spacing: normal`

### Banner
- `#portal-banner`: `height: 450px`, `background-size: cover`
- Mobile (max-width: 768px): `height: 195px`
- Caption pseudo-element (`:after`): `font-size: 12px`, white text, `bottom: 15px; left: 15px`, `background: rgba(0 0 0 / 35%)`, `max-width: 430px`
- Per-section banner images set via `.site-western-landscapes.section-{name} #portal-banner`

### Fullwidth Sections
- `.fullwidth-section`: `width: 100vw; position: relative; margin-left: -50vw; left: 50%; padding: 2em 0`
- The sub-site overrides: `padding: 0`

### Grid Containers (from ploneCustom.css)
- `.grid-container-2col`: `grid-template-columns: 50% 1fr; grid-gap: 30px` (mobile: `100%`)
- `.grid-container-3col`: `repeat(3, minmax(0, 1fr)); gap: 30px` (mobile: `block`)
- `.grid-container-4col`: `repeat(4, minmax(0, 1fr))` (mobile: `auto`)
- `.grid-container-5col`: `repeat(5, 1fr); grid-gap: 20px` (mobile: `block`)

---

## Navigation

### Global Nav Wrapper
- `#globalnav-wrapper`: `background-color: transparent; top: 100px; border-top: none`
- Mobile (max-width: 768px): `width: 100%; top: 105px; left: 0`

### Nav Links
- `#portal-globalnav`: `display: flex; justify-content: right; margin-right: 2.5%; background-color: transparent`
- `#portal-globalnav li a`: `background-color: transparent; font-size: 1rem; font-weight: 600; text-transform: uppercase; padding: 10px 20px; border: 3px solid transparent; font-family: 'Public Sans'; color: #fff`
- Tablet (max-width: 1024px): `font-size: 16px; padding: 10px 15px; margin: 0 0.125em`

### Nav States
- **Hover:** `background: rgba(0 0 0 / 35%); color: var(--gold)` (#dcc464)
- **Selected:** `background: rgba(0 0 0 / 35%); color: var(--gold)` (#dcc464)
- **Visited:** `color: #fff`

### Home Tab
- `#portaltab-home > a`: No background image, text visible (not icon-only)
- Hover: `background: rgba(0 0 0 / 35%); color: var(--gold)`

### Submenu/Dropdown
- Dropdown: `position: absolute; width: 15em; background: #fff`
- `#portal-globalnav ul.submenu a`: `text-transform: none; font-size: 15px; color: #666666`
- Hover: `background-color: #efefef; color: #E86128`
- Home tab submenu: `display: none` (hidden)

### Mobile Nav
- `#portal-globalnav` (max-width: 767px): `display: none`
- `#portal-globalnav.opened`: `display: block`
- `#portal-globalnav li`: `width: 100%; background: #d8c468` (gold)
- `.menu-toggle`: `font-weight: 600; font-size: 13px; padding: 12px 0 12px 35px`

### Landscape Biome Menu
- `.landscape-biome-menu`: `display: block`
- Mobile (max-width: 768px): `position: absolute; top: 304px`

### Search Box
- `.LSBox`: `top: 430px; position: relative; background: #fff; padding: 10px 13px; border-radius: 6px; right: 5%`
- Mobile: `top: 100px; position: absolute; background: transparent; left: 90px; width: 100px`
- `.LSBox .searchSection`: `display: none`

---

## Buttons

### `.btn.large-white` (from ploneCustom.css)
- `border: 1px solid #fff; padding: 15px; text-transform: uppercase; background: rgba(255,255,255,0.25); color: #fff; letter-spacing: 0.075em; border-radius: 4px; font-size: 14px; font-weight: 600`
- Hover: `background: rgba(255,0,0,0.25)`
- In `.blue-block`: hover `background: rgb(8 48 70)`
- Sub-site override: hover `background: rgb(131 84 64)`

### `.btn-grey`
- `padding: 10px 15px; text-transform: uppercase; background: #e6e6e6; color: #515151; border-radius: 4px; font-size: 14px; font-weight: 600`
- Hover: `background: #F8903E; color: #fff`

### `.btn-blue`
- `background-color: #0e71eb; border-color: #0e71eb; color: #fff; padding: 8px 15px; border-radius: 8px`
- Hover: `background: #1a5cbb`

### `.cta-button`
- `padding: 15px 25px; background: #f7bd4f; font-size: 20px; border-radius: 5px; border: 1px solid #fff; margin: 0 1.5em`
- Hover: `background: #f38b1a`
- Link: `color: #fff; font-family: 'Montserrat'; font-weight: 600`

### `.button` (generic)
- `padding: 10px 20px; margin: 10px 0; background-color: white; border: 1px solid #d6d7d8; border-radius: 5px; font-size: 18px`
- Mobile: `display: block`

### `.button-large`
- Same as `.button` but `font-size: 22px`

---

## Content Blocks

### `.blue-block`
- Sub-site: `background: rgba(37 50 75 / 90%); padding: 40px 30px; min-height: 400px; margin: 4em 1em; border-radius: 10px`
- `h2`: `font-size: 40px; line-height: 1.3em` (mobile: 30px)
- `h4`: `color: var(--yellow); font-size: 22px`
- `.subhead`: `letter-spacing: 3px; font-weight: 600; color: #D0F7FF; font-size: 14px; text-transform: uppercase`

### `.black-overlay-block`
- `background: rgba(8 7 7 / 80%); padding: 40px 30px; min-height: 400px; margin: 4em 1em; border-radius: 10px`
- `.subhead`: `color: #f1d215; font-size: 14px; letter-spacing: 4px; font-weight: 600`

### `.black-50-block`
- `background: rgb(0 0 0 / 50%); padding: 40px; margin: 3em`

### `.black-70-block`
- `background: rgb(0 0 0 / 70%); padding: 40px; margin: 1em; display: flex; gap: 20px; border-radius: 10px`
- `.subhead`: `letter-spacing: 2px; font-weight: 600; color: var(--yellow); font-size: 14px`
- Mobile: `flex-direction: column`

### `.callout`
- `background: #f2e6b5; padding: 1em; border-left: 1em solid #d3bd64`

### `.pullquote`
- `padding: 10px 0 10px 30px; border-left: 6px solid #d3bd64; margin-left: 30px`

### Background Utility Classes
- `.bg-dark` / `.bg-purple`: `background: var(--purple)` (#486182)
- `.bg-grey`: `background: var(--grey)` (#f8f5ef)
- `.bg-gold`: `background: var(--gold); border-top: none`
- `.bg-drk-gold`: `background: var(--darkgold)` (#bca647)
- `.bg-lt-gold`: `background: var(--ltgold)` (#ebdc9e)
- `.bg-orange`: `background: var(--orange)` (#f88630)

### `#wlfw-west` (landscape background block)
- `background-image: url(working-lands/large_sagebrush_landscape.jpg); background-size: cover; padding: 3em 0; margin-bottom: -10px`

---

## Footer

### `#portal-footer-wlfw` (WLFW sub-site footer - ACTIVE)
- `display: block; background: var(--darkgold)` (#bca647); `color: #fff; width: 100%; padding: 1.5em`
- `h3`: `margin-top: 0; color: #fff; border-bottom: 1px solid #ebebeb; letter-spacing: 2px; font-size: 1.5rem`
- `.bottom-nav`: `display: flex; align-items: center; justify-content: space-between; text-align: left; margin: 15px`
- Mobile: `text-align: center; flex-direction: column`
- `.ft-menu`: `color: #fff; text-align: center`
- `.ft-menu li a`: `color: #fff; font-size: 15px; line-height: 1.8em`
- `.ft-menu li a:hover`: `border-bottom: 1px solid #fff`
- `.eeo-statement`: `font-size: 0.75rem; line-height: 1.4em; margin-top: 15px`
- `.sitecredit`: `background: url(fergusonlynch-icon.png); font-size: 13px; text-transform: uppercase; margin: 25px auto 5px; width: 185px`

### `#portal-footer` (Main LP footer - also visible)
- `background: #2e76a0; color: #fff; padding: 1.5em`
- Contains 5-column grid with logos, Learn/Browse/Contact sections

### `#portal-siteactions`
- Sub-site: `background: var(--brown)` (#8b7b34)
- Base: `background: #000; text-align: center`

---

## Spacing & Utility Classes

### Padding
- `.pad80`: `padding: 80px 0`
- `.pad60`: `padding: 60px 0`
- `.pad40`: `padding: 40px`
- `.pad30`: `padding: 30px`
- `.pad20`: `padding: 20px`
- `.pad10`: `padding: 10px`

### Spacing
- `.space`: `height: 25px`
- `.space10`: `height: 10px`
- `.space15`: `height: 15px`
- `.space20`: `height: 20px`
- `.space30`: `height: 30px`
- `.space-left`: `margin-left: 2em`
- `.space-right`: `margin-right: 2em`

### Flex
- `.flex`: `display: flex; align-items: center`
- `.flex-block`: `display: flex; align-items: center` (mobile: `flex-direction: column`)
- `.flex-container`: `display: flex; align-items: flex-start` (mobile: `flex-direction: column`)
- `.flex-item`: `flex: 1`
- `.flex-item-wrap`: `flex: 1`
- `.flex-item-column`: `flex-direction: column; align-items: center; justify-content: center`

### Gaps
- `.gap10`: `gap: 10px`
- `.gap15`: `gap: 15px`
- `.gap20`: `gap: 20px`
- `.gap30`: `gap: 30px`

### Other
- `.white, .white a`: `color: #fff`
- `.center`: `text-align: center`
- `.center-mobile` (max-width: 767px): `text-align: center`
- `.text-shadow`: `text-shadow: 1px 2px 10px #3a3a3a`
- `.rounded`: `border-radius: 8px`
- `.rounded15`: `border-radius: 15px`
- `img.rounded`: `border-radius: 5px`
- `.responsive`: (responsive image class)
- `.underline`: underline decoration
- `.last-block`: `padding-bottom: 0; margin-bottom: -1em`

---

## Responsive Breakpoints

| Breakpoint | Target | Key Changes |
|------------|--------|-------------|
| `max-width: 1530px` | Large desktop | `#content`: `width: 100%; padding: 0 2em` |
| `max-width: 1024px` | Tablet | Nav links: `font-size: 16px; padding: 10px 15px` |
| `max-width: 768px` | Mobile / small tablet | Header: `100px`; Banner: `195px`; Nav wrapper: full width; Search box repositioned; `.narrow`: `max-width: 100%`; `.wlfw-biome-nav-bar`: smaller font; Grid layouts collapse to single column; `.black-70-block`: column direction; `.flex`: `padding: 30px` |
| `max-width: 767px` | Mobile | Nav hidden (toggle); Nav items: gold bg full-width; `h1`: `2.1-2.3rem`; `h2.large`: `2rem`; `.center-mobile`: center text; Footer: column direction; Grid 3-col/5-col: block layout |
| `max-device-width: 480px` | Handheld (mobile.css) | Logo hidden; font-size increases for touch targets |
| `max-width: 600px` | Small mobile | `.button`: `display: block` |

---

## Miscellaneous

### Navigation Tree Portlet
- `.portletNavigationTree .portletHeader`: `background: var(--heading); border-radius: 6px 6px 0 0; text-transform: uppercase; padding: 15px`
- Header link: `color: var(--gold); font-weight: 600`

### Tile Items
- `.tileItem`: `border-top: none`
- `.tileHeadline`: `margin-top: 0; line-height: 1.6em; font-size: 1.75em`
- `.tileHeadline a`: `color: var(--heading)`

### Login
- `.loginbutton`: `display: block`
- `#anon-personalbar`: `display: none`
- `#portal-personaltools-wrapper`: `right: 260px; top: -38px; position: absolute`
- Mobile: `right: 20px; top: 330px`

### Images
- `img.image-left, img.image-right, .captioned img`: `border: none`

### Banner Captions by Section
- Home: "Centennial Valley, MT. Credit: Jeremy Roberts, Conservation Media"
- About: "Oak trees"
- Resources: "Harvesting timber"
- Training: (empty)
- Workspace: "Crispin Jones, UnSplash"

### Elements Hidden on This Sub-site
- `.nest-navigation-bar`: `display: none`
- `.wlfw-navigation-bar`: `display: none` (WLFW logo bar)
- `#portal-footer`: hidden by sub-site override (`display: none`)
- `#breadcrumbs-you-are-here`: `display: none`
- `.top-header`: `display: none`

### Icon Font
- Font Awesome 4.2.0: `//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css`
- Material Icons: `https://fonts.googleapis.com/icon?family=Material+Icons`
