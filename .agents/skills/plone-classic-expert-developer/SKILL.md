---
name: plone-classic-expert-developer
description: Expert Plone 6 Classic UI development guidance. Covers backend (Python, Dexterity, plone.api) and Classic UI frontend (browser views, viewlets, portlets, themes, templates).
---

# Plone Classic UI Developer Expert

You are an expert Plone 6 Classic UI developer. You assist with full-stack development involving the Plone CMS backend and the Classic UI frontend. You do NOT work with Volto or React.

## When to Use

Use this skill when the user asks about:

- Plone 6 Classic UI frontend development.
- Diazo theming, Barceloneta, or theme add-ons.
- Browser views, viewlets, portlets, or page templates (ZPT/TAL).
- z3c.form forms and widgets.
- Static resource registration (CSS/JS bundles).
- Creating content types, behaviors, or ZCA adapters for Classic UI.
- Plone backend: Python, Dexterity, plone.api, ZCML.

## Hard Rules

These rules apply to every task. Never violate them.

1. **Plone 6 only** — Assume Plone 6+ with Python 3.x.
2. **Classic UI only** — This skill is for Classic UI (browser views, viewlets, ZPT templates, Diazo themes). Never suggest Volto, React components, or custom `plone.restapi` endpoints as the frontend approach. Note: `plone.restapi` is a core Plone 6 dependency used internally by Classic UI (e.g., TinyMCE, content browser) — just don't write custom REST services as your Classic UI frontend.
3. **Use generators for scaffolding** — Use `plonecli` (or `make add`) to scaffold new components (content types, behaviors, views, viewlets, themes, etc.). Then modify the generated files. Do not create FTI XML, ZCML registrations, or GenericSetup profiles entirely from scratch when a generator template exists.
4. **Always use the automated method** — Use `mrbob.ini` files with plonecli to avoid interactive prompts.
5. **Use `uvx cookieplone` for new projects** — Use `uvx cookieplone classic_project` for new Classic UI projects. Never use pip or zc.buildout to bootstrap unless explicitly instructed.
6. **Clean git before generating** — Before running any `plonecli add` command, ensure git history is clean. Commit any changes first.
7. **Use `plone.api`** — It is the canonical API for Plone. Use it for all standard operations.
8. **Follow community standards** — Use `plone.api`, black, flake8, Bootstrap Icons, Bootstrap 5.
9. **Prefer behaviors over custom fields** — When a user requests fields, check the Behavior Catalog before adding new schema fields.

## Decision Tree

### New project or new add-on?

- **New project** → `uvx cookieplone classic_project` (see "Creating a New Project").
- **New add-on package** → `uvx plonecli create addon` (see "Creating an Add-on Package").

### Content type: Container or Item?

- **Container** — Can hold child objects. Set `dexterity_type_base_class = Container`.
- **Item** — Leaf content, no children. Set `dexterity_type_base_class = Item`.
- IF the user doesn't specify → default to `Container`.

### Content type: Supermodel or Python schema?

- `dexterity_type_supermodel = y` → Schema defined in XML (supermodel format). Use when you need XML-based schema definitions or through-the-web editing of the schema.
- `dexterity_type_supermodel = n` → Schema defined as a Python interface on the class. **This is the default and preferred approach.**
- IF a Python class is created (`dexterity_type_create_class = y`) and supermodel is `n` → the schema is defined as a Python interface on the class.

### Frontend task type?

- **New look / brand** → Create a theme add-on (see "Creating a Barceloneta Theme Add-on").
- **External HTML template** → Use Diazo theming (see "Diazo Theming").
- **New page or UI** → Create a browser view (see "Creating a View").
- **Reusable UI snippet** → Create a viewlet (see "Creating a Viewlet").
- **Sidebar widget** → Create a portlet (see "Creating a Portlet").
- **User-facing form** → Use z3c.form (see "Creating a z3c.form Form").
- **Interactive JS behavior** → Create a Mockup pattern (see "Creating a Mockup Pattern").
- **Add CSS or JS** → Register a resource bundle (see "Registering Static Resources").

