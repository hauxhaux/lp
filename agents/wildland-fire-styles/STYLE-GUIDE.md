# Wildland Fire Sub-site Style Guide

**Source URL:** https://dev.landscapepartnership.org/networks/working-lands-for-wildlife/wildland-fire
**Sub-site CSS file:** `fire.css` (16,497 bytes)
**Body class:** `site-wildland-fire`
**Template class (home):** `template-fire_home`

---

## Page Inventory

| # | Page | URL Path (relative to base) | File |
|---|------|----------------------------|------|
| 1 | Home | `/` | `html/01-home.html` |
| 2 | About | `/about` | `html/02-about.html` |
| 3 | Fire Mapping | `/fire-mapping` | `html/03-fire-mapping.html` |
| 4 | Prescribed Burning | `/prescribed-burning` | `html/04-prescribed-burning.html` |
| 5 | Wildfire | `/wildfire` | `html/05-wildfire.html` |
| 6 | Policies | `/policies` | `html/06-policies.html` |
| 7 | Resources | `/resources` | `html/07-resources.html` |
| 8 | Training | `/training` | `html/08-training.html` |
| 9 | News & Events | `/news-and-events` | `html/09-news-and-events.html` |

**Base URL:** `https://dev.landscapepartnership.org/networks/working-lands-for-wildlife/wildland-fire`

---

## Color Palette

### CSS Custom Properties (defined in fire.css `:root`)

| Variable | Hex | Usage |
|----------|-----|-------|
| `--heading` | `#205c90` | Headings (h1 first heading), `.bg-blue` blocks, portlet headers |
| `--brown` | `#A26623` | H1/H2/H3/H4/H5/H6 headings, `.bg-brown` blocks |
| `--green` | `#788a3b` | Nest navigation bar background, `.bg-green` blocks |
| `--orange` | `#ef8f39` | `.bg-orange` blocks |
| `--redorange` | `#e86129` | `.bg-red-orange` blocks |
| `--tan` | `#dfdf9e` | Selected nav tab background, `.bg-tan` blocks |
| `--footer` | `#7d6042` | Footer background, `.bg-footer` blocks |
| `--lightbrown` | `#dacfbb` | Footer heading color, `.bg-ltbrown` blocks |
| `--grey` | `#f5f5f5` | `.bg-grey` blocks |

### Additional Colors (hardcoded in fire.css)

| Hex | Usage |
|-----|-------|
| `#0E1D1C` | Main nav background (`#globalnav-wrapper`, `#portal-globalnav`, nav link bg) |
| `#DFDF9E` | Selected nav tab background |
| `#84984c` | Nav hover background |
| `#222` | Selected nav tab text color |
| `#666` | Body text color (paragraphs) |
| `#676767` | `.intro` text, `.dark-grey` styleguide swatch |
| `#777` | Caption text |
| `#dbcfbc` | Footer link color |
| `#f4a221` | Footer link hover color |
| `#F59E20` | `.btn-solid-orange` background |
| `#e64c00` | Button hover background |
| `#f7931e` | `.readmore` hover color |
| `#f7931f` | `.orange` styleguide swatch |
| `#EA8206` | `.add-fire-resources h3` color, `.planning-support-btn h3` color |
| `#EBEBC2` | `.add-fire-resources` background |
| `#F2F2B0` | `.add-fire-resources:hover` background |
| `#84B3B3` | Edit bar background |
| `#eae493` | Firemap portlet background |
| `#54585b` | `.button` text color |
| `#888` | `.button` border color |
| `#ddd` | Portlet border |
| `#ededed` | Banner default background color |
| `#f6d514` | Cyclist (carousel) h2 color |

### Colors from ploneCustom.css (global, inherited)

