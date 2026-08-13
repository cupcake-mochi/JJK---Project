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
