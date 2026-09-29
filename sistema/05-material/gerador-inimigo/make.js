// Gera o BLOCO DE INIMIGO — a folha que o mestre leva para a mesa.
//   node make.js
// Sai bloco-de-inimigo.docx, que e copiado para 05-material/.
//
// Sao quatro partes, e a ordem importa:
//   1. O BLOCO      em branco, as linhas da peca 26 §3, para preencher.
//   2. O EXEMPLO    o mesmo bloco com os numeros de um Desastre de nivel 10.
//   3. AS PRONTAS   as seis maldicoes, no molde de bloco do 5e.
//   4. AS TABELAS   o mestre le e copia. Tudo aqui deriva; nada e escolha.
//
// v0.221: a escada passou a ser a viva, e as prontas sairam no molde de bloco do 5e,
// com o mesmo texto do capitulo 8 do livro do Bestiario.
// v0.282: a escada virou a GRADE da fase 2 do bestiario (peca 26 §4). A categoria e a
// dificuldade da luta, feita para N pessoas (x1 a x6); a vida e rodadas x N x a saida
// de um personagem; o golpe e a pressao x o golpe-base; ele age N vezes; e o que ele
// carrega se paga na vida, sem mexer no golpe.
const d = require('docx');
const fs = require('fs');
const H = require('../gerador-ficha/helpers.js');
// ⚠ A PALETA E A DO LIVRO, e nao a da ficha. As duas existem no projeto: a ficha
// e o manual do Fundamento usam ameixa 741B47; o Manual da Guilda, que e o que o
// jogador recebe, usa selo #211C35 com acento #8A7444. O bloco de inimigo e
// material de mesa como o livro, entao ele segue o livro.
// v0.200: as duas paletas do projeto viraram UMA — a Neve Saturado — entao o
// bloco nao precisa mais de paleta propria. A chamada fica porque os helpers da
// ficha sao os mesmos, e um dia isto pode divergir de novo.
H.setPaleta({
  ink: '251727', crimson: 'BC2A6E', deep: '2B1B2E', grey: '847B86',
  rule: 'F8C7DC', linha: '9A6F87', bandBg: 'F7E5EE', headBg: '2B1B2E',
  zebra: 'FADDEA', boxBg: 'FDF0F6', campoBg: 'FDF0F6',
});
const { C, P, FAIXA, TBL, BLOCO, NOTA, GAP } = H;
const X = require('./dados.js');
const { Document, Packer, Paragraph, TextRun, Footer, AlignmentType, PageBreak } = d;
const Pg = Paragraph;

// v0.282: a conta mora no conta.js; aqui so se monta o .docx em cima dela.
const K = require('./conta.js');
const { NUM, lista, virg, degrau, pressao, temIntervencao, precoIntervencao, arred, integridadeDe,
        dado, media, vidaCel, golpe, fmtGolpe, derivada, protecao, maestria, FEM, TR_TODOS, rotNv, montaPronta } = K;

function titulo(sub) {
  return [
    new Paragraph({ spacing: { after: 40 },
      children: [new TextRun({ text: 'PROJETO - M', bold: true, size: 15,
                               color: C.grey, characterSpacing: 60 })] }),
    new Paragraph({ spacing: { after: 160 },
      children: [new TextRun({ text: sub, bold: true, size: 34, color: C.crimson })] }),
  ];
}
function regra(cor) {
  return new Pg({ spacing: { before: 60, after: 60 },
    border: { bottom: { style: d.BorderStyle.SINGLE, size: 10, color: cor || C.crimson } },
    children: [new TextRun({ text: '', size: 2 })] });
}
function stat(rotulo, valor, vazio) {
  const kids = rotulo ? [new TextRun({ text: rotulo + ' ', bold: true, size: 19, color: C.deep })] : [];
  if (valor) kids.push(...H.runs(String(valor), { size: 19 }));
  return new Pg({
    spacing: { before: 34, after: vazio ? 46 : 34, line: 250 }, children: kids,
    border: vazio ? { bottom: { style: d.BorderStyle.SINGLE, size: 4,
                                color: C.linha, space: 3 } } : undefined,
  });
}
function nomeGrande(txt, sub) {
  return [
    new Pg({ spacing: { before: 0, after: 20 },
      border: txt ? undefined : { bottom: { style: d.BorderStyle.SINGLE, size: 6,
                                            color: C.linha, space: 4 } },
      children: [new TextRun({ text: txt || ' ', bold: true, size: 30, color: C.crimson })] }),
    new Pg({ spacing: { after: 60 },
      children: [new TextRun({ text: sub || ' ', italics: true, size: 18, color: C.grey })] }),
  ];
}
function secao(txt) {
  return new Pg({ spacing: { before: 90, after: 40 },
    children: [new TextRun({ text: txt, bold: true, size: 20, color: C.crimson,
                             characterSpacing: 40 })] });
}