| Hex | Usage |
|-----|-------|
| `#657F9E` | Default globalnav wrapper bg (overridden by fire.css to `#0E1D1C`) |
| `#4C6C8C` | Default nav hover (overridden by fire.css to `#84984c`) |
| `#95A664` | Default selected nav tab bg (overridden by fire.css to `#DFDF9E`) |
| `#efefef` | Submenu background |
| `#7d9cc0` | Submenu hover background |
| `#2e76a0` | Default portal footer bg (overridden by fire.css to `#7d6042`) |
| `#205C90` | Breadcrumb link color |

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

### Font Stacks by Element

| Element | Font Family | Weight | Size | Color | Other |
|---------|-------------|--------|------|-------|-------|
| `body` (global) | `'Open Sans', sans-serif` | — | — | — | Set in ploneCustom.css |
| `h1.documentFirstHeading` | `'Montserrat', sans-serif` | 500 | 2.6em | `#A26623` | `margin-top: 1.5em; margin-bottom: 0.5em` |
| `h1` | `'Montserrat', sans-serif` | 500 | 2.6em | `#A26623` | Same as above |
| `h2, h3, h4, h5, h6` | `'Montserrat', sans-serif` | 600 | — | `#A26623` | `line-height: 1.5em; letter-spacing: -0.0115em` |
| `p` | `'Merriweather', serif` | — | — | `#666` | `letter-spacing: 0.01em; line-height: 1.6em; padding-bottom: 15px` |
| `.intro` | `'Merriweather', serif` | — | 17px | `#676767` | `line-height: 1.7em; margin: 1em 0em` |
| Nav links | `'Source Sans Pro', sans-serif` | 400 | 16px (fire.css) / 18px (ploneCustom) | `#fff` | — |
| Nest nav bar | `'Montserrat'` | 600 | 12px | — | `text-transform: uppercase; letter-spacing: 1px` |
| Portlet headers | `'Montserrat', sans-serif` | — | 17px | `#666` | — |
| `.button` | `'Open Sans', Arial, sans-serif` | 700 | 1.125rem | `#54585b` | — |
| `.readmore` | `'Source Sans Pro', sans-serif` | 600 | 13px | — | `text-transform: uppercase` |
| `.caption` | — | — | 13px | `#777` | — |

---

## Layout & Structure

### Page Dimensions

| Element | Value |
|---------|-------|
| `#visual-portal-wrapper` max-width | `100%` |
| `#portal-columns` width | `1170px`, centered (`margin: 0 auto`) |
| `#portal-top` height | `164px` (desktop), `130px` (mobile) |
| `#portal-header` height | `130px` |
| `.narrow` (content wrapper) | `1170px` (from ploneCustom) |
| Home page `#content` | `width: 100%` |
| Home page `#portal-columns` | `width: 100%` |

### Banner Images

| Element | Height | Notes |
|---------|--------|-------|
| `.site-wildland-fire #portal-banner` | `300px` (desktop), `100px` (mobile) | `top: 22px; background-size: cover; background-position: center` |
| Home page banner | Hidden (`display: none !important`) | Uses cyclist/carousel instead |

### Section-specific Banner Images

| Section | Image File |
|---------|-----------|
| Prescribed Burning | `fire-images/fire-banner.jpg` |
| Wildfire | `fire-images/rx-fire-banner.jpg` |
| Fire Mapping | `fire-images/firemapping-gold-banner.jpg` |
| Training | `fire-images/longleaf-FB-group.jpg` |
| Policies | `fire-images/LongleafFire__1537797395957.jpg` |
| Research | `fire-images/SERX-firewalk.jpg` |
| Partners | `fire-images/LLFB-group-woods.jpg` |
| News & Events | `fire-images/firemap-banner.jpg` |
| About | `fire-images/sunset-through-the-smoke.jpg` (bg-position: center bottom) |
| Workspace | `fire-images/longleafFB-butterfly.jpg` |
| Apps Maps Data | `fire-images/mapviewer-bg.jpg` |
| Style Guide | `landscape-images/style-guide-banner.jpg` |

---

## Navigation

### Top-Level "Nest" Navigation Bar

