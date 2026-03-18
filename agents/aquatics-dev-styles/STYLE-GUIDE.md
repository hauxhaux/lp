# Aquatics Dev Site — Complete Style Reference

Crawled from: https://dev.landscapepartnership.org/networks/working-lands-for-wildlife/landscapes-wildlife/landscapes/aquatics

CSS source files: `css/wlfw-aquatics.css` (aquatics-specific), `css/ploneCustom.css` (site-wide), `css/base.css`, `css/dropdown-menu.css`, `css/mobile.css`, `css/reset.css`

**Note:** The `wlfw-aquatics.css` file is identical between dev and production sites.

---

## Page Inventory

| File | Page | URL Path (relative to `/networks/working-lands-for-wildlife/landscapes-wildlife/landscapes/aquatics`) |
|---|---|---|
| `html/01-home.html` | Home (Conserving Aquatic Ecosystems) | `/` |
| `html/02-about.html` | About | `/about` |
| `html/03-wildlife.html` | Wildlife | `/wildlife` |
| `html/04-resources.html` | Resources | `/resources` |
| `html/05-news-and-stories.html` | News & Stories | `/news-and-stories` |
| `html/06-partners.html` | Aquatics Organizations | `/about/partners` |
| `html/07-contact.html` | Contact | `/about/connect-contact` |
| `html/08-workspace.html` | Workspace | `/about/workspace` |
| `html/09-framework.html` | Aquatic Connectivity Framework | `/resources/framework` |
| `html/10-acf-practices.html` | ACF Conservation Practices | `/resources/acf-conservation-practices` |
| `html/11-acf-fact-sheet.html` | ACF Fact Sheet | `/resources/acf-fact-sheet` |
| `html/12-outreach-materials.html` | Outreach Materials | `/resources/outreach-materials` |
| `html/13-science-briefs.html` | Science Briefs | `/resources/science-briefs` |
| `html/14-webinars-videos.html` | Webinars and Videos | `/resources/webinars-and-videos` |
| `html/15-training.html` | Training | `/resources/training` |
| `html/16-nrcs-practices.html` | NRCS Conservation Practices & Materials | `/resources/nrcs-conservation-practices-materials` |
| `html/17-news.html` | Aquatics News | `/news-and-stories/news` |
| `html/18-stories.html` | Aquatics Stories | `/news-and-stories/stories` |
| `html/19-events.html` | Aquatics Events | `/news-and-stories/events` |

### Navigation Structure

**Top-level tabs:** Home, About, Wildlife, Resources, News & Stories

**About submenu:** ACF Partnerships, Aquatics Organizations, Contact, How to Apply to NRCS Programs (external), Workspace

**Wildlife submenu:** Eastern Hellbender, Bog Turtle, American Black Duck, Shorebirds (ext), Yazoo Darter (ext), Colorado River Mussels (ext), Conasauga River Aquatic Species (ext), Blanding's Turtle (ext), Northeast Turtles (ext)

**Resources submenu:** Aquatic Conservation Framework (ACF), The AquaCorridors Tool Suite, ACF Conservation Practices, ACF Fact Sheet, Apps Maps and Data, Outreach Materials, Science Briefs, Webinars and Videos, Training, NRCS Conservation Practices & Materials

**News & Stories submenu:** Aquatics News, Aquatics Stories, Aquatics Events

---

## Color Palette

### CSS Custom Properties (`:root` in `wlfw-aquatics.css`)

| Variable | Hex | Usage |
|---|---|---|
| `--darkgreen` / `--heading` | `#278e95` | Primary brand color; header bg, all headings, nav portlet headers |
| `--gold` | `#dcc464` | Accents, selected nav links, h1 underline bar, `.subheading` text |
| `--darkgold` | `#bca647` | Footer background (`#portal-footer-wlfw`), `.bg-drk-gold` |
| `--ltgold` | `#ebdc9e` | Light gold background blocks |
| `--brown` | `#825640` | Site actions bar (`#portal-siteactions`) background |
| `--orange` | `#f88630` | Hover states on biome nav, button backgrounds |
| `--yellow` | `#fbd84d` | Subhead labels inside dark blocks (`.blue-block h4`) |
| `--darkgrey` | `#262626` | Biome navigation bar background, list item text color |
| `--grey` | `#f8f5ef` | Light background sections (`.bg-grey`) |
| `--ltgrey` | `#efefef` | Subtle background blocks, submenu hover bg |
| `--white` | `#ffffff` | Body background, nav link color |