### Does an existing behavior cover the requested field?

- Check the Reference: Behavior Catalog below.
- IF a behavior provides the field → activate it in the content type's XML behaviors list.
- IF no behavior matches → add a custom schema field.

## Standard Generator Procedure

All backend component generation follows this same 3-step procedure.

### Procedure

1. **Create `mrbob.ini`** in the directory where you will run the command.
   - For `plonecli create`: the current working directory.
   - For `plonecli add`: the directory containing `pyproject.toml` (usually the `backend` folder).

   ```ini
   [variables]
   # Variables specific to each scenario (see catalog below)
   ```

2. **Run the command**:
   - For new add-ons: `uvx plonecli create -b mrbob.ini addon <package.name>`
   - For adding components: `uvx plonecli add -b mrbob.ini <template_name>`

3. **Delete `mrbob.ini`** after the command completes.

## Backend Scenario Catalog

### Creating a New Project

```bash
uvx cookieplone classic_project \
  --no-input \
  project_title="My Plone Site" \
  project_slug="my-plone-site" \
  description="A new Plone 6 Classic UI project." \
  author="Developer" \
  email="dev@example.com" \
  language_code="en"
```

### Creating an Add-on Package

**Template**: `addon` | **Command**: `uvx plonecli create -b mrbob.ini addon my.addon`

```ini
[variables]
author.name = Plone Developer
author.email = dev@plone.org
author.github.user = plone
package.description = An add-on for Plone
package.git.init = n
plone.version = 6.0.0
python.version = python3
vscode_support = n
```

### Creating a Content Type

**Template**: `content_type` | **Command**: `uvx plonecli add -b mrbob.ini content_type`

```ini
[variables]
dexterity_type_name = My Type
dexterity_type_desc = Description of the type
dexterity_type_icon_expr = puzzle
dexterity_type_supermodel = n
dexterity_type_base_class = Container
dexterity_type_global_allow = y
dexterity_type_filter_content_types = n
dexterity_type_create_class = y
dexterity_type_activate_default_behaviors = y
```

After generation, inspect `profiles/default/types/MyType.xml` to see which behaviors were auto-included before adding more.

### Creating a Behavior

**Template**: `behavior` | **Command**: `uvx plonecli add -b mrbob.ini behavior`

```ini
[variables]
behavior_name = MyBehavior
behavior_description = Description of the behavior
```

### Creating a Control Panel

**Template**: `controlpanel` | **Command**: `uvx plonecli add -b mrbob.ini controlpanel`

```ini
[variables]
controlpanel_python_class_name = MyControlPanel
```

### Creating a Form

**Template**: `form` | **Command**: `uvx plonecli add -b mrbob.ini form`

```ini
[variables]
form_python_class_name = MyForm
form_title = My Form
# form_name = my-form              # defaults to normalized class name
# form_register_for = IPloneSiteRoot
# form_permission = cmf.ManagePortal
```

### Creating an Indexer

**Template**: `indexer` | **Command**: `uvx plonecli add -b mrbob.ini indexer`

```ini
[variables]
indexer_name = my_index
```

### Creating a Subscriber

**Template**: `subscriber` | **Command**: `uvx plonecli add -b mrbob.ini subscriber`

```ini
[variables]
subscriber_handler_name = my_handler
```

The template creates a subscriber for `IObjectModifiedEvent` on `IDexterityContent`. Edit `configure.zcml` to change the event or interface.

### Creating an Upgrade Step

**Template**: `upgrade_step` | **Command**: `uvx plonecli add -b mrbob.ini upgrade_step`

```ini
[variables]
upgrade_step_title = Upgrade to new version
upgrade_step_description = Description of what this step does
```

### Creating a Vocabulary

**Template**: `vocabulary` | **Command**: `uvx plonecli add -b mrbob.ini vocabulary`

```ini
[variables]
vocabulary_name = MyVocabulary
# is_static_catalog_vocab = n
```

## Classic UI Frontend Scenario Catalog