// ----------------------------------------------------------------- 1. O BLOCO
// ⚠ O FORMATO E O DE BLOCO DE MONSTRO, e nao o de formulario. A primeira versao
// desta folha era uma planilha de construcao, e o Mizuki leu e disse que era
// confuso. O molde certo estava no Guia do Volo: um bloco vertical, lido de cima
// para baixo, com tudo ja calculado. Ninguem MONTA um monstro no 5e; a pessoa LE.
function bloco(f, primeiro, rotulo) {
  const v = (k) => (f ? (f[k] ?? '') : '');
  const vazio = !f;
  const out = [];
  if (!primeiro) out.push(new Pg({ children: [new PageBreak()] }));
  out.push(...titulo(rotulo || (f ? 'Ficha de inimigo — exemplo' : 'Ficha de inimigo')));
  if (vazio) out.push(P('Preencha de cima para baixo. **Defesa, vida, refino e o golpe você copia das tabelas do fim**; o resto você decide.'));
  out.push(GAP(120));
  out.push(...nomeGrande(v('nome'), f ? `${v('categoria')} ×${v('n')} · nível do grupo ${v('nivel')}` : 'tamanho · categoria ×N · papel · nível do grupo · grau'));
  out.push(regra());
  out.push(stat('Defesa', v('defesa'), vazio));
  out.push(stat('Vida e Integridade', f ? `${v('vida')} · ${integridadeDe(v('vida'))}` : '', vazio));
  out.push(stat('Deslocamento', f ? X.DESLOCAMENTO : '', vazio));
  out.push(regra(C.linha));
  out.push(TBL(['FOR', 'DES', 'CON', 'INT', 'ESS'],
    [[v('forca'), v('destreza'), v('con'), v('int'), v('ess')]],
    [20, 20, 20, 20, 20], { centerCols: [0, 1, 2, 3, 4] }));
  out.push(regra(C.linha));
  out.push(stat('Testes de Resistência', f ? `${v('trs')} — os dois treinados` : '', vazio));
  out.push(stat('CD dele', v('cd'), vazio));
  out.push(stat('Refino', v('refino'), vazio));
  out.push(stat('Resistência · imunidade · vulnerabilidade', v('resist'), vazio));
  out.push(regra());
  out.push(secao('AÇÕES'));
  // o molde do cap. 5: o ataque leva nome proprio, e o nome e a arma ou a parte do corpo.
  // Medido em 7 sistemas — nenhum poe "Ataque de" no NOME (`0` de `423` no SRD 2024).
  if (vazio) out.push(P('Cada ataque leva nome próprio, e o nome é a arma ou a parte do corpo que bate: **Mordida**, **Garra**, **Kanabō**. **Não escreva "Ataque de" no nome** — "ataque de" é como as **Ações Múltiplas** chamam o ataque na frase delas.'));
  out.push(stat('Por rodada', v('porRodada'), vazio));
  out.push(stat('Golpe', f ? `${v('acerto')} para acertar, ${v('dano')} de dano` : '', vazio));
  out.push(regra());
  out.push(BLOCO('traços — Passivas, aptidões e técnica', v('caracteristicas'), 2));
  out.push(BLOCO(`Intervenções — ${NUM[X.INTERVENCOES]} por luta, quando N × orçamento chega a ${X.PORTA_INTERVENCAO}`, v('intervencoes'), 2));
  out.push(BLOCO('pacto — o teto do permanente é metade da Essência dele', v('pacto'), 1));
  out.push(BLOCO('o que ele faz na mesa', v('notas'), 2));
  return out;
}

