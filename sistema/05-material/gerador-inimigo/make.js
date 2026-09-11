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
// v0.221: a escada passou a ser a viva — Capanga, Ameaca, Desastre, Catastrofe e
// Calamidade —, com as acoes DECLARADAS na categoria e o fator 0,923 de quem
// carrega Intervencao. As prontas deixaram de ser formulario: cada uma sai no
// molde de bloco do 5e, com o mesmo texto do capitulo 8 do livro do Bestiario.
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

const NUM = { 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito' };
const lista = (xs) => (xs.length > 1 ? `${xs.slice(0, -1).join(', ')} e ${xs[xs.length - 1]}` : xs[0]);
const virg = (x) => String(x).replace('.', ',');

// [nome, personagens, fator, acoes, carrega Intervencao] — peca 26 §4
function categoria(nome) {
  const c = X.CATEGORIAS.find((x) => x[0] === nome);
  if (!c) throw new Error(`a categoria "${nome}" nao existe na escada da peca 26 §4`);
  return c;
}

// ⚠ meio para BAIXO, e a regra e' declarada na peca 26 §4.1. Nao e' cosmetica:
// os fatores 0,25 e 1,50 poem doze das sessenta e tres celulas desta escala
// exatamente em ,5. O Math.round do JS arredonda meio para cima e o round do
// Python arredonda para o par — tres lugares com duas convencoes seria a licao
// no 9 num numero que o mestre le em voz alta.
const arred = (x) => Math.ceil(x - 0.5);
const esc = (v, f) => (v == null ? '—' : String(arred(v * f)));

// O dano vira DADO, no molde do resto do hobby: o `Guia do Mestre` de 2014 manda
// traduzir a margem de dano numa expressao de dado, e a peca 26 §4.4 e a dona da
// regra daqui — metade em dado, metade fixa. Abaixo de 5 o golpe e numero seco.
// v0.216: o TAMANHO do dado se escolhe entre d4 e d12, pelo que fecha a metade
// mais limpo, com no maximo oito dados na mao. Pedido do Mizuki: "n precisa
// sustentar pra sempre o d8, da pra usar d6, d4, d10, d12, para ajudar nos
// calculos". O teto de oito dados nao e cosmetico: sem ele o otimizador troca
// 5d8+26 por 10d4+24 — fecha melhor na aritmetica e e pior na mao.
const DADOS = [4, 6, 8, 10, 12];
function dado(alvo) {
  // ⚠ o piso continua 5, e nao 3. Com 3, um alvo de 3,0 virava `1d8` — que
  // entrega 4,5, cinquenta por cento a mais. Abaixo de 5 o golpe e numero seco.
  if (alvo < 5) return String(arred(alvo));
  const meta = alvo / 2;
  let bom = null;
  for (const d of DADOS) {
    const med = (d + 1) / 2;
    const n = Math.max(1, Math.round(meta / med));
    if (n > 8) continue;
    const fixo = alvo - n * med;
    if (fixo < 0) continue;
    const inteiro = Math.abs(fixo - Math.round(fixo)) < 1e-9 ? 0 : 1;
    const erro = Math.abs(n * med - meta);
    if (bom === null || inteiro < bom.inteiro
        || (inteiro === bom.inteiro && erro < bom.erro - 1e-9)
        || (inteiro === bom.inteiro && Math.abs(erro - bom.erro) < 1e-9 && n < bom.n)) {
      bom = { inteiro, erro, n, d, fixo: Math.round(fixo) };
    }
  }
  if (bom === null) {                       // nenhum dado coube no teto
    const n = Math.max(1, Math.round(alvo / 9));
    const m = arred(alvo - 4.5 * n);
    return m > 0 ? `${n}d8 + ${m}` : `${n}d8`;
  }
  return bom.fixo > 0 ? `${bom.n}d${bom.d} + ${bom.fixo}` : `${bom.n}d${bom.d}`;
}

function media(e) {
  const m = /^(\d+)d(\d+)(?:\s*\+\s*(\d+))?$/.exec(String(e).trim());
  return m ? Number(m[1]) * (1 + Number(m[2])) / 2 + Number(m[3] || 0) : Number(e);
}
// O dano de rodada da categoria. Quem carrega Intervencao leva o fator dela,
// pela peca 26 §6.5 — a Intervencao e acao extra e se paga no dano. A ordem e a
// do livro do Bestiario: o dano de rodada arredondado, e o fator por cima.
function danoDaRodada(danoLinha, c) {
  const r = arred(danoLinha * c[2]);
  return c[4] ? arred(r * X.FATOR_INTERVENCAO) : r;
}
function golpe(danoLinha, c) { return dado(danoDaRodada(danoLinha, c) / c[3]); }
// o golpe CRU, sem o fator — e dele que sai o orcamento de feitico (peca 26 §6.5)
function golpeCru(danoLinha, c) { return dado(arred(danoLinha * c[2]) / c[3]); }
// o molde do 5e: a media, arredondada para baixo, e os dados entre parenteses
const fmtGolpe = (e) => (String(e).includes('d') ? `\`${Math.floor(media(e))} (${e})\`` : `\`${e}\``);

function derivada(nv) {
  const dv = X.DERIVADAS.find((x) => {
    const [a, b] = x[0].split(' a ').map(Number);
    return nv >= a && nv <= b;
  });
  if (!dv) throw new Error(`nenhuma linha de DERIVADAS cobre o nivel ${nv}`);
  return dv;
}
// a protecao anda junto do refino — peca 11 §6: um terco do refino, mais um
const protecao = (refino) => Math.floor(refino / 3) + 1;

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
  out.push(...nomeGrande(v('nome'), f ? `${v('categoria')} ${v('sub')} · nível do grupo ${v('nivel')}` : 'tamanho · categoria · sub-categoria · nível do grupo · grau'));
  out.push(regra());
  out.push(stat('Defesa', v('defesa'), vazio));
  out.push(stat('Vida e Integridade', f ? `${v('vida')} · ${v('vida')}` : '', vazio));
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
  out.push(stat('Por rodada', v('porRodada'), vazio));
  out.push(stat('Golpe', f ? `${v('acerto')} para acertar, ${v('dano')} de dano` : '', vazio));
  out.push(regra());
  out.push(BLOCO('traços — Passivas, aptidões e técnica', v('caracteristicas'), 2));
  out.push(BLOCO(`Intervenções — ${NUM[X.INTERVENCOES]} por luta, de Desastre para cima`, v('intervencoes'), 2));
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
  const c = categoria('Desastre');
  const dv = derivada(10);
  const elem = X.RESISTENCIA.find((r) => r[0] === 'Elementais');
  return {
    nome: 'Maldição de nível 10', grau: '—', nivel: '10', categoria: c[0], sub: 'sozinho',
    forca: '3', destreza: '3', con: '2', int: '1', ess: '0',
    trs: 'Físico e Vigor',
    resist: `resistência a Elementais — multiplica o fator por ${elem[2].replace('×', '')}`,
    vida: esc(f[5], c[2]), dano: golpe(f[6], c), porRodada: `${NUM[c[3]]} ações, e uma Reação`,
    defesa: String(dv[1]), acerto: `+${dv[2]}`, cd: String(dv[3]), refino: String(dv[4]),
    caracteristicas: 'Escama (Passiva) · duas aptidões do catálogo da peça 11',
    intervencoes: 'a primeira bate um pouco menos que uma ação; as outras duas mudam o campo',
    pacto: 'nenhum — a Essência dele é 0, e o teto é metade dela',
    notas: `Age ${NUM[c[3]]} vezes por rodada e rola o dado uma vez em cada. Um esquadrão de ${NUM[X.CAMBIO]} capangas de ${f[7]} de vida vale o mesmo encontro.`,
  };
})();