### Creating a Barceloneta Theme Add-on

This is the recommended approach for production theming. It creates a proper Python add-on that compiles SCSS based on Bootstrap 5 / Barceloneta.

1. Scaffold the add-on (use `mrbob.ini` per the Standard Generator Procedure):

```bash
uvx plonecli create -b mrbob.ini addon plonetheme.mytheme
cd plonetheme.mytheme
uvx plonecli add theme_barceloneta
```

2. Build the theme assets:

```bash
npm install
npm run build
```

**Key customization files** inside `src/plonetheme/mytheme/theme/`:

| File | Purpose |
|------|---------|
| `scss/_variables.scss` | Override Bootstrap and Barceloneta variables (fonts, colors, spacing) |
| `scss/_maps.scss` | Override Bootstrap map variables (e.g., workflow state colors) |
| `scss/_custom.scss` | Custom SCSS rules for your design |
| `scss/theme.scss` | Main file — imports follow Bootstrap Option B order (mandatory) |
| `styles/theme.css` | Compiled CSS output (committed to the repo) |
| `index.html` | Static HTML layout used by Diazo |
| `manifest.cfg` | Diazo theme configuration |
| `rules.xml` | Diazo transformation rules |

**Development workflow**:

```bash
npm run watch   # auto-recompile on file changes
npm run build   # production build
```

**Test views** (append to your site URL, no login required):

- `@@test-rendering` — Alerts and notification variants
- `@@test-rendering-cheatsheet` — Bootstrap component library
- `@@test-rendering-icons` — Icon usage and code samples

### Diazo Theming

Use Diazo when you need to apply an external/static HTML template to Plone content without editing Plone templates. Use `theme` (not `theme_barceloneta`) for a plain Diazo setup.

```bash
uvx plonecli create -b mrbob.ini addon diazo.theme
cd diazo.theme
uvx plonecli add theme
```

**`rules.xml` fundamentals:**

```xml
<rules
    xmlns="http://namespaces.plone.org/diazo"
    xmlns:css="http://namespaces.plone.org/diazo/css"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <theme href="index.html" />

    <!-- Replace theme content placeholder with Plone's content -->
    <replace
        css:theme-children="#content"
        css:content-children="article#content"
        css:if-content="#content" />

    <!-- Drop elements not needed in the output -->
    <drop css:theme=".promo-banner" css:if-not-content=".section-front-page" />

    <!-- Insert content before/after a theme element -->
    <after css:theme="#logo" css:content="#portal-searchbox" />

    <!-- Merge attributes (e.g. CSS classes) -->
    <merge attributes="class" css:theme="body" css:content="body" />

</rules>
```

**Common Diazo directives:**

| Directive | Purpose |
|-----------|---------|
| `<theme>` | Specifies the static HTML file |
| `<replace>` | Replaces a theme node with a Plone content node |
| `<drop>` | Removes a node from the output |
| `<before>` / `<after>` | Inserts content before/after a theme node |
| `<merge>` | Merges attributes (e.g. class names) from content to theme |

**Conditions:**

- `css:if-content="body.section-front-page"` — Only on the front page
- `css:if-path="/news"` — Only on paths starting with `/news`
- `css:if-not-content=".selector"` — When selector not present in content

**`manifest.cfg` essentials:**

```ini
[theme]
title = My Theme
description = My custom Diazo theme
rules = /++theme++my.theme/rules.xml
prefix = /++theme++my.theme
doctype = <!DOCTYPE html>
```

**Performance**: Minimize rules — file size and rule count directly affect performance. Sometimes overriding a Plone template is more efficient than complex Diazo rules.

### Creating a View

Views combine a Python class with a ZPT template.

**ZCML registration** (`configure.zcml`):

```xml
<browser:page
    for="*"
    name="my-view"
    permission="zope2.View"
    class=".views.MyView"
    template="templates/my_view.pt"
    layer=".interfaces.IMyAddonLayer"
    />
```

**Python class** (`views.py`):

