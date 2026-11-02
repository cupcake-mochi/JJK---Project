# Organização do HD externo · 02/11/2026

Em 02/11/2026 a pasta `/media/mizuki/HD Externo II/Claude/` (no Windows, `E:\Claude\`) foi reorganizada. O mapa completo está no `LEIA-ME.md` da raiz do HD, fora do git. Nada foi apagado: o que saiu foi para `Claude/_quarentena-2026-11/`, com um `MOVIMENTOS.csv` de origem e destino.

## O que não mudou de caminho

- Este repositório, em `Claude/Claude 2/`, e os que moram dentro dele: `finalizado/` (JJK---PDF---RPG) e `ficha-android-r53/` (Ficha---RPG-JJK).
- As pastas do HD que este repositório cita: `Claude/invocacoes-pos46/`, `Claude/agentes-2026-09-27/` (o `bestiario/09-fase-2/pesquisa/leva-2/conta-recarga-dnd.py` lê um JSON de lá), `Claude/agentes-2026-09-16/`, `Claude/agentes-2026-09-26/` e `Claude/PDF - Sistema.OBSOLETO/`.

## O que saiu da cópia do HD

- **Itens não rastreados de `Claude/Claude 2/`** foram para `Claude/_quarentena-2026-11/Claude2-nao-rastreados/`, com o mesmo caminho interno: `entregas/`, `sistema/05-material/livro/planejamento-editorial/`, `piloto-editorial-r1/` e `r2/`, `manual/60-invocacoes.md`, `caminhos/05-Edicao-Integrada/`, `invocacoes/05-Edicao-Integrada/`, `sistema/01-pesquisa/integracao-v0.331/`, `sistema/99-arquivo/integracao-anterior-v0.331/` e `scripts-do-sheets-2026-10-05.zip`. O conteúdo já estava no git, exceto 1.373 PNGs de prévia gerados por script e 3 `.pyc` do `planejamento-editorial`.
- `entregas/continuidade-work-2026-10-03/` foi para `Claude/02-RPG/_historico/`, porque 18 arquivos de handoff só existiam ali.
- `Claude/entrega-v0.341/` … `Claude/entrega-v0.358/` foram para a quarentena: as 18 versões já são commits aqui.
- `Claude/backup-worktrees-2026-09-22/` foi para `Claude/02-RPG/_historico/`: o patch `revisao-peca-15` tem 6 arquivos que não estão no histórico.
- Os `PROMPT-*.md` soltos na raiz do HD estão em `Claude/_handoffs/`.

## Para quem for trabalhar na cópia do HD

A cópia `Claude/Claude 2/` está parada na v0.330, atrás do `origin/main`. Com os não rastreados fora do caminho, o `git pull` não esbarra mais em arquivo solto que o GitHub também tem. Os arquivos rastreados da cópia não foram tocados.
