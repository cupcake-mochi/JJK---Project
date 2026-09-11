#!/usr/bin/env bash
# Roda os validadores na ordem do subir.sh e mostra so' o resumo e as falhas.
RAIZ="/media/mizuki/HD Externo II/Claude/Claude 2"
f=0; p=0
roda() {
  out="$(python3 "$1" 2>&1)"; rc=$?
  pul="$(printf '%s\n' "$out" | grep -i 'PULAD' | grep -viE '^[[:space:]]*~*[[:space:]]*PULADA\.?[[:space:]]*$' | head -3)"
  if [ $rc -ne 0 ]; then f=$((f+1)); echo "  FALHA $1"; printf '%s\n' "$out" | grep -E '(^| )(!!|>>>|- )' | grep -v 'TUDO OK' | head -14 | sed 's/^ */    | /'
     printf '%s\n' "$out" | grep -q '^Traceback' && printf '%s\n' "$out" | tail -5 | sed 's/^/    | /'
  elif [ -n "$pul" ]; then p=$((p+1)); echo "  ok*   $1 — PULOU:"; printf '%s\n' "$pul" | sed 's/^ */    | /'
  else echo "  ok    $1"; fi
}
cd "$RAIZ/sistema/03-mecanica" && for v in conferir-*.py; do roda "$v"; done
cd "$RAIZ" && roda conferir-repositorio.py
cd "$RAIZ/manual/matematica" && for v in pac7.py v7.py; do roda "$v"; done
echo "  == $f falha(s), $p com PULADA"
