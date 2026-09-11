#!/usr/bin/env bash
# Replica o passo 0 do subir.sh: copia o recorte velho para finalizado/ e acerta
# as duas versoes do README da entrega. NAO commita nem da push na entrega.
set -u
RAIZ="/media/mizuki/HD Externo II/Claude/Claude 2"
cd "$RAIZ" || exit 1
ENT="$RAIZ/finalizado"; copiados=0
while IFS="$(printf '\t')" read -r fonte copia; do
  [ -n "$fonte" ] || continue
  [ -f "$fonte" ] || { echo "  falta a FONTE: ${fonte#$RAIZ/}"; continue; }
  if [ ! -f "$copia" ] || ! cmp -s "$fonte" "$copia"; then
    mkdir -p "$(dirname "$copia")"; cp "$fonte" "$copia" && { echo "  copiado  ${copia#$RAIZ/}"; copiados=$((copiados+1)); }
  fi
done < <(python3 conferir-repositorio.py --recorte 2>/dev/null)
RME="$ENT/README.md"
VER_ENT="$(python3 conferir-repositorio.py --versao-recorte 2>/dev/null)"
if [ -f "$RME" ] && [ -n "$VER_ENT" ] && ! grep -q "\*\*Recorte da v$VER_ENT\.\*\*" "$RME"; then
  sed -i -E "s/\*\*Recorte da v[0-9]+\.[0-9]+\.\*\*/**Recorte da v$VER_ENT.**/g" "$RME"; echo "  ajustado README da entrega -> v$VER_ENT"; copiados=$((copiados+1))
fi
VER_MAN="$(python3 conferir-repositorio.py --versao-manual 2>/dev/null)"
if [ -f "$RME" ] && [ -n "$VER_MAN" ]; then
  ATR=$(grep -oE '\*\*v7\.[0-9]+\*\*' "$RME" | grep -cv "^\*\*v$VER_MAN\*\*$" || true)
  if [ "${ATR:-0}" -gt 0 ]; then sed -i -E "s/\*\*v7\.[0-9]+\*\*/**v$VER_MAN**/g" "$RME"; echo "  ajustado README da entrega -> manual v$VER_MAN"; copiados=$((copiados+1)); fi
fi
echo "  entrega: $copiados arquivo(s) mexido(s) (recorte v$VER_ENT, manual v$VER_MAN)"
