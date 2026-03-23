# Aquatics Site — Complete Style Reference

Crawled from: https://landscapepartnership.org/networks/working-lands-for-wildlife/landscapes-wildlife/landscapes/aquatics

CSS source files: `css/wlfw-aquatics.css` (aquatics-specific), `css/ploneCustom.css` (site-wide), `css/base.css`, `css/mobile.css`

---

## Pages Crawled

| Screenshot | Page | URL |
|---|---|---|
| `screenshots/01-home.png` | Home | `/aquatics` |
| `screenshots/02-about.png` | About | `/aquatics/about` |
| `screenshots/03-meet-team.png` | Meet Our Team | `/aquatics/about/connect-contact` |
| `screenshots/04-acf-partnerships.png` | ACF Partnerships | `/aquatics/about/acf-partnerships` |
| `screenshots/05-organizations.png` | Aquatic Organizations | `/aquatics/about/partners` |
| `screenshots/06-wildlife.png` | Wildlife | `/aquatics/wildlife` |
| `screenshots/07-resources.png` | Resources | `/aquatics/resources` |
| `screenshots/08-framework.png` | Aquatic Connectivity Framework | `/aquatics/resources/framework` |
| `screenshots/09-news.png` | News & Stories | `/aquatics/news-and-stories` |
| `screenshots/10-stories.png` | Stories | `/aquatics/news-and-stories/stories` |

---

## Color Palette

Defined as CSS custom properties in `wlfw-aquatics.css` `:root`:

| Variable | Hex | Usage |
|---|---|---|
| `--darkgreen` / `--heading` | `#278e95` | Primary brand color; header bg, all headings, nav portlet headers |
| `--gold` | `#dcc464` | Accents, selected nav links, h1 underline bar, `.subheading` text |
| `--darkgold` | `#bca647` | Footer background (`.portal-footer-wlfw`) |
| `--ltgold` | `#ebdc9e` | Light gold background blocks |
| `--brown` | `#825640` | Site actions bar background |
| `--orange` | `#f88630` | Button backgrounds, hover states |
| `--yellow` | `#fbd84d` | Subhead labels inside dark blocks |
| `--darkgrey` | `#262626` | Biome navigation bar background |
| `--grey` | `#f8f5ef` | Light background sections |
| `--ltgrey` | `#efefef` | Subtle background blocks |
| `--white` | `#ffffff` | Body background |

Additional colors used directly (not as variables):

| Value | Usage |
|---|---|
| `#3b3b3b` | Body paragraph text |
| `#3c4d6a` | Intro text, pullquote text |
| `#176065` | Submenu link color |
| `#d3bd64` | Pullquote border, callout border |
| `#f2e6b5` | Callout background |
| `#345a67` | Timeline slider background |
| `rgba(38,96,116,0.65)` | Timeline item overlay |
| `#28526E` | CTA block background |

---

## Typography

### Font Families

Loaded via Google Fonts:
- **Merriweather** (400, 400i, 700) — headings
- **Montserrat** (400, 500, 600) — CTA buttons, subheads, `.heading-white`
- **Public Sans** (300, 400, 700, italic) — body text, navigation
- **Open Sans** (400, 400i, 600) — base site body fallback
- **Source Sans Pro** (400, 700) — loaded but secondary
- **Nunito Sans** (400, 700, italic) — loaded but secondary
- **Material Icons** — icon font

### Body Text

```css
body {
  font-family: 'Public Sans', sans-serif;
  background: #ffffff;
  -webkit-font-smoothing: antialiased;
  line-height: 1.5em;           /* from ploneCustom base */
}

p {
  color: #3b3b3b;
  font-size: 1.1rem;
  line-height: 1.65rem;
}
```

### Headings

All headings share a base rule (aquatics override, takes precedence):

```css
h1, h2, h3, h4, h5, h6 {
  color: var(--heading);        /* #278e95 */
  font-family: 'Merriweather', serif;
  line-height: 1.5em;
  letter-spacing: -0.025em;
  font-weight: 600;
  margin: 1em 0 0.5em;
}
```

| Element | Font Size | Line Height | Notes |
|---|---|---|---|
| `h1` / `h1.documentFirstHeading` | `2.8rem` | `3.4rem` | Has gold underline bar via `::after` |
| `h1` mobile | `2.3rem` | `2.6rem` | `max-width: 767px` |
| `h2` | `2.3rem` | `2.8rem` | — |
| `h2.large` | `2.8rem` | — | `margin: 0 0 0.5em` |
| `h3` | `1.6rem` | — | — |
| `h4` | `1.3rem` | — | — |