// O exemplo NAO tem nome nem ficcao de proposito: batizar maldicao e escolha de
// sabor do Mizuki. O que ele mostra e o PREENCHIMENTO — de onde cada numero saiu.
// Desde a v0.221 cada numero dele e COMPUTADO, e nao escrito: ate ali ele tinha
// `475` de vida e `1d8 + 4` de golpe, de uma tabela que o manual ja tinha trocado.
const EXEMPLO = (() => {
  const f = X.FAIXAS.find((x) => x[1] <= 10 && 10 <= x[2]);
  const dg = degrau('Desastre');
  const n = 4;
  const dv = derivada(10);
  const elem = X.RESISTENCIA.find((r) => r[0] === 'Elementais');
  const fr = Number(elem[2].replace('×', '').replace(',', '.'));
  return {
    nome: 'Maldição de nível 10', grau: '—', nivel: '10', categoria: dg[0], n: String(n),
    forca: '3', destreza: '3', con: '2', int: '1', ess: '0',
    trs: 'Físico e Vigor',
    resist: `resistência a Elementais — a vida se divide por ${elem[2].replace('×', '')}`,
    vida: String(vidaCel(f, dg, n, 1 / (fr * precoIntervencao(dg, n)))), dano: golpe(f, dg), porRodada: `${NUM[n]} ações, e uma Reação`,
    defesa: String(dv[1]), acerto: `+${dv[2]}`, cd: String(dv[3]), refino: String(dv[4]),
    caracteristicas: 'Escama (Passiva) · duas aptidões do catálogo da peça 11',
    intervencoes: 'a primeira bate um pouco menos que uma ação; as outras duas mudam o campo',
    pacto: 'nenhum — a Essência dele é 0, e o teto é metade dela',
    notas: `Age ${NUM[n]} vezes por rodada e rola o dado uma vez em cada. Um esquadrão de ${X.CAMBIO_POR_PESSOA * n} capangas de ${f[7]} de vida vale o mesmo encontro.`,
  };
})();

