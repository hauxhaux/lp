import json
from pathlib import Path
from typing import Any

import transaction
from plone import api
from zope.component.hooks import setSite


SITE_ID = "Plone"
EXPORT_ROOT = "/portal"

MIGRATION_DIR = Path("/app/migration")
FOLDER_TREE_PATH = MIGRATION_DIR / "lp_folder_tree.json"


def relative_path(old_path: str) -> str:
    """Convert exported Plone 4 paths into relative paths."""
    return old_path.removeprefix(EXPORT_ROOT).strip("/")


def ensure_folder(
    parent: Any,
    folder_id: str,
    title: str,
    description: str = "",
) -> Any:
    """Create a folder if it does not already exist."""
    existing = parent.get(folder_id)
    if existing is not None:
        return existing

    return api.content.create(
        type="Folder",
        id=folder_id,
        title=title or folder_id,
        description=description or "",
        container=parent,
        safe_id=False,
        checkConstraints=False,
    )


portal = app[SITE_ID]
setSite(portal)

folder_fti = portal.portal_types["Folder"]
folder_fti.global_allow = True

print("Connected to Plone site:")
print(portal.absolute_url())

data = json.loads(FOLDER_TREE_PATH.read_text())
data.sort(key=lambda row: row["path"].count("/"))

with api.env.adopt_roles(["Manager"]):
    for row in data:
        rel = relative_path(row["path"])

        if not rel:
            continue

        parts = rel.split("/")
        parent = portal

        for part in parts[:-1]:
            parent = parent[part]

        folder = ensure_folder(
            parent=parent,
            folder_id=row["id"],
            title=row.get("title") or row["id"],
            description=row.get("description") or "",
        )

        print(f"Ensured folder: {'/'.join(folder.getPhysicalPath())}")

    transaction.commit()