```python
from plone import api
from Products.Five.browser import BrowserView

class MyView(BrowserView):
    def __call__(self):
        # Do NOT put logic in __init__ — it causes misleading "View not found" errors
        return self.index()

    def some_data(self):
        return api.content.find(portal_type='Document')
```

**ZPT template** (`templates/my_view.pt`):

```xml
<html xmlns:metal="http://xml.zope.org/namespaces/metal"
      xmlns:tal="http://xml.zope.org/namespaces/tal"
      metal:use-macro="context/main_template/macros/master">
<body>
  <metal:content-core fill-slot="content-core">
    <h1 tal:content="context/title">Title</h1>
    <ul>
      <li tal:repeat="item view/some_data"
          tal:content="item/Title">Item</li>
    </ul>
  </metal:content-core>
</body>
</html>
```

**Available template slots:**

| Slot | Location |
|------|---------|
| `top_slot` | Page metadata area |
| `head_slot` | HTML `<head>` section |
| `content-core` | Main content area |
| `portlets_one_slot` | Left sidebar |
| `portlets_two_slot` | Right sidebar |

**Accessing views programmatically:**

```python
from plone import api
view = api.content.get_view(name="my-view", context=obj, request=request)

# or via getMultiAdapter:
from zope.component import getMultiAdapter
view = getMultiAdapter((context, request), name="my-view")
```

**Overriding an existing view template** — Use `z3c.jbot`: place a modified `.pt` file in your package's `overrides/` folder using the naming convention `package.module.template.pt`. Register in ZCML:

```xml
<include package="z3c.jbot" file="meta.zcml" />
<browser:jbot directory="overrides" />
```

**plonecli template:**

```ini
[variables]
view_python_class = y
view_python_class_name = MyView
view_base_class = BrowserView
view_name = my-view
view_template = y
view_template_name = my_view
view_register_for = *
# view_permission = zope2.View
```

### Creating a Viewlet

Viewlets are reusable UI snippets rendered inside a viewlet manager region on the page.

**ZCML registration:**

```xml
<browser:viewlet
    name="my.package.myviewlet"
    manager="plone.app.layout.viewlets.interfaces.IBelowContent"
    template="templates/myviewlet.pt"
    layer=".interfaces.IMyAddonLayer"
    permission="zope2.View"
    class=".viewlets.MyViewlet"
    />
```

**Python class** (`viewlets.py`):

```python
from plone.app.layout.viewlets import common as base

class MyViewlet(base.ViewletBase):
    def update(self):
        # Prepare variables — called before render()
        self.my_data = self._compute_data()

    def render(self):
        # Conditionally skip rendering
        if not self.my_data:
            return ""
        return self.index()
```

**Common viewlet managers** (all in `plone.app.layout.viewlets.interfaces`):

| Interface | Manager name | Page location |
|-----------|-------------|--------------|
| `IHtmlHead` | `plone.htmlhead` | Inside `<head>` |
| `IPortalHeader` | `plone.portalheader` | Page header |
| `IAboveContent` | `plone.abovecontent` | Above main content |
| `IAboveContentTitle` | `plone.abovecontenttitle` | Above the content title |
| `IBelowContentTitle` | `plone.belowcontenttitle` | Below the content title |
| `IAboveContentBody` | `plone.abovecontentbody` | Above the content body |
| `IBelowContentBody` | `plone.belowcontentbody` | Below the content body |
| `IBelowContent` | `plone.belowcontent` | Below main content |
| `IPortalFooter` | `plone.portalfooter` | Page footer |

Use `@@manage-viewlets` on your site to see all managers and viewlets in context.

**Control ordering and visibility** via `profiles/default/viewlets.xml`:

```xml
<!-- Reorder viewlets -->
<order manager="plone.belowcontentbody" skinname="*">
  <viewlet name="my.package.myviewlet" insert-before="*" />
</order>

<!-- Hide a viewlet -->
<hidden manager="plone.portalheader" skinname="My Theme">
  <viewlet name="plone.global_sections" />
</hidden>
```

**plonecli template:**

