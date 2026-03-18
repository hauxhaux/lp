# Working Lands for Wildlife (WLFW) Sub-site Style Guide

**Source URL:** https://dev.landscapepartnership.org/networks/working-lands-for-wildlife
**Crawl Date:** 2026-03-18
**Body class:** `template-wlfw_home portaltype-folder site-working-lands-for-wildlife`

---

## Page Inventory

| # | Page | URL Path | File |
|---|------|----------|------|
| 1 | Home | `/networks/working-lands-for-wildlife` | `html/01-home.html` |
| 2 | About | `/networks/working-lands-for-wildlife/about-us` | `html/02-about.html` |
| 3 | Partners | `/networks/working-lands-for-wildlife/about-us/partners` | `html/03-partners.html` |
| 4 | Where We Work | `/networks/working-lands-for-wildlife/about-us/where-we-work` | `html/04-where-we-work.html` |
| 5 | Landscapes & Wildlife | `/networks/working-lands-for-wildlife/landscapes-wildlife` | `html/05-landscapes-wildlife.html` |
| 6 | Science | `/networks/working-lands-for-wildlife/science` | `html/06-science.html` |
| 7 | News | `/networks/working-lands-for-wildlife/wlfw-news` | `html/07-news.html` |
| 8 | Events | `/networks/working-lands-for-wildlife/wlfw-news/events` | `html/08-events.html` |
| 9 | Stories | `/networks/working-lands-for-wildlife/wlfw-news/stories` | `html/09-stories.html` |
| 10 | Newsletters | `/networks/working-lands-for-wildlife/wlfw-news/newsletters` | `html/10-newsletters.html` |
| 11 | Get Involved | `/networks/working-lands-for-wildlife/get-involved` | `html/11-get-involved.html` |

---

## Color Palette

### Primary Colors
| Color | Hex | Usage |
|-------|-----|-------|
| Blue-Grey (Nav bg) | `#657F9E` | Main nav background, `.bg-blue` |
| Dark Blue | `#28526E` | CTA block bg, `.bg-darkblue` |
| Link Blue | `#205C90` | Links, visited links, breadcrumbs, FAQ labels, nav tree headers |
| Footer Blue | `#2e76a0` | Main LP footer background |
| Brown (Headings) | `#8E6747` | All headings h1-h6, featured heading text |

### Accent Colors
| Color | Hex | Usage |
|-------|-----|-------|
| Orange | `#f8903e` | `.btn-orange`, `a.large-orange` |
| Orange Hover | `#F7700D` | Orange button hover state |
| Gold CTA | `#f7bd4f` | `.cta-button` background |
| Gold CTA Hover | `#f38b1a` | CTA button hover |
| Gold Text | `#f6d514` | `.gold-text` class |
| Gold Heading | `#f7d25b` | `.heading-gold` |
| Gold Accent | `#fbd84d` | `.black-50-block .subhead` color |
| Red-Orange | `#dd733e` | `.bg-orange`, feature block headings |
| Red | `#FF6633` | `.btn-red` |
| Green (Selected) | `#95A664` | Nav selected state (`#portal-globalnav .selected a`) |
| Teal | `#408E9B` | `.text-big-blue` |

### Neutral Colors
| Color | Hex | Usage |
|-------|-----|-------|
| Body Text | `#444` | Paragraphs, content text |
| Grey Block | `#efefef` | `.grey-block`, submenu background |
| Light Grey | `#f6f3ed` | Portal banner default bg |
| Tan Block | `#e7e5da` | `.tan-block` |
| White | `#fff` | Body background, white blocks |
| Black 65% overlay | `rgb(0 0 0 / 65%)` | `.black-65-block` |
| Black 50% overlay | `rgb(0 0 0 / 50%)` | `.black-50-block`, `.overlay-block` |

