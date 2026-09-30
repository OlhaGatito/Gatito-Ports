#!/bin/sh
# Gatito-Extrator — standalone test launcher
# Keeps the visual interface open for the entire extraction/diagnostic flow.
set +u

GAMEDIR="$(CDPATH= cd -- "$(dirname "$0")" 2>/dev/null && pwd -P)" || exit 1
cd "$GAMEDIR" || exit 1

LOGDIR="\${GATITO_LOG_DIR:-$GAMEDIR/logs}"
mkdir -p "$LOGDIR" 2>/dev/null || true
LOG="\${GATITO_LOG:-$LOGDIR/gatito-extrator.log}"

GAME_DIR="\${GATITO_GAME_DIR:-$GAMEDIR/test-game}"
ENGINE="\${GATITO_ENGINE:-$GAMEDIR/../gatito-extract/gatito-extract-v2.py}"
RECIPE="\${GATITO_RECIPE:-$GAMEDIR/extractor.example.json}"
PYTHON="\${PYTHON:-python3}"

INPUT=""
ABI=""
DEMO=0
NO_PAUSE=0

while [ "$#" -gt 0 ]; do
    case "$1" in
        --game-dir) GAME_DIR="$2"; shift 2 ;;
        --recipe) RECIPE="$2"; shift 2 ;;
        --input) INPUT="$2"; shift 2 ;;
        --abi) ABI="$2"; shift 2 ;;
        --demo) DEMO=1; shift ;;
        --no-pause) NO_PAUSE=1; shift ;;
        *) echo "[Gatito-Extrator] argumento desconhecido: $1" >>"$LOG"; shift ;;
    esac
done

export GATITO_EXTRATOR_LOG="$LOG"

set -- "$PYTHON" "$GAMEDIR/gatito-ui.py" \
    --game-dir "$GAME_DIR" \
    --recipe "$RECIPE" \
    --engine "$ENGINE" \
    --log "$LOG"
[ -n "$INPUT" ] && set -- "$@" --input "$INPUT"
[ -n "$ABI" ] && set -- "$@" --abi "$ABI"
[ "$DEMO" -eq 1 ] && set -- "$@" --demo
[ "$NO_PAUSE" -eq 1 ] && set -- "$@" --no-pause

exec "$@"