```ini
[variables]
viewlet_python_class_name = MyViewlet
viewlet_name = myviewlet
viewlet_template = y
viewlet_template_name = viewlet
```

The `for` defaults to `IDocument`, `manager` to `IAboveContentTitle`, `permission` to `zope2.View`. Edit `configure.zcml` to change these.

### Creating a Portlet

Portlets are sidebar widgets that can be assigned to pages or folders. They support inheritance — parent folder settings automatically apply to child items unless blocked.

A portlet requires four components, all typically in one file (e.g., `portlets/my_portlet.py`). Import base classes from `plone.app.portlets.portlets.base`:

**1. Interface** — defines configurable fields:

```python
from plone.portlets.interfaces import IPortletDataProvider
from zope import schema
from zope.interface import implementer

class IMyPortlet(IPortletDataProvider):
    message = schema.TextLine(title=u"Greeting message", required=True)
```

**2. Assignment** — stores portlet instance data:

```python
from plone.app.portlets.portlets import base

@implementer(IMyPortlet)
class MyPortletAssignment(base.Assignment):
    def __init__(self, message=u"Hello World!"):
        self.message = message

    @property
    def title(self):
        return f"Greeting: {self.message}"
```

**3. Renderer** — renders the portlet:

```python
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class MyPortletRenderer(base.Renderer):
    template = ViewPageTemplateFile("templates/my_portlet.pt")

    def message(self):
        return self.data.message

    def render(self):
        return self.template()
```

**4. Forms** — add and edit forms:

```python
class MyPortletAddForm(base.AddForm):
    schema = IMyPortlet
    label = u"Add Greeting Portlet"
    description = u"This portlet displays a greeting."

    def create(self, data):
        return MyPortletAssignment(**data)

class MyPortletEditForm(base.EditForm):
    schema = IMyPortlet
    label = u"Edit Greeting Portlet"
```

**ZCML registration** (requires `xmlns:plone="http://namespaces.plone.org/plone"`):

```xml
<plone:portlet
    title="My Portlet"
    description="A portlet that displays a greeting message"
    addview="my.package.portlets.MyPortletAddForm"
    editview="my.package.portlets.MyPortletEditForm"
    assignment=".portlets.my_portlet.MyPortletAssignment"
    renderer=".portlets.my_portlet.MyPortletRenderer"
    schema=".portlets.my_portlet.IMyPortlet"
    />
```

**plonecli template:**

```ini
[variables]
portlet_name = MyPortlet
```

### Creating a z3c.form Form

Plone uses `z3c.form` integrated through `plone.z3cform` and `plone.app.z3cform`. The `plone.autoform` package simplifies form development with its `AutoExtensibleForm` base class.

**Define a schema interface:**

```python
from zope import schema
from zope.interface import Interface

class IContactForm(Interface):
    name = schema.TextLine(title=u"Your name", required=True)
    email = schema.TextLine(title=u"Email address", required=True)
    message = schema.Text(title=u"Message", required=True)
```

**Create the form class:**

```python
from plone.autoform.form import AutoExtensibleForm
from z3c.form import button, form

class ContactForm(AutoExtensibleForm, form.Form):
    schema = IContactForm
    ignoreContext = True  # True for standalone forms not bound to content
    label = u"Contact Us"

    @button.buttonAndHandler(u"Send")
    def handleSend(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        # Process the valid data
        self.status = u"Message sent."

    @button.buttonAndHandler(u"Cancel")
    def handleCancel(self, action):
        self.request.response.redirect(self.context.absolute_url())
```

**ZCML registration** (same as a browser view):

```xml
<browser:page
    name="contact-form"
    for="*"
    class=".forms.ContactForm"
    permission="zope2.View"
    layer=".interfaces.IMyAddonLayer"
    />
```

**Key properties:**

| Property | Purpose |
|----------|---------|
| `schema` | Interface defining form fields |
| `ignoreContext` | `True` for standalone forms; `False` for edit forms bound to content |
| `label` / `description` | Display text for the form header |

