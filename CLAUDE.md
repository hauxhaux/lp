# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is **plonetheme.lp**, a Plone 6.0+ CMS theme addon. It is a Python package (using Plone's Diazo/XSL transformation system) combined with a Node.js SCSS build pipeline. The theme inherits from Plone's Barceloneta base and uses Bootstrap 5.3. It uses a Classic Plone frontend.

Docker is used for running a full Plone environment. The Python package is mounted into the container for live development.

### Theme / Frontend

All commands run from `src/plonetheme.lp/src/plonetheme/lp/theme/`:

```bash
npm install         # Install Node deps (once per machine)
npm run watch       # Watch SCSS, auto-compile on change (keep running during dev)
npm run build       # Full build: compile → autoprefixer → minify
npm run css-lint    # Run stylelint on SCSS
```

### Docker

```bash
./devbuild.sh       # docker compose up -d --build
```
Plone is available at `http://localhost:8080` with credentials `admin`/`admin`.

## Architecture

### How it fits together

1. **Docker** (`docker-compose.yml`) runs `plone/plone-backend:6.1.3` and mounts `src/plonetheme.lp` into the container, so Python changes are live.
2. **Python package** (`src/plonetheme.lp/`) is a standard Plone addon registered via ZCML. It installs the Diazo theme via a GenericSetup profile.
3. **Diazo theme** (`theme/`) uses `rules.xml` (XSL transformation rules) to map Plone's rendered HTML onto `index.html` (the theme template). `manifest.cfg` registers the theme and points to the compiled CSS.
4. **SCSS pipeline** compiles `scss/theme.scss` → `styles/theme.css` (expanded) and `styles/theme.min.css` (minified). The production site uses `theme.min.css` as declared in `manifest.cfg`.

### Python package layout

```
src/plonetheme/lp/
├── configure.zcml       # Main ZCML — wires everything together
├── interfaces.py        # IBrowserLayer for theme-specific views
├── testing.py           # Test layer fixtures (INTEGRATION/FUNCTIONAL/ACCEPTANCE)
├── profiles/
│   ├── default/         # GenericSetup install profile (theme.xml, metadata.xml, etc.)
│   └── uninstall/       # GenericSetup uninstall profile
├── content/             # Custom content types
├── controlpanels/       # Control panel views
├── serializers/         # plone.restapi serializers
├── vocabularies/        # Controlled vocabularies
├── upgrades/            # Profile upgrade steps
└── theme/               # Diazo theme resources (see below)
```

### Theme layout

```
theme/
├── manifest.cfg         # Theme metadata; maps to rules.xml and production CSS
├── rules.xml            # Diazo XSL rules — the heart of the theme transformation
├── index.html           # Bootstrap 5.3 HTML shell that Diazo injects content into
├── scss/
│   ├── theme.scss       # Entry point; imports Bootstrap, Barceloneta, then custom files
│   ├── _variables.scss  # Bootstrap/theme variable overrides (primary: #4AC728 green)
│   ├── _maps.scss       # Plone/Bootstrap color map extensions
│   └── _custom.scss     # All custom styles: grid layouts, buttons, blocks, typography
├── styles/
│   ├── theme.css        # Compiled (expanded) — used in dev
│   └── theme.min.css    # Minified — used in production (referenced in manifest.cfg)
├── theme_images/        # Static image assets
└── tinymce-templates/   # TinyMCE editor templates
```

### Testing

Tests use `pytest` with the `pytest-plone` plugin. Three test layers are defined in `testing.py`:
- `INTEGRATION_TESTING` — unit/integration tests (no browser)
- `FUNCTIONAL_TESTING` — functional tests with WSGI
- `ACCEPTANCE_TESTING` — browser tests (Selenium)

Fixtures are auto-wired in `tests/conftest.py` from the testing layers.

### Key configuration files

| File | Purpose |
|---|---|
| `src/plonetheme.lp/pyproject.toml` | Package metadata, deps, ruff/pytest config |
| `src/plonetheme.lp/mx.ini` | mxdev: manages VCS/override deps for development |
| `src/plonetheme.lp/instance.yaml` | Zope instance template (ZCML includes, admin pw) |
| `src/plonetheme.lp/Makefile` | All dev tasks; uses `uv` as package manager |
| `docker-compose.yml` | Mounts theme into Plone 6.1.3 container |

### Styling conventions

- Custom color palette is set as CSS custom properties in `_custom.scss`
- Block-level styles use classes like `.feature-block`, `.blue-block`, `.orange-block`
- Grid layouts: `.layout-2col`, `.layout-3col`, etc. with gap variants
- Button variants: `.btn-orange`, `.btn-red`, `.btn-blue`, `.cta-button`
- Spacing: `.space`, `.pad`, `.gap` utility classes

The SCSS build uses `@plone/plonetheme-barceloneta-base` as a Node dependency — its paths are resolved via `--load-path=node_modules` in the sass compile step.

## Development Guidelines

- **Work incrementally.** Make small, focused changes. Do not produce large blocks of code all at once.
- **Follow Plone best practices.** Use GenericSetup profiles, ZCML, and standard Plone patterns — avoid workarounds.
- **Keep solutions simple.** If the right approach is unclear, ask before implementing.
- **Goal:** Recreating specific sub-sites of `https://landscapepartnership.org` within this theme. Reference crawls and style guides are in `agents/`.

## Workflow: Making and Testing Theme Changes

Follow this procedure for every theme/CSS task:

### 1. Before making changes
- Invoke the `plone-classic-expert-developer` skill for any Plone/theme work before starting.
- Run `npm run watch` in the background (from `src/plonetheme.lp/src/plonetheme/lp/theme/`) — keep it running during the session. Do NOT use `npm run build` during active dev.

### 2. Making changes
- Edit SCSS files. The watch process recompiles automatically.
- Wait no more than 2 seconds after saving before checking the output — do not use long sleeps.

### 3. After making changes — always test with Playwright
- Invoke the `playwright-cli` skill to open `http://localhost:8080` (admin/admin).
- Test all relevant interactions: hover states, dropdowns, active states, mobile widths.
- **Screenshots must go in `agents/` with a contextual name** (e.g. `agents/nav-hover-gold-test.png`). Never save screenshots to the project root.
- After testing, ask the user whether to clean up the test screenshots.

### Plone dev notes
- Site: `http://localhost:8080/Plone` — credentials `admin` / `admin`
- Barceloneta uses `ul.dropdown` (not `ul.submenu`) for nav dropdowns
- Use ID selectors (`#portal-globalnav`) for specificity over Bootstrap — avoid `!important`
- CSS custom properties: always use `--variable-name` (two dashes), not `var(variable-name)`
