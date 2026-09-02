# Prompt para continuar o Projeto - M em conversa nova

*Copie tudo abaixo da linha.*

---

Trabalhe em `/media/mizuki/HD Externo II/Claude/Claude 2/`.

**Projeto - M** é um sistema de RPG de mesa no universo de Jujutsu Kaisen, para um server de guilda com 5 a 7 mestres ativos e personagem persistente entre mesas. O filtro que decide tudo: **dois mestres que nunca se falaram chegam no mesmo número?**

## Leia nesta ordem antes de mexer em qualquer coisa

1. `sistema/ESTADO-ATUAL.md` — onde parou e o que vem em seguida
2. `README.md` — as **nove lições que custaram erro**, e elas moram só lá
3. `logs/CHANGELOG.md` — a entrada mais recente
4. `sistema/05-material/livro/REGRA-DE-VOZ.md` — como o livro escreve

## Onde está o projeto agora

**v0.200, escrita mas NÃO commitada.** A mensagem está pronta em `mensagem-de-commit.txt` na raiz. O fechamento inteiro já rodou — se nada mudar, é só o Mizuki rodar `./subir.sh`.

Manual do Fundamento na **v7.22**. **Vinte e seis peças de regra e vinte e seis validadores** em `sistema/03-mecanica/`, mais o `conferir-repositorio.py` e o `conferir-voz.py` — 27 validadores e 300 checagens no total.

O que a v0.200 fez: unificou a paleta do projeto na `Neve Saturado`, arrumou o nível 7 do Emanador, levou o clash de domínios do manual para o livro, e **pôs um dado no clash** — refino igual e Acerto do mesmo tipo rolam `1d12` cada, e separou por `4` ou mais o maior conquista.

## O que vem em seguida

**A v0.201 é a pressão do chefe**, e ela está medida e registrada em `sistema/03-mecanica/26-bestiario.md` §8. O chefe come `7%` da vida do grupo por rodada e levaria `14` rodadas para zerar; a tabela do `Guia do Mestre` de 2014 come `24%` e zera em `4,1`. **É `3,3 ×`, e a razão é constante em todos os níveis.**

Duas coisas travam a correção, e as duas estão escritas: o `72` é a base da régua de condição inteira, e levar o chefe a `114` tira oito das treze condições do nível publicado. E metade da comparação não existe em livro nenhum — o d20 não publica quanto o GRUPO entrega por rodada.

**Depois dela, na fila:**
- **Aptidões novas**, que o Mizuki pediu. Traga a escada de gate da peça 11 §5 e o catálogo atual antes de ele escolher.
- **Catálogo de maldições prontas**, esperando a lista dele.
- **O exemplo guiado de invocação.** O capítulo 60 tem quatro exemplos e nove montagens prontas, e **não tem o passo a passo** que o Fundamento tem para feitiço (`40-fundamento.md`, `Exemplo guiado: o primeiro feitiço da Régua`). Quem monta uma invocação do zero vê nove resultados e nenhuma escolha sendo feita.
- **Duas perguntas do clash que ficaram sem resposta** e são escolha do Mizuki: se o `Domínio Simples` entra na cascata (ele se chama domínio, e nada no texto fecha), e nada mais — a saída de furar a barreira já foi decidida e removida na v0.200.

## Como trabalhar aqui

⚠ Trabalhe na pasta **PRINCIPAL**, não em worktree. **Você não commita** — deixa a mensagem em `mensagem-de-commit.txt` na raiz e avisa.

**Não rode git do sandbox — nem status.** Para ver em que commit a pasta está, leia `.git/logs/HEAD` como arquivo.

**Código novo se escreve pelo bash**, com `cat > arquivo <<'EOF'`. Arquivo que a ferramenta de escrita grava fica invisível para o `python3` com frequência. Para `.md` a ferramenta serve.

**Número vem de conta rodada, nunca de intuição.** Se o Mizuki disser que algo está desbalanceado, meça antes de concordar — e diga a ele quando a conta o desmentir.

**Antes de propor mecânica nova, pesquise como outro sistema resolve o mesmo problema.** Os PDFs estão em `PDFs - Sistemas Extras/PDF_Sistemas/` — 5e (PHB 2024, Guia do Mestre, Volo, Tasha), Pathfinder 2e, GURPS 4ed e 3D&T.

**Todo número novo ganha validador com teste negativo:** perturbe numa cópia isolada, confira que a base passa antes com PULADA=0, e confira com diff que a perturbação bateu. E ponha contra-teste coerente — uma mudança legítima que precisa continuar verde.

**Nada de valor fica escrito dentro do validador:** leia o número do documento dono.

**Nome se confere com `conferir-nomes.py --candidatos`, sempre.** Grep no projeto não é triagem.

**Escolha de sabor é do Mizuki.** Traga as opções com o número e o trade-off de cada uma já calculados, e pergunte. **Mas não pergunte o que a conta responde.**

**Escreva no registro dele:** negrito abrindo com a regra e a razão logo depois, "você" falando com o leitor, frase encadeada por vírgula em vez de aforismo, parêntese para a exceção curta.

**Antes de fechar versão, releia o que VOCÊ escreveu** procurando antítese, frase teatral, tabela inútil e texto desnecessário. Os validadores não alcançam essa camada.

**Fale com ele diferente de como escreve o documento.** Uma ideia por parágrafo, frase curta, sem §3.4 no meio da frase. Se ele disser que não entendeu, a resposta certa é MENOS detalhe, recomeçando de mais atrás.

**Se mexer no livro, mande o PDF de duas colunas antes de ele commitar.**

## A ordem de fechar versão

1. Entrada no `logs/CHANGELOG.md` — ele é o dono da versão
2. Bump em `README.md`, `sistema/ESTADO-ATUAL.md` e `sistema/LEIA-ME.md`
3. Os quatro builds do livro, de `sistema/05-material/livro/build/`: `build.py`, `build.py --duas`, `build_docx.py`, `build_txt.py`
4. Os 26 validadores de `sistema/03-mecanica/`
5. `manual/matematica/pac7.py` e `v7.py`
6. `conferir-voz.py --estrito`, de `sistema/05-material/livro/`
7. `conferir-repositorio.py`, da raiz

*Se mexeu no manual do Fundamento: `node make.js` em `manual/gerador/`, copiar o `.docx` para `manual/`, e exportar o `.pdf` com `soffice --headless --convert-to pdf`.*

**O `conferir-repositorio.py` vai acusar `7.1` e `7.3` antes do commit** — são o recorte da entrega, e o `./subir.sh` conserta sozinho. O que não pode sobrar é qualquer outro.