```css
.nest-navigation-bar {
  display: block;
  background: #788a3b;         /* --green */
  padding: 10px 30px;          /* mobile: 5px 0 */
  font-weight: 600;
  font-size: 12px;
  letter-spacing: 1px;
  text-transform: uppercase;
  font-family: 'Montserrat';
}
```

Contains:
- "Return to Landscape Partnership Site" link (white, arrow-left icon)
- "Navigate Target Species" dropdown
- "Companion Sites" dropdown

### Main Navigation (`#globalnav-wrapper`)

```css
#globalnav-wrapper {
  background-color: #0E1D1C;    /* very dark green-black */
  border-top: 1px solid white;
  top: 135px;                    /* positioned below header */
}
```

### Nav Link States

| State | Background | Text Color |
|-------|-----------|------------|
| Default | `#0E1D1C` | `#fff` |
| Hover | `#84984c` (olive green) | `#fff` |
| Selected | `#DFDF9E` (tan/gold) | `#222` |
| Selected + Hover | `#84984c` | `#fff` |

### Nav Link Styles

```css
#portal-globalnav li a {
  background-color: #0E1D1C;
  font-size: 16px;
  /* Inherited from ploneCustom: font-family: 'Source Sans Pro'; padding: 14px */
}
```

### Submenu/Dropdown Styles (from ploneCustom.css, inherited)

| Property | Value |
|----------|-------|
| Dropdown width | `230px` |
| Background | `#efefef` |
| Text color | `#333` |
| Hover background | `#7d9cc0` |
| Hover text | `#fff` |
| Box shadow | `0px 0px 5px #666` |
| Sub-sub-menu offset | `margin: -4px 0 0 228px` |
| Font size | `11px` (submenu items) |

### Nav Tabs (8 items)

1. Home (`#portaltab-homelink`)
2. About (`#portaltab-about`)
3. Fire Mapping (`#portaltab-fire-mapping`)
4. Prescribed Burning (`#portaltab-prescribed-burning`)
5. Wildfire (`#portaltab-wildfire`)
6. Policies (`#portaltab-policies`)
7. Resources (`#portaltab-resources`)
8. Training (`#portaltab-training`)
9. News & Events (`#portaltab-news-and-events`)

---

## Buttons

### `.button` (default outline button)

```css
.button {
  color: #54585b;
  font-size: 1.125rem;
  padding: .75rem 1rem;
  border: 1px solid #888;
  border-radius: 0.25rem;
  font-weight: 700;
  font-family: "Open Sans", Arial, sans-serif;
  box-shadow: 2px 3px 5px -1px rgba(0,0,0,0.35);
  transition: background .2s linear, color .2s linear, border-color .2s linear;
}
.button:hover {
  background: #e64c00;
  color: #fff;
  border-color: transparent;
}
```

### `.btn-solid-orange`

```css
.btn-solid-orange {
  color: #fff;
  background: #F59E20;
  border-color: transparent;
}
.btn-solid-orange:hover {
  background: #e64c00;
  color: #fff;
}
```

### `.btn-orange` (used in carousel slides)

Referenced in HTML as `<a class="btn-orange small">` -- styled via ploneCustom.css global styles.

### `.readmore` link

```css
a.readmore {
  font-size: 13px;
  font-weight: 600;
  text-transform: uppercase;
  font-family: 'Source Sans Pro', sans-serif;
}
a.readmore:hover {
  color: #f7931e;
}
```

---

## Content Blocks & Components

### Slide Overlay (Hero Carousel)

```css
.slide-overlay {
  position: absolute;
  z-index: 5;
  top: 35%;                    /* mobile: 25% */
  background: rgba(0,0,0,0.6); /* mobile: 0.45 */
  padding: 30px 30px 40px;
  width: 70%;                  /* mobile: 100% */
  left: 15%;                   /* mobile: 0 */
  color: #fff;
  border-radius: 6px;          /* mobile: 0 */
  text-align: center;
}
```

### Background Color Utility Classes

