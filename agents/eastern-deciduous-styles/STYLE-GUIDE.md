# Eastern Deciduous Forests Site — Complete Style Reference

Crawled from: https://dev.landscapepartnership.org/networks/working-lands-for-wildlife/landscapes-wildlife/landscapes/eastern-deciduous-forests

CSS source files: `css/wlfw-forest.css` (sub-site-specific), `css/ploneCustom.css` (site-wide), `css/base.css`, `css/dropdown-menu.css`, `css/mobile.css`

---

## Pages Crawled

| Screenshot | Page | URL (relative to `/eastern-deciduous-forests`) |
|---|---|---|
| `screenshots/01-home.png` | Home | `/` |
| `screenshots/02-about.png` | About | `/about` |
| `screenshots/03-partners.png` | Eastern Deciduous Organizations | `/about/partners` |
| `screenshots/04-wildlife.png` | Wildlife | `/wildlife` |
| `screenshots/05-resources.png` | Resources | `/resources` |
| `screenshots/06-fact-sheets.png` | Fact Sheets | `/resources/facts-sheets` |
| `screenshots/07-maps.png` | Apps, Maps, and Data | `/resources/maps` |
| `screenshots/08-multimedia.png` | Multimedia | `/resources/multimedia` |
| `screenshots/09-training.png` | Training | `/training` |
| `screenshots/10-news.png` | News | `/news` |
| `screenshots/11-workspace.png` | Workspace | `/workspace` |

---

## Color Palette

Defined as CSS custom properties in `wlfw-forest.css` `:root`:

| Variable | Hex | Usage |
|---|---|---|
| `--darkgreen` / `--heading` | `#186450` | Primary brand color; header bg, all headings, nav portlet headers, submenu link hover |
| `--gold` | `#dcc464` | Accents, selected nav text, h1 underline bar, `.subheading` text, nav portlet header link color |
| `--darkgold` | `#bca647` | WLFW footer background (`#portal-footer-wlfw`), `.bg-drk-gold` blocks |
| `--ltgold` | `#ebdc9e` | Light gold background blocks (`.bg-lt-gold`) |
| `--brown` | `#8b7b34` | Site actions bar background (`#portal-siteactions`) |
| `--darkbrown` | `#825640` | Dark brown blocks (`.bg-darkbrown`) |
| `--orange` | `#f88630` | Biome nav hover color, companion-select hover |
| `--yellow` | `#fbd84d` | Blue-block h4 color, subhead labels inside dark blocks |
| `--darkgrey` | `#262626` | Biome navigation bar background, list item text |
| `--grey` | `#f8f5ef` | Light background sections (`.bg-grey`) |
| `--white` | `#ffffff` | Body background, nav link text |

Additional colors used directly (not as variables):

| Value | Usage |
|---|---|
| `#3b3b3b` | Body paragraph text (`p` color) |
| `#3c4d6a` | Intro text, pullquote text |
| `#d8c468` | `.gold-text` link color |
| `#d3bd64` | Pullquote border-left, callout border-left |
| `#f2e6b5` | Callout background |
| `#666666` | Submenu link text |
| `#E86128` | Submenu link hover text |
| `rgba(0 0 0 / 35%)` | Nav hover/selected background, banner caption overlay |
| `rgba(37 50 75 / 90%)` | `.blue-block` background |
| `rgba(8 7 7 / 80%)` | `.black-overlay-block` background |
| `rgb(0 0 0 / 50%)` | `.black-50-block` background |
| `rgb(0 0 0 / 70%)` | `.black-70-block` background |
| `#28526E` | CTA block background (from ploneCustom.css) |
| `rgb(131 84 64)` | `.btn.large-white:hover` in forest context |

---

## Typography

### Font Families (loaded via Google Fonts)

