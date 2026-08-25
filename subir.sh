#!/usr/bin/env bash
# Confere, commita e sobe. Um comando so'.
#
#   ./subir.sh "o que mudou"
#   ./subir.sh                  <- usa mensagem-de-commit.txt, se existir
#
# Ele NAO commita se algum validador falhar. O motivo esta no README: um commit
# que registra regra quebrada e' pior que nao commitar, porque daqui a tres
# versoes ninguem sabe em qual commit ela entrou.
#
# Por que este script existe: o assistente consegue editar os arquivos e rodar os
# validadores, mas nao consegue dar git commit nesta pasta — o mount expoe tudo
# com permissao fixa e rejeita o chmod que o git faz ao finalizar um objeto.
# Entao ele deixa a mensagem pronta em mensagem-de-commit.txt e voce roda isto.

set -u
cd "$(dirname "$0")" || exit 1
RAIZ="$(pwd)"

vermelho() { printf '\033[31m%s\033[0m\n' "$1"; }
verde()    { printf '\033[32m%s\033[0m\n' "$1"; }
amarelo()  { printf '\033[33m%s\033[0m\n' "$1"; }

# O erro do push NAO vai para /dev/null. Ate a v0.44 ia, e o script chutava o
# motivo ("se ele pediu senha...") em vez de mostrar o que o git disse — o que
# transforma rede caida, token vencido e repositorio errado no mesmo texto.
subir_para_o_remoto() {
    SAIDA_PUSH="$(git push 2>&1)"
    if [ $? -eq 0 ]; then
        verde "  push: subiu"
        return 0
    fi
    vermelho "  push: FALHOU — e o git disse isto:"
    printf '%s\n' "$SAIDA_PUSH" | sed 's/^/    | /'
    echo
    amarelo "  O commit JA ESTA FEITO. Nada se perdeu; falta so' o push."
    echo
    echo "  'Repository not found' quer dizer autenticacao, e nao repositorio"
    echo "  sumido — o GitHub responde 404 em vez de 403 para nao contar que um"
    echo "  repositorio privado existe. (Este aqui e' publico desde 13/08/2026,"
    echo "  entao hoje esse erro so' deve aparecer no push, que sempre autentica.)"
    echo
    echo "  Aconteceu em 13/08/2026, e a receita que resolveu foi esta — na ordem,"
    echo "  porque a terceira linha sozinha NAO resolve:"
    echo "    gh auth switch --user cupcake-mochi"
    echo "    printf 'protocol=https\\nhost=github.com\\n\\n' | git credential reject"
    echo "    gh auth setup-git"
    echo "    git push"
    echo
    echo "  O que estava acontecendo: o git guardava um token JA RECUSADO pelo"
    echo "  GitHub, com o nome de usuario certo. 'gh auth login' nao troca esse"
    echo "  token — ele grava no store do gh, e o helper velho responde primeiro."
    echo "  So' o 'git credential reject' apaga o antigo. Para ver quem o git esta"
    echo "  usando, sem vazar o token na tela:"
    echo "    printf 'protocol=https\\nhost=github.com\\n\\n' | git credential fill | grep '^username='"
    echo
    echo "  Se falou em rede, host ou timeout, e' so' repetir: git push"
    echo "  Nos dois casos, NAO precisa commitar de novo."
    return 1
}

# --------------------------------------------------------------------------
# A entrega e' um repositorio SEPARADO e nao tem script proprio. Ate a v0.148 a
# copia era digitada a mao, e ela derivou quatro vezes: cinco versoes na v0.121,
# duas na v0.135, uma pulada na v0.145, e duas pecas mais os dois artefatos na
# v0.148. Toda vez o conserto foi o mesmo `cp`, e toda vez alguem teve de
# lembrar. Agora ele acontece aqui, ANTES dos validadores, para a checagem 7 ver
# o estado sincronizado.
#
# A lista NAO mora aqui. Ela sai de `conferir-repositorio.py --recorte`, que e' o
# mesmo lugar de onde a checagem 7.1 le — uma lista, um dono. E a versao sai de
# `--versao-recorte`, cujo dono e' a entrada do topo do CHANGELOG.
#
# Nada disso e' silencioso: cada arquivo copiado aparece na tela. Um conserto que
# ninguem ve e' pior que o defeito, porque ele esconde que a entrega estava velha.
echo
echo "=== 0. a entrega ==="

ENT="$RAIZ/finalizado"
copiados=0