### Footer-Specific Colors (WLFW)
| Color | Hex | Usage |
|-------|-----|-------|
| Footer Link Blue | `#7dd4d6` | Site credit links |
| Footer Heading Blue | `#aae2fd` | LP footer h3, site credit text |
| Footer Link Hover | `#FFA64D` | Footer link hover |

### Blue Block Colors
| Color | Hex | Usage |
|-------|-----|-------|
| Blue Block | `rgba(20 83 120 / 80%)` | `.blue-block` |
| Blue Block h2 | `#fedb08` | Blue block heading color |
| Blue Block Subhead | `#D0F7FF` | Blue block subhead text |

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

### Font Families
| Font | Usage |
|------|-------|
| `'Open Sans', sans-serif` | Body text (primary) |
| `'Montserrat', sans-serif` | Headings h1-h6, CTA buttons, search input, subheads, nav tree headers, document description |
| `'Source Sans Pro', sans-serif` | Nav link text (`#portal-globalnav li a`) |
| `'Merriweather', serif` | Pull quotes (`.popquote`, `.quote`) |
| `'Material Icons'` | Icon font (various sizes) |
| `'Public Sans'` | Loaded but not explicitly used in ploneCustom.css (may be used by sub-sites) |
| `'Nunito Sans'` | Loaded but not explicitly used in ploneCustom.css |

### Heading Styles
| Element | Size | Weight | Color | Other |
|---------|------|--------|-------|-------|
| h1-h6 | varies | 500 | `#8E6747` | `font-family: 'Montserrat'`, `line-height: 1.5em`, `letter-spacing: -0.0125em` |
| h1 (`#content h1`) | 36px | 500 | `#8E6747` | `margin: 1.5em 0 0.5em` |
| h1 (`.documentFirstHeading`) | 36px | 500 | `#8E6747` | `margin: 1em 0 0.5em` |
| h2 | 30px | 500 | `#8E6747` | |
| h3 | 24px | 500 | `#8E6747` | `margin-bottom: .5em; margin-top: 1em` |
| h1 mobile (<600px) | 30px | - | - | `line-height: 1.2em` |

### Body Text
| Element | Size | Color | Line Height |
|---------|------|-------|-------------|
| `p` | 16px | `#444` | 1.6em |
| `body` | default | - | 1.5em |
| `.intro` | 20px | `#676767` | 1.5em |
| `.introtext` | 16px | `#444` | 1.5em, weight: 600 |
| `.smaller` | 14px | - | - |
| `#content li` | 1.2em | `#444` | 1.5em |
| `.documentDescription` | 1.35em | - | 1.5em, `font-family: 'Montserrat'`, weight: 500 |

### Special Text Styles
| Class | Size | Color | Other |
|-------|------|-------|-------|
| `.heading-gold` | 2.6em | `#f7d25b` | `letter-spacing: -0.025em`, `line-height: 2.3rem` |
| `.heading-white` | 2.7em | `#fff` | weight: 600, `Montserrat`, uppercase |
| `.heading-large` | 2.3em | - | `margin: 1em 0 0.5em` |
| `.subhead` (orange block) | 14px | `#b5700f` | `Montserrat`, `letter-spacing: 4px`, weight: 600 |
| `.subhead` (blue block) | 14px | `#D0F7FF` | `Montserrat`, `letter-spacing: 4px`, weight: 600 |
| `.popquote` | 1.5em | `#205c90` | `Merriweather`, italic, `line-height: 1.4em` |
| `.slogan` | 22px | - | italic, `line-height: 1.5em` |
| `.lead` | 115% | - | `line-height: 1.4em` |

---

## Layout & Structure

### Page Width
| Element | Width |
|---------|-------|
| `#visual-portal-wrapper` | `max-width: 1170px`, centered |
| `.narrow` | `width: 1170px`, centered |
| `.inner-container` | `width: 1170px`, centered |
| `#portal-header` | `width: 1170px`, centered |

