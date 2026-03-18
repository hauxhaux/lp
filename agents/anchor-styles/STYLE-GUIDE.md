# ANCHOR Sub-site Style Guide

Reference: `https://dev.landscapepartnership.org/key-issues/anchor`

---

## Page Inventory

| # | Page | URL Path | Notes |
|---|------|----------|-------|
| 1 | Home (ANCHOR) | `/key-issues/anchor` | Main landing page; hidden title/byline |
| 2 | ANCHOR Resources | `/key-issues/anchor/anchor-resources` | Folder listing with sub-items |
| 3 | ANCHOR MAP | `/key-issues/anchor/anchor-map` | Shorter banner (230px), interactive map |
| 4 | ANCHOR Registration Form | `/key-issues/anchor/anchor-registration-form` | Shorter banner (230px) |
| 5 | ANCHOR Fact Sheet | `/key-issues/anchor/anchor-resources/anchor-fact-sheet` | Document/download page |
| 6 | Appendix: Partner Resources | `/key-issues/anchor/anchor-resources/appendix-partner-resources` | Listing page |

Body class: `site-anchor` (used for CSS scoping)

---

## Google Fonts

Loaded in the HTML `<head>`:

```
Open Sans: 400, 400i, 600
Source Sans Pro: 400, 700
Merriweather: 400, 400i, 700
Montserrat: 400, 500, 600
Nunito Sans: 400, 700, 400i
Public Sans: 300, 400, 700, 300i, 400i
Material Icons (icon font)
```

Also loads: Font Awesome 4.2.0 via MaxCDN.

---

## Color Palette

### Primary / Brand Colors
| Name | Hex | Usage |
|------|-----|-------|
| Navy Blue | `#27426A` | Header nav bg, footer bg, headings (h1-h6), `.anchor-text` |
| Dark Blue | `#205C90` | Portlet headers, breadcrumb links |
| Slate Blue-Gray | `#657F9E` | Base site nav bg (overridden by `#27426A` for ANCHOR) |
| Muted Green | `#84984C` | Nav hover state |
| Light Gold | `#DFDF9E` | Nav selected tab bg |

### Accent Colors
| Name | Hex | Usage |
|------|-----|-------|
| Orange | `#F59E20` | `.btn-solid-orange` button bg |
| Hover Orange | `#E64C00` | Button hover state |
| Orange (general) | `#F7931F` / `#F7931E` | `.orange` swatch, readmore link hover |
| Gold | `#F6D514` | `.gold` swatch |
| Tan | `#F0DEBB` | `.bg-tan` background sections |
| Gold (footer heading) | `#F4D69E` | Footer h3 color |
| Yellow hover | `#FFE061` | nest-navigation-bar link hover |

### Neutral Colors
| Name | Hex | Usage |
|------|-----|-------|
| Dark Gray | `#666` / `#676767` | Body text, `.dark-grey` swatch |
| Medium Gray | `#777` | Captions |
| Dark Text | `#222` | Selected nav link text |
| Light Gray | `#F5F5F5` | `.light-grey` swatch, `.grey-bg` |
| Border Gray | `#DDD` | Portlet borders |
| Border Light | `#DFDFDF` | `.image-border` |
| Brown | `#A26623` | `.brown` swatch |
| Blue | `#6D97BF` | `.blue` swatch |
| Edit Bar Teal | `#84B3B3` | Edit bar bg (admin only) |

---

## Typography

### Headings
```css
h1.documentFirstHeading, h1 {
    color: #27426A;
    font-family: 'Montserrat', sans-serif;
    font-size: 2.6em;
    font-weight: 500;
    margin-bottom: 0.5em;
    margin-top: 1.5em;  /* 0 on mobile */
}

h2, h3, h4, h5, h6 {
    color: #27426A;
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
    line-height: 1.5em;
    letter-spacing: -0.0115em;
    margin-bottom: 0;
}
```

Note: Title and byline are hidden on document views via `display: none !important`.

### Body Text
```css
body {
    font-family: 'Open Sans', sans-serif;
    line-height: 1.5em;
}

p {
    color: #666;
    line-height: 1.6em;
    padding-bottom: 15px;
}

.intro {
    font-size: 17px;
    line-height: 1.7em;
    color: #676767;
    margin: 1em 0;
}
```