if [ ! -d "$ENT" ]; then
    amarelo "  finalizado/ nao existe neste clone — nada a sincronizar."
    echo "     (ele e' ignorado pelo .gitignore, entao um clone limpo nao carrega o recorte)"
else
    while IFS="$(printf '\t')" read -r fonte copia; do
        [ -n "$fonte" ] || continue
        if [ ! -f "$fonte" ]; then
            amarelo "  falta a FONTE: ${fonte#$RAIZ/}"
            continue
        fi
        if [ ! -f "$copia" ] || ! cmp -s "$fonte" "$copia"; then
            mkdir -p "$(dirname "$copia")"
            if cp "$fonte" "$copia"; then
                printf '  copiado  %s\n' "${copia#$RAIZ/}"
                copiados=$((copiados + 1))
            else
                vermelho "  FALHOU ao copiar para ${copia#$RAIZ/}"
                exit 1
            fi
        fi
    done < <(python3 conferir-repositorio.py --recorte 2>/dev/null)

    # A versao do recorte no README da entrega — o unico arquivo escrito a mao la.
    RME_ENT="$ENT/README.md"
    VER_ENT="$(python3 conferir-repositorio.py --versao-recorte 2>/dev/null)"
    if [ -f "$RME_ENT" ] && [ -n "$VER_ENT" ]; then
        if ! grep -q "\*\*Recorte da v$VER_ENT\.\*\*" "$RME_ENT"; then
            sed -i -E "s/\*\*Recorte da v[0-9]+\.[0-9]+\.\*\*/**Recorte da v$VER_ENT.**/g" "$RME_ENT"
            printf '  ajustado finalizado/README.md — recorte agora diz v%s\n' "$VER_ENT"
            copiados=$((copiados + 1))
        fi
    fi

    if [ "$copiados" -eq 0 ]; then
        verde "  a entrega ja estava em dia."
    fi
fi

# O lembrete vai num trap e nao no fim do script, porque o script tem TRES
# saidas antes do fim: validador reprovado, nada a commitar, e so'-push. Nas tres
# a entrega ja foi mexida, e nas tres o lembrete precisa aparecer.
lembrete_entrega() {
    [ "${copiados:-0}" -gt 0 ] || return 0
    echo
    amarelo "A entrega mudou (${copiados} arquivo(s)) e ela commita A MAO — nao tem script:"
    echo "  cd finalizado && git add -A && git commit -m \"recorte da v${VER_ENT:-}\" && git push && cd .."
}
trap lembrete_entrega EXIT

# --------------------------------------------------------------------------
echo
echo "=== 1. os validadores ==="

falhou=0
pulou=0
motivos_pulo=""

# Ate a v0.100 este bloco jogava a saida no /dev/null e imprimia so' "FALHA".
# O motivo ficava a um comando de distancia — e da ultima vez que um validador
# reprovou, a causa era UMA linha: o prompt de retomada citava um caminho que
# so' existe dentro do container do assistente. Ler isso custou uma sessao.
#
# Agora a saida e' guardada em toda rodada, e ela e' usada nos dois lados:
# no vermelho o motivo aparece na hora, e no verde ela e' lida atras de
# PULADA — que e' o verde que nao e' verde.
rodar_validador() {
    saida_val=""
    if saida_val="$(python3 "$1" 2>&1)"; then
        # o `grep -v` tira o marcador nu que alguns imprimem dentro do bloco
        # da checagem — ele diz que pulou e nao diz o que, e enche a tela
        pulos="$(printf '%s\n' "$saida_val" | grep -i 'PULAD' \
                 | grep -viE '^[[:space:]]*~*[[:space:]]*PULADA\.?[[:space:]]*$' | head -4)"
        if [ -n "$pulos" ]; then
            amarelo "  ok*   $1 — mas PULOU checagem:"
            printf '%s\n' "$pulos" | sed 's/^ */    | /'
            motivos_pulo="$motivos_pulo$pulos"
            pulou=1
        else
            printf '  ok    %s\n' "$1"
        fi
    else
        vermelho "  FALHA $1 — e ele disse isto:"
        # as linhas de erro que os validadores imprimem, sem a linha de sucesso
        motivo="$(printf '%s\n' "$saida_val" \
                  | grep -E '(^| )(!!|>>>|- )' | grep -v 'TUDO OK' | head -12)"
        # e se ele morreu de excecao, nada disso casa: o que vale e o fim da
        # saida. Sem esta metade o script mostrava um ">>> TUDO OK" de um bloco
        # anterior como se fosse o motivo da falha — medido na v0.101.
        if printf '%s\n' "$saida_val" | grep -q '^Traceback' || [ -z "$motivo" ]; then
            motivo="$motivo
$(printf '%s\n' "$saida_val" | tail -6)"
        fi
        printf '%s\n' "$motivo" | grep -v 'TUDO OK' | sed '/^$/d' | sed 's/^ */    | /'
        falhou=1
    fi
}

