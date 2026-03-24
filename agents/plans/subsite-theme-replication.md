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
  - **Print stylesheets** (`print.css`, or `@media print` blocks embedded in other files)
  - Any reset CSS.

### 1.4 Capture images from the original site
- Examine the header, footer, hero/banner, and top content area of the home page for images that are part of the site design (logos, banner photos, background images, partner logos, icons).
- Download these images using Playwright or direct fetch and save to `agents/SITE-styles/images/`.
- Use descriptive filenames: `header-logo.png`, `hero-banner.jpg`, `footer-partner-logo.png`, etc.
- Note which images are referenced via CSS (`background-image`) vs HTML (`<img>` tags) — this distinction matters for how they'll be integrated into the theme.
- These images serve as reference material and may be needed as assets in the theme's `theme_images/` directory during Phase 3.

### 1.5 Capture screenshots
- Use Playwright to take full-page screenshots of **every** captured URL at both widths:
  - **Desktop (1280px):** save to `agents/SITE-styles/screenshots/NN-slug.png`
  - **Mobile (375px):** save to `agents/SITE-styles/screenshots/NN-slug-mobile.png`
- Mobile screenshots are not optional — they are required for every page, not just the home page. Mobile layout differences (collapsed navs, stacked columns, hidden elements, different font sizes) must be visible in the reference material for accurate replication.

### 1.6 Write STYLE-GUIDE.md
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
  11. **Print styles** — document all `@media print` rules found in the captured CSS files: what elements are hidden, color overrides, layout simplifications, font changes, and any `@page` rules (margins, page size). If no print styles exist, note that explicitly so Phase 3 can create them from scratch.

### 1.7 Commit capture
```
git add agents/SITE-styles/
git commit -m "Capture SITE sub-site styles (HTML, CSS, images, screenshots, style guide)"
```

---

## Phase 2: Scaffold the SCSS

### 2.1 Switch theme.scss to the new sub-site

**Important:** Each sub-site starts from the base theme, not from another sub-site's custom styles. In `theme/scss/theme.scss`:

1. **Comment out** the existing `@import "custom";` line (this is the previous sub-site's styles).
2. **Add** `@import "custom-SITE";` in its place.

This ensures the new sub-site's styles are built on top of the clean Barceloneta/Bootstrap base, without interference from another sub-site's overrides. Only one sub-site custom file should be active at a time during development.

**Note:** The base `@import "print";` line (which imports `_print.scss`) must remain active — it sits between Barceloneta's print import and the custom sub-site import, and provides shared print defaults for all sub-sites.

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

## Phase 2.5: Structural Audit — Header, Footer & Top Section

Before writing any styles, compare the markup structure of the captured reference site against the local Plone site. The original sub-sites were built on older Plone versions with different markup conventions — **the HTML structure will not match 1:1**, and these differences must be understood up front so that styling decisions account for them.

### 2.5.1 Capture the local Plone markup

Use Playwright to load `http://localhost:8080/Plone` and extract the rendered HTML for three key regions:

1. **Header** — everything from the top of the page through the navigation bar (typically `#portal-header` and `#mainnavigation-wrapper`)
2. **Top section / hero** — the first content area below the nav (banners, hero images, lead text)
3. **Footer** — everything in `#portal-footer-wrapper`

Save these HTML snippets to `agents/SITE-styles/html/local-header.html`, `local-top-section.html`, and `local-footer.html` for reference.

### 2.5.2 Compare markup against the captured reference

For each of the three regions, open the corresponding captured HTML from Phase 1 and compare it side-by-side with the local Plone markup. Look for:

**Structural differences**
- Different element nesting (e.g. the original site wraps the logo in a `<div class="logo-wrapper">` but Plone uses `<a id="portal-logo">` directly)
- Missing or extra wrapper elements (the original may have containers or grid wrappers that Plone doesn't generate)
- Different tag types (e.g. `<nav>` vs `<div>`, `<ul>` vs `<ol>`, `<section>` vs `<div>`)

**Image differences**
- Images present in the original that are missing from Plone (logos, banner photos, decorative graphics)
- Images referenced as CSS `background-image` in the original that will need to be added to `theme_images/` and referenced in SCSS
- Images referenced as `<img>` tags that will need Diazo rules or `index.html` changes to appear
- Different image paths, sizes, or formats

**Layout and semantic differences**
- Different CSS class names (the original site's classes won't exist in Plone — identify what Plone uses instead)
- Different ID attributes
- Content that's dynamically generated in Plone but static in the original (e.g. nav links come from the site structure, not hardcoded HTML)
- Elements that exist in one version but not the other (e.g. search box placement, breadcrumb position, login links)

### 2.5.3 Flag inconsistencies to the user

**This step requires human input.** After completing the comparison, present the user with a clear summary of all markup and layout inconsistencies found. Organize the report by region:

```
## Structural Audit: SITE

### Header
- [list each difference: what the original has vs what Plone generates]
- [flag any images that need to be added]
- [note any Diazo rule or index.html changes required]

### Top Section / Hero
- [list differences]
- [flag missing images or background images]

### Footer
- [list differences]
- [flag missing images or content]

### Images to Transfer
- [list all images from agents/SITE-styles/images/ that need to be
  copied to theme/theme_images/ with recommended filenames]

### Recommended Approach
- [for each major inconsistency, suggest whether to solve with
  CSS alone, Diazo rules, index.html changes, or content editing]
```

**After presenting the audit, wait at least 10 seconds before proceeding to Phase 3.** Use `sleep 10` to pause — this gives the user time to read and react to the findings. Some inconsistencies may require content to be created in Plone, images to be uploaded to the CMS, or architectural decisions about how to bridge the markup gap. These decisions affect every subsequent styling commit. If the user intervenes during or after the pause with questions or instructions, address those before continuing.

### 2.5.4 Transfer required images

After the user has reviewed the audit, or the sleep has elapsed:

1. Copy any images needed for the theme from `agents/SITE-styles/images/` to `theme/theme_images/`.
2. If images need to be added to `index.html` (e.g. a logo or decorative element), make those changes now.
3. If images will be referenced from SCSS as `background-image`, note the paths for use in Phase 3.
4. Commit image assets and any structural HTML changes separately from style changes:
   ```
   git commit -m "Add SITE theme images and structural HTML for header/footer"
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

**Print behavior**
- Should this section be visible in print? (e.g. nav, search, and footer are typically hidden)
- Does the section need color or background adjustments for print? (e.g. remove dark backgrounds, use black text)
- Are there any layout simplifications needed? (e.g. single-column, full-width)

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

### 3.5 Print styles

After all visual sections are styled, review and extend print styles for this sub-site. This should be treated as its own section with its own commit.

**Architecture:** Print styles are layered in three tiers, loaded in order:

1. **Barceloneta print** (`@plone/plonetheme-barceloneta-base/scss/print`) — hides core Plone chrome, forces black text on transparent background.
2. **LP base print** (`_print.scss`) — shared across all sub-sites. Provides `@page` margins, hides LP-specific chrome (return-to-LP banner, social links, back-to-top), simplifies layout to single-column, protects content blocks from page breaks, and adds readable link treatment. **Do not duplicate these rules in sub-site files.**
3. **Sub-site overrides** (`_custom-SITE.scss`) — only needed for elements unique to this sub-site that aren't covered by the base.

**How to build sub-site print overrides:**

1. **Check STYLE-GUIDE.md** for the print styles inventory from Phase 1. If the CSS captured from the live site has `@media print` rules beyond what the base already covers, port them where they (1) differ significantly, and (2) apply to elements present in the the new theme.
2. **Review what `_print.scss` already handles** — read the file and confirm which elements are already addressed. Do not re-declare rules that are already in the base.
3. **Add a `@media print` block at the end of `_custom-SITE.scss`** only for sub-site-specific overrides, such as:
   - Hiding sub-site-unique decorative elements (e.g. a biome switcher, a timeline slider)
   - Adjusting sub-site-specific content blocks that use custom class names not covered by the base
   - Overriding base rules where the sub-site needs different behavior (e.g. keeping a specific background image visible)
4. **If no sub-site-specific overrides are needed**, add a comment at the end of `_custom-SITE.scss`:
   ```scss
   // Print styles: base _print.scss covers all needs for this sub-site.
   ```
5. **Test with Playwright** — use `page.emulateMedia({ media: 'print' })` to preview print rendering, then screenshot and verify that:
   - Navigation, footer, and chrome are hidden
   - Content is single-column and readable
   - No sub-site-specific elements break the print layout
6. **Commit** print styles separately:
   ```
   git commit -m "Add print styles for SITE sub-site"
   ```

### 3.6 Scoping commits

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
- Use Playwright to capture full-page screenshots of the local site at each page equivalent at **both desktop (1280px) and mobile (375px)** widths.
- Compare side-by-side with the corresponding reference screenshots in `agents/SITE-styles/screenshots/` (`NN-slug.png` for desktop, `NN-slug-mobile.png` for mobile).
- Note all remaining discrepancies at both widths.

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

### 4.3.1 Print layout testing
- Use Playwright with `page.emulateMedia({ media: 'print' })` to render the print view.
- Screenshot the home page and one content-heavy detail page in print mode.
- Verify:
  - Navigation, footer, search, and all chrome elements are hidden.
  - Content renders as a single readable column with black text.
  - Images are sized appropriately and don't overflow.
  - No content blocks break awkwardly across pages (`break-inside: avoid`).
  - External link URLs are printed after the link text.
  - Tables retain visible borders.
- Fix any print-specific issues found, commit separately.

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

### 5.4 Final structural audit recap

At the end of all work, **re-present the structural inconsistencies found during Phase 2.5 to the user**. This is critical because some issues identified in the audit may have been deferred, worked around, or only partially addressed during Phases 3–5.

Output a summary that revisits each inconsistency from the Phase 2.5 audit and reports its current status:

```
## Final Structural Audit Recap: SITE

### Header
- [original inconsistency] → [resolved / partially resolved / still outstanding]
  - How it was addressed (CSS workaround, Diazo rule, content edit, etc.)
  - OR: why it remains unresolved and what would be needed to fix it

### Top Section / Hero
- [same format]

### Footer
- [same format]

### Images
- [list each image from Phase 2.5 and whether it was transferred,
  referenced in SCSS/HTML, or still missing]

### Outstanding Items
- [any inconsistencies that could not be resolved with CSS/Diazo alone
  and require manual content editing, CMS uploads, or other user action]
```

This recap ensures the user has a complete picture of what was achieved and what still needs attention, rather than having to re-derive this from the Phase 2.5 audit and subsequent commits.

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
- [ ] **Test print layout** (at least once per sub-site, required in Phase 3.5 and Phase 4.3.1)
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
│   ├── 01-home.html          (captured reference pages)
│   ├── 02-about.html
│   ├── ...
│   ├── local-header.html     (Plone markup snapshots from Phase 2.5)
│   ├── local-top-section.html
│   └── local-footer.html
├── images/
│   ├── header-logo.png       (images captured from original site)
│   ├── hero-banner.jpg
│   └── ...
└── screenshots/
    ├── 01-home.png           (desktop reference captures)
    ├── 01-home-mobile.png    (mobile reference captures)
    ├── 02-about.png
    ├── 02-about-mobile.png
    ├── ...
    └── testing/              (development test screenshots)
        ├── nav-hover-test.png
        ├── mobile-header.png
        └── ...

theme/scss/
├── _print.scss              (shared base print styles — do not modify per sub-site)
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