### Header
| Property | Value |
|----------|-------|
| Height | 215px |
| Background | transparent |
| Logo margin | `70px 20px 20px` |
| Mobile header height (<768px) | 185px |
| Mobile logo position | `absolute; top: 30px; left: 10px` |
| Mobile logo width | 295px |

### Portal Banner
| Property | Value |
|----------|-------|
| Height | 350px |
| Background size | cover |
| Background color | `#efefef` (default), `#f6f3ed` (overridden) |
| Full-bleed | `width: 100vw; margin-left: -50vw; left: 50%` |
| Mobile height (<768px) | 130px |
| WLFW home | Hidden (`display: none`) via `.site-working-lands-for-wildlife #portal-banner` |

### Content Area
| Property | Value |
|----------|-------|
| `#portal-column-two` | `margin-top: 2em` |
| Breadcrumbs | `margin-left: 0; font-size: 12px; padding: 10px 20px` |
| Edit bar | `margin-left: 1.5em; margin-right: 1.5em; height: 32px; background: #75ad0a` |

### WLFW Home Template
- `#visual-portal-wrapper` set to `max-width: 100%` (full width)
- `#content` set to `width: 100%; padding-bottom: 0`
- Portal banner, breadcrumbs, edit bar, addthis toolbox all hidden
- CSS selectors: `.template-wlfw_home_test`, `.template-wlfw_home`

### Slideshow (Homepage)
| Property | Value |
|----------|-------|
| `.feature-slide` | `height: 600px; overflow: hidden; position: relative` |
| `.feature-slide img` | `object-fit: cover; height: 100%` |
| `.slide-overlay-wlfw` | `position: absolute; top: 13%; width: 50%; left: 25%; background: rgba(0,0,0,0.6); border-radius: 6px; text-align: center; padding: 30px 30px 40px` |
| Mobile (<768px) | `height: 460px; overlay width: 90%; left: 5%` |

---

## Navigation

### Main Nav (`#portal-globalnav`)
| Property | Value |
|----------|-------|
| Background | `#657F9E` |
| Position | `absolute; top: 0; width: 100%` |
| Display | `flex; justify-content: center` |
| Border top | `1px solid white` |
| Font | `'Source Sans Pro', sans-serif` |
| Font size | 18px |
| Font weight | 400 |
| Link padding | 14px |
| Link color | `#fff` |
| Hover bg | `#4C6C8C` |
| Hover color | `#fff` |
| Selected bg | `#95A664` (green) |
| Selected color | White |

### Home Icon
- Uses background image `menu-home-white.png` at `center 15px`
- `text-indent: -999em` (hides text)

### Submenu Dropdowns
| Property | Value |
|----------|-------|
| Background | `#efefef` |
| Text color | `#333333` |
| Width | 230px |
| Position | absolute, `left: -999em` (hidden), `left: auto` on hover |
| Box shadow | `0px 0px 5px #666` |
| Hover bg | `#7d9cc0` |
| Hover color | `#fff` |
| Font size | 11px |
| Nested submenu | `margin: -4px 0 0 228px` |

### Mobile Nav (<768px)
- Nav hidden by default (`display: none`)
- Toggled by `.menu-toggle` button
- Toggle button: `background: black url('menu-toggle.png') 10px center no-repeat; color: white`
- Nav items: `width: 100%`
- Submenus: `position: relative; width: 100%`

### WLFW-Specific Nav Elements
| Element | Default State | Notes |
|---------|---------------|-------|
| `.wlfw-nav-bar` | `display: none` | Return link nav bar |
| `.wlfw-navigation-bar` | `display: none` | WLFW logo nav bar |
| `.wlfw-biome-nav-bar` | `display: none` | Biome nav bar |
| `.nest-navigation-bar` | `display: none` | Sub-site return link bar, bg: `#405D68` |

### Nav Tab IDs
- `#portaltab-home` - Home
- `#portaltab-about-us` - About
- `#portaltab-landscapes-wildlife` - Landscapes & Wildlife
- `#portaltab-science` - Science
- `#portaltab-wlfw-news` - News
- `#portaltab-get-involved` - Get Involved