### H1 Gold Underline Bar

```css
h1.documentFirstHeading::after, #content h1::after {
  content: '';
  display: block;
  width: 80px;
  height: 5px;
  background-color: var(--gold);   /* #dcc464 */
  margin-top: 5px;
}
```

### Special Text Classes

```css
.subheading {
  display: block;
  font-family: 'Public Sans';
  font-size: 1.1rem;
  color: var(--gold);            /* #dcc464 */
}

.intro {
  font-size: 18px;
  line-height: 1.6em;
  color: #3c4d6a;
  font-family: 'Merriweather', serif;
  margin: 1em 0;
}

.pullquote {
  font-family: 'Merriweather', serif;
  font-size: 1.5rem;
  line-height: 1.5em;
  letter-spacing: -0.05em;
  color: #3c4d6a;
  padding: 10px 0 10px 30px;
  border-left: 6px solid #d3bd64;
  margin-left: 30px;
}

.callout {
  background: #f2e6b5;
  padding: 1em;
  border-left: 1em solid #d3bd64;
  clear: both;
}

.quote {
  font-size: 20px;
  font-family: 'Merriweather';
  font-style: italic;
  margin: 2em;
}

.cite {
  text-align: center;
  font-size: .9rem;
  padding-bottom: 2em;
}

.text-shadow {
  text-shadow: 1px 2px 10px #3a3a3a;
}

.heading-white {
  color: #fff !important;
  font-weight: 600;
  letter-spacing: -0.025em;
  font-family: 'Montserrat', sans-serif;
  font-size: 2.7em;
  text-transform: uppercase;
}

.heading-gold {
  color: #f7d25b !important;
  letter-spacing: -0.025em;
  font-size: 2.6em;
  margin: 30px 0 10px;
  line-height: 2.3rem;
}

.heading-large {
  font-size: 2.3em;
  margin: 1em 0 0.5em;
}
```

### List Items

```css
#content li {
  color: var(--darkgrey);       /* #262626 */
  font-size: 1rem;
  letter-spacing: 0.01em;
  margin-bottom: 10px;
  font-family: 'Public Sans', sans-serif;
}
```

### Document Description / Subtitle

```css
#content .documentDescription,
#content #description {
  font-size: 1.35em;
  line-height: 1.5em;
  font-family: 'Public Sans', sans-serif;
  font-weight: 500;
}
```

### News / Feed Items

```css
.tileHeadline {
  margin-top: 0;
  line-height: 1.6em;
  font-size: 1.75em;
}

#content .tileHeadline a { color: var(--heading); }

.card-title {
  font-size: 1.2rem;
  line-height: 1.6rem;
}
```

---

## Layout & Structure

### Page Width

```css
#content {
  margin: 1em auto;
  width: 80%;
}

@media only screen and (max-width: 1530px) {
  #content { width: 85%; }
}

/* Reusable container classes */
.narrow,
.inner-container {
  width: 1170px;
  margin: 0 auto;
}

@media only screen and (max-width: 768px) {
  .narrow, .inner-container {
    max-width: 100%;
    padding: 0 1rem;
  }
}
```

### Portal Header

```css
#portal-header {
  width: 100%;
  height: 150px;
  background-color: var(--darkgreen);   /* #278e95 */
  box-shadow: 0px 10px 20px -10px rgba(0,0,0,0.75);
}

/* Mobile */
@media only screen and (max-width: 768px) {
  #portal-header { height: 100px; }
}
```

### Logo

```css
#portal-logo img {
  width: 300px;
  position: relative;
  top: 15px;
  left: 35px;
}
```

### Banner / Hero Image

Each section has a different background image. Base:

```css
#portal-banner {
  display: block;
  height: 450px;
  background: url(aquatic-images/florida-wetlands.jpg) no-repeat center;
  background-size: cover;
}

@media only screen and (max-width: 768px) {
  #portal-banner { height: 195px; }
}
```

Per-section banner overrides:

| Section class | Image |
|---|---|
| Default (home) | `aquatic-images/florida-wetlands.jpg` |
| `.section-about` | `aquatic-images/usda-flickr-group-at-water.jpg` |
| `.section-wildlife` | `sydney-herron-unsplash.jpg` |
| `.section-resources` | `aquatic-images/baby-bog-turtle.webp` |
| `.section-resources.subsection-framework` | `aquatic-images/iStock-1769416417.webp` |
| `.section-news-and-stories` | `working-lands/scuba-scientists.jpg`, height 350px |
| `.section-news-and-stories.subsection-stories` | `aquatic-images/forest-stream-IMG_0746.webp` |
| `.section-training` | `working-lands/working-near-pond.jpg` |
| `.section-about.subsection-workspace` | `aquatic-images/usfws-prairie-potholes.jpg`, height 350px |
| `.section-maps-and-data` | `aquatic-images/ACF-watershed-map-banner.jpg`, height 350px |

---

## Navigation

### Global Navigation Bar

```css
#globalnav-wrapper {
  background-color: transparent;
  top: 100px;
  border-top: none;
}

#portal-globalnav {
  display: flex;
  justify-content: right;
  margin-right: 2.5%;
  background-color: transparent;
}

#portal-globalnav li a {
  background-color: transparent;
  font-size: 1rem;
  font-weight: 600;
  text-transform: uppercase;
  padding: 10px 20px;
  border: 3px solid transparent;
  margin: 0 0.15em;
  font-family: 'Public Sans';
  color: #ffffff !important;
}

/* Hover & selected */
#portal-globalnav a:hover,
#portal-globalnav .selected a:hover {
  background: rgba(0,0,0,0.35);
  color: var(--gold) !important;
}

#portal-globalnav .selected a {
  background: rgba(0,0,0,0.35);
  color: var(--gold) !important;
}

/* Submenu */
#portal-globalnav ul.submenu a {
  text-transform: none;
  font-size: 15px;
  color: #176065 !important;
}

#portal-globalnav ul.submenu a:hover {
  background-color: #efefef !important;
  color: #E86128 !important;
}
```

### Biome Navigation Bar (top landscape switcher)

```css
.wlfw-biome-nav-bar {
  background: var(--darkgrey);   /* #262626 */
  display: block;
  padding: 10px 30px;
  font-weight: 600;
  font-size: 12px;
  letter-spacing: 1px;
  z-index: 20;
}

.wlfw-biome-nav-bar a {
  color: #fff !important;
  text-transform: uppercase;
}

.wlfw-biome-nav-bar a:hover {
  color: var(--orange) !important;   /* #f88630 */
}
```

### Navigation Portlet (sidebar)

```css
.portletNavigationTree .portletHeader {
  background: var(--heading);       /* #278e95 */
  border-radius: 6px 6px 0 0;
  text-transform: uppercase;
  padding: 15px;
}

.portletNavigationTree .portletHeader a {
  color: var(--gold) !important;    /* #dcc464 */
  font-weight: 600;
}
```

### Breadcrumbs

```css
#portal-breadcrumbs {
  margin-left: 0;
  margin-top: 0;
  padding: 15px 35px;
  font-size: .9rem;
}
```

### Anchor Menu (in-page section nav)

```css
#anchor-menu-block {
  background: #efefef;
  display: grid;
  border-top: 7px solid #a6c372;
  border-bottom: 1px solid #e2dcdc;
  margin-top: -15px;
}

#content ul.anchor-menu {
  display: flex;
  flex-wrap: wrap;
  padding: 0;
  list-style: none;
  margin: 0 auto;
}

#content li.anchor-menu-item {
  padding: 15px 20px 5px;
  font-size: 17px;
  text-align: center;
  font-weight: 600;
  line-height: 1.2rem;
  text-transform: uppercase;
  flex: 1 1 auto;
}

.anchor-menu-item a.selected {
  color: #ff6c00 !important;
}
```

---

## Buttons

