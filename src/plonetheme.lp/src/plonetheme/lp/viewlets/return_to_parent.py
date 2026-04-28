"""Return-to-parent banner shown at the top of every lineage child site.

When the current request is rendered inside a folder marked as a
collective.lineage child site, this viewlet emits a single banner
linking back to the parent navigation root (typically the LP portal).

The element id (``return-to-lp-banner``) is what every per-site theme's
SCSS hooks into for branded styling — this viewlet is theme-agnostic and
only emits structure.
"""

from collective.lineage.interfaces import IChildSite
from collective.lineage.utils import parent_site
from plone import api
from plone.app.layout.viewlets.common import ViewletBase


class ReturnToParentViewlet(ViewletBase):
    """Render a return-to-parent banner inside lineage child sites."""

    def update(self):
        super().update()
        self.parent_url = None
        self.parent_title = None

        navroot = api.portal.get_navigation_root(self.context)
        if not IChildSite.providedBy(navroot):
            # Not inside a lineage child site — nothing to render.
            return

        # collective.lineage.parent_site() walks up from getSite() to the
        # nearest IChildSite or IPloneSiteRoot ancestor.
        parent = parent_site()
        if parent is None or parent is navroot:
            return

        self.parent_url = parent.absolute_url()
        self.parent_title = parent.Title() or "parent"

    def available(self):
        return self.parent_url is not None

    def render(self):
        if not self.available():
            return ""
        return self.index()