### Target Species Dropdown (`.tgt-species`)
- Hidden by default, shown on species sub-pages
- Float right, font-size 13px, font-family `'montserrat'`
- Dropdown bg: `#f3f3f3`, box-shadow: `0px 0px 10px rgba(0,0,0,.25)`
- Link color: `#3390aa`, hover: `#205c90`

### Landscape Biome Dropdown (`.landscape-biome-menu`)
- Hidden by default, shown on biome sub-pages (Grasslands, Aquatics, etc.)
- Similar styling to tgt-species
- Positioned absolute top: 2px, right: 20px, z-index: 25

---

## Buttons

### `.cta-button`
| Property | Value |
|----------|-------|
| Padding | `15px 25px` |
| Background | `#f7bd4f` |
| Hover bg | `#f38b1a` |
| Font size | 20px |
| Border radius | 5px |
| Border | `1px solid #fff` |
| Text | `#fff`, `'Montserrat'`, weight: 600 |

### `.btn-orange`
| Property | Value |
|----------|-------|
| Background | `#f8903e` |
| Hover bg | `#F7700D` |
| Padding | `10px 15px` |
| Border | `1px solid #fff` |
| Border radius | 5px |
| Font size | 13px |
| Font weight | 600 |
| Text color | `#fff` |

### `.btn-orange-large`
Same as `.btn-orange` but `font-size: 18px`, `display: inline-block`

### `a.large-orange`
| Property | Value |
|----------|-------|
| Background | `#f8903e` |
| Hover bg | `#F7700D` |
| Padding | 15px |
| Border | `1px solid #fff` |
| Border radius | 4px |
| Font size | 14px |
| Font weight | 600 |
| Text transform | uppercase |
| Letter spacing | 0.075em |

### `.btn-grey`
| Property | Value |
|----------|-------|
| Background | `#e6e6e6` |
| Hover bg | `#F8903E` (orange) |
| Hover color | `#fff` |
| Color | `#515151` |
| Font size | 14px |
| Text transform | uppercase |
| Border radius | 4px |

### `.btn-red`
| Property | Value |
|----------|-------|
| Background | `#FF6633` |
| Padding | `10px 15px` |
| Border radius | 5px |
| Font size | 18px |

### `.btn-blue`
| Property | Value |
|----------|-------|
| Background | `#0e71eb` |
| Hover bg | `#1a5cbb` |
| Color | `#fff` |
| Padding | `8px 15px` |
| Border radius | 8px |

### `a.overlay-btn`
| Property | Value |
|----------|-------|
| Background | `rgba(0, 0, 0, 0.5)` |
| Hover bg | `rgba(0, 0, 0, 0.6)` |
| Color | `#fafafa` |
| Font size | 20px |
| Font weight | 600 |
| Border radius | `0 0 5px 5px` |

### `a.overlay-btn-2`
| Property | Value |
|----------|-------|
| Background | `rgba(0, 0, 0, 0.5)` |
| Hover bg | `rgba(255, 255, 255, 1)` |
| Border | `1px solid #fff` |
| Font size | 1.3em |
| Padding | 15px |
| Border radius | 6px |
| Color | `#fff`, hover: `#222` |

### `a.overlay-btn-3`
| Property | Value |
|----------|-------|
| Background | `rgba(0, 0, 0, 0.35)` |
| Hover bg | `rgba(0, 0, 0, 0.75)` |
| Font size | 1.3em |
| Border radius | `0 0 6px 6px` |
| Hover color | `#f7c60e` |
| Width | 100% |

### `.button-dark`
| Property | Value |
|----------|-------|
| Background | `#274352` |
| Hover bg | `#132631` |
| Color | `#eaea8b` |
| Hover color | `#fb9a1e` |
| Padding | `15px 25px` |
| Border radius | 5px |
| Font size | 18px |