// ------------------------------------------------------ 3. AS SEIS PRONTAS
// Cada numero aqui e COMPUTADO de FAIXAS, CATEGORIAS e DERIVADAS, e nenhum e
// lido das PRONTAS: elas guardam so escolha e texto. O texto traz marcadores, e
// esta funcao enche cada um pela mesma regra que o livro do Bestiario usa — um
// marcador que ninguem conhece mata a geracao em vez de sair em branco.
const FEM = { Minúsculo: 'Minúscula', Pequeno: 'Pequena', Médio: 'Média', Grande: 'Grande', Imenso: 'Imensa', Colossal: 'Colossal' };
const TR_TODOS = ['Físico', 'Vigor', 'Intelecto', 'Espírito'];
const rotNv = (a, b) => (a === b ? `nível ${a}` : `nível ${a} a ${b}`);

function montaPronta(p) {
  const f = X.FAIXAS.find((x) => x[0] === p.faixa);
  if (!f) throw new Error(`a faixa "${p.faixa}" de ${p.nome} nao existe em FAIXAS`);
  const c = categoria(p.categoria);
  const [lo, hi] = [f[1], f[2]];
  const seg = [];
  for (let nv = lo; nv <= hi; nv++) {
    const dv = derivada(nv);
    const ch = [dv[1], dv[2], dv[3], dv[4]];
    const u = seg[seg.length - 1];
    if (u && u[2].join('|') === ch.join('|')) u[1] = nv; else seg.push([nv, nv, ch]);
  }
  const porMarco = (i, fmt) => {
    const base = fmt(seg[0][2][i]);
    const extra = seg.slice(1).filter((s) => s[2][i] !== seg[0][2][i])
      .map((s) => `${fmt(s[2][i])} no ${rotNv(s[0], s[1])}`);
    return base + (extra.length ? ` (${extra.join('; ')})` : '');
  };
  const tam = X.TAMANHOS.find((t) => t[0] === p.tamanho);
  if (!tam) throw new Error(`o tamanho "${p.tamanho}" de ${p.nome} nao existe`);
  const alcance = `${virg(tam[1] * 1.5)} m`;
  const area = X.AREA_NATURAL.find((a) => a[0] <= lo && hi <= a[1]);
  if (!area) throw new Error(`a faixa de ${p.nome} cruza uma borda da area natural`);
  const g = golpe(f[6], c);
  const pontos = media(golpeCru(f[6], c)) / ((8 + 1) / 2);   // o d8 do Fundamento
  const ret = area[5];
  const val = {
    acerto: porMarco(1, (x) => `\`+${x}\``), cd: porMarco(2, (x) => `\`${x}\``),
    alcance: `\`${alcance}\``, golpe: fmtGolpe(g),
    vizinho: tam[2] ? ', e metade desse dano em um vizinho do alvo' : '',
    esfera: `raio \`${area[3]}\``, cone: `\`${area[4]}\``,
    retangulo: `${ret.slice(0, -1).map((x) => `\`${x}\``).join(', ')} ou \`${ret[ret.length - 1]}\` quadrados`,
    deslocamento: `\`${X.DESLOCAMENTO}\``,
    tecnica_dano: fmtGolpe(`${Math.floor(pontos)}d8`), tecnica_alcance: `\`${X.ALCANCE_PROJETIL}\``,
  };
  const enche = (t) => t.replace(/\{(\w+)\}/g, (_, k) => {
    if (!(k in val)) throw new Error(`marcador {${k}} desconhecido em ${p.nome}`);
    return val[k];
  });
  // as travas do molde: Acoes Multiplas so em quem age mais de uma vez, e
  // Intervencoes so em quem a categoria da — e entao as tres
  if ((c[3] > 1) !== Boolean(p.acoes_multiplas)) {
    throw new Error(`${p.nome} age ${c[3]} vez(es) e ${p.acoes_multiplas ? 'traz' : 'nao traz'} Acoes Multiplas`);
  }
  if (c[4] !== (p.intervencoes.length > 0) || (c[4] && p.intervencoes.length !== X.INTERVENCOES)) {
    throw new Error(`${p.nome} (${c[0]}) com ${p.intervencoes.length} Intervencoes`);
  }
  return { f, c, lo, hi, seg, alcance, g, enche, vida: esc(f[5], c[2]) };
}