**Read-only display form** — Use `WidgetsView` to show field values without editing:

```python
from plone.autoform.view import WidgetsView

class ContactView(WidgetsView):
    schema = IContactForm
```

Access widgets in the template via `view/w/fieldname` and fieldsets via `view/fieldsets`.

**Customizing Dexterity add/edit forms:**

```python
from plone.dexterity.browser import add, edit

class MyTypeAddForm(add.DefaultAddForm):
    portal_type = "MyType"
    # Set enable_form_tabbing = False to disable fieldset tabs

class MyTypeAddView(add.DefaultAddView):
    form = MyTypeAddForm

class MyTypeEditForm(edit.DefaultEditForm):
    pass
```

Use the `plonecli add form` generator (see Backend Scenario Catalog) to scaffold form boilerplate, then modify the generated files.

### Creating a Mockup Pattern

Mockup and Patternslib form the JavaScript UI toolkit for Classic UI. Patterns provide declarative, reusable UI behaviors attached to HTML elements via CSS class selectors using the `pat-` prefix:

```html
<div class="pat-autotoc" data-pat-autotoc='{"section": "h2"}'>
  <!-- Content with headings -->
</div>
```

**Creating a custom pattern:**

```bash
cd my.addon
uvx plonecli add mockup_pattern
```

When prompted, enter the pattern name **without** the `pat-` prefix (e.g., `testpattern`).

**Generated file structure:**

```
resources/pat-testpattern/
  testpattern.js     # Pattern logic
  testpattern.scss   # Pattern styles
  testpattern.test.js
  documentation.md
```

**Build the bundle:**

```bash
yarn install
yarn build
```

This generates minified JS bundles and registers them in `profiles/default/registry/bundles.xml`.

**Use in templates:**

```html
<div class="pat-testpattern" data-pat-testpattern='{"option": "value"}'>
  Content
</div>
```

**Demo view**: Access `@@addon-pattern-demo` on your site to test the pattern.

**Note:** If the add-on was installed before adding the pattern, reimport the GenericSetup profile or reinstall the add-on for proper registration.

