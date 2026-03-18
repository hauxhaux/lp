# Literature Gateway Sub-site Style Guide

Reference: `https://dev.landscapepartnership.org/networks/working-lands-for-wildlife/the-literature-gateway`

Source CSS: `literature.css` (sub-site specific) + `ploneCustom.css` (shared portal styles)

---

## Page Inventory

| # | Page | URL Path | File |
|---|------|----------|------|
| 1 | Home | `/networks/working-lands-for-wildlife/the-literature-gateway` | `html/01-home.html` |
| 2 | Background | `.../the-literature-gateway/about` | `html/02-background.html` |
| 3 | Gateway Tool | `.../the-literature-gateway/gateway-tool` | `html/03-gateway-tool.html` |
| 4 | Resources | `.../the-literature-gateway/resources` | `html/04-resources.html` |
| 5 | Advanced Search | `.../the-literature-gateway/search_form` | `html/05-advanced-search.html` |
| 6 | Login | `.../the-literature-gateway/login` | (not crawled, standard Plone) |
| 7 | Register | `.../the-literature-gateway/request_login_pre` | (not crawled, standard Plone) |

### Nav tabs (portal-globalnav)

- **Home** - `/networks/working-lands-for-wildlife/the-literature-gateway/`
- **Background** - `.../the-literature-gateway/about`
- **Gateway Tool** - `.../the-literature-gateway/gateway-tool`
- **Resources** - `.../the-literature-gateway/resources`

---

## Color Palette

### CSS Custom Properties (`:root`)

| Variable | Hex | Usage |
|----------|-----|-------|
| `--darkblue` | `#266074` | Header bg, nav bg, footer bg, heading color |
| `--lightblue` | `#3484a3` | Secondary blue |
| `--green` | `#b1c260` | Accent green |
| `--topgreen` | `#88b66a` | Return-to-WLFW bar, edit bar |
| `--heading` | `#266074` | All heading colors (h1-h6) |
| `--yellow` | `#F9D909` | Yellow accent |

### Additional Colors Used

| Hex | Usage |
|-----|-------|
| `#266074` | Dark blue - nav background, globalnav, footer background |
| `#3890ae` | Nav hover background |
| `#bac966` | Nav selected/active background (yellow-green) |
| `#88b66a` | Top green bar ("Return to WLFW"), edit bar |
| `#e86129` | Orange - link hover, feature block headings, readmore hover |
| `#f7931e` / `#f7931f` | Orange - readmore button, styleguide orange swatch |
| `#F59E20` | Solid orange button background |
| `#ef8f39` | Orange button (`.btn-orange`) |
| `#e64c00` | Button hover (darker orange) |
| `#fd7916` | Blue block link hover |
| `#f1d215` | Blue block h4 color (gold) |
| `#f9d90f` | Blue block link color (gold) |
| `#fced20` | WLFW nav bar link hover (bright yellow) |
| `#D0F7FF` | Light cyan - blue block subhead, footer heading color |
| `#d0f7ff` | Footer heading color (same) |
| `#b3dde7` | Sitecredit link color |
| `#a9e1f3` | Personal tools visited link |
| `#276f88` | Content h1 documentFirstHeading color |
| `#222` | Nav selected text |
| `#666` | Paragraph text, portlet header |
| `#676767` | Intro text, dark grey swatch |
| `#777` | Caption text |
| `#9d9d9d` | Material icons black variant |
| `#fff` | White - backgrounds, nav text, button text |
| `#efefef` | Feature block border, submenu hover bg, grey background |
| `#f5f5f5` | Light grey swatch |
| `#ddd` | Portlet border |
| `#ccc` | Fire resources border |
| `#205c90` | Portlet header bg, dark blue swatch |
| `#a26623` | Brown swatch |
| `#444` | Gateway tool return bar bg |
| `rgba(20 83 120 / 80%)` | Blue block overlay (`.blue-block`) |
| `rgba(0, 0, 0, 0.6)` | Slide overlay bg |
| `rgba(0, 0, 0, 0.5)` | Center block overlay, portlet overlay |
| `rgba(255, 255, 255, 0.25)` | Large white button bg |
| `#ff9900` / `#f90` | Footer menu link hover |

---

## Typography

### Font Families