### Portlet Headings
```css
dl.portlet dt {
    font-family: 'Montserrat', sans-serif;
    font-size: 17px;
    color: #666;
}
```

### Readmore Links
```css
a.readmore {
    font-size: 13px;
    font-weight: 600;
    text-transform: uppercase;
    font-family: 'Source Sans Pro', sans-serif;
}
/* hover: color #f7931e */
```

---

## Layout

### Page Width
- `#portal-header`: 1170px centered (100% on mobile)
- `#portal-columns`: 1170px centered, margin: 20px auto (100% below 1169px)
- `#visual-portal-wrapper`: max-width 100%, min-height calc(100vh - 190px)
- `.narrow` / `.inner-container`: 1170px max-width, centered

### Grid System (from ploneCustom.css)
CSS Grid-based layouts used throughout:

| Class | Columns | Gap |
|-------|---------|-----|
| `.grid-container-2col` | 50% + 1fr | 30px |
| `.grid-container-3col` | repeat(3, minmax(0,1fr)) | 30px |
| `.grid-container-4col` | repeat(4, minmax(0,1fr)) | 0 |
| `.grid-container-5col` | repeat(5, 1fr) | 20px |
| `.grid-container-three-quarter` | 80% + 1fr (anchor) / 75% + 1fr (base) | 25-30px |
| `.grid-container-2col-no-gap` | 50% + 1fr | 0 |

All grid layouts collapse to single column at 768px.

### Flex Containers
```css
.flex-container {
    display: flex;
    align-items: flex-start;
}
/* Collapses to column at 768px */
```

### Fullwidth Sections
```css
.fullwidth-section {
    width: 100vw;
    position: relative;
    margin-left: -50vw;
    left: 50%;
    padding: 2em 0;
    margin-bottom: 2em;
}
```

### Spacing Utilities
| Class | Value |
|-------|-------|
| `.space` | height: 25px |
| `.space10` | height: 10px |
| `.space15` | height: 15px |
| `.space20` | height: 20px |
| `.space30` | height: 30px |
| `.pad10` | padding: 10px |
| `.pad20` | padding: 20px |
| `.pad30` | padding: 30px |
| `.gap10` | gap: 10px |
| `.gap15` | gap: 15px |
| `.gap20` | gap: 20px |
| `.gap30` | gap: 30px |
| `.clear` | clear: both |

---

## Header / Banner

### Nest Navigation Bar (top bar above header)
```css
.nest-navigation-bar {
    background: #27426A;  /* anchor.css overrides base #405D68 */
    display: block;       /* anchor.css overrides base display:none */
    padding: 10px 30px;
    font-weight: 600;
    font-size: 12px;
    letter-spacing: 1px;
    text-transform: uppercase;
    font-family: 'Montserrat';
}
.nest-navigation-bar a { color: #fff; }
.nest-navigation-bar a:hover { color: #ffe061; }
.nest-nav-inner { margin: 0 auto; width: 100%; padding: 1px 30px; }
```

Contains: "Return to Landscape Partnership Site" link + dropdowns for Target Species, WLFW Landscapes, Companion Sites.

### Portal Header
```css
#portal-top { height: 0; background-image: none; }
#portal-header { width: 100%; }
```

### Logo
```css
#portal-logo img {
    width: 577px;
    height: 182px;
    position: relative;
    top: 10px;
    left: 16%;
}
/* Mobile: width 350px, height auto, left 10px */
```

Logo image: `anchor-images/anchor-logo.png`

### Banner Image
```css
.site-anchor #portal-banner {
    background: url(anchor-images/iStock-157431434-grasslands.jpg) no-repeat center / cover;
    height: 440px;
}
/* Mobile: height 230px */
```

For ANCHOR Map / Registration Form pages:
```css
.section-anchor-map #portal-banner,
.section-anchor-registration-form #portal-banner {
    height: 230px;
}
```

### Search Box
```css
#portal-searchbox { top: -30px; right: 30px; border-radius: 6px; }
.LSBox {
    top: 85px;
    position: relative;
    background: rgba(255, 255, 255, 0.35);
    padding: 11px 15px;
    border-radius: 6px;
    border: 1px solid #fff;
    right: 2rem;
}
```

