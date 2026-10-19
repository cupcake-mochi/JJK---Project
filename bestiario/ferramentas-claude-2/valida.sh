#!/usr/bin/env bash
# Roda os validadores na ordem do subir.sh e mostra so' o resumo e as falhas.
RAIZ="$(cd "$(dirname "$0")/../.." && pwd)" || exit 1
f=0; p=0
roda() {
  out="$(python3 "$@" 2>&1)"; rc=$?
  pul="$(printf '%s\n' "$out" | grep -i 'PULAD' | grep -viE '^[[:space:]]*~*[[:space:]]*PULADA\.?[[:space:]]*$' | head -3)"
  if [ $rc -ne 0 ]; then f=$((f+1)); echo "  FALHA $1"; printf '%s\n' "$out" | grep -E '(^| )(!!|>>>|- )' | grep -v 'TUDO OK' | head -14 | sed 's/^ */    | /'
     printf '%s\n' "$out" | grep -q '^Traceback' && printf '%s\n' "$out" | tail -5 | sed 's/^/    | /'
  elif [ -n "$pul" ]; then p=$((p+1)); echo "  ok*   $1 — PULOU:"; printf '%s\n' "$pul" | sed 's/^ */    | /'
  else echo "  ok    $1"; fi
}
cd "$RAIZ/sistema/03-mecanica" || exit 1
for v in conferir-*.py; do roda "$v"; done
cd "$RAIZ" || exit 1
roda conferir-repositorio.py
cd "$RAIZ/sistema/05-material/livro" || exit 1
roda conferir-voz.py --legado-sem-regressao
echo "  == $f falha(s), $p com PULADA"

[ "$f" -eq 0 ]
