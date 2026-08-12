# RPG da Guilda — pasta do projeto

Sistema de RPG de mesa em desenvolvimento, ambientado no universo de Jujutsu Kaisen, para um server de guilda com 5 a 7 mestres ativos e personagem persistente entre mesas. Material de fã, gratuito, sem fins comerciais.

## Onde está cada coisa

| Pasta | Conteúdo |
|---|---|
| `00-fundacao/` | Pitch de design e decisões que valem para o projeto inteiro |
| `01-pesquisa/` | Dossiê de metodologia, referências e análise do espaço de design |
| `02-esqueleto/` | Arquitetura do sistema: subsistemas, como se conectam, o que cada um resolve |
| `03-mecanica/` | As peças de regra, numeradas na ordem em que foram escritas, e os doze validadores |
| `04-playtest/` | Roteiro de teste, formulários e retorno organizado por tema |
| `05-material/` | A **ficha de personagem** e o gerador dela. Falta o quick-start e o livro |
| `99-arquivo/` | **Material morto.** Nada aqui é regra corrente — ver o `LEIA-ME.md` de lá |
| `skills/` | Cópia de trabalho das quatro skills de apoio |

**Sobre o `99-arquivo/`:** quando uma peça é substituída, ela não é apagada — vai para lá com um cabeçalho dizendo de onde saiu, o que a substituiu e **por que morreu**. Se você está escrevendo peça nova, não leia de lá.

## Ordem de leitura para quem chega agora

1. `ESTADO-ATUAL.md` — onde o projeto parou e o que vem em seguida
2. `00-fundacao/pitch-de-design.md` — o que este jogo é e o que ele não é
3. `01-pesquisa/dossie-de-metodologia.md` — a seção 8 é o resumo executivo: as dez travas que o sistema precisa respeitar
4. `../logs/CHANGELOG.md` — o que mudou e por quê

## As quatro skills

Instaladas na conta e disponíveis em qualquer conversa, não só nesta pasta:

- **`design-mecanicas-rpg`** — teste de dominância, bônus automático, filtro multi-mestre, aprovação de habilidade de jogador
- **`balanceamento-simulacao`** — contrato de invariantes, busca exaustiva, matriz de dominância, regressão
- **`playtesting-rpg`** — estágios de teste, casos-sonda para divergência entre mestres, formulários
- **`redacao-acessivel-rpg`** — jargão, colisão de termo, progressive disclosure, como não soar como texto de máquina

A pasta `skills/` guarda a versão com arquivos separados. A versão instalada traz esse conteúdo embutido — mexer nos arquivos da pasta **não** altera a skill instalada.

## Versão atual

**v0.37.** Fases 0 a 3 fechadas; a Fase 4 (mecânica) está em andamento com **doze peças escritas e doze validadores passando**. O manual do Fundamento está na **v7.8**, e ele é um subsistema fechado — a técnica e o feitiço já funcionam. O `.pdf` continua na v7.4, porque é exportado à mão.

**Dá para montar uma ficha de nível 2, jogar uma missão inteira e recuperar entre elas**, por seis das nove rotas de Origem. Desde a v0.32 não sobrou peça de regra travando ninguém nessa faixa: das dezessete coisas que uma ficha de nível 2 precisa, **treze existem, e as quatro que faltam não mordem nessa faixa**. O que falta para as outras três rotas, e a ordem do resto, está no `ESTADO-ATUAL.md`.

O que falta hoje não é regra, é **material**. A **ficha de personagem** saiu na v0.35 e está em `05-material/`, com o gerador dela; falta o quick-start. E `04-playtest/` continua vazia — **zero sessões em 35 versões**.

Os validadores rodam de `03-mecanica/`, e **isso não é detalhe**. Os três que leem o manual — `conferir-nomes.py`, `conferir-manual.py` e `conferir-pericias.py` — acham o `.docx` por caminho relativo à própria posição: rodados de outro lugar, eles **pulam** as checagens em silêncio e saem verdes sem terem conferido nada. Os mesmos três precisam de `python-docx`, e pulam igual sem ele:

```
pip install python-docx --break-system-packages
cd sistema/03-mecanica && python3 conferir-nomes.py
```

Os dois últimos não leem o manual e não precisam de nada: o `conferir-criacao.py` confere a ficha de exemplo da peça 8 contra as fórmulas das outras peças, e o `conferir-ficha.py` confere a ficha de `05-material/` contra os catálogos delas.
