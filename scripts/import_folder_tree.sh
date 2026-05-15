#/bin/sh

docker compose run --rm backend sh -lc '
SECURITY_POLICY_IMPLEMENTATION=PYTHON \
DEBUG_MODE=off \
VERBOSE_SECURITY=off \
DEFAULT_ZPUBLISHER_ENCODING=utf-8 \
ZOPE_FORM_MEMORY_LIMIT=1MB \
ZOPE_FORM_DISK_LIMIT=1GB \
ZOPE_FORM_MEMFILE_LIMIT=4KB \
ZODB_CACHE_SIZE=30000 \
CLIENT_HOME=/app/var \
bin/zconsole run /app/etc/zope.conf /app/src/lp.content/scripts/import_folders.py
'
