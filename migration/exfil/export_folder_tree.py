portal = context.portal_url.getPortalObject()
catalog = portal.portal_catalog

brains = catalog.searchResults(
    portal_type=["Folder", "Large Plone Folder"],
    sort_on="path"
)

def esc(value):
    if value is None:
        return ""
    value = str(value)
    value = value.replace("\\", "\\\\")
    value = value.replace('"', '\\"')
    value = value.replace("\n", "\\n")
    value = value.replace("\r", "\\r")
    value = value.replace("\t", "\\t")
    return value

lines = []
lines.append("[")

first = 1

for brain in brains:
    obj = brain.getObject()

    path = "/".join(obj.getPhysicalPath())
    parent_path = "/".join(obj.aq_parent.getPhysicalPath())

    owner = ""

    try:
        owner = obj.Creator()
    except:
        owner = ""

    local_roles = []

    try:
        for userid, roles in obj.get_local_roles():
            role_items = []
            for role in roles:
                role_items.append('"%s"' % esc(role))

            local_roles.append(
                '{"userid": "%s", "roles": [%s]}' % (
                    esc(userid),
                    ",".join(role_items)
                )
            )
    except:
        pass

    exclude_from_nav = 0

    try:
        exclude_from_nav = obj.getExcludeFromNav()
    except:
        try:
            exclude_from_nav = obj.exclude_from_nav
        except:
            exclude_from_nav = 0

    if not first:
        lines.append(",")
    first = 0

    lines.append("{")
    lines.append('"path": "%s",' % esc(path))
    lines.append('"parent_path": "%s",' % esc(parent_path))
    lines.append('"id": "%s",' % esc(obj.getId()))
    lines.append('"title": "%s",' % esc(obj.Title()))
    lines.append('"description": "%s",' % esc(obj.Description()))
    lines.append('"portal_type": "%s",' % esc(obj.portal_type))
    lines.append('"review_state": "%s",' % esc(getattr(brain, "review_state", "")))
    lines.append('"owner": "%s",' % esc(owner))
    lines.append('"exclude_from_nav": %s,' % str(bool(exclude_from_nav)).lower())
    lines.append('"local_roles": [%s]' % ",".join(local_roles))
    lines.append("}")

lines.append("]")

return "\n".join(lines)
