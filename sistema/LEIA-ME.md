# RPG da Guilda — pasta do projeto

Sistema de RPG de mesa em desenvolvimento, ambientado no universo de Jujutsu Kaisen, para um server de guilda com 5 a 7 mestres ativos e personagem persistente entre mesas. Material de fã, gratuito, sem fins comerciais.

## Onde está cada coisa

| Pasta | Conteúdo |
|---|---|
| `00-fundacao/` | Pitch de design e decisões que valem para o projeto inteiro |
| `01-pesquisa/` | Dossiê de metodologia, referências e análise do espaço de design |
| `02-esqueleto/` | Arquitetura do sistema: subsistemas, como se conectam, o que cada um resolve |
| `03-mecanica/` | As peças de regra, numeradas na ordem em que foram escritas, e os sete validadores |
| `04-playtest/` | Roteiro de teste, formulários e retorno organizado por tema |
| `05-material/` | Texto final: livro, ficha, cheat sheets, layout |
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

**v0.27.** Fases 0 a 3 fechadas; a Fase 4 (mecânica) está em andamento com **onze peças escritas e sete validadores passando**. O manual do Fundamento está na **v7.6**, e ele é um subsistema fechado — a técnica e o feitiço já funcionam. O `.pdf` continua na v7.4, porque é exportado à mão.

**Dá para montar uma ficha de nível 2, jogar uma missão inteira e recuperar entre elas**, por seis das nove rotas de Origem. Desde a v0.26 isso é literal: das dezessete coisas que uma ficha de nível 2 precisa, **doze existem, e as cinco que faltam não mordem nessa faixa**. O que falta para as outras três rotas, e a ordem do resto, está no `ESTADO-ATUAL.md`.

Os validadores rodam de `03-mecanica/`. Os dois que leem o manual — `conferir-nomes.py` e `conferir-manual.py` — precisam de `python-docx`:

```
pip install python-docx --break-system-packages
```