| Font | Source | Usage |
|------|--------|-------|
| **Merriweather** | Google Fonts (`400,400i,700`) | Body text, document descriptions |
| **Montserrat** | Google Fonts (`400,500,600`) | Headings (h1-h6), nav links, buttons, subheads, footer menu, sitecredit |
| **Open Sans** | Google Fonts (`400,400i,600`) | Button font, readmore links |
| **Source Sans Pro** | Google Fonts (`400,700`) | Loaded but not explicitly used in literature.css |
| **Nunito Sans** | Google Fonts (`400,700,400i`) | Loaded but not explicitly used in literature.css |
| **Public Sans** | Google Fonts (`300,400,700,300i,400i`) | Loaded but not explicitly used in literature.css |
| **Material Icons** | Google Fonts | Icon font for feature blocks |
| **Font Awesome 4.2.0** | MaxCDN | Additional icons |

### Google Fonts Load Tags

```html
<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,400i,600|Source+Sans+Pro:400,700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Merriweather:400,400i,700|Montserrat:400,500,600&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Public+Sans:ital,wght@0,300;0,400;0,700;1,300;1,400&display=swap" rel="stylesheet">
```

### Font Sizes

| Element | Size | Weight | Family | Other |
|---------|------|--------|--------|-------|
| Body | (inherited) | -- | Merriweather, serif | `-webkit-font-smoothing: antialiased` |
| h1 (`#content h1`) | 32px | 600 | Montserrat | color: `--heading` |
| h1 `.documentFirstHeading` | 34px | 600 | Montserrat | color: `#276f88`, text-transform: capitalize |
| h2 | 26px | 600 | Montserrat | |
| h3 | 24px | 600 | Montserrat | |
| h4 | 20px | 600 | Montserrat | |
| All headings (h1-h6) | -- | 600 | Montserrat, Verdana, sans-serif | line-height: 1.3em, letter-spacing: -0.0115em |
| p | 16px | -- | (inherited Merriweather) | color: `#666`, line-height: 1.6em, letter-spacing: 0.01em |
| `.intro` | 18px | -- | -- | line-height: 1.7em, color: `#676767` |
| `.heading-white` | 2.7em (mobile: 2.4em) | 600 | Montserrat | text-transform: uppercase, letter-spacing: -0.025em |
| `.subhead` | 14px | -- | -- | text-transform: uppercase, letter-spacing: 2px, color: `#7f7f87` |
| `.blue-block .subhead` | 14px | 600 | Montserrat | letter-spacing: 4px, color: `#D0F7FF`, uppercase |
| `.small-heading` | 14px | -- | -- | uppercase, letter-spacing: 1px |
| `.caption` | 13px | -- | -- | color: `#777` |
| Nav links | 16px | 500 | Montserrat | text-transform: uppercase |
| Nav submenu links | 15px | -- | -- | text-transform: none |
| WLFW nav bar | 13px | 600 | Montserrat | uppercase, letter-spacing: 1px |
| Footer menu items | 15px | 500 | Montserrat | |
| Portlet header | 17px | -- | Montserrat | color: `#666` |
| Breadcrumbs | 85% | -- | -- | |

---

## Layout & Structure

### Page Width

| Element | Width | Notes |
|---------|-------|-------|
| `#visual-portal-wrapper` | max-width: 100% | Full-width wrapper |
| `#portal-columns` | 1170px | Content area, centered (`margin: 0 auto`) |
| `#portal-columns` (mobile) | 96% | At `max-width: 768px` |
| `.narrow` | 1170px | Centered container (`margin: 0 auto`) |
| `.narrow` (mobile) | max-width: 100%, padding: 0 1rem | |
| `.section-gateway-tool #portal-columns` | 100% | Full-width for tool page |

### Header / Banner

| Element | Value | Notes |
|---------|-------|-------|
| `#portal-top` height | 215px | Background image: `literature-images/bird-banner.jpg` |
| `#portal-top` (mobile) | 130px | background-size: 100% |
| `#portal-top` bg-size | 52% | `background-repeat: repeat-x` |
| `#portal-header` height | 130px | Transparent background, positioned relative |
| Logo width | 780px | `left: 10%`, `top: 75px`, z-index: 2 |
| Logo (mobile) | width: 95% | `left: 5px`, `top: 10px` |
| Min viewport height | `calc(100vh - 220px)` | On `#visual-portal-wrapper` |

### Banner Images (section-specific)