```css
a.btn-orange {
  color: #fff !important;
  letter-spacing: 1px;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 13px;
  background: #ef8f39;
}

#content a.large-orange {
  border: 1px solid #fff;
  padding: 15px;
  text-transform: uppercase;
  background: #f8903e;
  color: #fff !important;
  letter-spacing: 0.075em;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 600;
}
#content a.large-orange:hover { background: #F7700D; }

#content a.btn-grey {
  padding: 10px 15px;
  text-transform: uppercase;
  background: #e6e6e6;
  color: #515151 !important;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 600;
}
#content a.btn-grey:hover { background: #F8903E; color: #fff !important; }

#content a.btn.large-white {
  border: 1px solid #fff;
  padding: 15px;
  text-transform: uppercase;
  background: rgba(255,255,255,0.25);
  color: #fff !important;
  letter-spacing: 0.075em;
  border-radius: 4px;
  font-size: 14px;
  font-weight: 600;
}

.cta-button {
  padding: 15px 25px;
  background: #f7bd4f;
  font-size: 20px;
  border-radius: 5px;
  text-align: center;
  margin: 0 1.5em;
  border: 1px solid #fff;
}
.cta-button:hover { background: #f38b1a; }

#content .cta-button a {
  color: #fff;
  font-family: 'Montserrat';
  font-weight: 600;
}

a.overlay-btn {
  background: rgba(0,0,0,0.5);
  display: block;
  padding: 10px;
  color: #fafafa !important;
  font-size: 20px;
  font-weight: 600;
  border-radius: 0 0 5px 5px;
  text-align: center;
}

#content a.overlay-btn-2 {
  background: rgba(0,0,0,0.5);
  border: 1px solid #fff;
  font-size: 1.3em;
  padding: 15px;
  border-radius: 6px;
  color: #fff !important;
  text-align: center;
  transition: all .5s ease-in-out;
}
#content a.overlay-btn-2:hover { background: rgba(255,255,255,1); color: #222 !important; }
```

---

## Content Blocks

### Background Image Blocks

```css
.bg-acf {
  background: url(working-lands/acf-watershed.jpg) no-repeat center !important;
  background-size: cover !important;
  padding: 3rem;
}

#fire-block {
  background: url(...) no-repeat right center;
  background-size: cover;
  min-height: 400px;
}
```

### Colored Overlay Blocks

```css
.blue-block {
  /* aquatics version */
  background: rgba(37, 50, 75, 0.90);
  padding: 40px 30px;
  min-height: 400px;
  border-radius: 10px;
  margin: 4em 1em;
}
.blue-block h2 { font-size: 40px; line-height: 1.3em; }
.blue-block h4 { color: var(--yellow); font-size: 22px; }
.blue-block .subhead {
  letter-spacing: 3px;
  font-weight: 600;
  color: #D0F7FF;
  font-size: 14px;
  text-transform: uppercase;
}

.black-overlay-block {
  background: rgba(8,7,7,0.80);
  padding: 40px 30px;
  min-height: 400px;
  border-radius: 10px;
  margin: 4em 1em;
}
.black-overlay-block .subhead {
  color: #f1d215;
  font-size: 14px;
  letter-spacing: 4px;
  font-weight: 600;
}

.black-70-block {
  background: rgba(0,0,0,0.70);
  padding: 2rem;
  margin: 1em;
  display: flex;
  gap: 20px;
  border-radius: 10px;
}
.black-70-block .subhead {
  letter-spacing: 2px;
  font-weight: 600;
  color: var(--yellow);     /* #fbd84d */
  font-size: 14px;
}

.black-50-block {
  background: rgba(0,0,0,0.50);
  padding: 40px;
}

.col-60 {
  background: rgba(0,0,0,0.60);
  padding: 0 2rem 1rem;
}

.orange-block {
  background: #ef9b26;
  margin: 0;
  padding: 50px;
  min-height: 400px;
}
.orange-block .subhead {
  font-family: 'Montserrat', sans-serif;
  letter-spacing: 4px;
  font-weight: 600;
  color: #b5700f;
  font-size: 14px;
}
.orange-block p { color: #fff; font-size: 18px; line-height: 1.7em; }

.grey-block { background: #efefef; margin: 0; padding: 30px; }
.white-block { background: #fff; margin: 0; padding: 30px; }
.tan-block { background: #e7e5da; padding: 2rem; border-radius: 6px; }
.basic-block {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 0 2rem 1rem;
  margin: 2rem 0;
}
.block-w-border {
  margin: 2rem auto;
  padding: 1rem 2rem;
  border: 4px solid #d5d5d5;
}
.overlay-block {
  padding: 30px;
  background: rgba(0,0,0,0.50);
}
```

### Background Utility Classes

```css
.bg-dark    { background: var(--darkgreen); }  /* #278e95 */
.bg-blue    { background: var(--heading); }    /* #278e95 */
.bg-grey    { background: var(--grey); }       /* #f8f5ef */
.bg-gold    { background: var(--gold); }       /* #dcc464 */
.bg-drk-gold{ background: var(--darkgold); }  /* #bca647 */
.bg-lt-gold { background: var(--ltgold); }    /* #ebdc9e */
.bg-orange  { background: var(--orange); }    /* #f88630 */
.bg-brown   { background: var(--brown); }     /* #825640 */
.bg-ltgrey  { background: var(--ltgrey); }   /* #efefef */
```

