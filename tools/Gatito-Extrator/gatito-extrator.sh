#!/bin/sh
# Gatito-Extrator — entry point
# This wrapper intentionally calls run.sh so the same flow can be tested
# directly and later integrated into a PortMaster launcher.
set +u
GAMEDIR="$(CDPATH= cd -- "$(dirname "$0")" 2>/dev/null && pwd -P)" || exit 1
exec "$GAMEDIR/run.sh" "$@"
