# SE FireMap Sub-site Style Guide

Extracted from `https://www.landscapepartnership.org/networks/working-lands-for-wildlife/wildland-fire/fire-mapping/regional-fire-mapping/se-firemap`

---

## 1. Page Inventory

| # | Page | URL slug | Notes |
|---|------|----------|-------|
| 01 | Home | `/se-firemap` | Hero content, viewer CTA, storymap embed, card grid |
| 02 | About | `/se-firemap/about` | Partners listing, banner image |
| 03 | Story of the SE FireMap | `/se-firemap/background` | StoryMap embed, banner image |
| 04 | SE FireMap Viewer 2.0 | `/se-firemap/se-firemap-viewer-start` | Survey/entry page, different layout (no main nav) |
| 05 | Data Products | `/se-firemap/data-products` | Content page with tables, banner image |
| 06 | Resources | `/se-firemap/resources` | Documentation listing, banner image |
| 07 | News | `/se-firemap/news` | News collection, tile listings |

---

## 2. Color Palette

### Primary Colors
| Color | Hex | Usage |
|-------|-----|-------|
| Orange (primary accent) | `#e86129` | h1-h6 headings, nav hover, link hover, CTA emphasis |
| Gold/Amber | `#f9b30c` / `#F59E20` | Selected nav tab bg, buttons |
| Dark charcoal (nav bg) | `#0E1D1C` | Global nav background |
| Brown (footer) | `#7d6042` | Footer background |
| White | `#fff` | Page background, header bg |

### Secondary/Accent Colors
| Color | Hex | Usage |
|-------|-----|-------|
| Orange (button) | `#f8903e` / `#ef8f39` | Button backgrounds |
| Orange hover | `#e64c00` / `#F7700D` | Button hover states |
| Gold (timeline) | `#ffc107` | Timeline carousel accents, dots |
| Yellow gold | `#ffdf5a` / `#f1d215` | Timeline headings, blue-block h4 |
| Green (nest nav) | `#899f3f` | Nested navigation bar bg |
| Green (content action) | `#75ad0a` | Content action menus |
| Blue (portlet header) | `#205C90` | Portlet navigation header bg |
| Blue (block) | `rgba(20, 83, 120, 0.80)` | Blue overlay blocks |
| Timeline dark bg | `#2d3031` | Timeline carousel background |

### Neutral Colors
| Color | Hex | Usage |
|-------|-----|-------|
| Body text | `#666` / `#676767` | Paragraph text |
| Light grey bg | `#f5f5f5` / `#efefef` | Background blocks, submenu hover |
| Cool grey bg | `#dbdedf` | Alternative bg |
| Dark grey bg | `#cacaca` | Alternative bg |
| Footer link | `#dbcfbc` / `#dacfbb` | Footer text and link color |

### Styleguide CSS Classes
```css
.orange { background: #f7931f; }
.brown { background: #a26623; }
.dark-blue { background: #205c90; }
.light-grey { background: #f5f5f5; }
.dark-grey { background: #676767; }
```

---

## 3. Typography

### Font Families
| Font | Usage | Weights |
|------|-------|---------|
| **Montserrat** | Headings (h1-h6), nav links, subheads, buttons | 400, 500, 600, 700 |
| **Merriweather** | Body paragraphs, intro text, tables | 400, 400i, 700 |
| **Open Sans** | Buttons (`.button` class) | 400, 400i, 600 |
| **Source Sans Pro** | Read more links, descriptions | 400, 700 |
| **Libre Franklin** | Timeline carousel headings | 300-900 |
| **Roboto** | Timeline carousel body | 300 |
| **Nunito Sans** | Loaded but usage unclear | 400, 700 |
| **Public Sans** | Loaded but usage unclear | 300, 400, 700 |
| **Material Icons** | Icon font | normal |