| Font | Weights | Usage |
|---|---|---|
| **Public Sans** | 300, 400, 700 (+ italic) | Body text, nav links, `.subheading`, list items, document description, `.black-50-block h2` |
| **Merriweather** | 400, 400i, 700 | All headings (h1-h6), `.intro` text, `.pullquote`, `.quote` |
| **Montserrat** | 400, 500, 600 | `.heading-white`, subhead labels in blocks, CTA button text |
| **Open Sans** | 400, 400i, 600 | Base body font (ploneCustom.css fallback) |
| **Source Sans Pro** | 400, 700 | Nav links in ploneCustom.css (overridden by wlfw-forest.css) |
| **Material Icons** | — | Icon font for material design icons |
| **Nunito Sans** | 400, 700 (+ italic) | Loaded but usage unclear |

### Heading Styles

| Element | Font | Size | Line-height | Weight | Color | Notes |
|---|---|---|---|---|---|---|
| h1-h6 (all) | Merriweather, serif | varies | 1.5em | 600 | `--heading` (#186450) | letter-spacing: -0.025em |
| h1 / h1.documentFirstHeading | Merriweather | 2.8rem | 3.4rem | 600 | `--heading` | margin-top: 35px; gold underline bar after |
| h1 mobile (<=767px) | Merriweather | 2.1-2.3rem | 2.5-2.6rem | 600 | `--heading` | |
| h2 | Merriweather | 2.3rem | 2.8rem | 600 | `--heading` | |
| h2.large | Merriweather | 2.8rem | — | 600 | `--heading` | mobile: 2rem |
| h3 | Merriweather | 1.7rem | 1.5em | 600 | `--heading` | |
| h4 | Merriweather | 1.5rem | 1.5em | 600 | `--heading` | |

### H1 Gold Underline Bar

```css
h1.documentFirstHeading:after, #content h1:after {
    content: '';
    display: block;
    width: 80px;
    height: 5px;
    background-color: var(--gold);  /* #dcc464 */
    margin-top: 5px;
}
```

### Body Text

| Element | Font | Size | Line-height | Color |
|---|---|---|---|---|
| body | Public Sans, sans-serif | — | — | — |
| p | — | 1.1rem | 1.65rem | #3b3b3b |
| #content li | Public Sans | 1rem | — | `--darkgrey` (#262626) |
| .intro | Merriweather, serif | 18px | 1.6em | #3c4d6a |
| .documentDescription | Public Sans | 1.35em | 1.5em | — (weight 500) |
| .subheading | Public Sans | 1.1rem | — | `--gold` (#dcc464) |

### Special Text

| Class | Font | Size | Color | Notes |
|---|---|---|---|---|
| `.pullquote` | Merriweather, serif | 1.5rem | #3c4d6a | border-left: 6px solid #d3bd64; padding-left: 30px; letter-spacing: -0.05em |
| `.quote` | Merriweather | 20px | — | font-style: italic; margin: 2em |
| `.cite` | — | 0.9rem | — | text-align: center; padding-bottom: 2em |
| `.heading-white` | Montserrat, sans-serif | 2.7em | #fff | font-weight: 600; text-transform: uppercase |
| `.heading-gold` | — | 2.6em | #f7d25b | letter-spacing: -0.025em (from ploneCustom) |
| `.text-shadow` | — | — | — | text-shadow: 1px 2px 10px #3a3a3a |

---

## Layout & Structure

### Page Width

| Element | Width | Notes |
|---|---|---|
| `#visual-portal-wrapper` | max-width: 100% | margin: 0 auto; border-radius: 0 |
| `#content` | 1170px | margin: 1em auto |
| `#content` (<=1530px) | 100% | padding: 0 2em |
| `.template-atct_edit #visual-portal-wrapper` | 1170px | edit mode |
| `#portal-header` (ploneCustom) | 1170px | margin: 0 auto (overridden by wlfw-forest to 100%) |

### Header

| Property | Value | Notes |
|---|---|---|
| Height | 150px | desktop |
| Height (mobile <=768px) | 100px | |
| Background | `--darkgreen` (#186450) | |
| Width | 100% | full-width |

### Logo

| Property | Desktop | Mobile (<=768px) |
|---|---|---|
| Width | 560px | 335px |
| Position | relative, top: 15px, left: 35px | top: -15px, left: 5px |
| Logo container width | — | 340px |

### Banner (#portal-banner)

| Property | Desktop | Mobile (<=768px) |
|---|---|---|
| Height | 450px | 195px |
| Background | `working-lands/forest-crispin-jones-unsplash.jpg` | same |
| Background-size | cover | cover |
| Caption | pseudo-element `:after` with text | hidden on mobile |
| Caption style | 12px white text, `rgba(0 0 0 / 35%)` bg, padding: 0.5rem 1.2rem | — |

Per-section banner overrides:
- **About**: `working-lands/oak-trees-banner.jpg`, caption "Oak trees"
- **Resources**: `working-lands/timber-harvest.jpg`, caption "Harvesting timber"
- **Training**: remote image URL (group walking in woods)
- **News**: caption "toad"
- **Workspace**: same as home

### Breadcrumbs

```css
#portal-breadcrumbs {
    margin-left: 0;
    margin-top: 0;
    padding: 15px 35px;
    font-size: .9rem;
}
#breadcrumbs-you-are-here { display: none; }
```

---

## Navigation

### Biome Navigation Bar (`.wlfw-biome-nav-bar`)

The top-level landscape selector bar above the main nav:

| Property | Value |
|---|---|
| Background | `--darkgrey` (#262626) |
| Padding | 10px 30px |
| Font-weight | 600 |
| Font-size | 12px (desktop), 11px (mobile) |
| Letter-spacing | 1px (desktop), normal (mobile) |
| Link color | #fff, uppercase |
| Link hover | `--orange` (#f88630), uppercase |

Mobile (<=768px): padding 10px 15px, font-size 11px.

### WLFW Navigation Bar

Hidden on this sub-site: `.wlfw-navigation-bar { display: none; }`

### Main Navigation (#portal-globalnav)

Positioned absolutely inside `#globalnav-wrapper`:

| Property | Value |
|---|---|
| Wrapper background | transparent |
| Wrapper position | absolute, top: 100px |
| Nav display | flex, justify-content: right |
| Nav margin-right | 2.5% |
| Nav background | transparent |

### Nav Links

| State | Background | Color | Font | Padding | Other |
|---|---|---|---|---|---|
| Default | transparent | `--white` (#fff) | Public Sans, 1rem, 600, uppercase | 10px 20px | border: 3px solid transparent |
| Hover | `rgba(0 0 0 / 35%)` | `--gold` (#dcc464) | — | — | — |
| Selected | `rgba(0 0 0 / 35%)` | `--gold` (#dcc464) | — | — | — |
| Visited | — | #fff | — | — | — |

At <=1024px: font-size 16px, padding 10px 15px, margin 0 0.125em, text-align center.

### Home Tab Override

```css
#portaltab-home > a {
    background: url(none)!important;
    text-indent: 0;
}
#portaltab-home > a:hover {
    background: rgba(0 0 0 / 35%)!important;
    color: var(--gold) !important;
}
```

Home submenu is hidden: `li#portaltab-home ul.submenu { display: none; }`

### Submenu (Dropdown) Links

| Property | Value |
|---|---|
| Text-transform | none (not uppercase) |
| Font-size | 15px |
| Color | #666666 |
| Hover background | #efefef |
| Hover color | #E86128 (orange) |
| Hover on non-forest | `--darkgreen` (#186450) |

Dropdown container: `position: absolute; width: 15em; background: #fff; box-shadow: 0px 0px 5px #666;` (from dropdown-menu.css / ploneCustom.css).

### Mobile Navigation (<=767px)

```css
#portal-globalnav { display: none; }
#portal-globalnav.opened { display: block; }
#portal-globalnav li {
    width: 100%;
    background: #d8c468;  /* gold background */
}
```

Menu toggle: `.menu-toggle { font-weight: 600; font-size: 13px; padding: 12px 0 12px 35px; }`

### Navigation Portlet (Sidebar Tree)

```css
.portletNavigationTree .portletHeader {
    background: var(--heading);  /* #186450 */
    border-radius: 6px 6px 0 0;
    text-transform: uppercase;
    padding: 15px;
}
.portletNavigationTree .portletHeader a {
    color: var(--gold)!important;  /* #dcc464 */
    font-weight: 600;
}
```

---

## Buttons

### Large White Button (`.btn.large-white`)

| State | Background | Color | Border | Other |
|---|---|---|---|---|
| Default | rgba(255,255,255,0.25) | #fff | 1px solid #fff | uppercase, 14px, 600, letter-spacing: 0.075em, border-radius: 4px |
| Hover | rgb(131 84 64) | #fff | — | forest-specific override |
| Hover (in blue-block) | rgb(8 48 70) | #fff | — | ploneCustom |

### Large Orange Button (`.large-orange`)

| State | Background | Color | Border |
|---|---|---|---|
| Default | #f8903e | #fff | 1px solid #fff |
| Hover | #F7700D | #fff | — |

Other: uppercase, 14px, 600, letter-spacing: 0.075em, border-radius: 4px.

### Grey Button (`.btn-grey`)

| State | Background | Color |
|---|---|---|
| Default | #e6e6e6 | #515151 |
| Hover | #F8903E | #fff |

Other: uppercase, 14px, 600, border-radius: 4px.

### CTA Button (`.cta-button`)

| State | Background | Color | Other |
|---|---|---|---|
| Default | #f7bd4f | #fff | 20px, 600, Montserrat, border-radius: 5px, padding: 15px 25px |
| Hover | #f38b1a | #fff | — |

### Overlay Buttons

| Class | Background | Font-size | Hover |
|---|---|---|---|
| `.overlay-btn` | rgba(0,0,0,0.5) | 20px | rgba(0,0,0,0.6), color #616161 |
| `.overlay-btn-2` | rgba(0,0,0,0.5) | 1.3em | rgba(255,255,255,1), color #222 |
| `.overlay-btn-3` | rgba(0,0,0,0.35) | 1.3em | rgba(0,0,0,0.75), color #f7c60e |

---

## Content Blocks

### Background Utility Classes

| Class | Background | Notes |
|---|---|---|
| `.bg-dark` | `--darkgreen` (#186450) | |
| `.bg-blue` | `--heading` (#186450) | same as dark green |
| `.bg-grey` | `--grey` (#f8f5ef) | |
| `.bg-gold` | `--gold` (#dcc464) | border-top: none |
| `.bg-drk-gold` | `--darkgold` (#bca647) | |
| `.bg-lt-gold` | `--ltgold` (#ebdc9e) | |
| `.bg-orange` | `--orange` (#f88630) | |
| `.bg-brown` | `--brown` (#8b7b34) | |
| `.bg-darkbrown` | `--darkbrown` (#825640) | |

### Blue Block (`.blue-block`)

| Property | Value |
|---|---|
| Background | rgba(37 50 75 / 90%) |
| Padding | 40px 30px |
| Min-height | 400px |
| Margin | 4em 1em |
| Border-radius | 10px |
| h2 | 40px, line-height 1.3em |
| h4 | `--yellow` (#fbd84d), 22px |
| .subhead | 14px, 600, letter-spacing 3px, uppercase, color #D0F7FF |
| p | #fff, 18px, line-height 1.7em |

Mobile (<=768px): margin 2em, h2 30px.

### Black Overlay Block (`.black-overlay-block`)

| Property | Value |
|---|---|
| Background | rgba(8 7 7 / 80%) |
| Padding | 40px 30px |
| Min-height | 400px |
| Margin | 4em 1em |
| Border-radius | 10px |
| .subhead | color #f1d215, 14px, letter-spacing 4px, 600 |

### Black 50% Block (`.black-50-block`)

| Property | Value |
|---|---|
| Background | rgb(0 0 0 / 50%) |
| Padding | 40px |
| Margin | 3em |

### Black 70% Block (`.black-70-block`)

| Property | Value |
|---|---|
| Background | rgb(0 0 0 / 70%) |
| Padding | 40px |
| Margin | 1em |
| Display | flex, gap: 20px |
| Border-radius | 10px |
| .subhead | letter-spacing 2px, 600, `--yellow`, 14px |

Mobile (<=768px): flex-direction: column.

### Callout Block (`.callout`)

| Property | Value |
|---|---|
| Background | #f2e6b5 |
| Padding | 1em |
| Border-left | 1em solid #d3bd64 |
| Clear | both |

### Other Block Classes

| Class | Description |
|---|---|
| `.turf-block` | Background image: `working-lands/rich-turf.jpg`, cover |
| `.mapviewer-block` | Background image: `fire-images/mapviewer-bg.jpg`, min-height 400px |
| `#fire-block` | Background image: `fire-images/outdoor-alabama-slide.jpg`, min-height 400px |
| `#bobscapes-block` | Background image: `bobscapes-images/bobscapes-slide-bg.jpg` |
| `#birdlocale-block` | Background image: `birdlocale-images/birdlocale-block.jpg` |
| `.tan-block` | Background #e7e5da, padding 2rem, border-radius 6px |
| `.block-w-border` | Border: 4px solid #d5d5d5, margin 2rem auto, padding 1rem 2rem |

---

## Search Box

### Desktop

```css
#portal-searchbox {
    margin-right: 20px;
    margin-top: 0;
    padding: 7px;
}
```

### Mobile (<=768px)

```css
#portal-searchbox {
    position: absolute;
    top: 5px;
}
#portal-searchbox [type="submit"] {
    border: none;
    color: transparent;
    background: no-repeat transparent url(magnifier-white.png) center center;
    height: 25px;
    width: 25px;
}
#searchGadget {
    width: 8em;
    padding: 3px;
    border-radius: 6px;
}
```

### LiveSearch Box (`.LSBox`)

Desktop: top 430px, relative position, white bg, padding 10px 13px, border-radius 6px.
Mobile: top 100px, absolute position, transparent bg, left 90px, width 100px.

---

## Footer

### WLFW Footer (`#portal-footer-wlfw`)

| Property | Value |
|---|---|
| Display | block |
| Background | `--darkgold` (#bca647) |
| Color | #fff |
| Width | 100% |
| Padding | 1.5em |

The default `#portal-footer` is hidden (`display: none`).

### Footer Headings

```css
#portal-footer-wlfw h3 {
    margin-top: 0;
    color: #fff;
    border-bottom: 1px solid #ebebeb;
    letter-spacing: 2px;
    font-size: 1.5rem;
}
```

### Footer Menu Links

```css
#portal-footer-wlfw .ft-menu li a {
    color: #fff !important;
    font-size: 15px;
    line-height: 1.8em;
}
#portal-footer-wlfw .ft-menu li a:hover {
    border-bottom: 1px solid #fff;
}
```

### Footer Bottom Navigation

```css
#portal-footer-wlfw .bottom-nav {
    text-align: left;
    margin: 15px;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
/* Mobile: flex-direction: column, text-align: center */
```

### EEO Statement

```css
#portal-footer-wlfw .eeo-statement {
    font-size: .75rem;
    line-height: 1.4em;
    margin-top: 15px;
}
.eeo-statement a {
    font-weight: 600;
    color: #fff!important;
}
.eeo-statement a:hover {
    color: #29457b !important;
}
```

### Site Actions Bar

```css
#portal-siteactions {
    background: var(--brown);  /* #8b7b34 */
}
```

### Site Credit

```css
#portal-footer-wlfw .sitecredit {
    background: url(fergusonlynch-icon.png) no-repeat scroll 0 2px transparent;
    background-size: 36px;
    font-size: 13px;
    letter-spacing: 0.05em;
    line-height: 1.1rem;
    padding-left: 50px;
    text-transform: uppercase;
    margin: 25px auto 5px;
    width: 185px;
}
```

---

## Spacing Utilities

| Class | Value |
|---|---|
| `.pad80` | padding: 80px 0 |
| `.pad60` | padding: 60px 0 |
| `.pad40` | padding: 40px |
| `.pad20` | padding: 20px |
| `.fullwidth-section` | padding: 0 |

---

## Tile / Listing Items

```css
.tileItem { border-top: none; }
.tileHeadline {
    margin-top: 0;
    line-height: 1.6em;
    font-size: 1.75em;
}
#content .tileHeadline a { color: var(--heading); }
```

---

## Responsive Breakpoints

All `@media` rules found in `wlfw-forest.css`:

| Breakpoint | Targets |
|---|---|
| `max-width: 1530px` | #content width goes to 100% with padding |
| `max-width: 1024px` | Nav links: smaller padding, font-size 16px |
| `max-width: 768px` | Header 100px, logo 335px, banner 195px, search repositioned, biome nav 11px, .LSBox repositioned, various block adjustments |
| `max-width: 767px` | Nav hidden (toggle), h1 2.1-2.3rem, h2.large 2rem, mobile-specific layout |

Key differences between 768px and 767px:
- **768px**: Header/banner/searchbox/biome-nav mobile adaptations
- **767px**: Full nav toggle (hide/show), text size reductions

---

## Google Fonts Loaded

```html
<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,400i,600|Source+Sans+Pro:400,700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Merriweather:400,400i,700|Montserrat:400,500,600&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Public+Sans:ital,wght@0,300;0,400;0,700;1,300;1,400&display=swap" rel="stylesheet">
```

---

## Key Differences from Aquatics Sub-site

| Property | Aquatics | Eastern Deciduous Forests |
|---|---|---|
| Primary color (`--darkgreen`/`--heading`) | `#278e95` (teal) | `#186450` (dark forest green) |
| Brown variable | `#825640` | `#8b7b34` (more olive/khaki) |
| Dark brown | — | `#825640` (new variable) |
| Submenu link color | `#176065` | `#666666` |
| Submenu hover color | `#E86128` text, `#efefef` bg | `#E86128` text, `#efefef` bg (same) |
| Submenu non-hover link color override | `--darkgreen` (#186450) | `--darkgreen` (#186450) |
| `.btn.large-white:hover` | — | `rgb(131 84 64)` (brown) |
| Mobile nav background | — | `#d8c468` (gold) |

---

## CSS File Inventory

| File | Lines | Purpose |
|---|---|---|
| `wlfw-forest.css` | 835 | Sub-site-specific styles (colors, header, nav, banners, typography, blocks, footer) |
| `ploneCustom.css` | 6323 | Site-wide custom styles (base layout, buttons, blocks, footer, nav base) |
| `base.css` | 2418 | Plone base styles (lists, tables, forms, portlets) |
| `dropdown-menu.css` | 102 | Dropdown navigation mechanics (positioning, show/hide) |
| `mobile.css` | 68 | Legacy mobile styles (max-device-width: 480px) |
| `reset.css` | 19 | CSS reset |
| `print.css` | 154 | Print stylesheet |
| `fullcalendar.css` | 1035 | Calendar widget styles |
| `jquery-ui.css` | 411 | jQuery UI component styles |
| `dateinput.css` | 152 | Date input widget |
| `tinymce.css` | 39 | TinyMCE editor styles |
| `contentleadimage.css` | 16 | Lead image styles |
| `ploneboard.css` | 134 | Discussion board styles |
| `truegallery.css` | 835 | Gallery portlet styles |