| Class | Background |
|-------|-----------|
| `.bg-brown` | `#A26623` |
| `.bg-green` | `#788a3b` |
| `.bg-ltbrown` | `#dacfbb` |
| `.bg-tan` | `#dfdf9e` |
| `.bg-orange` | `#ef8f39` |
| `.bg-blue` | `#205c90` |
| `.bg-footer` | `#7d6042` |
| `.bg-grey` | `#f5f5f5` |
| `.bg-red-orange` | `#e86129` |

### Add Resource / Planning Support Buttons (CTA blocks)

```css
.add-fire-resources {
  padding: 20px 10px 15px 80px;
  margin: 2em 0;
  background: #EBEBC2 url(fire-images/add-resource-fire.png) no-repeat;
  background-size: 60px;
  border: 1px solid #ccc;
  border-radius: 8px;
  transition: all 0.2s ease-in-out;
}
.add-fire-resources:hover {
  background: #F2F2B0 url(fire-images/add-resource-fire.png) no-repeat;
  background-size: 63px;
}
.add-fire-resources h3 { color: #EA8206; font-size: 18px; font-weight: 600; }
.add-fire-resources p { font-size: 13px; font-style: italic; }
```

### Portlets (Sidebar)

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
.portletNavigationTree .portletHeader {
  background: #205C90;
  border-radius: 4px 4px 0 0;
  text-transform: uppercase;
  padding: 15px;
}
```

### Company Logos (grayscale effect)

```css
.company-logo img {
  filter: grayscale(100%);
  transform: scale(0.95);
  opacity: 0.35;
  transition: all .4s ease;
  margin: 12px;
  width: 150px;
}
```

### Carousel (Cyclist)

- Full-width wrapper: `#cyclist-wrapper-full` (`width: 100%`)
- Feature images: `background-size: cover; background-position: center center`
- Carousel h2 color: `#f6d514` (gold/yellow)
- Carousel p: `font-size: 18px; color: #ededed`
- Dot nav uses `square.png` / `square-active.png` images
- Uses jQuery Cycle plugin (fade transition, 8000ms timeout)

---

## Footer

### Wildland Fire Footer (`#fire-footer`)

```css
#fire-footer {
  display: block;
  position: relative;
  text-align: center;
}
```

**Note:** The global ploneCustom.css hides `#fire-footer` by default (`display: none`). The sub-site's `fire.css` overrides this to show it.

### Footer Wrapper

```css
#portal-footer-wrapper {
  margin-top: 5em;
  background: #7d6042;          /* --footer brown */
}
#portal-footer {
  background: #7d6042;
  height: 350px;
}
```

### Footer Links

```css
#fire-footer a:link, #fire-footer a:visited { color: #dbcfbc; }
#fire-footer a:hover { color: #f4a221; }
```

### Footer Headings

```css
#fire-footer h4 {
  margin-top: 20px;
  color: #dacfbb;               /* --lightbrown */
  text-transform: uppercase;
  padding: 30px 0 0;
}
```

### Footer Navigation (`.bottom-nav`)

```css
.bottom-nav {
  text-align: left;
  margin: 20px 0;
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  padding-top: 20px;
  gap: 15px;
}
/* Mobile: flex-direction: column; align-items: center; text-align: center */
```

### Footer Menu (`ul.ft-menu`)

From ploneCustom.css:
```css
#portal-footer ul.ft-menu {
  list-style: none;
  padding: 0;
  margin: 0;
}
.ft-menu li a {
  color: #fff;
  font-size: 14px;
}
.ft-menu li a:hover {
  color: #f4a221;
}
```

### Site Credit

```css
#fire-footer .sitecredit {
  background: url(fergusonlynch-icon.png) no-repeat scroll 0 2px transparent;
  background-size: 36px;
  font-size: 13px;
  letter-spacing: 0.05em;
  line-height: 1.1rem;
  padding-left: 52px;
  text-transform: uppercase;
  width: 185px;
  margin: 6px auto;
}
```

### Footer Contributors (logos)

