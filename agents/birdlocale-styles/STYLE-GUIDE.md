# BirdLocale Sub-site Style Guide

**Source URL:** https://dev.landscapepartnership.org/networks/working-lands-for-wildlife/birdlocale
**CSS file:** `birdlocale.css` (sub-site specific, 801 lines)
**Crawl date:** 2026-03-18

---

## Page Inventory

| # | Page | URL Path | Description |
|---|------|----------|-------------|
| 1 | Home | `/networks/working-lands-for-wildlife/birdlocale` | Landing page with header banner, feature blocks, partner logos |
| 2 | Technical Background | `.../birdlocale/background` | Text content about the project history, goals, and partnership |
| 3 | How to Access the Web App | `.../birdlocale/how-to-access-the-web-app` | Login/access instructions for the BirdLocale web application |
| 4 | Contributors | `.../birdlocale/birdlocale-contributors` | Partner logo grid with contributor organizations |

---

## Color Palette

### Brand Colors
| Color | Hex | Usage |
|-------|-----|-------|
| Green (lime) | `#b0bc1f` | Nav hover/selected border, WLFW nav bar links, material icon borders/color |
| Orange | `#f88630` | Breadcrumb current, readmore hover, site credit hover, `.orange` utility |
| Brown | `#624f44` | H1-H6 heading text |
| Dark brown | `#2f2a25` | Body text (paragraphs), `.dark-brown` utility |
| Medium brown | `#91806e` | Breadcrumb "you are here", material icons brown, `.brown` utility |
| Light brown / cream | `#f8f5ef` | Footer wrapper bg, feature block bg, footer heading text, site credit text, EEO text, `.lite-brown` utility |
| Gold/tan (mobile nav) | `#b59553` | Mobile nav background |

### Accent Colors
| Color | Hex | Usage |
|-------|-----|-------|
| Orange (alt) | `#f7931e` | Readmore hover text (commented-out button bg) |
| Orange (dark) | `#E86128` | Submenu link hover text |
| Hover orange | `#ff9900` | Footer menu link hover |
| Green (olive/footer) | `#95a662` | Footer bar background (`#portal-footer`) |
| Green (edit bar) | `#88b66a` | Edit bar background, content actions |
| Cyan (visited) | `#a9e1f3` | Personal tools visited link |
| Cyan (footer heading) | `#d0f7ff` | Footer container h4 |
| Gray (intro text) | `#676767` | `.intro` class text |
| Dark gray (WLFW bar) | `#444` | WLFW nav bar background |
| Light gray (submenu hover) | `#efefef` | Submenu hover bg, grid tile bg |
| White | `#fff` | Body bg, portal wrapper bg, nav link default, various elements |
| Nav hover bg | `rgba(0,0,0,0.35)` | Nav hover/selected background overlay |
| Overlay bg | `rgba(0,0,0,0.5)` | `.portlet-overlay` background |

---

## Typography

### Font Families
| Font | Weights | Usage |
|------|---------|-------|
| **Nunito Sans** | 400, 700 (also italic) | Body font, all headings (h1-h6) |
| **Montserrat** | 400, 500, 600 | Mobile menu toggle, footer menu items, WLFW nav bar |
| **Open Sans** | 400, 400i, 600 | Readmore links |
| **Source Sans Pro** | 400, 700 | Loaded but not explicitly referenced in birdlocale.css |
| **Merriweather** | 400, 400i, 700 | Loaded but not explicitly referenced in birdlocale.css |
| **Public Sans** | 300, 400, 700 (+ italic) | Loaded but not explicitly referenced in birdlocale.css |
| **Material Icons** | normal | Icon font for material design icons |

### Font Sizes
| Element | Size | Weight | Other |
|---------|------|--------|-------|
| Body | (browser default, 1rem) | normal | `font-family: 'Nunito Sans'`, antialiased |
| H1 / `.documentFirstHeading` | `2.1rem` | 700 | color: `#624f44`, margin-bottom: 0.5em |
| H2 | `1.8rem` | 700 | — |
| H3 | `1.6rem` | 700 | — |
| H4 | `1.3rem` | 700 | — |
| All headings (h1-h6) | — | 700 | line-height: 1.3em, letter-spacing: -0.0115em |
| Paragraphs | `1rem` | normal | color: `#2f2a25`, line-height: 1.6em |
| `.intro` | `18px` | normal | color: `#676767`, line-height: 1.7em |
| Nav links | `18px` | 600 | uppercase, border-radius: 30px |
| Nav links (tablet) | `16px` | 600 | uppercase |
| Submenu links | `15px` | — | not uppercase |
| Breadcrumbs | `0.75rem` | 600 | uppercase, letter-spacing: 2px |
| Footer menu | `15px` | 500 | font-family: Montserrat |
| WLFW nav bar links | `13px` | 600 | uppercase, letter-spacing: 1px |
| Menu toggle (mobile) | `13px` | 600 | font-family: Montserrat |
| Readmore | `13px` | 600 | uppercase, font-family: Open Sans |
| Tile headline | `1.5em` | 600 | — |
| Site credit | `13px` | — | uppercase, letter-spacing: 0.05em |
| EEO statement | `13px` | — | line-height: 1.3em |