| Section | Image | Notes |
|---------|-------|-------|
| Home (`.section-the-literature-gateway-1`) | `literature-images/forest-1.jpg` | cover, left top |
| Background (`.section-about`) | `literature-images/about-banner.jpg` | center, hidden (`display: none`) |
| Contact (`.section-contact`) | `literature-images/contact-banner.jpg` | |
| Home landing | height: 35px, bg: white | |

### Content Blocks

| Block | Height | Background |
|-------|--------|------------|
| `.gateway-block` | min-height: 400px | `literature-images/smoky-mtn-fall.jpg`, cover, center |
| `.mapviewer-block` | min-height: 200px | `literature-images/Indigo-bunting.jpg`, cover |
| `.block-400` | min-height: 400px | |
| `.block-200` | min-height: 200px | |

---

## Navigation

### Top Return Bar (`.wlfw-nav-bar`)

- Background: `#88b66a` (top green)
- Padding: `10px 30px`
- Font: Montserrat, 600 weight, 13px
- Links: white, uppercase, letter-spacing: 1px
- Link hover: `#fced20` (bright yellow)

### Main Navigation (`#globalnav-wrapper`)

- Background: `#266074` (dark blue)
- Border-bottom: `2px solid #266074`
- Position: `top: 175px`
- Links aligned right: `display: flex; justify-content: flex-end; margin-right: 4em`

### Nav Links (`#portal-globalnav li a`)

- Background: `#276074`
- Font: Montserrat, 500 weight, 16px
- Text-transform: uppercase
- Padding: `10px 30px`
- Color: white (inherited)

### Nav States

| State | Background | Text Color |
|-------|------------|------------|
| Default | `#276074` | white |
| Hover | `#3890ae` | white |
| Selected | `#bac966` | `#222` (dark) |
| Selected + hover | `#3890ae` | white |

### Submenu Links

- Text-transform: none
- Font-size: 15px
- Hover: background `#efefef`, color `#E86128` (orange)

### Home Tab

- Home tab submenu is hidden (`display: none`)
- Home icon uses no background image (text visible)

### Mobile Navigation (`max-width: 767px`)

- `#portal-globalnav` hidden by default, shown when `.opened`
- Nav items: `width: 100%`
- Mobile toggle font: Montserrat, 600, 13px
- `#globalnav-wrapper` top: `-40px`

### Gateway Tool Page Navigation

- Nav, breadcrumbs, header, edit bar all hidden
- `#portal-top` height: 0, no background
- Shows `.gateway-nav-bar` instead: bg `#444`, padding `10px 30px`
- Links: white, uppercase, Montserrat 600, 13px, letter-spacing: 1px
- Hover: `#e86129` (orange)

### Personal Tools

- Position: `right: 30px; top: -40px`
- Link color: white
- Visited: `#a9e1f3`

### Search Box (`.LSBox`)

- Position: relative, `top: 70px`
- Background: white
- Padding: 11px
- Border-radius: 6px
- Box-shadow: `0px 1px 5px 0 rgb(75 75 75 / 25%)`
- Mobile: `top: 113px`, absolute, transparent bg, no shadow, `left: 57px`, width: 150px

---

## Buttons

### `.button` (generic)

- Color: `#54585b`
- Font: Open Sans, 700 weight, 1.125rem
- Padding: `.75rem 1rem`
- Border: `1px solid #888`, border-radius: 0.25rem
- Box-shadow: `2px 3px 5px -1px rgba(0, 0, 0, 0.35)`
- Transition: background/color/border 0.2s linear
- Hover: bg `#e64c00`, color white, border transparent

### `.btn-solid-orange`

- Background: `#F59E20`
- Color: white
- Border: transparent
- Hover: bg `#e64c00`

### `.btn-orange`

- Background: `#ef8f39`
- Color: white
- Font: Montserrat, 600, 13px
- Text-transform: uppercase
- Letter-spacing: 1px

### `.btn.large-white` (inside `#content`)

- Border: `1px solid #fff`
- Background: `rgba(255, 255, 255, 0.25)`
- Color: white
- Padding: 15px
- Text-transform: uppercase
- Font: Montserrat, 600, 14px
- Letter-spacing: 0.075em
- Border-radius: 4px
- Transition: all 0.3s ease-in-out
- Hover (in `.blue-block`): bg `rgb(8 48 70)`

### `a.readmore`

- Font-size: 13px
- Font-weight: 600
- Text-transform: uppercase
- Font: Open Sans
- Hover color: `#f7931e`

---

## Content Blocks

### `.blue-block`