---

## Layout Utilities

### Flex

```css
.flex          { display: flex; align-items: center; }
.flex-block    { display: flex; align-items: center; }
.flex-end-block{ display: flex; align-items: flex-end; }
.flex-wrap     { flex-wrap: wrap; }
.flex-item     { flex: 1; }
.flex-item-wrap{ flex: 1; }
.align-center  { align-content: center; }
.centered-block{ display: grid; align-items: center; justify-items: center; }

/* Mobile column-reverse layout (used on Aquatics home) */
.flex-block-reverse-mobile {
  display: flex;
  align-items: center;
}
@media (max-width: 767px) {
  .flex-block-reverse-mobile { flex-direction: column-reverse; }
  .flex-block                { flex-direction: column; }
  .black-70-block            { flex-direction: column; }
}
```

### Spacing

```css
.pad80 { padding: 80px 0; }
.pad60 { padding: 60px 0; }
.pad40 { padding: 40px; }
.pad20 { padding: 20px; }
```

### CTA Strip

```css
#cta-block {
  display: grid;
  align-items: center;
  justify-items: center;
  height: 120px;
  background-color: #28526E;
  width: 100vw;
  position: relative;
  margin-left: -50vw;
  left: 50%;
}
```

---

## Timeline Slider (AquaCorridors section)

```css
#timeline {
  display: flex;
  background-color: #345a67;
  margin-bottom: 3rem;
}

.tl-item {
  position: relative;
  width: 24.33%;
  height: 70vh;
  min-height: 600px;
  color: #fff;
  overflow: hidden;
  transition: width 0.5s ease;
  border-right: 1px solid #444;
}
.tl-item:hover { width: 100% !important; }

.tl-item::after {
  background: rgba(38,96,116,0.65);
  transition: opacity 0.5s ease;
}
.tl-item:hover::after { opacity: 0; }

.tl-content h3 { color: #eeca37; }
.tl-content p  { color: #ffffff; }

.tl-bg {
  filter: grayscale(100%);
  transition: filter 0.5s ease;
}
.tl-item:hover .tl-bg { filter: grayscale(0); }

.tl-content .button {
  padding: 5px 15px;
  background: #fff;
  border-radius: 6px;
  font-weight: bold;
}
.tl-content a.button:hover { color: #fd8d58; }
```

---

## Footer

```css
/* Aquatics-specific footer */
#portal-footer-wlfw {
  display: block;
  background: var(--darkgold);   /* #bca647 */
  color: #fff;
  width: 100%;
  padding: 1.5em;
}

#portal-footer-wlfw h3 {
  margin-top: 0;
  color: #fff;
  border-bottom: 1px solid #ebebeb;
  letter-spacing: 2px;
  font-size: 1.5rem;
}

#portal-footer-wlfw .ft-menu li a {
  color: #fff !important;
  font-size: 15px;
  line-height: 1.8em;
}

#portal-footer-wlfw .bottom-nav {
  text-align: left;
  margin: 15px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

#portal-footer-wlfw .eeo-statement {
  font-size: .75rem;
  line-height: 1.4em;
  margin-top: 15px;
}

/* Site actions bar below footer */
#portal-siteactions {
  background: var(--brown);   /* #825640 */
}
```

---

## Responsive Breakpoints

| Breakpoint | Value |
|---|---|
| Mobile nav/biome bar | `max-width: 767px` |
| Tablet/mobile general | `max-width: 768px` |
| Small tablet | `max-width: 600px` |
| Handheld (legacy) | `max-device-width: 480px` |
| Wide content | `max-width: 1530px` (→ 85% content width) |

---

## Link Styles

```css
a:visited { color: #205C90 !important; }    /* base site-wide */
a.gold-text { color: #d8c468 !important; }  /* aquatics utility */

/* Inside nav portlet header */
.portletNavigationTree .portletHeader a {
  color: var(--gold) !important;   /* #dcc464 */
  font-weight: 600;
}

/* Inside dark blocks */
.eeo-statement a { font-weight: 600; color: #fff !important; }
```

---

## Loaded Google Fonts Summary

```
Merriweather:400,400i,700
Montserrat:400,500,600
Open+Sans:400,400i,600
Source+Sans+Pro:400,700
Nunito+Sans:ital,wght@0,400;0,700;1,400
Public+Sans:ital,wght@0,300;0,400;0,700;1,300;1,400
Material+Icons
font-awesome 4.2.0 (Bootstrap CDN)
```