### Additional Hard-coded Colors

| Value | Usage |
|---|---|
| `#3b3b3b` | Body paragraph text (`p` color) |
| `#3c4d6a` | Intro text, pullquote text |
| `#176065` | Submenu link color (`#portal-globalnav ul.submenu a`) |
| `#d8c468` | Gold text class (`.gold-text`) |
| `#d3bd64` | Pullquote border, callout border |
| `#f2e6b5` | Callout background |
| `#E86128` | Submenu hover text color |
| `#ef8f39` | `.btn-orange` background |
| `#29457b` | EEO statement link hover color |
| `#91C45E` | Tooltip link color |
| `#eeca37` | Timeline content h3 color |
| `#345a67` | Timeline background |
| `#a6c372` | Anchor menu border-top |
| `#ff6c00` | Anchor menu selected link |
| `#D0F7FF` | Blue block subhead color |
| `#f1d215` | Black overlay block subhead color |
| `rgba(0,0,0,0.35)` | Nav hover/selected background |
| `rgba(0,0,0,0.50)` | Overlay block backgrounds |
| `rgba(0,0,0,0.70)` | Dark overlay blocks |
| `rgba(0,0,0,0.80)` | Black overlay block bg |
| `rgba(37,50,75,0.90)` | Blue block background |
| `rgba(38,96,116,0.65)` | Timeline item overlay |

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

Also loaded: Font Awesome 4.2.0 (`//maxcdn.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.min.css`)

### Font Families

| Font | Usage |
|---|---|
| `'Public Sans', sans-serif` | Body text, nav links, list items, document descriptions, subheadings, `.black-50-block h2` |
| `'Merriweather', serif` | All headings (h1-h6), intro text, pullquotes, quotes, timeline headings |
| `'Montserrat', sans-serif` | `.heading-white` class (white overlay headings) |
| `'Source Sans Pro', sans-serif` | Used in ploneCustom.css for base nav links (overridden by aquatics CSS) |

### Font Sizes

| Element | Size | Line Height | Weight | Other |
|---|---|---|---|---|
| `body` | (inherited) | — | — | `font-family: 'Public Sans'` |
| `p` | `1.1rem` | `1.65rem` | 400 | color `#3b3b3b` |
| `h1` (content) | `2.8rem` | `3.4rem` | 600 | color `--heading`, `letter-spacing: -0.025em` |
| `h1` (mobile <767px) | `2.3rem` | `2.6rem` | 600 | — |
| `h2` | `2.3rem` | `2.8rem` | 600 | — |
| `h2.large` | `2.8rem` | — | 600 | mobile: `2rem` |
| `h3` | `1.6rem` | — | 600 | — |
| `h4` | `1.3rem` | — | 600 | — |
| `.documentDescription` | `1.35em` | `1.5em` | 500 | `'Public Sans'` |
| `.intro` | `18px` | `1.6em` | 400 | `'Merriweather'`, color `#3c4d6a` |
| `.subheading` | `1.1rem` | — | — | `'Public Sans'`, color `--gold` |
| `#content li` | `1rem` | — | — | color `--darkgrey`, `letter-spacing: 0.01em`, `margin-bottom: 10px` |
| `.pullquote` | `1.5rem` | `1.5em` | — | `'merriweather'`, `letter-spacing: -0.05em`, border-left: `6px solid #d3bd64` |
| `.quote` | `20px` | — | — | `'Merriweather'`, italic |
| `.cite` | `.9rem` | — | — | `text-align: center` |
| Nav links | `1rem` (desktop) / `16px` (tablet <=1024px) | — | 600 | uppercase, `'Public Sans'` |
| Submenu links | `15px` | — | — | not uppercase |
| `.heading-white` | `2.7em` | — | 600 | `'Montserrat'`, uppercase |
| Breadcrumbs | `.9rem` | — | — | — |

### h1 Gold Underline Bar