function blocoPronto(p) {
  const m = montaPronta(p);
  const out = [new Pg({ children: [new PageBreak()] }), ...titulo(`${p.nome} — maldição pronta`)];
  out.push(P(`*${p.linha}*`));
  out.push(P(p.notas));
  out.push(GAP(80));
  const corpos = p.corpos_na_mesa > 1 ? ` · ${NUM[p.corpos_na_mesa]} corpos` : '';
  const pap = p.papel ? ` · ${p.papel}` : '';
  out.push(...nomeGrande(p.nome, `Maldição ${FEM[p.tamanho]} · ${p.categoria} ×${m.n}${pap}${corpos} · nível ${m.lo} a ${m.hi}`));
  out.push(regra());
  for (const [a, b, v] of m.seg) {
    const pre = m.seg.length > 1 ? `*${rotNv(a, b)}* · ` : '';
    out.push(stat('', `${pre}**Defesa** \`${v[0]}\` · **Acerto** \`+${v[1]}\` · **CD** \`${v[2]}\` · **Refino** \`${v[3]}\` *(proteção \`+${protecao(v[3])}\`)*`));
  }
  const mov = p.movimentos.map((mv) => ` · **${mv}** \`${X.DESLOCAMENTO}\``).join('');
  // o golpe saiu do cabecalho em 11/09/2026: ele mora no ataque, em `Acoes`, com o
  // alcance junto (`Bestiario/04-fase-1/fila/DECIDIDO-as-tres-respostas-da-passada.md` §1)
  out.push(stat('', `**Vida** \`${m.vida}\` · **Integridade** \`${integridadeDe(m.vida)}\` · **Deslocamento** \`${X.DESLOCAMENTO}\`${mov}`));
  out.push(regra(C.linha));
  // o atributo é o do começo da faixa, e o marco que muda ele dentro da faixa aparece na célula, como
  // a Defesa por marco. v0.235: o de ataque diz que é dele que saem o acerto e a CD
  const at = m.atNv(m.lo).map((v, i) => {
    const sobe = [];
    for (let nv = m.lo + 1; nv <= m.hi; nv++) {
      if (m.atNv(nv)[i] !== m.atNv(nv - 1)[i]) sobe.push(`${m.atNv(nv)[i]} do nível ${nv}`);
    }
    return `${v}${sobe.length ? ` (${sobe.join('; ')})` : ''}${i === m.iAtk ? ', acerto e CD' : ''}`;
  });
  out.push(TBL(['FOR', 'DES', 'CON', 'INT', 'ESS'], [at], [20, 20, 20, 20, 20], { centerCols: [0, 1, 2, 3, 4] }));
  out.push(regra(C.linha));
  out.push(stat('', TR_TODOS.map((t) => `**${t}** ${p.trs.includes(t) ? 'treinado' : '—'}`).join(' · ')));
  out.push(stat('', '**Resistências** — · **Imunidades** — · **Vulnerabilidades** — · **Perícias** —'));
  out.push(regra());
  if (p.tracos.length) {
    out.push(secao('TRAÇOS'));
    p.tracos.forEach((t) => out.push(P(`**${t.nome}.** ${m.enche(t.texto)}`)));
  }
  out.push(secao('AÇÕES'));
  if (p.acoes_multiplas) out.push(P(`**Ações Múltiplas.** ${m.enche(p.acoes_multiplas)}`));
  p.acoes_nomeadas.forEach((x) => out.push(P(`**${x.nome}.** ${m.enche(x.texto)}`)));
  if (p.intervencoes.length) {
    const n = NUM[p.intervencoes.length];
    out.push(secao('INTERVENÇÕES'));
    out.push(P(`${n[0].toUpperCase()}${n.slice(1)} por luta, cada uma usada uma vez. Sai no máximo uma por rodada, logo depois do turno de outra criatura.`));
    p.intervencoes.forEach((iv, k) => out.push(P(`**${k + 1}. ${iv.nome}.** ${m.enche(iv.texto)}`)));
  }
  return out;
}

function prontas() {
  const out = [new Pg({ children: [new PageBreak()] })];
  const fs6 = X.PRONTAS.map((p) => montaPronta(p));
  const lo = Math.min(...fs6.map((m) => m.lo));
  const hi = Math.max(...fs6.map((m) => m.hi));
  out.push(...titulo(`Maldições prontas — do nível ${lo} ao ${hi}`));
  out.push(P('Seis fichas para abrir e usar, no molde de bloco do 5e. **Nenhum número foi escolhido:** todos saem das tabelas do fim desta folha, e os atributos cabem na criação da peça 2, com nove pontos e teto `3`, e dez no chefe.'));
  out.push(P('**A coluna do `Capanga` está vazia.** As seis são `Ameaça ×1` e `Desastre ×4`; ficha de esquadrão é o próximo passo.'));
  out.push(GAP(120));
  out.push(TBL(['MALDIÇÃO', 'CATEGORIA', 'NÍVEL', 'VIDA', 'GOLPE', 'AÇÕES'],
    X.PRONTAS.map((p, i) => [p.nome + (p.corpos_na_mesa > 1 ? ` (×${p.corpos_na_mesa} na mesa)` : ''),
      `${p.categoria} ×${fs6[i].n}`, p.faixa, fs6[i].vida, fs6[i].g, String(fs6[i].n)]),
    [22, 18, 12, 12, 24, 12], { centerCols: [2, 3, 4, 5] }));
  out.push(GAP(100));
  out.push(NOTA(`As prontas vão do \`×1\` ao \`×4\`. A grade monta qualquer célula, do \`×1\` ao \`×${X.N_MAXIMO}\`, pelas tabelas do fim.`));
  X.PRONTAS.forEach((p) => out.push(...blocoPronto(p)));
  return out;
}

