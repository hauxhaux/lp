# Bobscapes Sub-site Style Guide

> Reference captured from `https://bobscapes.org/` (redirects from `https://dev.landscapepartnership.org/networks/working-lands-for-wildlife/landscapes-wildlife/quail/bobscapes`)
> Captured: 2026-03-18

---

## Page Inventory

| # | Page | URL | File |
|---|------|-----|------|
| 1 | Home | `https://bobscapes.org/` | `html/01-home.html` |
| 2 | Background | `https://bobscapes.org/background` | `html/02-background.html` |
| 3 | Access the Mobile App | `https://bobscapes.org/access-mobile-app` | `html/03-access-mobile-app.html` |
| 4 | Data Request | `https://bobscapes.org/data-request` | `html/04-data-request.html` |
| 5 | News | `https://bobscapes.org/news` | `html/05-news.html` |

---

## CSS Files

| File | Description | Media |
|------|-------------|-------|
| `bobscapes.css` | **Sub-site specific styles** (copied from quail.css) | screen |
| `ploneCustom.css` | Shared LP platform styles (buttons, grids, blocks) | all |
| `base.css` | Plone base styles | screen |
| `reset.css` | CSS reset | screen |
| `dropdown-menu.css` | Nav dropdown positioning | screen |
| `mobile.css` | Mobile overrides | handheld, max-device-width: 480px |
| `print.css` | Print styles | print |
| `jquery.css` | jQuery UI styles | all |
| `tinymce.css` | TinyMCE editor styles | screen |
| `dateinput.css` | jQuery tools dateinput | screen |
| `fullcalendar.css` | FullCalendar plugin | screen |
| `truegallery.css` | Plone TrueGallery portlet | screen |
| `contentleadimage.css` | Content lead image | screen |
| `ploneboard.css` | Ploneboard forum | all |
| Font Awesome 4.2.0 | Icon font (CDN) | — |

---

## Color Palette

### Primary Colors (Bobscapes-specific)

| Color | Hex | Usage |
|-------|-----|-------|
| Gold/Yellow | `#ffda3e` | Header background (`#portal-header`) |
| Dark Brown | `#5d442a` | Nav bar background (`.bobscapes-nav-bar`) |
| Medium Brown | `#7d6042` | Footer background (`#bobscapes-footer`) |
| Dark Brown (footer border) | `#54402d` | Footer divider borders, footer `h3` underline |
| Near Black | `#2c2c2c` | Body text, headings, nav link text |
| Rust/Red-Brown | `#a84e47` | Nav hover text, home tab hover |
| Orange (selected) | `#dd7031` | Selected nav tab background |
| Gold (footer heading) | `#d4a447` | Footer `h3` color |
| Cream (footer text) | `#ede6d7` | Footer link color, EEO statement |
| Amber (footer hover) | `#f4a221` | Footer link hover |
| Gold (ft-menu hover) | `#f1c058` | `.ft-menu a:hover` |
| Gold (nav hover) | `#ffe061` | `.bobscapes-nav-bar a:hover` |
| Animated underline | `#ED9700` | `.underline-animation::after` |
| Page background | `#E9E6D4` | `body` background (warm cream/tan) |
| Dark bar | `#34281c` | Site actions bar background (`#portal-siteactions`) |

### Content Block Colors

| Color | Hex | Usage |
|-------|-----|-------|
| Framework block | `#fbecbf` | `.framework-block` background (light yellow) |
| Green box | `#8fa85d` | `.green-box` background |
| Blue section | `#2fb9d2` | `.blue-section` background |
| Dark border | `#4b4744` | `.quail-block` top border |
| White | `#ffffff` | `.bg-white`, search box, image borders |

### Shared Platform Button Colors (from ploneCustom.css)

