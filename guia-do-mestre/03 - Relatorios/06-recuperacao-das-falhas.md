# 06 — Recuperação das falhas (rodada 3, 21/10/2026)

Agente único, orçamento de ~20 buscas. Status: RECUPERADO / SÓ LINK / DESISTI / pendente.

> Obs.: no meio da rodada o Internet Archive caiu ("Temporarily Offline" na API CDX). Os alvos 1 e 2 saíram antes disso.

| # | Alvo | Status |
|---|------|--------|
| 1 | Never Unprepared — prévia 16 p. (Gnome Stew) | RECUPERADO |
| 2 | Arc Dream — "Advice for new Delta Green handlers" | RECUPERADO |
| 3 | Principia Apocrypha (inglês) | RECUPERADO |
| 4 | TTRPG Safety Toolkit Guide v2.5 (inglês) | SÓ LINK (+ créditos oficiais baixados) |
| 5 | Savage Worlds Test Drive (Pinnacle) | SÓ LINK |
| 6 | Year Zero Engine SRD (Free League) | RECUPERADO |
| 7 | Mothership — material grátis de Warden | DESISTI (sem fonte oficial achada) |
| 8 | Cypher System Reference Document (MCG) | SÓ LINK |
| 9 | Lines & Veils — fonte primária (Ron Edwards, Sex and Sorcery) | DESISTI (Archive fora do ar; pista nova anotada) |
| 10 | Quick Primer for Old School Gaming (Matt Finch) | DESISTI (orçamento; nada oficial novo) |

## 1) Never Unprepared — prévia de 16 p. — RECUPERADO
- **Caminho:** API do Wayback → o snapshot "mais próximo" (16/12/2025) é a página 404 do site (HTML). Busca no CDX filtrando `application/pdf` achou dois: 07/05/2021 (veio **truncado em 1 MiB**, PDF quebrado, apagado) e **14/05/2015** (2.058.714 bytes, igual ao Content-Length original, termina em `%%EOF`, 16 páginas, texto extraível ~4.900 palavras; créditos: Phil Vecchione, Engine Publishing, © 2012).
- **Legalidade:** a prévia era distribuída de graça pela própria Gnome Stew/Engine Publishing nesse endereço.
- **Arquivo:** `02 - PDFs baixados/1 - Guias e ensaios de mestragem/Never Unprepared - previa 16 p. (Phil Vecchione, Engine Publishing, via Wayback 2015).pdf`
- **Link:** http://web.archive.org/web/20150514053103/http://www.gnomestew.com/files/Never-Unprepared-Preview.pdf (original: http://www.gnomestew.com/files/Never-Unprepared-Preview.pdf, fora do ar)

## 2) Arc Dream — "Advice For New Delta Green Handlers" — RECUPERADO
- **Caminho:** API do Wayback → snapshot de 28/10/2025, é o post de verdade (título, texto completo, assinatura S_Cogswell, datado de **28/12/2017**). Extraí só o `<article>` e converti com weasyprint (2 p.).
- **Conteúdo confere com o relatório 03 (l.147):** avisar antes da criação que a morte é muito provável; "há coisas piores que a morte"; mentalidade de D&D/fantasia heroica mata; falta de controle como fonte de horror. Os conselhos foram **compilados de redes sociais** pela Arc Dream, não são do Handler's Guide.
- **Arquivo:** `02 - PDFs baixados/6 - Artigos (copias offline)/Arc Dream - Advice For New Delta Green Handlers, dez 2017 (copia offline).pdf`
- **Link:** http://web.archive.org/web/20251028190425/https://arcdream.com/home/2017/12/advice-for-new-delta-green-handlers/

## 3) Principia Apocrypha original (inglês) — RECUPERADO
- **Caminho:** principiaapocrypha.com não tem snapshot na API do Wayback. A busca levou à **página oficial do David Perry** (quem organizou o texto), no blog dele: https://lithyscaphe.blogspot.com/p/principia-apocrypha.html — lá estão os PDFs no Drive dele, o Google Doc original e a lista de traduções (a PT-BR do amarcelo está listada como oficial). Licença CC BY-NC-SA 4.0, declarada na página.
- **Arquivos** (em `02 - PDFs baixados/1 - Guias e ensaios de mestragem/`):
  - `Principia Apocrypha - original em ingles, livreto 31 p. (David Perry, lithyscaphe).pdf` — versão final, "Booklet Style". **É imagem, sem texto pesquisável** (pdftotext devolve 0 palavras).
  - `Principia Apocrypha - original em ingles, letra grande 52 p. (David Perry, lithyscaphe).pdf` — versão final "Large Type", pra celular. Também imagem.
  - `Principia Apocrypha - Google Doc original, rascunho anterior com texto pesquisavel 16 p. (David Perry).pdf` — exportado do Google Doc "for posterity"; tem texto (~4.900 palavras), mas abre com "Find the new, final release here", ou seja, **é a versão anterior à final**. Usar pra busca de texto; citar pela versão final.
- **Links:** https://drive.google.com/file/d/1rN5w4-azTq3Kbn0Yvk9nfqQhwQ1R5by1/view · https://drive.google.com/open?id=1VSa6hSvQAlyvkTfmqhix1Z2EoFJPR-CP · https://drive.google.com/open?id=1HEYO4a3AwQEZ29pjaPKPyQCip8PwSeodAZtmtKfZ2X4
- **Crédito (confere com o 03, l.98):** "text from Ben Milton, Steven Lumpkin, and David Perry (myself)".