### Heading Styles
```css
h1 {
    color: #e86129;
    font-family: 'Montserrat', sans-serif;
    font-size: 38px;
    font-weight: 700;         /* .documentFirstHeading uses 500 */
    margin-bottom: 0.5em;
}

h2, h3, h4, h5, h6 {
    color: #e86129;
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
    line-height: 1.5em;
    letter-spacing: -0.0115em;
    margin-bottom: 10px;
}

h3 { font-size: 24px; }
h4 { font-size: 20px; }
```

### Body Text
```css
p {
    font-family: 'Merriweather', serif;
    color: #666;
    font-size: 16px;
    letter-spacing: 0.01em;
    line-height: 1.6em;
}

.intro {
    font-family: 'Merriweather', serif;
    font-size: 18px;
    line-height: 1.7em;
    color: #676767;
}
```

### Subheadings
```css
.subhead {
    text-transform: uppercase;
    font-size: 14px;
    letter-spacing: 2px;
    color: #7f7f87;
    line-height: 1em;
}
```

---

## 4. Layout & Structure

### Page Dimensions
- `#visual-portal-wrapper`: `max-width: 100%`, `min-height: calc(100vh - 190px)`
- `#portal-columns`: `width: 1170px`, `margin: 0 auto`, `top: -10px`
- Home page (`template-fire_home`): `#portal-columns` full width, `#content` 100% width

### Header
- `#portal-top`: height `164px` (desktop), `130px` (mobile ≤768px)
- `#portal-header`: `background: #fff`, height `130px`, `position: relative`, full width
- `#portal-logo img`: width `400px`, `left: 20%`, `top: 10px`
- Mobile logo: width `300px`, `top: -90px`, `left: 5px`

### Banner
- `#portal-banner`: height `300px` (desktop), `150px` (mobile ≤768px)
- `background-position: center`, `background-size: cover`
- Hidden on home page, viewer, search, and some special sections
- Per-section background images defined in CSS

### Search Box
- `#portal-searchbox`: `top: -30px`, `right: 30px`

---

## 5. Navigation

### Global Nav Bar
```css
#globalnav-wrapper {
    background-color: #0E1D1C;
    border-bottom: medium none;
    border-top: 1px solid white;
    top: 135px;
}

#portal-globalnav {
    background-color: #0E1D1C;
}

#portal-globalnav li a {
    background-color: #0E1D1C;
    font-size: 16px;
    font-family: 'Montserrat', sans-serif;
    font-weight: 500;
    text-transform: uppercase;
    padding: 10px 20px;
}
```

### Nav States
- **Default**: white text on `#0E1D1C` dark background
- **Selected**: `background: #f9b30c` (gold/amber), `color: #222`
- **Hover**: `background: #e86129` (orange), `color: #fff`
- **Selected + Hover**: same orange hover

### Home Tab
- Uses background image (`menu-home-white.png`), text hidden via `text-indent: -999em`
- Hover: orange bg with same icon

### Submenus
```css
#portal-globalnav ul.submenu a {
    text-transform: none;
    font-size: 15px;
}

#portal-globalnav ul.submenu a:hover {
    background-color: #efefef !important;
    color: #E86128 !important;
}
```

### Nested Navigation Bar (WLFW)
- Not shown on viewer/home pages
- `background: #899f3f` (green)
- Links: white, uppercase, 13px, letter-spacing 2px, Montserrat 600
- Hover: `color: #ffe061` (gold)

### Mobile Nav
- `.menu-toggle`: black bg, white text, hamburger icon, Montserrat 600, 16px
- `#portal-globalnav.opened`: `display: block`, `text-align: center`
- `#globalnav-wrapper`: `top: -40px` at ≤768px

---

## 6. Buttons

### Standard Button
```css
.button {
    color: #54585b;
    font-size: 1.125rem;
    padding: .75rem 1rem;
    border: 1px solid #888;
    border-radius: 0.25rem;
    font-weight: 700;
    font-family: "Open Sans", Arial, sans-serif;
    box-shadow: 2px 3px 5px -1px rgba(0, 0, 0, 0.35);
    transition: background .2s linear, color .2s linear, border-color .2s linear;
}
.button:hover {
    background: #e64c00;
    color: #ffffff;
    border-color: transparent;
}
```