---

## Navigation

### Main Nav (Global Nav)
```css
#globalnav-wrapper {
    background-color: #27426A;
    border-bottom: medium none;
    border-top: 1px solid white;
    top: 388px;     /* positioned absolutely over banner */
}

#portal-globalnav {
    background-color: #27426A;
    display: flex;
    justify-content: center;
}

#portal-globalnav li a {
    background-color: #27426A;
    font-size: 16px;
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
    padding: 14px;
    color: #fff;
}
```

### Nav States
```css
/* Selected */
#portal-globalnav .selected a {
    background: #DFDF9E;
    color: #222;
}

/* Hover */
#portal-globalnav a:hover,
#portal-globalnav .selected a:hover {
    background: #84984C;
    color: #fff;
}
```

### Submenu (Dropdowns)
```css
#portal-globalnav ul {
    position: absolute;
    width: 230px;
    left: -999em;          /* hidden off-screen, shown on hover */
    background: #fff;
    box-shadow: 0px 0px 5px #666;
}

#portal-globalnav ul.submenu a {
    font-weight: 400;
    background: #efefef;
    color: #333;
    border-top-width: 1px;
}

#portal-globalnav ul.submenu a:hover {
    background-color: #7d9cc0;
    color: #fff;
}
```

### Mobile Nav
- `.menu-toggle`: shown at 768px, black bg with hamburger icon
- `#portal-globalnav`: hidden, shown with `.opened` class
- Nav items stack 100% width
- `#globalnav-wrapper`: top: 45px on mobile

### Nav Tab IDs
| Tab | ID | Notes |
|-----|-----|-------|
| Home | `#portaltab-anchor-homepage` | Submenu hidden |
| ANCHOR Resources | `#portaltab-anchor-resources` | Has submenu |
| ANCHOR MAP | — | Main tab link |
| ANCHOR Registration Form | — | Main tab link |

---

## Buttons

### Default Button
```css
.button {
    color: #54585B;
    font-size: 1.125rem;
    padding: .75rem 1rem;
    border: 1px solid #888;
    border-radius: 0.25rem;
    font-weight: 700;
    font-family: "Open Sans", Arial, sans-serif;
    box-shadow: 2px 3px 5px -1px rgba(0,0,0,0.35);
}
.button:hover {
    background: #E64C00;
    color: #fff;
    border-color: transparent;
}
```

### Solid Orange Button
```css
.btn-solid-orange {
    color: #fff;
    background: #F59E20;
    border-color: transparent;
}
.btn-solid-orange:hover {
    background: #E64C00;
    color: #fff;
}
```

---

## Content Blocks

### Background Blocks
```css
.bg-tan { background: #F0DEBB; padding: 2rem; }
.bg-white-rounded { background: #fff; border-radius: 15px; }
.fullwidth-section { /* see Layout section */ }
.grey-bg { background: #f5f5f5; }
```

### Partner Block
```css
.partner-block {
    display: flex;
    align-items: center;
    justify-content: space-around;
    gap: 20px;
    margin: 2em auto;
}
/* Mobile: 3-column grid */
```

### Card White
```css
.card-white {
    padding: 15px;
    border-radius: 3px;
    background-color: #fff;
}
```

### Image Utilities
```css
.rounded { border-radius: 8px; }
img.rounded { border-radius: 5px; }
.rounded15 { border-radius: 15px; }
.shadow-btm { box-shadow: 3px 8px 10px -4px rgb(0 0 0 / 40%); }
.image-border { border: 1px solid #dfdfdf; }
.image-right { margin: 0 0 0 2em; }
```

### Caption
```css
.caption { padding: 0 0 10px; color: #777; font-size: 13px; }
dd.image-caption { color: #666; font-size: 100%; max-width: 100%; padding: 20px; text-align: center; }
```

### Tile Items (Listings)
```css
.tileHeadline { font-size: 1.5em; font-weight: 600; }
.tileImage img { width: 280px; height: auto; }
```

---

## Footer

```css
#portal-footer {
    background: #27426A;  /* anchor.css overrides base #2e76a0 */
    color: #fff;
    padding: 1.5em;
}

#portal-footer h3 {
    color: #F4D69E;
}

#portal-footer p {
    color: #fff;
    font-size: 12px;
}

#portal-footer .sitecredit a { color: #fff; }
#portal-footer .sitecredit a:hover { color: #F0DEBB; }
```