- Background: `rgba(20 83 120 / 80%)` (dark blue semi-transparent overlay)
- Padding: `40px 30px`
- `.subhead`: Montserrat, 600, 14px, letter-spacing: 4px, color `#D0F7FF`, uppercase
- `h4`: color `#f1d215` (gold), 22px
- `p`: color white, 16px, line-height: 1.7em
- Links: color `#f9d90f` (gold), hover `#fd7916` (orange)

### `.feature-block`

- Border: `6px solid #efefef`
- Padding: 30px (mobile: 15px, center text)
- Background: white
- `h3`: margin-top: 10px, 28px, color `#e86129` (orange)

### `.gateway-block`

- Background image: `literature-images/smoky-mtn-fall.jpg`, cover, center
- Min-height: 400px
- Position: relative, top: -35px

### `.slide-overlay`

- Position: absolute, z-index: 5, top: 55%
- Background: `rgba(0, 0, 0, 0.6)`
- Padding: `30px 30px 40px`
- Width: 70%, left: 15%
- Color: white
- Border-radius: 6px, text-align: center
- Mobile: top: 35%, width: 100%, left: 0, border-radius: 0, bg: 0.45 opacity

### `.gateway-tool-overlay`

- Background image: `literature-images/chestnut-sided-warbler.jpg`
- Padding: `90px 15px 20px`
- Border-radius: 10px
- Background-position: left center, cover

### `.center-block-overlay`

- Background: `rgba(0, 0, 0, 0.5)`
- Border: `1px solid #fff`
- Padding: 20px
- Border-radius: 12px

### Material Icons

- `.material-icons`: size 60px, color white
- `.material-icons-black`: size 68px, color `#9d9d9d`

---

## Grid Layouts (from ploneCustom.css, used by Literature Gateway)

| Class | Columns | Gap |
|-------|---------|-----|
| `.grid-container-2col` | `50% 1fr` | 30px |
| `.grid-container-2col-no-gap` | `50% 1fr` | 0 |
| `.grid-container-3col` | `repeat(3, minmax(0, 1fr))` | 30px |
| `.grid-container-3col-gap10` | `repeat(3, 1fr)` | 10px |
| `.grid-container-three-quarter` | `68% 1fr` (literature.css) / `75% 1fr` (ploneCustom) | 30px |

All grid layouts collapse to single column at `max-width: 768px`.

### Utility Classes

| Class | Value |
|-------|-------|
| `.shiftup` | `position: relative; top: -40px` |
| `.floatright` | `float: right` |
| `.space10` | `height: 10px; display: block` (from ploneCustom) |
| `.space20` | `height: 20px; display: block` (from ploneCustom) |
| `.space40` | `height: 40px; display: block` |
| `.bg-grey` | `background: #efefef` |
| `.gap10` | `gap: 10px; padding-right: 10px` |
| `.gap15` | `gap: 15px` |
| `.gap20` | `gap: 20px` |
| `.gap30` | `gap: 30px` |

---

## Footer

### Main Footer (`#portal-footer-wrapper`)

- Background: `#266074` (dark blue)

### Literature Gateway Footer (`#portal-footer-lit-gateway`)

- `display: block` (overrides `display: none` in ploneCustom.css)
- Padding: 2em
- Margin: 2em auto
- Width: 80% (mobile: 100%, padding: 1.5em, margin: 1em auto)

### Footer Layout (`.footer-container`)

- `display: flex; flex-direction: row; justify-content: space-between; align-items: flex-start`
- Mobile: `flex-direction: column-reverse; align-items: center`
- `.block-1`: margin-top: 1.5em (logos)
- `.block-2`: width: 15% (Browse menu)
- `.block-50`: width: 53% (Contributors section); mobile: 90%

### Footer Headings

- Color: `#d0f7ff` (light cyan)
- Margin-top: 15px

### Footer Menu (`.ft-menu`)

- `display: flex; flex-direction: column; justify-content: space-evenly`
- Items: Montserrat, 500 weight, 15px, padding: 2px 0
- Link color: white
- Link hover: `#ff9900` (orange)

### Sitecredit

- Font: Montserrat, 12px, uppercase
- Letter-spacing: 0.05em
- Link color: `#b3dde7`
- Link hover: `#f90`
- Background icon: `fergusonlynch-icon.png`

### Hidden Footer Elements

- `.lp-footer`: hidden (main LP footer)
- `.footer-left`: hidden
- `.footer-rt`: hidden
- `#jumpmenu`: hidden
- Other sub-site footers (bobscapes, birdlocale, fire, sefiremap, wlfw) are present in HTML but hidden via their respective CSS