cd "$RAIZ/sistema/03-mecanica" || exit 1
for f in conferir-*.py; do
    rodar_validador "$f"
done

cd "$RAIZ" || exit 1
rodar_validador conferir-repositorio.py

cd "$RAIZ/manual/matematica" || exit 1
for f in pac7.py v7.py; do
    rodar_validador "$f"
done
cd "$RAIZ" || exit 1

if [ "$falhou" -ne 0 ]; then
    echo
    vermelho "Algum validador falhou. Nada foi commitado."
    echo "As linhas de erro estao acima. Para ver o resto:"
    echo "  cd sistema/03-mecanica && python3 conferir-XXXX.py"
    exit 1
fi

# Pular NAO trava o commit, de proposito: uma biblioteca que falta nao e' regra
# quebrada. Mas o aviso e' amarelo e aparece em toda rodada, porque cinco dos
# validadores leem o .docx do manual e sem python-docx eles conferem menos.
if [ "$pulou" -ne 0 ]; then
    echo
    amarelo "Algum validador PULOU checagem — o verde acima vale menos do que parece."
    if printf '%s' "$motivos_pulo" | grep -qi 'docx'; then
        echo "  Falta a biblioteca que le o manual:"
        echo "  pip install python-docx --break-system-packages"
    fi
fi

# --------------------------------------------------------------------------
echo
echo "=== 2. o que mudou ==="

# Arvore limpa NAO quer dizer nada a fazer: pode haver commit sem push. Ate a
# v0.44 este ramo saia com codigo 0 aqui, e ai dois commits ficaram parados no
# disco enquanto o script dizia "nada a fazer" — o unico jeito de descobrir era
# ler os refs na mao.
if [ -z "$(git status --porcelain)" ]; then
    RAMO="$(git rev-parse --abbrev-ref HEAD)"
    LOCAL="$(git rev-parse HEAD)"
    REMOTO="$(git rev-parse "origin/$RAMO" 2>/dev/null || echo 'nenhum')"
    if [ "$LOCAL" != "$REMOTO" ]; then
        amarelo "  Nada novo para commitar, mas o $RAMO local nao bate com o origin/$RAMO."
        echo "    local : $LOCAL"
        echo "    remoto: $REMOTO"
        echo
        echo "=== so' o push, entao ==="
        subir_para_o_remoto || exit 1
        echo
        verde "Pronto."
        exit 0
    fi
    amarelo "  Nada mudou, e nao ha commit sem push. Nada a fazer."
    exit 0
fi
git status --short | sed 's/^/  /'

# --------------------------------------------------------------------------
echo
echo "=== 3. a mensagem ==="

MSG_ARQ="mensagem-de-commit.txt"
if [ "$#" -ge 1 ] && [ -n "$1" ]; then
    MSG="$1"
    echo "  (da linha de comando)"
    echo "$MSG" | sed 's/^/  | /'
elif [ -f "$MSG_ARQ" ]; then
    MSG=""
    echo "  (de $MSG_ARQ)"
    sed 's/^/  | /' "$MSG_ARQ"
else
    vermelho "  Sem mensagem. Passe uma como argumento ou crie $MSG_ARQ."
    echo '  Exemplo:  ./subir.sh "v0.28 — tabela de XP"'
    exit 1
fi

# --------------------------------------------------------------------------
echo
echo "=== 4. commit e push ==="

git add -A || { vermelho "  git add falhou"; exit 1; }

if [ -n "$MSG" ]; then
    git commit -q -m "$MSG" || { vermelho "  git commit falhou"; exit 1; }
else
    git commit -q -F "$MSG_ARQ" || { vermelho "  git commit falhou"; exit 1; }
    rm -f "$MSG_ARQ"      # usada, entao sai do caminho
fi

echo "  commit: $(git log --oneline -1)"

subir_para_o_remoto || exit 1

echo
verde "Pronto."