### Solid Orange Button
```css
.btn-solid-orange {
    color: #ffffff;
    background: #F59E20;
    border-color: transparent;
}
/* hover: background: #e64c00 */
```

### Orange Accent Button
```css
a.btn-orange {
    color: #fff;
    letter-spacing: 1px;
    font-family: 'Montserrat';
    font-weight: 600;
    text-transform: uppercase;
    font-size: 13px;
    background: #ef8f39;
}
```

### Orange Border Button
```css
.button-orange {
    background: #f8903e;
    padding: 10px 15px;
    border: 4px solid #fff;
    font-size: 15px;
    text-transform: uppercase;
    outline: 1px solid #fbc499;
}
/* hover: background: #F7700D */
```

### Large White CTA Button
```css
#content a.btn.large-white {
    border: 1px solid #fff;
    padding: 15px;
    text-transform: uppercase;
    background: rgba(255, 255, 255, 0.25);
    color: #fff;
    letter-spacing: 0.075em;
    border-radius: 4px;
    font-size: 14px;
    font-weight: 600;
    transition: all 0.3s ease-in-out;
}
```

### Read More Link
```css
a.readmore {
    font-size: 13px;
    font-weight: 600;
    text-transform: uppercase;
    font-family: 'Source Sans Pro', sans-serif;
}
/* hover: color: #f7931e */
```

---

## 7. Content Blocks

### Full-Width Sections
- `.fullwidth-section`: `margin-bottom: 3em`; at ≤1169px: `width: 100vw`, `margin-left: -1.5em`
- `.fullwidth-section-sefiretool`: `width: 100vw`, centered with negative margin trick
- `.fullwidth-section-timeline`: similar centering, `padding: 2em 0`

### Dark Overlay Blocks
```css
.dark-block {
    background: rgba(0 0 0 / 80%);
    padding: 40px 30px;
    min-height: 460px;
}
.dark-block-75 {
    background: rgba(0 0 0 / 75%);
    padding: 40px;
}
/* h4 in dark-block-75: color #f8903e */
```

### Blue Overlay Block
```css
.blue-block {
    background: rgba(20 83 120 / 80%);
    padding: 40px 30px;
    min-height: 400px;
}
/* h4: #f1d215, links: #f9d90f, link hover: #fd7916 */
/* p text: #fff */
```

### Map Viewer Block
- `.mapviewer-block`: background image, `background-size: cover`, `min-height: 400px`

### Feature Block
```css
.feature-block {
    border: 6px solid #efefef;
    padding: 20px;
    background: #fff;
}
/* h3: font-size 28px, color #e86129 */
```

### Background Classes
- `.bg-grey`: `#efefef`
- `.bg-coolgrey`: `#dbdedf`
- `.bg-darkgrey`: `#cacaca`
- `.bg-storymap`: `#FBF3CC` (light yellow)

### Slide Overlay
```css
.slide-overlay {
    position: absolute;
    z-index: 5;
    top: 55%;
    background: rgba(0, 0, 0, 0.6);
    padding: 30px;
    width: 70%;
    left: 15%;
    color: #fff;
    border-radius: 6px;
    text-align: center;
}
```

### Card White
```css
.card-white h4 {
    font-size: 18px;
    line-height: 1.5rem;
    margin-top: .75rem;
}
```

### Grid Layouts
- `.grid-container-three-quarter`: `grid-template-columns: 68% 1fr`, gap `30px`; mobile: single column
- `.twocol-container`: flex, gap `30px`; ≤1200px: column direction
- `.flex-container`: flex, gap `15px`; ≤768px: column direction

---

## 8. Footer

### Footer Wrapper
```css
#portal-footer-wrapper {
    background: #7d6042;
}
#portal-footer {
    background: #7d6042;
    height: 250px;
}
```