The footer shows logos for: WLFW, USDA, The Longleaf Alliance, U.S. Endowment for Forestry & Communities, SERPPAS, America's Longleaf Restoration Initiative, NC State, Tall Timbers.

```css
#fire-footer img { margin: 0 15px 10px; }
```

---

## Responsive Breakpoints

All `@media` rules found in `fire.css`:

| Breakpoint | Elements Affected |
|-----------|-------------------|
| `max-width: 600px` | `#portal-logo` position/size |
| `max-width: 767px` | `.bottom-nav` (column layout), `.narrow h2`, `.grid-item` padding |
| `max-width: 768px` | `#portal-top` height, `#portal-columns` width, `#portal-banner` height, `#globalnav-wrapper` position, `.LSBox` positioning, `.nest-navigation-bar` padding, `.slide-overlay` sizing, `.news-image img` sizing |

From ploneCustom.css (inherited):

| Breakpoint | Elements Affected |
|-----------|-------------------|
| `max-width: 1170px` | `#portal-header` and `.narrow` width: 100% |
| `max-width: 768px` | Mobile nav (hamburger toggle), `#portal-globalnav` hidden/toggle, `#portal-header` height, `#globalnav-wrapper` margin, `#portal-logo` position, submenu positioning |

---

## Other CSS Files Downloaded

| File | Size | Purpose |
|------|------|---------|
| `fire.css` | 16,497B | **Sub-site specific** -- all custom styles |
| `cyclist.css` | 3,176B | Carousel/slider styles |
| `ploneCustom.css` | 130,516B | Global portal customizations (nav, footer, layout) |
| `base.css` | 70,023B | Plone base styles |
| `reset.css` | 483B | CSS reset |
| `dropdown-menu.css` | 2,110B | Nav dropdown positioning logic |
| `mobile.css` | 1,107B | Mobile-specific overrides |
| `slick.css` | 4,134B | Slick carousel library |
| `jquery-ui.css` | 8,746B | jQuery UI widgets |
| `fullcalendar.css` | 22,332B | Calendar widget |
| `truegallery.css` | 22,270B | Gallery portlet |
| `ploneboard.css` | 3,824B | Discussion board |
| `dateinput.css` | 2,410B | Date input widget |
| `contentleadimage.css` | 308B | Lead image styling |
| `tinymce.css` | 858B | TinyMCE editor |
| `print.css` | 2,490B | Print stylesheet |

---

## External Resources

### Font Awesome
```html
<link href="//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css" rel="stylesheet" />
```

### Slick Carousel
```html
<link rel="stylesheet" href="//cdn.jsdelivr.net/jquery.slick/1.3.15/slick.css" />
```

---

## Key Structural Notes

1. **Multiple footers exist** in the HTML (WLFW, Bobscapes, BirdLocale, Wildland Fire, SE FireMap, Literature Gateway). Only the Wildland Fire footer (`#fire-footer`) is shown; others are hidden via `display: none` in ploneCustom.css.

2. **Multiple nav bars exist** in the HTML (`.wildlandfire-nav-bar`, `.bobscapes-nav-bar`, `.wlfw-nav-bar`, `.wlfw-biome-nav-bar`, `.sefire-nav-bar`, `.gateway-nav-bar`). All are hidden via ploneCustom.css. The visible nav elements are `.nest-navigation-bar` and `#globalnav-wrapper`.

3. **The home page** uses a jQuery Cycle carousel (`#cyclist`) with slide overlays. Interior pages use a `#portal-banner` with section-specific background images (300px desktop, 100px mobile).

4. **Logo** is an image at `fire-images/wildland-fire.png`, positioned via `#portal-logo img { top: -35px; left: 15% }`.

5. **Search box** (`.LSBox`) is repositioned differently on mobile (absolute positioning, transparent background).

6. **The sub-site's CSS cascade:** `reset.css` -> `base.css` -> `dropdown-menu.css` -> `ploneCustom.css` -> `fire.css` (loaded last, highest specificity for sub-site overrides).
