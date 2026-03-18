# Sub-site Theme Replication Plan

Repeatable process for taking a Landscape Partnership sub-site URL and replicating its visual design in plonetheme.lp, commit-by-commit.

---

## Prerequisites

### Start the local Plone server

Before any work begins, the Docker-based Plone server **must** be running. From the project root:

```bash
./devbuild.sh       # docker compose up -d --build
```

This starts the Plone 6 backend at `http://localhost:8080` (credentials: `admin`/`admin`). Docker Desktop must be open first. The server takes ~30 seconds to become available after `./devbuild.sh` completes.

**Verify it's running** by navigating Playwright to `http://localhost:8080/Plone` and confirming the page loads.

### Start the SCSS watch process

From `src/plonetheme.lp/src/plonetheme/lp/theme/`:

```bash
npm run watch       # Keep running in background during entire session
```

---

## CRITICAL: Visual Testing Before Every Commit

**Never commit style changes without first visually confirming they match the reference design.** This is the single most important rule of this process.

Before every commit in Phase 3 and Phase 4:

1. **Reload** the local Plone site in Playwright (`http://localhost:8080/Plone`)
2. **Screenshot** the affected section(s) at desktop width (1280px)
3. **Compare** against the reference screenshot in `agents/SITE-styles/screenshots/`
4. **Test interactions** — hover states, dropdowns, mobile toggler, etc.
5. **Fix any discrepancies** found — iterate until the section visually matches
6. **Only then commit** the changes

If the server is not running, start it with `./devbuild.sh` before proceeding. Do not commit untested CSS.

---

## Phase 1: Crawl & Capture

**Input:** A sub-site URL, e.g. `https://landscapepartnership.org/SITE`

### 1.1 Enumerate pages
- Visit the sub-site root and map all navigable pages (follow nav links, sidebar links, footer links).
- Record each URL in a table: `page name | URL path | notes`.
- Aim for ~10 representative pages covering all layout variants (home, listing, detail, news, team, etc.).

### 1.2 Capture HTML
- Use Playwright to save full-page HTML for each URL.
- Save to `agents/SITE-styles/html/NN-slug.html` (zero-padded, e.g. `01-home.html`).
- Preserve all `<link>`, `<style>`, and inline style attributes.

### 1.3 Extract CSS
- From the HTML `<head>`, collect all `<link rel="stylesheet">` and `@import` URLs.
- Download each CSS file to `agents/SITE-styles/css/`.
- Key files to look for:
  - Site-wide base CSS (often `base.css` or similar)
  - Site-wide custom overrides (`ploneCustom.css`)
  - **Sub-site-specific CSS** (e.g. `wlfw-SITE.css`) — this is the most important file.
  - Mobile/responsive overrides (`mobile.css`)
  - Any reset CSS.

### 1.4 Capture screenshots
- Use Playwright at desktop width (1280px) to take full-page screenshots of each URL.
- Save to `agents/SITE-styles/screenshots/NN-slug.png`.
- Also capture one at mobile width (375px) for the home page.

### 1.5 Write STYLE-GUIDE.md
- Create `agents/SITE-styles/STYLE-GUIDE.md` organized by feature:
  1. **Page inventory** — table of all captured pages with URLs
  2. **Color palette** — extract all CSS custom properties from the sub-site CSS; list hex values and usage
  3. **Typography** — font families (Google Fonts), heading styles, body text, special text treatments
  4. **Layout & structure** — page width, header height, content width, banner heights
  5. **Navigation** — global nav positioning, link styles, hover/selected states, dropdown/submenu styles
  6. **Buttons** — all button variants with colors, sizes, hover states
  7. **Content blocks** — background blocks, overlays, cards, grids
  8. **Footer** — layout, colors, link styles
  9. **Responsive breakpoints** — document all `@media` rules with their px values
  10. **Google Fonts** — all loaded families and weights

### 1.6 Commit capture
```
git add agents/SITE-styles/
git commit -m "Capture SITE sub-site styles (HTML, CSS, screenshots, style guide)"
```

---

## Phase 2: Scaffold the SCSS

### 2.1 Switch theme.scss to the new sub-site

**Important:** Each sub-site starts from the base theme, not from another sub-site's custom styles. In `theme/scss/theme.scss`:

1. **Comment out** the existing `@import "custom";` line (this is the previous sub-site's styles).
2. **Add** `@import "custom-SITE";` in its place.

This ensures the new sub-site's styles are built on top of the clean Barceloneta/Bootstrap base, without interference from another sub-site's overrides. Only one sub-site custom file should be active at a time during development.

```scss
// @import "custom";                // <-- comment out previous sub-site
@import "custom-SITE";              // <-- active sub-site
```

### 2.2 Create the custom SCSS file
- Create `theme/scss/_custom-SITE.scss` with the same section structure as the style guide.
- Add a header comment block (matching `_custom.scss` conventions).

### 2.3 Define CSS custom properties
- Port the sub-site's color palette into `:root` variables at the top of `_custom-SITE.scss`.
- Match variable names to those in the live site's CSS for clarity.

### 2.4 Add Google Fonts
- If the sub-site uses different fonts than what's already loaded, add `<link>` tags to `theme/index.html`.

### 2.5 Verify compilation and commit
- Confirm `npm run watch` recompiles without errors.
- **Start the Plone server** (`./devbuild.sh`) if not already running.
- Verify the local site still loads correctly in Playwright.
- Commit scaffold.

```
git commit -m "Add SITE SCSS scaffold with color palette and font imports"
```

---

## Phase 3: Incremental Style Adoption

Work through the site top-to-bottom, one visual section at a time. Each section gets its own commit. The goal is not to follow a fixed list of sections — instead, **evaluate the captured reference material to discover what sections exist and what styling each requires**.

### 3.1 How to identify sections

Read STYLE-GUIDE.md and examine the reference screenshots to break the page into discrete visual regions. Common regions include header, navigation, banner/hero, content area, sidebar, footer — but each sub-site may have unique regions (e.g. a biome switcher, a timeline slider, a partner grid). Let the reference material define the sections, not a template.

For each identified section:
1. Determine its **boundaries** — where does it start and end visually?
2. Identify its **sub-components** — what distinct elements live inside it? (e.g. a header might contain a logo, search box, and login link, or it might just be a logo)
3. Note any **interactive states** — hover, active, expanded, focus
4. Note any **responsive behavior** — does it change at breakpoints?

### 3.2 How to evaluate a section

For each section, compare the reference material against what Plone 6 + Barceloneta renders by default. Ask:

- **What already matches?** Barceloneta/Bootstrap may already handle some things. Don't override what's already correct.
- **What needs overriding?** Identify the specific CSS properties that differ.
- **What needs structural HTML changes?** Some styling requires changes to `index.html` or `rules.xml` — identify these before writing SCSS.

Use the captured CSS files to find the exact rules the live site uses. Cross-reference with STYLE-GUIDE.md for context on why those rules exist.

### 3.3 Types of styling to address per section

When working on any section, systematically consider these categories:

**Box model & layout**
- Dimensions (width, height, min/max variants)
- Position (static, relative, absolute, fixed) and offsets (top, right, bottom, left)
- Display mode (block, flex, grid) and alignment (justify, align)
- Margin, padding, box-sizing
- Overflow behavior

**Color & background**
- Background color, gradient, or image
- Background position, size, repeat, attachment
- Overlays (pseudo-elements with rgba backgrounds)
- Border colors
- Box shadow, text shadow

**Typography**
- Font family, weight, size, line-height, letter-spacing
- Text color, text-transform, text-decoration
- Text alignment, white-space, word-spacing

**Borders & decoration**
- Border width, style, color (per-side if needed)
- Border-radius
- Outline
- Decorative pseudo-elements (underline bars, accent lines)

**Interactive states**
- `:hover`, `:focus`, `:active`, `:visited`
- Transitions and timing
- Cursor changes

**Responsive behavior**
- Which breakpoints affect this section?
- What changes at each breakpoint? (layout, visibility, sizing, font adjustments)

Not every section will need all categories. Use the reference CSS and screenshots to determine which are relevant.

### 3.4 Per-section workflow

**The Plone server MUST be running for this phase.** If it's not, start it with `./devbuild.sh` before proceeding.

For each section, repeat this cycle:

1. **Read** the relevant parts of STYLE-GUIDE.md and the captured CSS
2. **Invoke** the `plone-classic-expert-developer` skill for Plone-specific guidance on the elements involved
3. **Check** whether `index.html` or `rules.xml` changes are needed — if so, make those first
4. **Write** SCSS rules in `_custom-SITE.scss`, targeting Plone's actual DOM selectors (inspect with Playwright if unsure)
5. **Wait** for `npm run watch` to recompile (≤2s)
6. **Reload and screenshot** the local Plone site with Playwright at desktop width
7. **Compare** against the reference screenshot — look for exact color matches, spacing, font rendering, and layout alignment
8. **Test interactions** — hover states, dropdowns, mobile toggler, etc. Screenshot each interaction state
9. **Iterate** — fix every discrepancy found, re-screenshot, until the section is a visual match
10. **Only after visual confirmation**, commit with a message describing what was styled

### 3.5 Scoping commits

Each commit should represent a coherent visual section or sub-section. Guidelines:

- **One section per commit** when the section is small or straightforward.
- **Split into sub-commits** when a section is large. For example, if navigation has complex dropdowns and mobile behavior, commit the base nav links first, then dropdowns, then mobile — each as a separate commit.
- **Group related fixes** — if fixing one element requires a small tweak to an adjacent element, include both.
- **Never mix unrelated sections** in a single commit.
- **Never commit without testing** — every commit must have been visually verified against the reference design using Playwright screenshots.

### 3.6 Specificity and selector strategy

- Use Plone's ID selectors (`#portal-globalnav`, `#content-header`, `#portal-footer-wrapper`) for specificity over Bootstrap classes — this avoids `!important`.
- Scope sub-site-specific styles under a body class (e.g. `.section-SITE`) if the theme needs to support multiple sub-sites simultaneously.
- Prefer nesting selectors in SCSS to keep rules grouped and readable.
- Reference the captured HTML files to confirm the exact class names and DOM hierarchy Plone generates.

---

## Phase 4: Validation & Polish

### 4.1 Full-page comparison
- Use Playwright to capture full-page screenshots of the local site at each page equivalent.
- Compare side-by-side with the reference screenshots in `agents/SITE-styles/screenshots/`.
- Note all remaining discrepancies.

### 4.2 Interaction testing
- Test with Playwright:
  - Nav hover states (each link)
  - Nav dropdown open/close
  - Mobile toggler → offcanvas open/close
  - Search box focus state
  - Button hover states
  - Any interactive content (sliders, accordions, tabs)
- Screenshot each interaction state.

### 4.3 Cross-width testing
- Test at: 375px, 768px, 992px, 1280px, 1530px+
- Screenshot at each width.
- Fix any breakpoint issues found.

### 4.4 Fix remaining issues
- Address each discrepancy found in 4.1–4.3.
- **Visually verify each fix with Playwright** before committing.
- One commit per fix or small group of related fixes.

### 4.5 Computed style spot-checks
- Use `playwright-cli eval` to compare computed styles on key elements (header, nav links, h1, buttons, footer) between local and reference.
- Fix any pixel-level differences that matter.

### 4.6 Final commit
- **Take final full-page screenshots** at desktop and mobile widths.
- Confirm all sections match the reference design.
```
git commit -m "Final SITE theme polish: fix remaining style inconsistencies"
```

---

## Phase 5: Diazo / index.html Changes (if needed)

Some sub-sites may require changes to the HTML shell or Diazo rules:

### 5.1 index.html
- Add sub-site-specific wrapper classes or containers.
- Add conditional markup for sub-site detection (if themes differ by section).

### 5.2 rules.xml
- Add Diazo rules for sub-site-specific content mapping.
- Conditional rules based on URL path (e.g. `<rules css:if-content=".section-SITE">`).

### 5.3 Visually verify and commit
- **Test all structural changes with Playwright** before committing.
- Confirm Diazo rules produce the expected DOM output.
```
git commit -m "Add Diazo rules and HTML structure for SITE sub-site"
```

---

## Checklist per section (copy for each section in Phase 3)

- [ ] Read STYLE-GUIDE.md section
- [ ] Invoke `plone-classic-expert-developer` skill
- [ ] Write SCSS rules
- [ ] Confirm `npm run watch` recompiled successfully
- [ ] **Plone server is running** (`./devbuild.sh`)
- [ ] **Playwright screenshot of local site**
- [ ] **Compare against reference screenshot — exact visual match**
- [ ] **Test hover/interactive states with Playwright**
- [ ] **Iterate and fix until match is confirmed**
- [ ] Commit with descriptive message

---

## File naming conventions and screenshot organization

**Never clutter the `agents/` root folder.** All files must be organized within neatly structured subfolders at the appropriate level.

- **Reference screenshots** go in `agents/SITE-styles/screenshots/` (the per-page captures from Phase 1).
- **Testing screenshots** (taken during development) go in `agents/SITE-styles/screenshots/testing/`.
- **Never place screenshots directly in `agents/`.** Always use the sub-site's subfolder hierarchy.

```
agents/SITE-styles/
├── STYLE-GUIDE.md
├── css/
│   ├── base.css
│   ├── ploneCustom.css
│   ├── wlfw-SITE.css       (or equivalent sub-site CSS)
│   ├── mobile.css
│   └── reset.css
├── html/
│   ├── 01-home.html
│   ├── 02-about.html
│   └── ...
└── screenshots/
    ├── 01-home.png           (reference captures)
    ├── 02-about.png
    ├── ...
    └── testing/              (development test screenshots)
        ├── nav-hover-test.png
        ├── mobile-header.png
        └── ...

theme/scss/
├── _custom-SITE.scss        (new file for this sub-site)
└── theme.scss               (updated to import _custom-SITE.scss)
```

## Notes

- **Always start the Plone server** with `./devbuild.sh` before any visual testing. Docker Desktop must be running first.
- Always use `npm run watch` (not `npm run build`) during development.
- **Never commit CSS changes without visual verification** via Playwright screenshots against the reference design.
- Use ID selectors for specificity over Bootstrap — avoid `!important`.
- The `plone-classic-expert-developer` skill should be invoked before any Plone/theme work.
- All test screenshots go in `agents/` with contextual names, cleaned up after each session.
- Sub-site detection in Plone Classic uses body classes like `.section-SITE` — use these for conditional styling.