---

## Layout & Structure

### Page Dimensions
| Element | Value |
|---------|-------|
| `#visual-portal-wrapper` max-width | `100%` |
| `#portal-columns` width | `1170px` (desktop), `96%` (mobile) |
| `#portal-top` height | `630px` (desktop), `265px` (mobile <=768px) |
| `#portal-header` height | `635px` (desktop), `240px` (mobile <=768px) |
| Header background image | `birdlocale-images/birdlocale-header.jpg` (right bottom / cover) |
| Header mobile bg image | `birdlocale-images/birdlocale-block.jpg` (center bottom / cover) |
| Body background | `#fff` with `blank.png` image |

### Logo
| Property | Value |
|----------|-------|
| Logo width | `320px` (desktop), `280px` (<=1024px), `290px` (<=768px) |
| Logo position | `left: 10%`, `top: 20px`, `z-index: 2` |
| Mobile logo | `position: absolute`, `top: 15px`, `left: 5px` |

### Columns
| Element | Value |
|---------|-------|
| `#portal-column-one` | `position: relative`, `top: 4em` |
| `#portal-column-two` | `position: relative`, `top: 2em` |

---

## Navigation

### WLFW Top Bar
| Property | Value |
|----------|-------|
| Background | `#444` |
| Padding | `10px 30px` |
| Font | Montserrat, 600, 13px |
| Link color | `#b0bc1e` (lime green) |
| Link hover | `#f88630` (orange) |
| Text transform | uppercase, letter-spacing: 1px |
| z-index | 20 |

### Global Nav (`#globalnav-wrapper`)
| Property | Desktop | Mobile (<=768px) |
|----------|---------|-------------------|
| Background | transparent | transparent |
| Position | `top: 25px`, `left: 30%` | `top: 70px`, `left: 0` |
| Width | `70%` | `100%` |
| Border-top | none | — |
| Display | flex, justify: right | none (toggled via `.opened`) |

### Nav Links (`#portal-globalnav li a`)
| Property | Desktop | Tablet (<=1024px) | Mobile (<=767px) |
|----------|---------|---------------------|-------------------|
| Font size | `18px` | `16px` | same |
| Font weight | 600 | 600 | 600 |
| Text transform | uppercase | uppercase | uppercase |
| Padding | `10px 20px` | `10px 15px` | `0 2em` |
| Border | `3px solid transparent` | `3px solid transparent` | — |
| Border radius | `30px` | `30px` | — |
| Background | transparent | transparent | — |

### Nav Hover State
| Property | Value |
|----------|-------|
| Background | `rgba(0,0,0,0.35)` |
| Color | `#fff` |
| Border | `3px solid #b0bc1f` (lime green) |
| Border radius | `30px` |

### Nav Selected State
Same as hover state: `rgba(0,0,0,0.35)` bg, white text, `3px solid #b0bc1f` border, `30px` radius.

### Submenu (`ul.submenu`)
| Property | Value |
|----------|-------|
| Text transform | none (overrides uppercase) |
| Font size | `15px` |
| Hover background | `#efefef` |
| Hover text color | `#E86128` (orange) |
| Width | `15em` (from dropdown-menu.css) |

### Mobile Nav (<=768px)
| Property | Value |
|----------|-------|
| `#portal-globalnav` | `display: none` by default |
| `#portal-globalnav.opened` | `display: block` |
| `#portal-globalnav li` | `width: 100%`, `background: #b59553` (gold/tan) |
| Menu toggle font | Montserrat, 600, 13px |

### Home Tab
- Home tab submenu hidden (`#portaltab-home ul.submenu { display: none }`)
- Home link text-indent reset to 0

### Search Box
| Property | Value |
|----------|-------|
| Position | `top: -30px`, `right: 30px` |
| Hidden at | `<=1024px` |

### Personal Tools
| Property | Value |
|----------|-------|
| Position | `right: 30px`, `top: -40px` |
| Link color | `#fff` |
| Visited color | `#a9e1f3` |