### `.more-link`
| Property | Value |
|----------|-------|
| Background | `url(orange-arrow.svg) no-repeat right center` |
| Font size | 13px |
| Font weight | 600 |
| Text transform | uppercase |
| Padding | `3px 18px 3px 3px` |
| Text align | right |

---

## Content Blocks

### `.white-block`
Background: `#fff`, padding: 30px

### `.grey-block`
Background: `#efefef`, padding: 30px, links have no border-bottom

### `.orange-block`
Background: `#ef9b26`, padding: 50px, min-height: 400px, text: `#fff`

### `.blue-block`
Background: `rgba(20 83 120 / 80%)`, padding: `50px 30px`, min-height: 400px

### `.black-65-block`
Background: `rgb(0 0 0 / 65%)`, padding: 40px

### `.black-50-block`
Background: `rgb(0 0 0 / 50%)`, padding: 40px

### `.overlay-block`
Background: `rgba(0 0 0 / 50%)`, padding: 30px

### `.tan-block`
Background: `#e7e5da`, padding: 2rem, border-radius: 6px

### `.centered-block`
Display: grid, align-items: center, justify-items: center

### `.flex-block`
Display: flex, align-items: center. Mobile (<767px): `flex-direction: column`

### `.block-w-border`
`margin: 2rem auto; padding: 1rem 2rem; border: 4px solid #d5d5d5`

### `.feature-block`
Border: `6px solid #efefef`, padding: 30px, background: `#fff`, h3 color: `#dd733e`

### `#cta-block`
Full-bleed block: `background-color: #28526E; height: 120px`, grid centered

### Background Image Blocks (WLFW)
| Class | Image | Min-height |
|-------|-------|------------|
| `.bg-warbler` | `working-lands/warbler-photo.jpg` | 230px |
| `.bg-ranchers` | `working-lands/ranchers-wlfw.jpg` | 200px |
| `.bg-resources` | `working-lands/unsplash-mockup.jpg` | 200px |
| `.bg-grasslands` | `working-lands/east-central-grasslands.jpg` | 300px |
| `.bg-grasslands-sunset` | `working-lands/grasslands.jpg` | 300px |
| `.bg-aquatics` | `working-lands/aquatic-corridors.jpeg` | 300px |
| `.bg-forest` | `working-lands/deciduous-forest.jpeg` | 300px |
| `.bg-western-wlfw` | `working-lands/western-wlfw.jpeg` | 300px |

---

## Grid Layouts

### Float-based Columns
| Class | Width | Margin-right |
|-------|-------|-------------|
| `.span3` | 23.15% | 1.65% |
| `.span4` | 31.6239% | 1.65% |
| `.span6` | 47.75% | 1.65% |
| `.span8` | 66.6667% | - |
| `.span9` | 74.4681% | - |
| `.five-column` | 18% | 1.65% |

### CSS Grid Layouts
| Class | Columns | Gap |
|-------|---------|-----|
| `.grid-container-2col` | `50% 1fr` | 30px |
| `.grid-container-3col` | `repeat(3, minmax(0, 1fr))` | 30px |
| `.grid-container-4col` | `repeat(4, minmax(0, 1fr))` | - |
| `.grid-container-4col-w-gap` | `repeat(4, 1fr)` | 30px |
| `.grid-container-5col` | `repeat(5, 1fr)` | 20px |
| `.grid-container-6col` | `repeat(6, 1fr)` | 20px |
| `.grid-container-65-35` | `65% 1fr` | 30px |
| `.grid-container-30-70` | `30% auto` | - |
| `.grid-container-70-30` | `70% auto` | - |
| `.grid-container-three-quarter` | `75% 1fr` | 30px |

### Gap Utilities
| Class | Gap |
|-------|-----|
| `.gap` | 30px |
| `.gap10` | 10px |
| `.gap15` | 15px |
| `.gap20` | 20px |
| `.gap30` | 30px |