// --------------------------------------------------------------- 4. TABELAS
// ⚠ O texto daqui passou pela REGRA-DE-VOZ.md na v0.199, e ela corta tres
// coisas: a folha falando de si mesma, a justificativa do numero e titulo em
// frase. O que fica responde "quanto e" e "o que acontece".
function tabelas() {
  const out = [new Paragraph({ children: [new PageBreak()] }), ...titulo('As tabelas')];
  out.push(P('As tabelas de onde saem os números da ficha. **Você só volta aqui quando monta um inimigo novo.**'));
  out.push(GAP(140));
  const NS = Array.from({ length: X.N_MAXIMO }, (_, i) => i + 1);

  out.push(FAIXA('Como montar um inimigo'));
  out.push(P('**1 · Escolha o nível do grupo.** É o nível das fichas que vão sentar na mesa.'));
  out.push(P(`**2 · Escolha a categoria e o N.** A categoria é a dificuldade da luta, do \`${X.DEGRAUS[0][0]}\` à \`${X.DEGRAUS[X.DEGRAUS.length - 1][0]}\`, e o N é para quantos personagens do nível ela é feita, do \`×1\` ao \`×${X.N_MAXIMO}\`.`));
  out.push(P('**3 · Copie a vida da tabela do degrau, na coluna do N, e o golpe.** Ele age N vezes por rodada. Defesa, acerto e CD saem da tabela por nível.'));
  out.push(P('**4 · Decida o que ele é.** O tamanho, os cinco atributos, o papel e as características. O que muda o encontro — resistência, `Recarga`, `Intervenção`, Expansão — divide a vida, e o golpe fica.'));
  out.push(P(`**5 · Se quiser um bando**, use o \`Capanga\`, ou ponha capangas ao lado do chefe pela tabela *Chefe com capangas*.`));
  const f10 = X.FAIXAS.find((x) => x[1] <= 10 && 10 <= x[2]);
  const des = degrau('Desastre');
  const dv10 = derivada(10);
  out.push(NOTA(`**Um exemplo.** Um grupo de quatro, de nível 10, vai enfrentar uma luta moderada. Isso é um \`Desastre ×4\`: \`${vidaCel(f10, des, 4)}\` de vida, ele rola \`${golpe(f10, des)}\` quatro vezes por rodada, Defesa \`${dv10[1]}\`, acerto \`+${dv10[2]}\` e CD \`${dv10[3]}\`.`));
  out.push(GAP(160));

  out.push(FAIXA('Os degraus'));
  out.push(TBL(['categoria', 'a luta dura', 'o golpe', 'Intervenção'],
    X.DEGRAUS.map((dg) => {
      const ab = NS.filter((n) => temIntervencao(dg, n));
      return [dg[0], `${virg(dg[1])} rodadas`, dg[0] === 'Capanga' ? 'metade do golpe-base' : `${virg(pressao(dg).toFixed(3))} × o golpe-base`,
        ab.length ? `a partir do ×${ab[0]}` : '—'];
    }),
    [22, 22, 32, 24], { centerCols: [1, 2, 3], boldCols: [0] }));
  out.push(GAP(150));

  // ⚠ vida e golpe em tabelas SEPARADAS: um numero se anota, o outro se rola.
  X.DEGRAUS.filter((dg) => dg[0] !== 'Capanga').forEach((dg) => {
    out.push(FAIXA(`Vida · ${dg[0]}`));
    out.push(TBL(['nível do grupo', ...NS.map((n) => `×${n}`)],
      X.FAIXAS.map((f) => [f[0], ...NS.map((n) => String(vidaCel(f, dg, n)))]),
      [22, 13, 13, 13, 13, 13, 13], { centerCols: [0, 1, 2, 3, 4, 5, 6], boldCols: [0] }));
    out.push(GAP(120));
  });
  out.push(new Paragraph({ children: [new PageBreak()] }));
  out.push(FAIXA('O golpe'));
  out.push(P('O golpe não depende do N: o `×6` bate o mesmo golpe do `×1`, seis vezes.'));
  out.push(TBL(['nível do grupo', ...X.DEGRAUS.map((c) => c[0])],
    X.FAIXAS.map((f) => [f[0], ...X.DEGRAUS.map((dg) => golpe(f, dg))]),
    [15, 17, 17, 17, 17, 17], { centerCols: [0, 1, 2, 3, 4, 5], boldCols: [0] }));
  out.push(GAP(150));
  out.push(FAIXA('Defesa, acerto e CD'));
  out.push(P('Esta escada muda em **marco**, e a de cima muda em **faixa de Classe**. Confira as duas separado. O que sai dela se paga na vida: cada ponto de Defesa acima custa `10%`, e cada ponto de acerto e CD, `8,7%`.'));
  out.push(TBL(['nível', 'Defesa', 'acerto', 'CD do inimigo', 'refino'],
    X.DERIVADAS.map((r) => [r[0], String(r[1]), `+${r[2]}`, String(r[3]), String(r[4])]),
    [22, 20, 19, 20, 19], { centerCols: [0, 1, 2, 3, 4], boldCols: [0] }));
  out.push(NOTA('Ele acerta um alvo que investiu em defesa em **50% a 55%**, e o Teste de Resistência treinado dele falha **35%**. **No `×1` e no `×2`**, a condição que tira ação dá a ele um Teste de Resistência no começo do turno — com a maestria no `×1`, com desvantagem no `×2`.'));

  out.push(GAP(150));
  out.push(FAIXA('Capanga e câmbio'));
  const [rLo, rHi] = X.CORPOS_CONTRA_UM.map((v) => v.toFixed(2).replace('.', ','));
  out.push(P(`O \`Capanga ×N\` é um esquadrão de **${NUM[X.CORPOS_POR_PESSOA]} corpos por personagem**, com a vida num pool só. Cada corpo cai num golpe de um personagem — a vida dele é o dano do grupo por rodada dividido por quatro, para baixo — e bate metade do golpe-base. Um \`Desastre ×N\` vale **${X.CAMBIO_POR_PESSOA}N capangas** do mesmo nível. N corpos de \`×1\` **não** valem um \`×N\`: eles cobram de \`${rLo}×\` a \`${rHi}×\` o que ele cobra.`));
  out.push(TBL(['nível do grupo', 'capanga: vida', 'o dado dele'],
    X.FAIXAS.map((f) => [f[0], String(f[7]), dado(f[8])]),
    [34, 33, 33], { centerCols: [0, 1, 2], boldCols: [0] }));
  out.push(NOTA(`No máximo **${NUM[X.TETO_EMPILHAMENTO]}** corpos do mesmo esquadrão atacam o mesmo alvo por rodada, e do segundo em diante o golpe sai pela metade. E o esquadrão inteiro faz uma ação em área por rodada, e não uma por corpo.`));
  out.push(GAP(150));

  out.push(FAIXA('Chefe com capangas'));
  out.push(P('**Cada capanga que entra ao lado de um chefe tira `1 ÷ (rodadas × N)` da vida e do golpe dele**, até metade do grupo em capangas. Na `Ameaça`, use a fração do `Desastre`.'));
  out.push(TBL(['cada capanga tira', ...NS.map((n) => `×${n}`)],
    X.DEGRAUS.filter((dg) => !['Capanga', 'Ameaça'].includes(dg[0])).map((dg) => [dg[0], ...NS.map((n) => `${virg((100 / (dg[1] * n)).toFixed(1))}%`)]),
    [22, 13, 13, 13, 13, 13, 13], { centerCols: [1, 2, 3, 4, 5, 6], boldCols: [0] }));
  out.push(GAP(150));

  out.push(new Paragraph({ children: [new PageBreak()] }));
  out.push(FAIXA('Resistência, imunidade e vulnerabilidade'));
  out.push(P('Resistência a até `2` tipos fixos, no total da criatura, não desconta PV. Um grupo completo continua pago, mesmo quando seus tipos são escritos separadamente. Imunidades não recebem essa isenção. A proteção cobrada divide a vida crua. A vulnerabilidade não cobra nem devolve.'));
  out.push(TBL(['se ele resiste a…', 'resistir divide a vida por', 'ser imune divide por'],
    X.RESISTENCIA.map((r) => [r[0], r[2], r[3]]),
    [34, 33, 33], { centerCols: [1, 2], boldCols: [0] }));
  out.push(P('Três ou mais tipos mistos que não completem um grupo continuam sem preço definido; não aplique a isenção a esse caso.'));
  out.push(NOTA(`A \`Intervenção\` divide a vida por \`1 + ${virg(X.INTERVENCAO_EXTRA)} ÷ (rodadas × N)\`, e a Expansão de Domínio completa, por \`1,92\`.`));

  out.push(new Paragraph({ children: [new PageBreak()] }));
  out.push(FAIXA('Tamanho'));
  out.push(P('O tamanho diz onde o corpo cabe e até onde o golpe alcança. **Ele não cobra nada.**'));
  const grupos = [];
  X.TAMANHOS.forEach((tm) => {
    const g = grupos.find((x) => x[1] === tm[1] && x[2] === tm[2]);
    if (g) g[0].push(tm[0]); else grupos.push([[tm[0]], tm[1], tm[2]]);
  });
  out.push(TBL(['tamanho', 'ocupa na grade', 'alcance', 'o golpe pega'],
    grupos.map(([nomes, lado, viz]) => [nomes.join(' · '), `${lado}×${lado}`, `${virg(lado * 1.5)} m`,
      viz ? 'o alvo, e metade em um vizinho' : 'só o alvo']),
    [34, 20, 16, 30], { centerCols: [1, 2], boldCols: [0] }));
  out.push(GAP(150));
  out.push(FAIXA('Área natural'));
  out.push(P('O sopro, o rugido, o chão que cede: a área que não vem de técnica. **A cobertura sai do nível**, e a forma é o jeito de gastar ela. Resolve por Teste de Resistência contra a CD dele — o golpe na falha, metade no sucesso.'));
  out.push(TBL(['nível', 'cobre', 'Esfera', 'Cone', 'Retângulo'],
    X.AREA_NATURAL.map(([a, b, q, esf, cone, ret]) => [`${a} a ${b}`, `${q} quadrados`, `raio ${esf}`, cone, ret.join(' · ')]),
    [14, 18, 16, 16, 36], { centerCols: [0, 1, 2, 3], boldCols: [0] }));
  out.push(NOTA('No máximo uma ação em área por rodada, e a de `Recarga` não conta. A `Recarga` ocupa as ações múltiplas do turno, e cada alvo leva `2,5 ×` o golpe na falha, metade no sucesso. O `Cone` sai sempre do corpo dele, e a largura em qualquer ponto é igual à distância até ele.'));
  return out;
}