---

## Buttons & Links

### Readmore Links (`a.readmore`)
| Property | Value |
|----------|-------|
| Font size | `13px` |
| Font weight | 600 |
| Text transform | uppercase |
| Font family | Open Sans |
| Border bottom | none |
| Hover color | `#f7931e` (orange) |

### Content Links
- `#content a:link` and `dl.portlet a:link`: `border-bottom: none` (removes underlines)

---

## Content Blocks

### Feature Block (`.feature-block`)
| Property | Value |
|----------|-------|
| Background | `#f8f5ef` (cream) |
| Padding | `30px` |
| Border | none |
| Border radius | `15px` |
| Margin | `0 0 30px` |
| Hover | `box-shadow: 0px 1px 5px 0 rgb(75 75 75 / 25%)` |
| Paragraph font size | `20px` |

### Portlet Overlay (`.portlet-overlay`)
| Property | Value |
|----------|-------|
| Background | `rgba(0, 0, 0, 0.5)` |
| Border | `1px solid #fff` |
| Padding | `10px` |
| Border radius | `10px` |

### Grid Tile (`.grid_layout .tileItem`)
| Property | Value |
|----------|-------|
| Text align | center |
| Background | `#efefef` |

### Grid Image (`.gridImage img`)
| Property | Value |
|----------|-------|
| Background | `#fff` |
| Object fit | contain |
| Box shadow | `0px 1px 5px 0 rgb(75 75 75 / 25%)` |
| Margin | `2em 2em 1em` |

### Tile Items
| Property | Value |
|----------|-------|
| `.tileItem` | `clear: both` |
| `.tileHeadline` | `font-size: 1.5em`, `font-weight: 600` |
| `.tileImage img` | `width: 220px`, `height: auto` |

### LSBox (Search overlay)
| Property | Desktop | Mobile (<=768px) |
|----------|---------|-------------------|
| Position | `relative`, `top: 130px` | `absolute`, `top: 113px` |
| Background | `#fff` | transparent |
| Padding | `11px` | `11px` |
| Border | `1px solid #fff` | none |
| Border radius | `6px` | `6px` |
| Box shadow | `0px 1px 5px 0 rgb(75 75 75 / 25%)` | none |
| Right | `2.5%` | — |
| Left (mobile) | — | `57px` |
| Width (mobile) | — | `150px` |

---

## Flex & Grid Layouts

### `.flex-container`
| Property | Value |
|----------|-------|
| Display | flex |
| Direction | row (column on mobile <=768px) |
| Align items | flex-start |
| Gap | `15px` |

### `.flex-container.space-between` (mobile <=768px)
| Property | Value |
|----------|-------|
| Display | grid |
| Grid columns | `repeat(4, 1fr)` |
| Grid gap | `10px` |

### `.flex-container-center`
| Property | Value |
|----------|-------|
| Display | flex |
| Align/justify | center |
| Gap | `25px` |
| Flex wrap | wrap |
| Margin | `0 1em` |

### `.bird-footer-layout`
| Property | Desktop | Mobile (<=768px) |
|----------|---------|-------------------|
| Display | grid | grid |
| Grid columns | `25% 25% auto` | `100%` |
| Column gap | `30px` | — |
| Padding top | `20px` | `30px` |

---

## Footer

### Footer Wrapper (`#portal-footer-wrapper`)
| Property | Value |
|----------|-------|
| Background | `#f8f5ef` (cream) |

### BirdLocale Footer (`#birdlocale-footer`)
| Property | Value |
|----------|-------|
| Background | `#f8f5ef url(birdlocale-images/birdlocale-footer.jpg) no-repeat center / cover` |
| Padding | `2em 0` |
| H3 color | `#f8f5ef` (cream) |
| H4 color | `#d0f7ff` (light cyan) |

### Footer Bar (`#portal-footer`)
| Property | Value |
|----------|-------|
| Background | `#95a662` (olive green) |
| Display | block |
| Padding | `0` |

### Footer Menu (`.ft-menu`)
| Property | Value |
|----------|-------|
| Font family | Montserrat |
| Font weight | 500 |
| Font size | `15px` |
| Item padding | `2px 0` |
| Link color | `#fff` |
| Link hover | `#ff9900` (orange) |

### Bottom Nav (`.bottom-nav`)
| Property | Desktop | Mobile (<=768px) |
|----------|---------|-------------------|
| Display | flex | grid |
| Grid columns | — | `repeat(1, 1fr)` |
| Justify | space-between | — |
| Align | flex-start | — |
| Margin | `20px 0` | `20px 0` |
| Padding top | `20px` | `0` |