Both `h1.documentFirstHeading:after` and `#content h1:after` generate a gold bar:
- Width: `80px`
- Height: `5px`
- Color: `var(--gold)` (`#dcc464`)
- Margin-top: `5px`

---

## Layout & Structure

### Page Width

| Element | Width | Notes |
|---|---|---|
| `#visual-portal-wrapper` | `max-width: 100%` | Overrides ploneCustom's `1170px` |
| `#content` | `80%` | Narrower at `<=1530px`: `85%` |
| `.narrow` (ploneCustom) | `1170px` | Standard content container |
| `.inner-container` (ploneCustom) | `1170px` | Standard content container |

### Header

| Property | Value |
|---|---|
| Height (desktop) | `150px` |
| Height (mobile <=768px) | `100px` |
| Background | `var(--darkgreen)` (`#278e95`) |
| Box shadow (desktop) | `0px 10px 20px -10px rgba(0,0,0,0.75)` |
| Box shadow (mobile) | none (`rgba(0,0,0,0)`) |
| Logo width (desktop) | `300px`, positioned `top: 15px; left: 35px` |
| Logo width (mobile) | `200px`, positioned `top: -18px; left: 5px` |

### Biome Nav Bar (top bar above header)

| Property | Value |
|---|---|
| Background | `var(--darkgrey)` (`#262626`) |
| Padding | `10px 30px` |
| Font weight | 600 |
| Font size | `12px` (mobile: `11px`) |
| Letter spacing | `1px` (mobile: `normal`) |
| Link color | `#fff`, uppercase |
| Link hover | `var(--orange)` (`#f88630`) |

### Banner (`#portal-banner`)

| Property | Value |
|---|---|
| Height (desktop) | `450px` |
| Height (mobile <=768px) | `195px` |
| Background | `url(aquatic-images/florida-wetlands.jpg) no-repeat center; background-size: cover` |
| Per-section heights | News & Stories: `350px`, Workspace: `350px`, Maps & Data: `350px` |
| Per-section mobile | `200px !important` |

Section-specific banner images are defined per body class (e.g., `.site-aquatics.section-about`, `.site-aquatics.section-wildlife`, etc.).

### Breadcrumbs

| Property | Value |
|---|---|
| Padding | `15px 35px` |
| Font size | `.9rem` |
| "You are here" label | `display: none` |

---

## Navigation

### Global Nav (`#globalnav-wrapper`)

| Property | Value |
|---|---|
| Background | `transparent` |
| Position | `top: 100px` (absolute, sits over the banner) |
| Mobile (<=768px) | `width: 100%; top: 105px; left: 0` |

### Nav Links (`#portal-globalnav li a`)

| Property | Value |
|---|---|
| Font family | `'Public Sans'` |
| Font size | `1rem` (desktop), `16px` (<=1024px) |
| Font weight | 600 |
| Text transform | uppercase |
| Padding | `10px 20px` (desktop), `10px 15px` (<=1024px) |
| Border | `3px solid transparent` |
| Margin | `0 0.15em` (desktop), `0 0.125em` (<=1024px) |
| Color | `var(--white)` (`#ffffff`) |
| Layout | `display: flex; justify-content: right; margin-right: 2.5%` |

### Nav Hover/Selected States

| State | Background | Text Color |
|---|---|---|
| Default | transparent | `#ffffff` |
| Hover | `rgba(0,0,0,0.35)` | `var(--gold)` (`#dcc464`) |
| Selected | `rgba(0,0,0,0.35)` | `var(--gold)` (`#dcc464`) |
| Selected + Hover | `rgba(0,0,0,0.35)` | `var(--gold)` (`#dcc464`) |

### Submenu Links (`#portal-globalnav ul.submenu a`)

| Property | Value |
|---|---|
| Text transform | none (not uppercase) |
| Font size | `15px` |
| Color | `#176065` |
| Hover background | `#efefef` |
| Hover text | `#E86128` (orange) |

### Submenu Dropdown (`#portal-globalnav ul`)

From `dropdown-menu.css`:
- Position: absolute
- Width: `15em` (base) / `230px` (ploneCustom override)
- Background: `#fff`
- Appears on hover via `left: auto` (hidden with `left: -999em`)