| Color | Hex | Usage |
|-------|-----|-------|
| Orange button | `#f8903e` | `.btn-orange`, `.btn-orange-large` |
| Orange hover | `#F7700D` | `.btn-orange:hover` |
| Red button | `#FF6633` | `.btn-red` |
| Blue button | `#0e71eb` | `.btn-blue` |
| Blue hover | `#1a5cbb` | `.btn-blue:hover` |
| Tan button | `#d4d5c6` | `.btn-tan` |
| Tan hover | `#C1C1B5` | `.btn-tan:hover` |
| Dark button | `#274352` | `.button-dark` |
| Dark hover | `#132631` | `.button-dark:hover` |

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

Also loaded via CDN:
- Font Awesome 4.2.0: `//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css`

### Font Usage

| Element | Font Family | Weight | Size | Other |
|---------|-------------|--------|------|-------|
| Nav bar links (`.bobscapes-nav-bar`) | `'montserrat'` | 600 | 13px | uppercase, letter-spacing: 2px |
| Main nav links (`#portal-globalnav li a`) | `'montserrat'` | 600 | 130% (~17px) | — |
| Mobile menu toggle | `'Montserrat'` | — | 85% | — |
| Page heading (`#content h1`) | (inherited) | 500 | 2.3em | color: #2c2c2c |
| Footer menu (`.ft-menu li`) | (inherited) | — | 14px | uppercase, text-align: center |
| Site credit | (inherited) | — | 13px | letter-spacing: 0.05em, uppercase |
| EEO statement | (inherited) | — | 13px | line-height: 1.3em |
| Blue section h3 | (inherited) | — | 1.8rem | margin: 0 |
| Footer h3 | (inherited) | — | — | letter-spacing: 2px, color: #d4a447 |

---

## Layout & Structure

### Page Wrapper

| Property | Value |
|----------|-------|
| `#visual-portal-wrapper` background | `#fff` |
| `#visual-portal-wrapper` max-width | `100%` |
| `#visual-portal-wrapper` min-height | `calc(100vh - 190px)` |
| `#visual-portal-wrapper` border-radius | `0` |

### Header (`#portal-header`)

| Property | Value |
|----------|-------|
| Background color | `#ffda3e` (bright gold/yellow) |
| Height | `170px` desktop, `145px` mobile (768px) |
| Width | `100%` |
| Background-size | `cover` |
| Border | transparent / none |

### Logo (`#portal-logo`)

| Property | Desktop | Mobile (<=768px) |
|----------|---------|-------------------|
| Position | `relative` | `relative` |
| Top | `1em` | `-1em` |
| Left | `3em` | `0.5em` |
| Image width | `400px` | `330px` |
| Container width | — | `335px` |

### Content Area (`#content`)

| Property | Desktop | Mobile (<=1024px) |
|----------|---------|---------------------|
| Width | `1170px` | `100%` |
| Margin | `0 auto 2em` | `0 auto -5em` |
| Padding | — | `0 1em` |
| Background | Quail image (right bottom, no-repeat) | Same, `background-size: 150px` |
| Min-height | `60vh` | `60vh` |

Home page (`#content` on `.template-bobscapes_home`): no background, `margin: 0`, `width: 100%`.

### Search Box (`.LSBox`)

| Property | Desktop | Mobile (<=768px) |
|----------|---------|-------------------|
| Position | `relative` | `absolute` / `display: none` |
| Top | `-60px` | `30px` |
| Right | `3.5em` | `100px` |
| Background | `#ffffff` | transparent |
| Padding | `10px 13px` | `11px` |
| Border-radius | `6px` | `6px` |
| Border | `1px solid #fff` | none |
| Width | — | `150px` |

---

## Navigation

### Top Nav Bar (`.bobscapes-nav-bar`) — Brown bar above content

| Property | Value |
|----------|-------|
| Background | `#5d442a` (dark brown) |
| Padding | `10px 40px` (desktop), `10px` (mobile) |
| Padding-left | `70px` (desktop), `15px` (mobile) |
| Font | `'montserrat'`, 600 weight, 13px |
| Display | `block` |