### Site Credit (`.sitecredit`)
| Property | Value |
|----------|-------|
| Background image | `fergusonlynch-icon.png` |
| Font size | `13px` |
| Text transform | uppercase |
| Letter spacing | `0.05em` |
| Width | `185px` |
| Margin | `25px auto 5px` |
| Link color | `#f8f5ef` |
| Link hover | `#f88630` |

### EEO Statement
| Property | Value |
|----------|-------|
| Font size | `13px` |
| Line height | `1.3em` |
| Color | `#f8f5ef` |
| Link color | `#f8f5ef` |

### Hidden Elements
- `.lp-footer` — hidden
- `.footer-left` — hidden
- `.footer-rt` — hidden
- `.nest-navigation-bar` — hidden

---

## Partner Logos (`.company-logo img`)
| Property | Value |
|----------|-------|
| Filter | grayscale(100%) |
| Opacity | 0.35 |
| Transform | scale(0.95) |
| Transition | all 0.4s ease |
| Margin | `12px` |
| Width | `150px` |

---

## Material Icons

### Default (`.material-icons`)
| Property | Value |
|----------|-------|
| Font size | `60px` |
| Color | `#fff` |

### Brown variant (`.material-icons-brown`)
| Property | Value |
|----------|-------|
| Font size | `68px` |
| Color | `#91806e` |

### Green variant (`.material-icons-green`)
| Property | Value |
|----------|-------|
| Font size | `60px` |
| Color | `#b0bc1f` |
| Border | `3px solid #b0bc1f` |
| Border radius | 50% (circle) |
| Padding | `15px` |
| Background | `#fff` |

---

## Responsive Breakpoints

| Breakpoint | Elements affected |
|------------|-------------------|
| `max-width: 1024px` | Logo (280px), nav links (16px, 15px padding), search box hidden |
| `max-width: 768px` | Portal columns (96%), portal-top (265px), portal-header (240px), logo (290px), globalnav wrapper (100%, left: 0), nav hidden/toggled, mobile nav bg (#b59553), footer grid (1col), bird-footer-layout (1col), LSBox (absolute), bottom-nav (grid), flex-container (column), site credit centered |
| `max-width: 767px` | Nav links margin (0 2em) |
| `max-width: 600px` | Footer logo flex layout |
| `max-device-width: 480px` | mobile.css: columns full width, logo hidden, globalnav min-width, search centered |

---

## Google Fonts Loaded

```html
<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,400i,600|Source+Sans+Pro:400,700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Merriweather:400,400i,700|Montserrat:400,500,600&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Public+Sans:ital,wght@0,300;0,400;0,700;1,300;1,400&display=swap" rel="stylesheet">
```

Also loads Font Awesome 4.2.0 from MaxCDN.

---

## CSS Files Inventory

| File | Size | Purpose |
|------|------|---------|
| `birdlocale.css` | 14KB | Sub-site specific styles (primary file) |
| `base.css` | 70KB | Plone base styles |
| `ploneCustom.css` | 130KB | Site-wide LP custom styles |
| `dropdown-menu.css` | 2KB | Navigation dropdown behavior |
| `mobile.css` | 1KB | Mobile device overrides |
| `reset.css` | <1KB | CSS reset |
| `jquery.css` | 9KB | jQuery UI styles |
| `fullcalendar.css` | 22KB | Calendar widget |
| `truegallery-portlet.css` | 22KB | Gallery portlet |
| `ploneboard.css` | 4KB | Discussion board |
| `contentleadimage.css` | <1KB | Content lead image |
| `dateinput.css` | 2KB | Date picker |
| `tinymce.css` | <1KB | TinyMCE editor |
| `print.css` | 2KB | Print styles |

---

## Key Differences from Other LP Sub-sites

Compared to the Aquatics sub-site style guide in `agents/aquatics-styles/`:
- **Primary brand color:** Lime green `#b0bc1f` (vs Aquatics teal `#278e95`)
- **Nav accent:** Same lime green `#b0bc1f` for borders (vs Aquatics gold `#dcc464`)
- **Body font:** Nunito Sans (vs Aquatics also uses different fonts)
- **Heading color:** Brown `#624f44` (earth tone palette)
- **Header height:** Much taller at `635px` desktop (vs Aquatics `150px`)
- **Footer:** Multi-section with olive green bar (`#95a662`), cream background, bird-specific footer layout
- **Mobile nav bg:** Gold/tan `#b59553` (vs Aquatics different scheme)
- **Overall palette:** Earth tones (browns, greens, cream) reflecting wildlife/nature theme