### SE FireMap Custom Footer
- `#sefiremap-footer`: block, relative, text-align left
- `h4`: `color: #dacfbb`, uppercase, `letter-spacing: 3px`
- Links: `color: #dbcfbc`, hover: `#fff`
- Partner logos displayed in `.flex-row` (flex, space-between)
- Bottom nav (`.bottom-nav`): flex on desktop, grid single-column on mobile
- Site credit: Ferguson Lynch logo + text, 13px, uppercase

### Footer Link Colors
- Default: `#dbcfbc`
- Hover: `#fff`
- `#sefiremap a:hover`: `#f4a221` (gold)

---

## 9. Responsive Breakpoints

| Breakpoint | Elements affected |
|-----------|-------------------|
| `≤768px` | Header height (130px), logo (300px wide, repositioned), banner (150px), nav toggler, portal-columns full width, grid layouts collapse to single column, slide overlay full width, storymap bg → white, bottom-nav → grid, nest-nav padding reduced |
| `≤1130px` | Grid layout tile items → 100% width |
| `≤1160px` | Flex row wraps |
| `≤1169px` | Full-width sections use 100vw with adjusted margins |
| `≤1200px` | Two-column container → column direction |
| `≥700px` | `.mobile-only` hidden |
| `≥701px` | `.desktop-only` shown |

---

## 10. Google Fonts

Loaded in `<head>`:
```html
<link href="https://fonts.googleapis.com/css?family=Open+Sans:400,400i,600|Source+Sans+Pro:400,700&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Merriweather:400,400i,700|Montserrat:400,500,600&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Nunito+Sans:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Public+Sans:ital,wght@0,300;0,400;0,700;1,300;1,400&display=swap" rel="stylesheet">
```

Loaded via `@import` in CSS:
```css
@import url("https://fonts.googleapis.com/css?family=Libre+Franklin:300,400,600,700,800,900&display=swap");
@import url("https://fonts.googleapis.com/css?family=Roboto:300&display=swap");
```

Also uses Font Awesome 4.2.0 from MaxCDN.

---

## 11. Special Components

### "Return to Landscape Partnership Site" Banner
- Top-of-page link bar (green background from parent WLFW styles)
- White text, uppercase, small font

### Portlets
```css
dl.portlet {
    font-size: 90%;
    border: 1px solid #ddd;
    border-radius: 6px;
    margin-bottom: 1.5em;
}
dl.portlet dt {
    padding: 1em 1em 0.25em;
    background: transparent;
    color: #666;
    font-family: 'Montserrat', sans-serif;
    font-size: 17px;
}
```

### Breadcrumbs
```css
#portal-breadcrumbs {
    font-size: 85%;
    margin: 1.5em auto 1em;
    padding: 10px 0;
}
```
Hidden on home page and some special sections.

### Timeline Carousel
- Dark background (`#2d3031`)
- Year labels: Montserrat 700, 32px, white
- Month labels: Montserrat 600, 14px, uppercase, `#ffc107` (gold)
- Category badges: colored borders (green for releases, blue for meetings, orange for publications)
- Slick dots: `#ffc107` active, `rgba(255,255,255,0.6)` inactive
- Navigation buttons: `btn-warning` style (`#ffc107`)

### News Tiles
```css
.tileHeadline { font-size: 1.5em; font-weight: 600; }
.tileImage img { width: 220px; height: auto; }
```

---

## 12. Key Body Classes for Conditional Styling

- `.site-se-firemap` — general se-firemap site wrapper
- `.template-fire_home` — home page template
- `.template-document_view` — standard document pages
- `.template-se-firemap-viewer` — viewer app
- `.template-se-firemap-viewer-start` — viewer entry page
- `.template-se-firemap-survey` — survey page
- `.section-data-products` — data products section
- `.section-resources` — resources section
- `.section-workspace` — workspace section
- `.subsection-about-page` — about page
- `.subsection-background-page` — story/background page
- `.section-southeast-se-firemap-home-page` — alternate home page class
- `.content-se-firemap-collection` — collection content type