### Nav Bar Links (`.bobscapes-nav-bar a`)

| State | Color | Other |
|-------|-------|-------|
| Default | `#fff` | uppercase, 13px, letter-spacing: 2px |
| Hover | `#ffe061` (gold) | — |

### Main Navigation (`#globalnav-wrapper`)

| Property | Desktop | Mobile (<=768px) |
|----------|---------|-------------------|
| Position | `absolute` | — |
| Top | `121px` | `-15px` |
| Right | `3em` | — |
| Left | — | `0px` |
| Background | `transparent` | — |
| Border | none | — |

### Main Nav Links (`#portal-globalnav li a`)

| State | Background | Color | Other |
|-------|------------|-------|-------|
| Default | `transparent` | `#2c2c2c` | font: montserrat 600, 130%, padding: 0.75em 1.5em |
| Visited | — | `#2c2c2c` | — |
| Hover | none | `#a84e47` (rust) | — |
| Selected | `#dd7031` (orange) | `#fff` | — |
| Selected hover | — | `#a84e47` | — |

### Mobile Nav (`#portal-globalnav li` at <=768px)

| Property | Value |
|----------|-------|
| Width | `100%` |
| Background | `#efefef` |
| Font-size | `16px` |

### Menu Toggle (Mobile, `.menu-toggle` at <=768px)

| Property | Value |
|----------|-------|
| Font | `'Montserrat'` |
| Color | white |
| Text-align | left |
| Padding | `10px 15px 10px 50px` |
| Font-size | `85%` |
| Background | `url(menu-toggle.png) 20px center no-repeat black` |

### Dropdown Menu (`#portal-globalnav ul.submenu`)

| Property | Value |
|----------|-------|
| Position | absolute |
| Width | `15em` |
| Background | `#fff` |
| Border | `1px solid White` (sides + bottom) |
| Submenu link hover bg | `#fff` |

### Home Tab (`#portaltab-home > a`)

| State | Color |
|-------|-------|
| Hover | `#a84e47` (rust) |
| Submenu | hidden (`display: none`) |

---

## Buttons (Shared from ploneCustom.css)

### `.btn-orange`

| Property | Value |
|----------|-------|
| Background | `#f8903e` |
| Padding | `10px 15px` |
| Border | `1px solid #fff` |
| Border-radius | `5px` |
| Font-size | `13px` |
| Font-weight | `600` |
| Text color | `#fff` |
| Letter-spacing | `0.025em` |
| Hover background | `#F7700D` |

### `.btn-orange-large`

Same as `.btn-orange` but `font-size: 18px`, `display: inline-block`.

### `.btn-red`

| Property | Value |
|----------|-------|
| Background | `#FF6633` |
| Font-size | `18px` |
| Border-radius | `5px` |

### `.btn-blue`

| Property | Value |
|----------|-------|
| Background | `#0e71eb` |
| Padding | `8px 15px` |
| Border-radius | `8px` |
| Hover background | `#1a5cbb` |

### `.btn-tan`

| Property | Value |
|----------|-------|
| Background | `#d4d5c6` |
| Border-radius | `6px` |
| Margin | `1em` |
| Padding | `10px` |
| Text color | `#797979` |
| Hover background | `#C1C1B5` |

### `.cta-button` (from ploneCustom.css)

Defined in shared styles — used across sub-sites.

---

## Content Blocks

### `.framework-block`

| Property | Value |
|----------|-------|
| Background | `#fbecbf` (light yellow/cream) |
| Padding | `20px 30px` |

### `.green-box`

| Property | Value |
|----------|-------|
| Background | `#8fa85d` |
| Text-align | center |
| Padding | `30px` |
| Color | `#fff` |
| Margin | `1em 0` |
| Border-radius | `10px` |

### `.blue-section`

| Property | Value |
|----------|-------|
| Background | `#2fb9d2` |
| Text-align | center |
| Padding | `20px` |
| Color | `#fff` |
| Border-radius | `8px` |
| h3 font-size | `1.8rem` |