## 4) TTRPG Safety Toolkit Guide v2.5 (inglês) — SÓ LINK
- **Caminho:** o site oficial (ttrpgsafetytoolkit.com) diz que a **versão 2.5** do guia está no Drive do toolkit e linka o PDF direto (`1M3LpDnVOc2G5UV03mWsqSU2QkDvHcmWX`). O download pelo `drive.usercontent.google.com` devolve de novo **"Google Drive - Can't download file"**: é o dono bloqueando download, não falha nossa. Não tem itch nem outro espelho oficial no site. Wayback não deu pra tentar (Archive fora do ar). Apaguei o HTML.
- **Brinde:** o Google Doc de **Credits** do toolkit exporta normal (3 p.). Ele confirma que "Lines and Veils were designed by Ron Edwards" e, como fonte, aponta **pra uma pergunta do RPG Stack Exchange**, não pro *Sex & Sorcery* (ver alvo 9).
- **Arquivo:** `02 - PDFs baixados/3 - Seguranca e sessao zero/TTRPG Safety Toolkit - Credits (Google Doc oficial).pdf`
- **Links:** guia v2.5 (ler online): https://drive.google.com/file/d/1M3LpDnVOc2G5UV03mWsqSU2QkDvHcmWX/view · pasta: https://drive.google.com/drive/folders/114jRmhzBpdqkAlhmveis0nmW73qkAZCj · créditos: https://docs.google.com/document/d/1XD1PA7vdPsDIKMjW9b1AzOMoKAhtR2v_T46tVfsMZqI/edit

## 6) Year Zero Engine SRD — RECUPERADO
- **Caminho:** a página de licenças da Free League respondeu desta vez (com user-agent de navegador) e tem o link direto.
- **Arquivo:** `02 - PDFs baixados/4 - SRDs e regras de referencia/Year Zero Engine SRD v1.0 (Free League, FTL).pdf` — 45 p., "Year Zero Engine Standard Reference Document v1.0, Authored by Tomas Härenstam, © 2023 Fria Ligan AB", uso pela Free Tabletop License.
- **Link:** https://freeleaguepublishing.com/wp-content/uploads/2023/11/YZE-Standard-Reference-Document.pdf (página: https://freeleaguepublishing.com/community-content/free-tabletop-licenses/; a licença YZE v1.1 de 03/2026 está na mesma página)

## 5) Savage Worlds Test Drive — SÓ LINK
- **Caminho:** peginc.com respondeu 200 desta vez (sem 429). A página do Savage Worlds não tem PDF direto do Test Drive; o que aparece é **produto na loja**: *Deadlands: The Weird West — Blood on the Range, Savage Worlds Test Drive (SWADE)*. Loja = carrinho/conta, então não baixei. O único PDF direto da página é a ficha (`SWADE_Character_Sheet.pdf`), fora do escopo.
- **Link:** https://peginc.com/store/deadlands-the-weird-west-blood-on-the-range-savage-worlds-test-drive-swade/

## 7) Mothership — material grátis de Warden — DESISTI
- **Caminho:** uma busca. Só achei: o *Player's Survival Guide* é o livro de regras (um guia de fã diz que existe "free rules PDF", sem link oficial nos resultados) e o *Warden's Operations Manual* é pago. O resto é material de fã no itch (Warden's Player Reference, módulos sob licença), que não conta como oficial. Não gastei mais busca.
- **Pra próxima:** olhar direto https://www.tuesdayknightgames.com/pages/mothership-rpg (não testado) atrás do PDF grátis do Survival Guide.

## 8) Cypher System Reference Document — SÓ LINK
- **Caminho:** o anúncio da licença leva à página oficial https://www.montecookgames.com/cypher-open-license/ — mas o HTML dela não traz link direto pra arquivo (PDF/DOCX/RTF/Drive), provavelmente vem por JS ou formulário. Existe um espelho **de fã** (https://cypher-srd.statichost.eu, versão 2023-04-18, o próprio autor avisa de erros) — **não é oficial**, não baixei.
- **Link:** https://www.montecookgames.com/cypher-open-license/

## 9) Lines & Veils — fonte primária — DESISTI (com pista nova)
- **Caminho:** a API do Wayback não tem `adept-press.com/sex-and-sorcery`; quando fui buscar no CDX o Internet Archive estava **fora do ar** ("Temporarily Offline"). O fórum The Forge (indie-rpgs.com/archive) não deu pra tentar dentro do orçamento.
- **Pista nova:** o Google Doc oficial de créditos do TTRPG Safety Toolkit (baixado no alvo 4) credita "Lines and Veils were designed by Ron Edwards" e cita como fonte **https://rpg.stackexchange.com/questions/30906/what-do-the-terms-lines-and-veils-mean** — nem o próprio toolkit aponta pro *Sex & Sorcery*. A linha do 03 (l.116) continua "crédito confirmado / livro não confirmado".
- **Pra próxima:** Wayback de `adept-press.com/*` e busca no `indie-rpgs.com/archive` por "lines and veils" (posts do Ron Edwards de 2003–2004), quando o Archive voltar.

## 10) Quick Primer for Old School Gaming — DESISTI
- **Caminho:** sem busca nova nesta rodada (orçamento acabou nos outros). Situação igual à do 02/03: link antigo da Lulu 404, cópia só no Internet Archive (não oficial, não conta). Não achei distribuição oficial atual.
- **Pra próxima:** conferir se a Mythmere Games / Frog God Games tem o Primer grátis hoje.

## Resumo
- Baixados nesta rodada: 7 arquivos (prévia do Never Unprepared; post do Delta Green; Principia em inglês ×3; YZE SRD v1.0; créditos do Safety Toolkit).
- Buscas/fetches gastos: ~21.
