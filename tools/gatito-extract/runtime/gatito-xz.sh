#!/bin/sh
# Gatito XZ fallback runner: INPUT OUTPUT
set -u
SRC="$1"
DST="$2"
say() { printf 'GATITO_XZ|%s\n' "$*"; }
if [ ! -s "$SRC" ]; then say "ERRO: entrada XZ ausente/vazia"; exit 10; fi
mkdir -p "$(dirname "$DST")"
try_pipe() {
  NAME="$1"; shift
  say "Tentando: $NAME"
  if "$@" < "$SRC" > "$DST" 2>/tmp/gatito-xz.err && [ -s "$DST" ]; then
    say "OK: $NAME"; return 0
  fi
  ERR="$(tr '\n' ' ' </tmp/gatito-xz.err 2>/dev/null | cut -c1-180)"
  say "ERRO: $NAME $ERR"
  rm -f "$DST"
  return 1
}
if command -v xz >/dev/null 2>&1; then
  if try_pipe 'xz -dc' xz -dc; then exit 0; fi
else say 'INDISPONÍVEL: xz'; fi
if command -v xzdec >/dev/null 2>&1; then
  if try_pipe xzdec xzdec; then exit 0; fi
else say 'INDISPONÍVEL: xzdec'; fi
for TOOL in lzmadec unlzma lzma; do
  if command -v "$TOOL" >/dev/null 2>&1; then
    case "$TOOL" in
      unlzma) if try_pipe 'unlzma -c' "$TOOL" -c; then exit 0; fi ;;
      lzma) if try_pipe 'lzma -dc' "$TOOL" -dc; then exit 0; fi ;;
      lzmadec) if try_pipe lzmadec "$TOOL"; then exit 0; fi ;;
    esac
  fi
done
if command -v busybox >/dev/null 2>&1 && busybox xz --help >/dev/null 2>&1; then
  if try_pipe 'busybox xz -dc' busybox xz -dc; then exit 0; fi
fi
say 'FALHA: nenhuma rota XZ/LZMA disponível'
say 'Diagnóstico: xz pode exigir liblzma.so; verificar PATH e ABI'
exit 20