---

## Portlets

### Navigation Portlet

- Header: bg `#205C90`, border-radius: `4px 4px 0 0`, uppercase, padding: 15px

### Generic Portlet (`dl.portlet`)

- Font-size: 90%
- Border: `1px solid #ddd`, border-radius: 6px
- Margin-bottom: 1.5em
- Header: transparent bg, Montserrat 17px, color `#666`

---

## Responsive Breakpoints

| Breakpoint | Elements Affected |
|------------|-------------------|
| `max-width: 768px` | `#portal-columns` (96%), `.narrow` (100%), `#portal-top` (130px), `#portal-logo img` (95%), `.LSBox` (absolute, 113px), `.footer-container` (column-reverse), `.block-50` (90%), `#portal-footer-lit-gateway` (100%), `.grid-container-2col` (single col), `.grid-container-3col` (single col), `.grid-container-three-quarter` (single col), `.heading-white` (2.4em), `.sitecredit` (margin adjust), `.bottom-nav` (single col grid), `.flex-container` (column), `.flex-container.space-between` (4-col grid) |
| `max-width: 767px` | `#portal-globalnav` (hidden, toggled by `.opened`), `.bird-overlay` (hidden), `.feature-block` (padding: 15px, center text) |

---

## Hidden Elements (by section)

### Always Hidden
- `.lp-footer` - main LP footer
- `#jumpmenu`, `.rss`, `.rss-feeds`, `.footer-mid`, `.footer-rt`
- `.nest-navigation-bar`
- `.template-document_view .documentByLine` and `.documentFirstHeading`

### Section-specific
- `.section-the-literature-gateway #portal-banner` - hidden
- `.section-gateway-tool` - hides nav, breadcrumbs, header, edit bar, portal-top (height: 0)
- `.section-about #portal-breadcrumbs` - hidden
- `.content-the-literature-gateway-1 #portal-breadcrumbs` - hidden
- Home tab submenu (`li#portaltab-home ul.submenu`) - hidden

---

## Key Background Images

| Image Path | Used In |
|------------|---------|
| `literature-images/bird-banner.jpg` | `#portal-top` header background |
| `literature-images/forest-1.jpg` | Home page `#portal-banner` |
| `literature-images/smoky-mtn-fall.jpg` | `.gateway-block` hero |
| `literature-images/Indigo-bunting.jpg` | `.mapviewer-block` |
| `literature-images/about-banner.jpg` | Background page banner |
| `literature-images/contact-banner.jpg` | Contact page banner |
| `literature-images/chestnut-sided-warbler.jpg` | `.gateway-tool-overlay` |
| `literature-images/literature-logo-wlfw.svg` | Site logo |
| `literature-images/LG-logo-white.svg` | Footer logo |
| `literature-images/canada-warbler-masked.png` | Used in ploneCustom.css |

---

## CSS File Inventory

| File | Size | Purpose |
|------|------|---------|
| `literature.css` | 25KB | Sub-site-specific styles (primary) |
| `ploneCustom.css` | 130KB | Shared portal customizations (grids, blocks, shared classes) |
| `base.css` | 70KB | Plone base styles |
| `reset.css` | 483B | CSS reset |
| `dropdown-menu.css` | 2KB | Dropdown menu styles |
| `mobile.css` | 1KB | Mobile-specific styles |
| `print.css` | 2.5KB | Print styles |
| `jquery.css` | 9KB | jQuery UI styles |
| `dateinput.css` | 2.4KB | Date input widget |
| `fullcalendar.css` | 22KB | Calendar widget |
| `truegallery.css` | 22KB | Gallery portlet |
| `ploneboard.css` | 4KB | Discussion board |
| `contentleadimage.css` | 308B | Lead image |
| `tinymce.css` | 858B | TinyMCE editor |
| `font-awesome.min.css` | (CDN) | Font Awesome 4.2.0 icons |

---

## Body Classes (for CSS targeting)

- `template-document_view` - standard document view
- `portaltype-document` - Plone Document content type
- `site-the-literature-gateway` - identifies the sub-site
- `section-the-literature-gateway-1` - home page section
- `section-about` - background page
- `section-gateway-tool` - gateway tool page
- `section-resources` - resources page
- `content-the-literature-gateway-1` - content identifier
- `userrole-anonymous` - anonymous user