---

## Footer

### Main LP Footer (`#portal-footer`)
| Property | Value |
|----------|-------|
| Background | `#2e76a0` |
| Color | `#fff` |
| Padding | 1.5em |
| h3 color | `#aae2fd` |
| h3 font-size | 20px |
| h3 text-transform | uppercase |
| Footer link color | `#fff` |
| Footer link size | 15px |
| Footer link hover | `border-bottom: 1px solid #fff` |
| Site credit color | `#aae2fd` |
| Site credit link color | `#7dd4d6` |
| Site credit link hover | `#ffffff` |

### WLFW Footer (`#portal-footer-wlfw`)
| Property | Value |
|----------|-------|
| Default display | `none` (hidden globally, toggled on by template) |
| h3 color | `#fff` |
| h3 border-bottom | `1px solid #ebebeb` |
| h3 letter-spacing | 2px |
| h3 font-size | 1.5rem |
| Bottom nav | `display: flex; align-items: center; justify-content: space-between` |
| Bottom nav mobile | `flex-direction: column; text-align: center` |
| ft-menu color | `#fff; text-align: center` |
| EEO statement | `font-size: .75rem; line-height: 1.4em` |
| Site credit | Same as LP footer but with 36px background-size |

### WLFW Footer Structure (from HTML)
```
#portal-footer-wlfw
  .narrow
    .bottom-nav
      .grid.center-mobile  -> WLFW logo + LP logo
      .grid.center-mobile  -> h3 "BROWSE" + ul.ft-menu.twocolumn (8 links)
                              .sitecredit
      .grid.center-mobile  -> USDA-NRCS logo + EEO statement + Register/Login
```

---

## Spacing Utilities

| Class | Value |
|-------|-------|
| `.space` | `height: 25px` |
| `.space10` | `height: 10px` |
| `.space15` | `height: 15px` |
| `.space20` | `height: 20px` |
| `.space30` | `height: 30px` |
| `.space-left` | `margin-left: 2em` |
| `.space-right` | `margin-right: 2em` |
| `.space-btm` | `padding-bottom: 10px` |
| `.space-top-bottom` | `margin: 2em auto` |
| `.pad10` | `padding: 10px` |
| `.pad20` | `padding: 20px` |
| `.pad30` | `padding: 30px` |
| `.pad40` | `padding: 40px` |

---

## Responsive Breakpoints

| Breakpoint | Usage |
|------------|-------|
| `max-width: 1170px` | Header and `.narrow` go `width: 100%` |
| `max-width: 979px` | Slide overlays reposition (`width: 70%; left: 15%`) |
| `max-width: 768px` | **Major mobile breakpoint**: nav hidden/toggled, columns go full-width, header height 185px, banner height 130px, feature-slide height 460px, grids collapse to single column |
| `max-width: 767px` | Orange/blue blocks reduce padding, flex-blocks go column, heading sizes reduce |
| `max-width: 600px` | h1 reduces to 30px, `.about` section adjusts |
| `max-width: 500px` | News images go full-width |
| `max-width: 420px` | Featured images go non-float |
| `min-device-width: 320px` / `max-device-width: 480px` | Smartphone (empty) |
| `min-device-width: 768px` / `max-device-width: 1024px` | iPad (empty) |

---

## Image Styles

| Class | Styles |
|-------|--------|
| `.styled-img` | `border-radius: 4px; box-shadow: 0 0 5px 0 rgba(0,0,0,0.1); max-width: 100%` |
| `.responsive-img` | `border: 1px solid #ccc; max-width: 100%; padding: 4px; border-radius: 4px; box-shadow` |
| `.img-responsive` | `border-radius: 4px; max-width: 100%` |
| `.circle-img` | `border-radius: 100%` |
| `.image-circle` | `border-radius: 50%` |
| `.image-fit` | `object-fit: cover` |
| `.tileImage img` | `width: 250px; height: auto` |
| `.gridImage img` | `width: 100%; height: 220px; object-fit: cover` |