// `node make.js --json`: as seis prontas calculadas, para o capitulo 8 do livro do Bestiario.
// O livro formata e nao refaz a conta — a conta mora aqui, e so aqui.
const doc = new Document({
  creator: 'Projeto - M', title: 'Bloco de inimigo',
  styles: { default: { document: { run: { font: 'Calibri', size: 20, color: C.ink } } } },
  sections: [{
    // ⚠ 1153 nao e escolha: A4 tem 11906 twips e as tabelas tem 9600, entao
    // (11906 - 9600) / 2 = 1153 de cada lado.
    properties: { page: { margin: { top: 720, bottom: 640, left: 1153, right: 1153 } } },
    footers: { default: new Footer({ children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: 'Projeto - M · bloco de inimigo · peça 26',
                               size: 14, color: C.grey })] })] }) },
    children: [...bloco(null, true), ...bloco(EXEMPLO), ...prontas(), ...tabelas()],
  }],
});

// a fracao do chefe com capangas sai da regra (1 ÷ rodadas x N), lida dos DEGRAUS do dados.js
Packer.toBuffer(doc).then((b) => {
  fs.writeFileSync('bloco-de-inimigo.docx', b);
  console.log(`gerado: bloco-de-inimigo.docx ${Math.round(b.length / 1024)} KB`);
});