### Home Tab

- Text is visible (no icon replacement, unlike ploneCustom default)
- Hover: `rgba(0,0,0,0.35)` bg, gold text
- Home submenu: `display: none`

### Mobile Nav (<=767px)

| Property | Value |
|---|---|
| `#portal-globalnav` | `display: none` (hidden by default) |
| `#portal-globalnav.opened` | `display: block` (toggled) |
| `#portal-globalnav li` | `width: 100%; background: #d8c468` (gold) |
| `.menu-toggle` | `font-weight: 600; font-size: 13px; padding: 12px 0 12px 35px` |

### Landscape Biome Menu

| Property | Value |
|---|---|
| Display | `block` |
| Mobile (<=768px) | `position: absolute; top: 304px` |
| Contains | Navigate WLFW Landscapes dropdown with 4 landscape links |

### Companion Sites Menu

Dropdown with 8 external links to partner sites (APPLCC, Conservation Design, etc.)

---

## Buttons

### `.btn-orange`

| Property | Value |
|---|---|
| Background | `#ef8f39` |
| Color | `#fff` |
| Font size | `13px` |
| Font weight | 600 |
| Letter spacing | `1px` |
| Text transform | uppercase |

### `.btn.large-white` (from ploneCustom)

| Property | Value |
|---|---|
| Background | `rgba(255,255,255,0.25)` |
| Border | `1px solid #fff` |
| Color | `#fff` |
| Font size | `14px` |
| Font weight | 600 |
| Padding | `15px` |
| Letter spacing | `0.075em` |
| Border radius | `4px` |
| Text transform | uppercase |
| Hover | aquatics override: `rgb(131,84,64)` (brown) bg |

### `.btn-grey` (from ploneCustom)

| Property | Value |
|---|---|
| Background | `#e6e6e6` |
| Color | `#515151` |
| Font size | `14px` |
| Font weight | 600 |
| Padding | `10px 15px` |
| Border radius | `4px` |
| Text transform | uppercase |
| Hover | bg `#F8903E`, color `#fff` |

### `.cta-button` (from ploneCustom)

| Property | Value |
|---|---|
| Background | `#f7bd4f` |
| Font size | `20px` |
| Padding | `15px 25px` |
| Border radius | `5px` |
| Border | `1px solid #fff` |
| Hover | bg `#f38b1a` |
| Font family | `'Montserrat'`, weight 600 |

### Timeline `.tl-content .button`

| Property | Value |
|---|---|
| Background | `#fff` |
| Border radius | `6px` |
| Padding | `5px 15px` |
| Font weight | bold |
| Hover text | `#fd8d58` |

---

## Content Blocks

### `.blue-block`

| Property | Value |
|---|---|
| Background | `rgba(37,50,75,0.90)` (aquatics override) |
| Padding | `40px 30px` |
| Min height | `400px` |
| Margin | `4em 1em` (mobile: `2em`) |
| Border radius | `10px` |
| h2 | `40px`, line-height `1.3em` (mobile: `30px`) |
| h4 | color `var(--yellow)` (`#fbd84d`), `22px` |
| `.subhead` | `14px`, `letter-spacing: 3px`, color `#D0F7FF`, uppercase |

### `.black-overlay-block`

| Property | Value |
|---|---|
| Background | `rgba(8,7,7,0.80)` |
| Padding | `40px 30px` |
| Min height | `400px` |
| Margin | `4em 1em` (mobile: `2em`) |
| Border radius | `10px` |
| `.subhead` | color `#f1d215`, `14px`, `letter-spacing: 4px` |

### `.black-50-block`

| Property | Value |
|---|---|
| Background | `rgb(0,0,0,0.50)` |
| Padding | `40px` |
| Margin | `3em` |

### `.black-70-block`

| Property | Value |
|---|---|
| Background | `rgb(0,0,0,0.70)` |
| Padding | `2rem` |
| Margin | `1em` |
| Display | `flex`, gap `20px` |
| Border radius | `10px` |
| `.subhead` | color `var(--yellow)`, `14px`, `letter-spacing: 2px` |
| Mobile (<=768px) | `flex-direction: column` |

### `.basic-block`