**Resources:**
- [Mockup interactive docs](https://plone.github.io/mockup/)
- [Patternslib](https://patternslib.com/)

### Registering Static Resources

Register CSS and JavaScript bundles via `profiles/default/registry/bundles.xml`. Store compiled files in `browser/static/`.

```xml
<registry>
  <records interface="plone.bundles.interfaces.IBundleRegistry"
           prefix="plone.bundles.my-addon">
    <value key="enabled">True</value>
    <value key="csscompilation">++plone++my.addon/my-addon.css</value>
    <value key="jscompilation">++plone++my.addon/my-addon.js</value>
    <value key="depends">plone</value>
    <value key="load_defer">True</value>
  </records>
</registry>
```

**Key attributes:**

| Attribute | Purpose |
|-----------|---------|
| `enabled` | Whether the bundle loads |
| `csscompilation` | Path to compiled CSS |
| `jscompilation` | Path to compiled JS |
| `depends` | Bundle dependency (load after this); `all` or `*` = load last |
| `load_async` | Load JS asynchronously |
| `load_defer` | Load JS deferred |

**Note:** CSS defined in the Theming control panel always renders last, regardless of `depends`.

Register the static directory in ZCML:

```xml
<plone:static directory="static" name="my.addon" type="plone" />
```

### Creating a Browser Layer

Layers ensure your views and viewlets only activate when your add-on is installed.

**Interface** (`interfaces.py`):

```python
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

class IMyAddonLayer(IDefaultBrowserLayer):
    """Marker interface for my add-on browser layer."""
```

**GenericSetup** (`profiles/default/browserlayer.xml`):

```xml
<layers>
  <layer name="my.addon"
         interface="my.addon.interfaces.IMyAddonLayer" />
</layers>
```

Reference this layer in all ZCML registrations via the `layer` attribute.

## Backend Guidelines

### Using plone.api

Use `plone.api` for all standard operations:

- **Content**: `api.content.create`, `api.content.get`, `api.content.find`, `api.content.move`, `api.content.delete`, `api.content.transition`.
- **Portal**: `api.portal.get()`, `api.portal.get_tool('portal_catalog')`, `api.portal.show_message(...)`, `api.portal.send_email(...)`.
- **Users & Groups**: `api.user.create`, `api.user.get_current`, `api.user.grant_roles`, `api.group.create`, `api.group.add_user`.
- **Env**: `api.env.plone_version()`, `api.env.debug_mode()`.

### Database & ZCA

- Interact with ZODB via `plone.api` or standard accessors.
- Keep ZCML clean. Use `<include package=".subpackage" />` to organize large packages.

## Classic UI Template Reference

### TAL Statements (execution order: define → condition → repeat → content/replace → attributes → omit-tag)

```xml
<!-- Define a variable -->
<div tal:define="items python:context.objectValues()">

  <!-- Conditional rendering -->
  <ul tal:condition="items">

    <!-- Repeat over a sequence -->
    <li tal:repeat="item items">

      <!-- Set content (escapes HTML) -->
      <span tal:content="item/title">Placeholder</span>

      <!-- Replace entire element with raw HTML -->
      <div tal:replace="structure item/body_text" />

      <!-- Set attributes -->
      <a tal:attributes="href item/absolute_url; title item/title">Link</a>

      <!-- Remove the wrapping tag, output only text -->
      <span tal:omit-tag="" tal:content="item/title" />
    </li>
  </ul>
</div>
```

### TALES Expression Types

| Prefix | Example | Purpose |
|--------|---------|---------|
| _(default path)_ | `context/title` | Traverse object attributes |
| `python:` | `python:len(context.items())` | Python expression |
| `string:` | `string:Hello ${context/title}` | String interpolation |
| `not:` | `not:context/is_folderish` | Boolean negation |
| `exists:` | `exists:request/form/q` | Test if path exists |
| `nocall:` | `nocall:context/my_method` | Reference without calling |

### METAL Macros

```xml
<!-- Define a macro -->
<div metal:define-macro="my-macro">
  <metal:slot metal:define-slot="body">Default body</metal:slot>
</div>

<!-- Use the macro and fill its slot -->
<div metal:use-macro="context/@@my-view/macros/my-macro">
  <p metal:fill-slot="body">Custom body content</p>
</div>
```

### Template Global Variables

Available in all Classic UI templates without explicit definition:

| Variable | Value |
|----------|-------|
| `context` | Current content object |
| `view` | Current view instance |
| `request` | HTTP request |
| `portal` | Plone site root |
| `portal_url` | URL of the Plone site root |
| `member` | Current logged-in member (or `None`) |
| `checkPermission` | `checkPermission(perm, obj)` callable |

## Classic UI Guidelines

### Do Not Use as Classic UI Frontend Patterns

- Custom `plone.restapi` service endpoints as your UI layer (use browser views instead). Note: `plone.restapi` itself is a core Plone 6 dependency used internally by Classic UI — just don't build your frontend on custom REST endpoints.
- React/JSX components.
- Volto blocks or Volto add-ons.

### Icons

Plone 6 Classic UI uses **Bootstrap Icons** as the default icon system.

In templates:

```xml
<!-- Inline SVG via traversal -->
<span tal:replace="structure icons/alarm" />

<!-- From Python (view or viewlet) -->
<span tal:replace="structure python:view.icons.tag('alarm')" />
```

Register custom icons in `profiles/default/registry/icons.xml`:

```xml
<registry>
  <record name="plone.icon.myicon"
          interface="plone.base.interfaces.IPloneSiteRoot">
    <value>++plone++my.addon/icons/myicon.svg</value>
  </record>
</registry>
```

### Content Type Icons

Set a Bootstrap Icon name as the content type icon in the FTI XML:

```xml
<property name="icon_expr">string:${portal_url}/++plone++plone-bootstrap-icons/puzzle.svg</property>
```

## Error Handling and Recovery

### Generator failures

- IF `plonecli add` fails with a template error → check that you are in the correct directory (the one containing `pyproject.toml`).
- IF `plonecli add` produces unexpected output → verify `mrbob.ini` variable names match the template's expected variables.
- IF the generated code has registration errors → check `configure.zcml` for duplicate or missing registrations.

### Common ZCML issues

- **Component not found**: Ensure the ZCML file is included from the package's top-level `configure.zcml`.
- **Duplicate registration**: Two components registered for the same interface/name. Remove the duplicate.
- **Missing dependency**: Add `<include package="..." />` for required packages.
- **View not found**: Logic in `__init__()` raised an exception — move logic to `__call__()`.

### Theme issues

- **CSS not updating**: Check bundle is enabled in registry; clear browser cache; run `npm run build`.
- **Diazo not applied**: Verify `manifest.cfg` path and that theming is enabled in Site Setup → Theming.
- **SCSS import order errors**: `theme.scss` must follow Bootstrap Option B order — do not reorder imports.

## Reference: Field Types and Widgets

### Backend Fields (zope.schema)

```python
from zope import schema
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from z3c.relationfield.schema import RelationChoice, RelationList
from plone.app.vocabularies.catalog import CatalogSource

title = schema.TextLine(title=u"Title", required=True)
description = schema.Text(title=u"Description", required=False)
details = RichText(title=u"Details", required=False)
count = schema.Int(title=u"Count", default=0)
enabled = schema.Bool(title=u"Enabled", default=True)
start = schema.Datetime(title=u"Start Date")
image = NamedBlobImage(title=u"Image", required=False)
file = NamedBlobFile(title=u"File", required=False)
related_items = RelationList(
    title=u"Related Items",
    default=[],
    value_type=RelationChoice(title=u"Target", source=CatalogSource())
)
```

To make a field searchable in the full-text index:

```python
from plone.app.dexterity.textindexer import searchable
searchable("details")
details = RichText(title=u"Details", required=False)
```

If the user asks for a dropdown or selection from a list of values, create a vocabulary for that field.

## Reference: Behavior Catalog

### Common Behaviors (plone.app.contenttypes)

- `plone.richtext`: Rich text field for main body content.
- `plone.leadimage`: Lead Image field.
- `plone.collection`: Query criteria for Collection content types.
- `plone.tableofcontents`: Auto-generates table of contents from headings.

### General Behaviors (plone.app.dexterity)

- `plone.dublincore`: Includes title, description, tags, language, dates, creator, rights. **Use this as the default.**
- `plone.basic`: Title and description only. Use only if `plone.dublincore` is not included.
- `plone.categorization`: Tags and language. Use only if `plone.dublincore` is not included.
- `plone.publication`: Effective and expiration dates. Use only if `plone.dublincore` is not included.
- `plone.ownership`: Creator, contributor, rights. Use only if `plone.dublincore` is not included.
- `plone.shortname`: Rename an item from its edit form.
- `plone.namefromtitle`: Auto-generate URL slug from title.
- `plone.namefromfilename`: Auto-generate URL slug from filename (default for File/Image).
- `plone.textindexer`: Enables full-text indexing support for extra fields.
- `plone.translatable`: Multilingual content linking. Use only on multilingual sites.

### Additional Behaviors

- `plone.versioning` (from `plone.app.versioningbehavior`): Versioning support.
- `plone.relateditems` (from `plone.app.relationfield`): Related items field.
- `plone.locking` (from `plone.app.lockingbehavior`): Content locking.

### Event Behaviors (plone.app.event)

- `plone.eventbasic`: `start`, `end`, `whole_day`, `open_end` fields.
- `plone.eventrecurrence`: Recurrence configuration.
- `plone.eventlocation`: `location` field.
- `plone.eventattendees`: `attendees` field.
- `plone.eventcontact`: `contact_name`, `contact_email`, `contact_phone`, `event_url` fields.

### Important Note on Default Behaviors

Always inspect the generated `.xml` file for your new content type (`profiles/default/types/MyType.xml`) to see auto-included behaviors before adding more.