### Footer Layout
Uses `.grid-container-5col` (5-column grid, 20px gap):
1. WLFW logo + USDA logo
2. EBTJV logo + SARP logo
3. "Learn" links (About, Members, Community, Issues, Help)
4. "Browse" links (Projects, Maps, News, Resources, Training)
5. "Contact" + LP logo + site partner dropdown

### Footer Menu
```css
#portal-footer ul.ft-menu {
    list-style: none;
    margin: 0;
    padding: 0;
}
#portal-footer .ft-menu li a {
    color: #fff;
    font-size: 14px;
}
#portal-footer .ft-menu li a:hover {
    color: #f0debb;
}
```

---

## Portlets (Sidebar)

```css
dl.portlet {
    font-size: 90%;
    border: 1px solid #ddd;
    border-radius: 6px;
    margin-bottom: 1.5em;
}

.portletNavigationTree .portletHeader {
    background: #205C90;
    border-radius: 4px 4px 0 0;
    text-transform: uppercase;
    padding: 15px;
}
```

---

## Responsive Breakpoints

| Breakpoint | Behavior |
|-----------|----------|
| 1170px | `#portal-header` and `.narrow` go 100% width |
| 1169px | `#portal-columns` goes 100% width |
| 979px | Top header link font size reduces |
| 768px | **Primary mobile breakpoint**: nav collapses, grid layouts stack, banner shrinks to 230px, logo shrinks to 350px, `.menu-toggle` appears |
| 767px | h1 margin-top: 0, `.grid-container-5col` stacks |
| 480px | Mobile media for handheld stylesheet |

---

## Back to Top Button
```css
.back-to-top a {
    background: #222;
    border-radius: 5px;
    bottom: 0.75em;
    color: #ccc;
    height: 35px;
    line-height: 35px;
    position: fixed;
    right: 0.75em;
    width: 110px;
    font-size: 13px;
    text-transform: uppercase;
    z-index: 100;
}
.back-to-top:hover a {
    background: #000;
    color: #87A301;
}
```

Uses jQuery fade in/out at 250px scroll offset.

---

## CSS File Hierarchy (Load Order)

1. `reset.css` — CSS reset
2. `jquery.css` — jQuery UI styles
3. `base.css` — Plone base styles (70KB, comprehensive)
4. `dropdown-menu.css` — Portal globalnav dropdown mechanics
5. `tinymce.css` — TinyMCE editor styles
6. `print.css` — Print stylesheet
7. `mobile.css` — Basic mobile overrides
8. `dateinput.css` — jQuery tools date input
9. `fullcalendar.css` — Calendar widget styles
10. `truegallery.css` — Gallery portlet styles
11. `contentleadimage.css` — Lead image content type
12. `ploneboard.css` — Discussion board styles
13. **`ploneCustom.css`** — Main site-wide custom styles (6323 lines, all shared LP styles)
14. Font Awesome 4.2.0
15. Google Fonts
16. **`anchor.css`** — ANCHOR sub-site specific overrides (loaded last, 692 lines)

The `anchor.css` file is the key sub-site stylesheet. It overrides `ploneCustom.css` for ANCHOR-specific branding (navy blue `#27426A` for nav/footer instead of the default LP blue-gray `#657F9E`).

---

## Key Differences from Base LP Site

- **Nav background**: `#27426A` (navy) instead of `#657F9E` (blue-gray)
- **Footer background**: `#27426A` instead of `#2E76A0`
- **Heading font**: Montserrat (same as base but explicitly set)
- **Nav font**: Montserrat at 16px, 600 weight (base uses Source Sans Pro at 18px)
- **Selected nav**: Light gold `#DFDF9E` bg with `#222` text (base uses `#95A664` green)
- **Nav hover**: `#84984C` muted green (base uses `#4C6C8C` blue)
- **Banner**: Custom grasslands image, 440px height (230px for sub-pages)
- **nest-navigation-bar**: Visible (display:block), `#27426A` bg (base hides it)
- **Title/byline**: Hidden on document views
- **Breadcrumbs**: Hidden
- **Portal-top**: Height 0, no background image