### `.quail-block` (hero image block)

| Property | Value |
|----------|-------|
| Background | `url(bobscapes-images/quail-forever-landscape-w-quail.jpg)` no-repeat center top |
| Background-size | cover |
| Min-height | `540px` (desktop), `10px` / hidden (<=768px) |
| Border-top | `6px solid #4b4744` |

### `.cellphone-block` (hero image block)

| Property | Value |
|----------|-------|
| Background | `url(bobscapes-images/hand-w-phone.jpg)` no-repeat center center |
| Background-size | cover |
| Min-height | `540px` (desktop), `480px` (<=768px) |
| Padding | `40px` (desktop), `20px 20px 30px` (<=768px) |
| Display | flex, column, justify-content: flex-end |
| h2 color | `#fff` |
| h2 mobile font-size | `2em`, line-height `1.5em` |

### `.fullwidth-section`

| Property | Value |
|----------|-------|
| Padding | `0` |

---

## Flex Layouts (Bobscapes-specific)

### `.flex-container-center`

| Property | Desktop | Mobile (<=768px) |
|----------|---------|-------------------|
| Display | flex | flex |
| Justify-content | center | center |
| Align-items | center | center |
| Gap | `30px` | `20px` |
| Flex-direction | row | column |

### `.flex-container`

| Property | Desktop | Mobile (<=768px) |
|----------|---------|-------------------|
| Display | flex | flex |
| Align-items | flex-start | center |
| Gap | `20px` | `20px` |
| Flex-direction | row | column |

---

## Grid Layouts (from ploneCustom.css — shared)

| Class | Columns | Gap |
|-------|---------|-----|
| `.grid-container-2col` | `50% 1fr` | `30px` |
| `.grid-container-2col-no-gap` | `50% 1fr` | `0` |
| `.grid-container-3col` | `repeat(3, minmax(0, 1fr))` | `30px` |
| `.grid-container-4col` | `repeat(4, minmax(0, 1fr))` | `0` |
| `.grid-container-4col-w-gap` | `repeat(4, 1fr)` | `30px` |
| `.grid-container-4colstack` | `25% 25% 25% 25%` | `0` |
| `.grid-container-50-25-25` | `50% auto auto` | `30px` |
| `.grid-container-25-50-25` | `auto 50% auto` | `30px` |
| `.grid-container-15-70-15` | `auto 67% auto` | `20px` |
| `.grid-container-20-80` | `20% auto` | `0` |
| `.grid-container-30-70` | `30% auto` | `0` |
| `.grid-container-70-30` | `70% auto` | `0` |
| `.grid-container-40-60` | `40% auto` | `0` |

**Gap utilities:** `.gap10` (10px), `.gap15` (15px), `.gap20` (20px), `.gap30` (30px)

All multi-column grids collapse to single column at `768px`.

---

## Footer (`#bobscapes-footer`)

| Property | Value |
|----------|-------|
| Background | `#7d6042` (medium brown) |
| Color | `#fff` |
| Padding | `1.5em 0` |
| Width | `100%` |

### Footer Links

| State | Color |
|-------|-------|
| Default | `#ede6d7` (cream) |
| Hover | `#f4a221` (amber) |

### Footer Menu (`.ft-menu`)

| Property | Value |
|----------|-------|
| Font-size | `14px` |
| Text-transform | uppercase |
| Text-align | center |
| Padding per item | `3px 0` |
| Link color | `#ede6d7` |
| Link hover | `#f1c058` (gold) |

### Footer Headings (`#bobscapes-footer h3`)

| Property | Value |
|----------|-------|
| Color | `#d4a447` (gold) |
| Letter-spacing | `2px` |
| Margin | `15px 0` |
| `.underline` variant | `border-bottom: 1px solid #54402d` |

### Footer Divider (`.border-left`)