function blocoPronto(p) {
  const m = montaPronta(p);
  const out = [new Pg({ children: [new PageBreak()] }), ...titulo(`${p.nome} — maldição pronta`)];
  out.push(P(`*${p.linha}*`));
  out.push(P(p.notas));
  out.push(GAP(80));
  const corpos = p.corpos_na_mesa > 1 ? ` · ${NUM[p.corpos_na_mesa]} corpos` : '';
  out.push(...nomeGrande(p.nome, `Maldição ${FEM[p.tamanho]} · ${p.categoria}${corpos} · nível ${m.lo} a ${m.hi}`));
  out.push(regra());
  for (const [a, b, v] of m.seg) {
    const pre = m.seg.length > 1 ? `*${rotNv(a, b)}* · ` : '';
    out.push(stat('', `${pre}**Defesa** \`${v[0]}\` · **Acerto** \`+${v[1]}\` · **CD** \`${v[2]}\` · **Refino** \`${v[3]}\` *(proteção \`+${protecao(v[3])}\`)*`));
  }
  const mov = p.movimentos.map((mv) => ` · **${mv}** \`${X.DESLOCAMENTO}\``).join('');
  out.push(stat('', `**Vida** \`${m.vida}\` · **Integridade** \`${m.vida}\` · **O golpe** ${fmtGolpe(m.g)} *(alcance ${m.alcance})* · **Deslocamento** \`${X.DESLOCAMENTO}\`${mov}`));
  out.push(regra(C.linha));
  const at = p.arranjo.split('·').map((s) => s.trim());
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
  out.push(P('Seis fichas para abrir e usar, no molde de bloco do 5e. **Nenhum número foi escolhido:** todos saem das tabelas do fim desta folha, e os atributos cabem no orçamento de nove pontos com teto `3` que a peça 2 dá a qualquer ficha.'));
  out.push(P('**A coluna do `Capanga` está vazia.** As seis cobrem `Ameaça` e `Desastre`; ficha de esquadrão é o próximo passo.'));
  out.push(GAP(120));
  out.push(TBL(['MALDIÇÃO', 'CATEGORIA', 'NÍVEL', 'VIDA', 'GOLPE', 'AÇÕES'],
    X.PRONTAS.map((p, i) => [p.nome + (p.corpos_na_mesa > 1 ? ` (×${p.corpos_na_mesa})` : ''),
      p.categoria, p.faixa, fs6[i].vida, fs6[i].g, String(fs6[i].c[3])]),
    [20, 16, 12, 12, 26, 14], { centerCols: [2, 3, 4, 5] }));
  out.push(GAP(100));
  const fora = X.CATEGORIAS.filter((c) => c[1] != null && c[1] > 4).map((c) => `a \`${c[0]}\` exige ${NUM[c[1]]}`);
  out.push(NOTA(`A mesa padrão é de quatro, e as categorias acima dela ficam de fora das prontas: ${lista(fora)} feiticeiros. As linhas delas existem nas tabelas e montam na hora, se a sua mesa for grande.`));
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

  out.push(FAIXA('Como montar um inimigo'));
  out.push(P('**1 · Escolha o nível do grupo.** É o nível das fichas que vão sentar na mesa.'));
  const pes = X.CATEGORIAS.filter((c) => c[1] != null).map((c) => `\`${c[0]}\` é ${NUM[c[1]]}`);
  out.push(P(`**2 · Escolha a categoria.** Ela responde uma pergunta só: **quantos personagens este inimigo exige?** ${lista(pes)}. O \`Capanga\` é o bando: um esquadrão de ${NUM[X.CAMBIO]} vale um \`Desastre\`.`));
  out.push(P('**3 · Copie a linha das três primeiras tabelas** — vida, golpe, e a de Defesa, acerto e CD.'));
  out.push(P('**4 · Decida o que ele é.** O tamanho, os cinco atributos, as características que ele carrega, e se ele resiste a algum tipo de dano.'));
  out.push(P(`**5 · Se quiser um bando**, troque o corpo grande por ${NUM[X.CAMBIO]} capangas, ou ponha até três ao lado dele pela tabela *Um corpo ou vários*.`));
  const f10 = X.FAIXAS.find((x) => x[1] <= 10 && 10 <= x[2]);
  const des = categoria('Desastre');
  const dv10 = derivada(10);
  out.push(NOTA(`**Um exemplo.** Um grupo de nível 10 vai enfrentar uma maldição que os quatro precisam para derrubar. Isso é um \`Desastre\`: \`${esc(f10[5], des[2])}\` de vida, ele rola \`${golpe(f10[6], des)}\` ${NUM[des[3]]} vezes por rodada, Defesa \`${dv10[1]}\`, acerto \`+${dv10[2]}\` e CD \`${dv10[3]}\`.`));
  out.push(GAP(160));

  out.push(FAIXA('Vida'));
  out.push(P('A linha vale a **faixa inteira**. Dentro dela o grupo ganha vida e o inimigo não — se quiser manter o aperto no fim da faixa, acrescente capangas. A do `Capanga` é a de um corpo.'));
  out.push(TBL(['nível do grupo', ...X.CATEGORIAS.map((c) => c[0])],
    X.FAIXAS.map((f) => [f[0], ...X.CATEGORIAS.map((c) => (c[1] == null ? String(f[7]) : esc(f[5], c[2])))]),
    [20, 16, 16, 16, 16, 16], { centerCols: [0, 1, 2, 3, 4, 5], boldCols: [0] }));
  out.push(GAP(150));

  // ⚠ vida e golpe em tabelas SEPARADAS. Estavam na mesma celula, e o Mizuki leu
  // e disse que era informacao jogada: um numero se anota, o outro se rola.
  out.push(FAIXA('O golpe'));
  out.push(P('O `×` diz quantas vezes ele rola por rodada. **Menos ações quer dizer golpe maior**, e quem carrega `Intervenção` — do `Desastre` para cima — já sai com o fator dela.'));
  out.push(TBL(['nível do grupo', ...X.CATEGORIAS.map((c) => c[0])],
    X.FAIXAS.map((f) => [f[0], ...X.CATEGORIAS.map((c) => `${golpe(f[6], c)}  ×${c[3]}`)]),
    [15, 17, 17, 17, 17, 17], { centerCols: [0, 1, 2, 3, 4, 5], boldCols: [0] }));
  out.push(new Paragraph({ children: [new PageBreak()] }));
  out.push(FAIXA('Defesa, acerto e CD'));
  out.push(P('Esta escada muda em **marco**, e a de cima muda em **faixa de Classe**. Confira as duas separado.'));
  out.push(TBL(['nível', 'Defesa', 'acerto', 'CD do inimigo', 'refino'],
    X.DERIVADAS.map((r) => [r[0], String(r[1]), `+${r[2]}`, String(r[3]), String(r[4])]),
    [22, 20, 19, 20, 19], { centerCols: [0, 1, 2, 3, 4], boldCols: [0] }));
  out.push(NOTA('Ele acerta um alvo que investiu em defesa em **50% a 55%**, e o Teste de Resistência treinado dele falha **35%**.'));

  out.push(GAP(150));
  out.push(FAIXA('Capanga e câmbio'));
  const [rLo, rHi] = X.AMEACA_CONTRA_DESASTRE.map((v) => v.toFixed(2).replace('.', ','));
  out.push(P(`Um \`Desastre\` vale **${X.CAMBIO} capangas** do mesmo nível. O capanga cai num golpe de um personagem — a vida dele é o dano do grupo por rodada dividido por quatro, para baixo —, e o esquadrão vem com a vida num pool só. Quatro \`Ameaça\` **não** valem um \`Desastre\`: elas cobram de \`${rLo}×\` a \`${rHi}×\` o que ele cobra.`));
  out.push(TBL(['nível do grupo', 'capanga: vida', 'o dado dele', `o pool dos ${NUM[X.CAMBIO]}`],
    X.FAIXAS.map((f) => [f[0], String(f[7]), dado(f[8]), String(f[7] * X.CAMBIO)]),
    [22, 20, 22, 36], { centerCols: [0, 1, 2, 3], boldCols: [0] }));
  out.push(NOTA(`No máximo **${NUM[X.TETO_EMPILHAMENTO]}** corpos do mesmo esquadrão atacam o mesmo alvo por rodada, e do segundo em diante o golpe sai pela metade. E o esquadrão inteiro faz uma ação em área por rodada, e não uma por corpo.`));
  out.push(GAP(150));

  out.push(FAIXA('Um corpo ou vários'));
  const tomado = virg((100 - X.SUBCATEGORIAS[1][2]).toFixed(1));
  out.push(P(`O mesmo encontro cabe num corpo só ou com capangas ao lado. **Cada um dos três primeiros capangas toma \`${tomado}%\` do chefe** — a vida e o golpe dele.`));
  out.push(TBL(['a luta é…', 'o chefe fica com', 'capangas', 'e ela cobra'],
    X.SUBCATEGORIAS.map(([nome, n, frac, cobra]) => [nome, `${virg(frac.toFixed(1))}% da linha`,
      n === 0 ? '—' : String(n), `${virg(cobra.toFixed(1))}% da vida do grupo`]),
    [24, 26, 16, 34], { centerCols: [1, 2], boldCols: [0] }));
  out.push(NOTA('As quatro formas cobram o mesmo, porque a fração do chefe foi medida para isso. Acima de três capangas o câmbio deixa de ser linear: um esquadrão cheio cobre os próprios buracos.'));
  out.push(GAP(150));

  out.push(FAIXA('Resistência, imunidade e vulnerabilidade'));
  out.push(P('Resistir sobe a vida efetiva do inimigo, então ela **multiplica o fator da categoria** — e o fator vezes quatro é quantas pessoas ele exige. A vulnerabilidade não cobra nem devolve.'));
  out.push(TBL(['se ele resiste a…', 'resistir multiplica o fator por', 'ser imune multiplica por'],
    X.RESISTENCIA.map((r) => [r[0], r[2], r[3]]),
    [34, 33, 33], { centerCols: [1, 2], boldCols: [0] }));
  const imuFis = Number(X.RESISTENCIA.find((r) => r[0] === 'Físicos')[3].replace('×', '').replace(',', '.'));
  out.push(NOTA(`Um \`Desastre\` imune a \`Físicos\` exige \`${virg(Math.round(des[1] * imuFis * 10) / 10)}\` personagens, e não \`${des[1]}\`. Se você vender isso, está vendendo o item mais caro do livro.`));

  out.push(new Paragraph({ children: [new PageBreak()] }));
  out.push(FAIXA('Tamanho'));
  out.push(P('O tamanho diz onde o corpo cabe e até onde o golpe alcança. **Ele não cobra nada.**'));
  const grupos = [];
  X.TAMANHOS.forEach((t) => {
    const g = grupos.find((x) => x[1] === t[1] && x[2] === t[2]);
    if (g) g[0].push(t[0]); else grupos.push([[t[0]], t[1], t[2]]);
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
  out.push(NOTA('No máximo uma ação em área por rodada, e a de `Recarga` não conta. O `Cone` sai sempre do corpo dele, e a largura em qualquer ponto é igual à distância até ele.'));
  return out;
}

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

// a sub-categoria e lida do dados.js, e nao guardada aqui — a guarda do bloco 7
// do conferir-ficha.py procura esta forma de leitura: ([nome, n, frac, cobra])
Packer.toBuffer(doc).then((b) => {
  fs.writeFileSync('bloco-de-inimigo.docx', b);
  console.log(`gerado: bloco-de-inimigo.docx ${Math.round(b.length / 1024)} KB`);
});