| Property | Value |
|---|---|
| Border | `1px solid #ddd` |
| Border radius | `8px` |
| Padding | `0 2rem 1rem` |
| Margin | `2rem 0` |

### `.callout`

| Property | Value |
|---|---|
| Background | `#f2e6b5` |
| Padding | `1em` |
| Border-left | `1em solid #d3bd64` |

### Background Image Blocks

- `.turf-block` — `url(working-lands/rich-turf.jpg)`
- `.aquacorridors-block` — `url(working-lands/usfws-coastal-delta-kodiak-refuge-alaska.jpg)`
- `.bg-acf` — `url(working-lands/acf-watershed.jpg)`, padding `3rem` (mobile: `2rem 1rem`)

### Background Utility Classes

| Class | Color |
|---|---|
| `.bg-dark` | `var(--darkgreen)` (`#278e95`) |
| `.bg-blue` | `var(--heading)` (`#278e95`) |
| `.bg-grey` | `var(--grey)` (`#f8f5ef`) |
| `.bg-gold` | `var(--gold)` (`#dcc464`), `border-top: none` |
| `.bg-drk-gold` | `var(--darkgold)` (`#bca647`) |
| `.bg-lt-gold` | `var(--ltgold)` (`#ebdc9e`) |
| `.bg-orange` | `var(--orange)` (`#f88630`) |
| `.bg-brown` | `var(--brown)` (`#825640`) |
| `.bg-ltgrey` | `var(--ltgrey)` (`#efefef`) |

---

## Spacing Utilities

| Class | Value |
|---|---|
| `.pad80` | `padding: 80px 0` |
| `.pad60` | `padding: 60px 0` |
| `.pad40` | `padding: 40px` |
| `.pad20` | `padding: 20px` |

---

## Flex / Layout Utilities (from ploneCustom)

| Class | Properties |
|---|---|
| `.flex-block` | `display: flex; align-items: center` (mobile: `flex-direction: column`) |
| `.flex` | `display: flex; align-items: center` (mobile: `padding: 30px`) |
| `.flex-end-block` | `display: flex; align-items: flex-end` |
| `.flex-item-column` | `flex-direction: column; align-items: center; justify-content: center` |
| `.flex-column-end` | `flex-direction: column; justify-content: flex-end` |
| `.flex-item-wrap` | `flex: 1` |
| `.flex-item` | `flex: 1` |
| `.flex-block-reverse-mobile` | `display: flex; align-items: center` (mobile <=767px: `flex-direction: column-reverse`) |
| `.centered-block-flex` | `text-align: center; flex: 1` |

---

## Footer

### `#portal-footer-wlfw` (WLFW custom footer, displayed)

| Property | Value |
|---|---|
| Display | `block` |
| Background | `var(--darkgold)` (`#bca647`) |
| Color | `#fff` |
| Padding | `1.5em` |
| h3 | color `#fff`, `border-bottom: 1px solid #ebebeb`, `letter-spacing: 2px`, `1.5rem` |
| `.bottom-nav` | `display: flex; align-items: center; justify-content: space-between` (mobile: `flex-direction: column; text-align: center`) |
| `.ft-menu` | `text-align: center`, color `#fff` |
| `.ft-menu li a` | color `#fff`, `15px`, `line-height: 1.8em` |
| `.ft-menu li a:hover` | `border-bottom: 1px solid #fff` |
| `.eeo-statement` | `font-size: .75rem; line-height: 1.4em; margin-top: 15px` |
| `.eeo-statement a` | `font-weight: 600; color: #fff` |
| `.eeo-statement a:hover` | `color: #29457b` |
| `.sitecredit` | `font-size: 13px; letter-spacing: 0.05em; text-transform: uppercase` |
| `.sitecredit a` | `color: #fff` |

### `#portal-footer` (default Plone footer)

- `display: none` (hidden by aquatics CSS)

### `#portal-siteactions`

- Background: `var(--brown)` (`#825640`)

---

## AquaCorridors Tool Suite Section

Special styles for the AquaCorridors sub-section:

| Property | Value |
|---|---|
| Banner | `url(aqua-corridors-images/aquacorridors-banner-bg.jpg)`, height `350px` |
| Banner mobile (<=600px) | stacked logo version, height `175px` |
| Banner logo | `500px x 121px`, centered at `top: 30%` |
| h1 | hidden (`display: none`) |
| Breadcrumbs | hidden |

### Anchor Menu (`#anchor-menu-block`)

| Property | Value |
|---|---|
| Background | `#efefef` |
| Border-top | `7px solid #a6c372` |
| Border-bottom | `1px solid #e2dcdc` |
| Layout | `display: grid` |
| Items (`.anchor-menu-item`) | `font-size: 17px; font-weight: 600; text-transform: uppercase; padding: 15px 20px 5px` |
| Selected state | color `#ff6c00` |
| Mobile (<=767px) | `margin-top: 85px`, reduced padding |

### Timeline Slider (`#timeline`)

| Property | Value |
|---|---|
| Background | `#345a67` |
| Item height | `70vh`, min `600px` |
| Default width | `24.3333%` each |
| Hover width | `100%` |
| Overlay | `rgba(38,96,116,0.65)` |
| Transition | `width 0.5s ease` |
| Content position | centered at `top: 45%` |
| h1/headings | `'Merriweather'`, color `#dcc464`, `1.8rem` |
| h3 | color `#eeca37` |
| p | color `#ffffff` |

---

## Tile / News Items

| Property | Value |
|---|---|
| `.tileItem` | `border-top: none` |
| `.tileHeadline` | `margin-top: 0; line-height: 1.6em; font-size: 1.75em` |
| `.tileHeadline a` | color `var(--heading)` |
| `.card-title` | `font-size: 1.2rem; line-height: 1.6rem` |

---

## Navigation Portlet

| Property | Value |
|---|---|
| `.portletNavigationTree .portletHeader` | bg `var(--heading)`, `border-radius: 6px 6px 0 0`, uppercase, `padding: 15px` |
| `.portletHeader a` | color `var(--gold)`, weight 600 |

---

## Responsive Breakpoints

All `@media` rules found in `wlfw-aquatics.css`:

| Breakpoint | Usage |
|---|---|
| `max-width: 1530px` | Content width increases to `85%` |
| `max-width: 1024px` | Nav link size/padding adjustments |
| `max-width: 768px` | Mobile header (100px), mobile banner (195px), mobile nav position, mobile logo, mobile search, mobile biome nav, mobile landscape menu, LSBox repositioning, blue-block/black-overlay margins, mobile grid |
| `max-width: 767px` | Nav fully hidden (toggled), gold mobile nav bg, h1/h2 size reductions, flex-block-reverse-mobile, anchor-menu adjustments, bg-acf padding, footer column layout |
| `max-width: 600px` | AquaCorridors mobile banner, h1 size reduction (ploneCustom) |

---

## Miscellaneous

### Search Box (`#portal-searchbox`)

| Property | Value |
|---|---|
| Margin-right | `20px` |
| Padding | `7px` |
| Mobile (<=768px) | `position: absolute; top: 5px` |
| Mobile submit button | transparent bg, white magnifier icon, `25x25px` |
| Mobile input | `width: 8em; border-radius: 6px` |

### Live Search Box (`.LSBox`)

| Property | Value |
|---|---|
| Desktop | `top: -60px; right: 5%`, white bg, `border-radius: 6px` |
| Mobile (<=768px) | `top: 100px; position: absolute; left: 90px; width: 100px`, transparent bg |

### Personal Tools (`#portal-personaltools-wrapper`)

- Desktop: `right: 260px; top: -38px; position: absolute`
- Mobile: `right: 20px; top: 330px`
- Link color: `#fff`
- Visited: `#a9e1f3`

### Edit Template

- `#visual-portal-wrapper` forced to `1170px` width
- Banner caption turned off
- `.LSBox` repositioned

### Images

- `img.image-left, img.image-right, .captioned img` — `border: none`

### Text Shadow Utility

- `.text-shadow` — `text-shadow: 1px 2px 10px #3a3a3a`

### Tooltip

| Property | Value |
|---|---|
| `.tooltipContent` | `width: 288px; padding: 1em; border: 2px solid #fff; border-radius: 8px; background: rgba(0,0,0,0.75)` |
| Link color | `#91C45E` |