---

## Material Icons

| Class | Size | Color |
|-------|------|-------|
| `.material-icons` | 90px | `#fff` |
| `.material-icons-40` | 40px | `#fff` |
| `.material-icons-black` | 68px | `#9d9d9d` |
| `.material-icons-grey` | 68px | `#9d9d9d` |
| `.material-icons-small` | 40px | `#9d9d9d` |
| `.material-icons-gold` | 48px | `#f8cf95` |
| `.material-icons-gold-circle` | 60px | `#fff`, bg: `#efe48d`, 70px circle |

### Circle Icon Buttons
| Class | Border | Hover |
|-------|--------|-------|
| `.circle-icon` | `3px solid #fff`, 50%, padding: 10px | bg: `#f19023` |
| `.circle-icon-left` | `3px solid #fff`, 50%, padding: 4px | bg: `#f19023` |

---

## CSS Files Downloaded

| File | Description |
|------|-------------|
| `css/ploneCustom.css` | Main custom stylesheet (7596 lines) - all site-wide and WLFW-specific styles |
| `css/base.css` | Plone base content styles (1119 lines) |
| `css/dropdown-menu.css` | Navigation dropdown positioning (102 lines) |
| `css/reset.css` | CSS reset (23 lines) |
| `css/mobile.css` | Mobile device overrides (66 lines) |
| `css/jquery-tokeninput.css` | jQuery token input widget |
| `css/dateinput.css` | jQuery tools date input |
| `css/fullcalendar.css` | Full calendar component |
| `css/truegallery-portlet.css` | Gallery portlet styles |
| `css/ploneboard.css` | Forum/message board styles |

---

## Key Differences from Aquatics Sub-site

The WLFW sub-site shares the global Landscape Partnership CSS (ploneCustom.css) and does NOT have its own dedicated sub-site CSS file. Instead, it relies on:

1. **Body class**: `site-working-lands-for-wildlife` - used to hide the portal banner
2. **Template class**: `template-wlfw_home` - used to make the homepage full-width and hide various UI elements
3. **WLFW Footer**: `#portal-footer-wlfw` - hidden globally, toggled on per-template (the toggle CSS for enabling it is NOT in ploneCustom.css, suggesting it's done via template-level logic or additional inline styles)
4. **Nav bar elements**: `.wlfw-nav-bar`, `.wlfw-navigation-bar`, `.wlfw-biome-nav-bar` - all hidden by default
5. **Slide overlay**: `.slide-overlay-wlfw` - specific positioning for WLFW homepage carousel

The WLFW sub-site uses the same blue-grey (`#657F9E`) navigation, the same brown (`#8E6747`) headings, and the same orange (`#f8903e`) button accents as the main Landscape Partnership site. There is no separate teal/dark green color scheme like the Aquatics sub-site uses.

---

## Notable WLFW HTML Structure

### Body Classes
```
template-wlfw_home portaltype-folder site-working-lands-for-wildlife userrole-anonymous content-working-lands-for-wildlife
```

### Nav Tabs (Secondary Nav)
```
Home | About (with submenu: Partners, Community Search, Where We Work) | Landscapes & Wildlife (with deep submenus) | Science (with submenus) | News (Events, Stories, Newsletters) | Get Involved (with submenus)
```

### Homepage Sections
1. Feature slideshow (jQuery Cycle, fade transitions, 8s intervals)
2. Landscape blocks (Grasslands, Aquatics, Eastern Forests, Western Landscapes) with background images
3. Focus species cards (topic-wrapper with hover overlays)
4. Conservation tools section (Bobscapes, Literature Gateway, BirdLocale, SE FireMap)
5. News grid
6. Resources library
7. Videos and webinars
8. WLFW footer with logos + browse links + USDA credit