| Property | Desktop | Mobile |
|----------|---------|--------|
| Border-left | `1px solid #54402d` | none |
| Padding-left | `20px` | `0` |

### Site Actions Bar (`#portal-siteactions`)

| Property | Value |
|----------|-------|
| Background | `#34281c` (very dark brown) |

### Site Credit (`.sitecredit`)

| Property | Value |
|----------|-------|
| Background image | `fergusonlynch-icon.png` (36px) |
| Font-size | `13px` |
| Letter-spacing | `0.05em` |
| Text-transform | uppercase |
| Line-height | `1.2rem` |
| Width | `185px` |
| Padding-left | `50px` |

### EEO Statement (`.eeo-statement`)

| Property | Value |
|----------|-------|
| Font-size | `13px` |
| Line-height | `1.3em` |
| Color | `#ede6d7` |

### Bottom Navigation (`.bottom-nav`)

| Property | Desktop | Mobile (<=1023px) |
|----------|---------|---------------------|
| Display | flex | flex |
| Justify-content | space-between | space-evenly |
| Align-items | flex-start | center |
| Flex-direction | row | column |
| Text-align | left | center |

---

## Animated Underline Effect (`.underline-animation`)

| Property | Value |
|----------|-------|
| Display | inline-block |
| Position | relative |
| `::after` height | `3px` |
| `::after` bottom | `-5px` |
| `::after` color | `#ED9700` (amber/orange) |
| `::after` transform | `scaleX(0)` -> `scaleX(1)` on hover |
| Transition | `transform 0.35s ease-out` |
| Transform-origin | `bottom center` |

---

## Responsive Breakpoints

| Breakpoint | Target |
|------------|--------|
| `max-width: 1024px` | Tablet: `#content` goes full width, smaller bg |
| `max-width: 1023px` | `.bottom-nav` column layout |
| `max-width: 768px` | Mobile: most grids collapse, nav full-width, header shorter, logo smaller, flex-containers go column, `.border-left` removed, `.quail-block` hidden |
| `max-width: 600px` | (empty rule in bobscapes.css) |
| `max-device-width: 480px` and `min-device-width: 320px` | Small mobile header |
| `max-device-width: 480px` (mobile.css) | Plone mobile: columns stack, logo hidden, large touch targets |

---

## Hidden Elements

The following elements are explicitly hidden (`display: none`):

- `#portal-banner`
- `.loginbutton a`, `.registerbutton a`
- `#jumpmenu`, `.rss`, `.rss-feeds`, `.footer-mid`, `.footer-rt`
- `.nest-navigation-bar`
- `.wlfw-navigation-bar img`
- `#portal-footer` (replaced by `#bobscapes-footer`)
- `.LSBox .searchSection`
- `li#portaltab-home ul.submenu`
- On home page: `#edit-bar`, `#portal-breadcrumbs`, `.addthis_toolbox`

---

## Key Design Notes

1. **This is a Plone 4 sub-site** using the old-style `portal_css` registry (not Diazo/Barceloneta). The sub-site CSS (`bobscapes.css`) is noted as "copied from quail.css".

2. **Color scheme is warm/earthy**: gold header, brown nav bar, brown footer, cream page background. This contrasts with the teal/green palette of the Aquatics sub-site.

3. **Montserrat is the brand font** used for navigation. Body text appears to inherit from the platform defaults (likely Open Sans or the browser default).

4. **Content width is fixed at 1170px** on desktop with a decorative quail background image in the lower right corner (hidden on certain pages).

5. **The homepage uses a full-width layout** with a 2-column grid: a quail image block and a cellphone/app block, each with `min-height: 540px`.

6. **Font Awesome 4.2.0** is loaded for icons (older version, using `fa-` prefix classes).

7. **No Google Fonts specific to Bobscapes** — it inherits the platform-wide Google Fonts stack (Open Sans, Source Sans Pro, Merriweather, Montserrat, Nunito Sans, Public Sans, Material Icons).
