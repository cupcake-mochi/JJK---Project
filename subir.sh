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

# --------------------------------------------------------------------------
echo
echo "=== 1. os validadores ==="

falhou=0

cd "$RAIZ/sistema/03-mecanica" || exit 1
for f in conferir-*.py; do
    if python3 "$f" > /dev/null 2>&1; then
        printf '  ok    %s\n' "$f"
    else
        vermelho "  FALHA $f"
        falhou=1
    fi
done

cd "$RAIZ" || exit 1
if python3 conferir-repositorio.py > /dev/null 2>&1; then
    printf '  ok    conferir-repositorio.py\n'
else
    vermelho "  FALHA conferir-repositorio.py"
    falhou=1
fi

cd "$RAIZ/manual/matematica" || exit 1
for f in pac7.py v7.py; do
    if python3 "$f" > /dev/null 2>&1; then
        printf '  ok    %s\n' "$f"
    else
        vermelho "  FALHA $f"
        falhou=1
    fi
done
cd "$RAIZ" || exit 1

if [ "$falhou" -ne 0 ]; then
    echo
    vermelho "Algum validador falhou. Nada foi commitado."
    echo "Rode o que falhou sozinho para ver o erro inteiro:"
    echo "  cd sistema/03-mecanica && python3 conferir-XXXX.py"
    exit 1
fi

# --------------------------------------------------------------------------
echo
echo "=== 2. o que mudou ==="

if [ -z "$(git status --porcelain)" ]; then
    amarelo "  Nada mudou desde o ultimo commit. Nada a fazer."
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

# O erro do push NAO vai para /dev/null. Ate a v0.44 ia, e o script chutava o
# motivo ("se ele pediu senha...") em vez de mostrar o que o git disse — o que
# transforma rede caida, token vencido e repositorio errado no mesmo texto.
SAIDA_PUSH="$(git push 2>&1)"
if [ $? -eq 0 ]; then
    verde "  push: subiu"
else
    vermelho "  push: FALHOU — e o git disse isto:"
    printf '%s\n' "$SAIDA_PUSH" | sed 's/^/    | /'
    echo
    amarelo "  O commit JA ESTA FEITO. Nada se perdeu; falta so' o push."
    echo "  Se falou em autenticacao, token ou pediu senha:   gh auth login"
    echo "  Se falou em rede, host ou timeout, e' so' repetir: git push"
    echo "  Nos dois casos, nao precisa commitar de novo."
    exit 1
fi

echo
verde "Pronto."
