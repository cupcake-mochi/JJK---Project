// Gera o BLOCO DE INIMIGO — a folha que o mestre leva para a mesa.
//   node make.js
// Sai bloco-de-inimigo.docx, que e copiado para 05-material/.
//
// Sao tres partes, e a ordem importa:
//   1. AS TABELAS   o mestre le e copia. Tudo aqui deriva; nada e escolha.
//   2. O BLOCO      as dezessete linhas da peca 26 §3, para preencher.
//   3. O EXEMPLO    o mesmo bloco com os numeros de uma Alcateia de nivel 10.
const d = require('docx');
const fs = require('fs');
const H = require('../gerador-ficha/helpers.js');
// ⚠ A PALETA E A DO LIVRO, e nao a da ficha. As duas existem no projeto: a ficha
// e o manual do Fundamento usam ameixa 741B47; o Manual da Guilda, que e o que o
// jogador recebe, usa selo #211C35 com acento #8A7444. O bloco de inimigo e
// material de mesa como o livro, entao ele segue o livro. Os valores saem do
// :root do livro/build/manual.css.
// v0.200: as duas paletas do projeto viraram UMA — a Neve Saturado — entao o
// bloco nao precisa mais de paleta propria. A chamada fica porque os helpers da
// ficha sao os mesmos, e um dia isto pode divergir de novo.
H.setPaleta({
  ink: '251727', crimson: 'BC2A6E', deep: '2B1B2E', grey: '847B86',
  rule: 'F8C7DC', linha: '9A6F87', bandBg: 'F7E5EE', headBg: '2B1B2E',
  zebra: 'FADDEA', boxBg: 'FDF0F6', campoBg: 'FDF0F6',
});
const { C, W, P, FAIXA, TBL, BLOCO, LINHA, NOTA, GAP } = H;
const X = require('./dados.js');
const { Document, Packer, Paragraph, TextRun, Footer, AlignmentType, PageBreak } = d;

const acoes = (pes) => Math.max(1, pes - 1);
// ⚠ meio para BAIXO, e a regra e' declarada na peca 26 §4.1. Nao e' cosmetica:
// 19 das 56 celulas desta folha caem exatamente em ,5, porque os fatores sao
// 0,25 · 0,50 · 1,50. O Math.round do JS arredonda meio para cima e o round do
// Python arredonda para o par — tres lugares com duas convencoes seria a licao
// no 9 num numero que o mestre le em voz alta.
const arred = (x) => Math.ceil(x - 0.5);
const esc = (v, f) => (v == null ? '—' : String(arred(v * f)));

// O dano vira DADO, no molde do resto do hobby: o `Guia do Mestre` de 2014 manda
// traduzir a margem de dano numa expressao de dado, e a peca 26 §4.4 e a dona da
// regra daqui — metade em d8, metade fixa. Abaixo de 3 nao vale a pena: o d8
// balancaria mais que o proprio golpe.
function dado(alvo) {
  // ⚠ o piso e 5, e nao 3. Com 3, um alvo de 3,0 virava `1d8` — que entrega 4,5,
  // cinquenta por cento a mais — e a linha da Classe 1 saia com `1` ao lado de
  // `1d8`, que le como defeito. Com 5 a faixa mais baixa fica toda em numero
  // seco, e nenhuma celula da tabela erra mais de 20% do alvo.
  if (alvo < 5) return String(arred(alvo));
  const n = Math.max(1, Math.round(alvo / 9));
  const m = arred(alvo - 4.5 * n);
  return m > 0 ? `${n}d8 + ${m}` : `${n}d8`;
}
function golpe(danoRodada, fator, pes) {
  return dado(arred(danoRodada * fator) / acoes(pes));
}

function titulo(sub) {
  return [
    new Paragraph({ spacing: { after: 40 },
      children: [new TextRun({ text: 'PROJETO - M', bold: true, size: 15,
                               color: C.grey, characterSpacing: 60 })] }),
    new Paragraph({ spacing: { after: 160 },
      children: [new TextRun({ text: sub, bold: true, size: 34, color: C.crimson })] }),
  ];
}

// --------------------------------------------------------------- 1. TABELAS
// ⚠ O texto daqui passou pela REGRA-DE-VOZ.md na v0.199, e ela corta tres
// coisas que a primeira versao tinha: a folha falando de si mesma ("sao duas
// tabelas por isso"), a justificativa do numero ("a Alcateia e a linha do
// manual sem tocar em nada") e titulo em frase. O que fica responde "quanto e"
// e "o que acontece" — nunca "por que o numero e esse".
function tabelas() {
  const out = [new Paragraph({ children: [new PageBreak()] }),
               ...titulo('As tabelas')];
  out.push(P('As tabelas de onde saem os números da ficha. **Você só volta aqui quando monta um inimigo novo.**'));
  out.push(GAP(140));

  out.push(FAIXA('Como montar um inimigo'));
  out.push(P('**1 · Escolha o nível do grupo.** É o nível das fichas que vão sentar na mesa.'));
  out.push(P('**2 · Escolha a categoria.** Ela responde uma pergunta só: **quantos personagens este inimigo exige?** `Ronda` é um, `Dupla` é dois, `Alcateia` é quatro, `Calamidade` é seis.'));
  out.push(P('**3 · Copie a linha das três primeiras tabelas** — vida, golpe, e a de Defesa, acerto e CD.'));
  out.push(P('**4 · Decida o que ele é.** Os cinco atributos, as características que ele carrega, e se ele resiste a algum tipo de dano.'));
  out.push(P('**5 · Se quiser um bando**, troque o corpo grande por quatro capangas na terceira tabela.'));
  out.push(NOTA('**Um exemplo.** Um grupo de nível 10 vai enfrentar uma maldição que os quatro precisam para derrubar. Isso é uma `Alcateia`: `475` de vida, ela rola `1d8 + 4` três vezes por rodada, Defesa `16`, acerto `+6` e CD `14`.'));
  out.push(GAP(160));

  out.push(FAIXA('Vida'));
  out.push(P('A linha vale a **faixa inteira**. Dentro dela o grupo ganha vida e o inimigo não — se quiser manter o aperto no fim da faixa, acrescente capangas.'));
  out.push(TBL(['nível do grupo', ...X.CATEGORIAS.map(c => c[0])],
    X.FAIXAS.map(f => [f[0], ...X.CATEGORIAS.map(c => esc(f[5], c[2]))]),
    [22, 19, 19, 20, 20], { centerCols: [0,1,2,3,4], boldCols: [0] }));
  out.push(GAP(150));

  // ⚠ vida e golpe em tabelas SEPARADAS. Estavam na mesma celula, `82 · 1d8`, e o
  // Mizuki leu e disse que era informacao jogada. Sao dois numeros de naturezas
  // diferentes — um se anota, o outro se rola — e uma celula com os dois nao
  // bate o olho. O 5e faz igual: a vida e um numero, e o golpe fica na linha de
  // acao, longe dela.
  out.push(FAIXA('O golpe'));
  out.push(P('O `×` diz quantas vezes ele rola por rodada. **Menos ações quer dizer golpe maior** — a `Dupla` bate mais forte que a `Calamidade` e entrega menos no total.'));
  // o `×N` vai na CELULA e nao so no cabecalho: o golpe nao cresce junto com a
  // categoria — a `Dupla` bate mais forte que a `Calamidade` porque tem uma acao
  // contra cinco —, e sem o multiplicador na frente do numero isso le como erro.
  out.push(TBL(['nível do grupo', ...X.CATEGORIAS.map(c => c[0])],
    X.FAIXAS.map(f => [f[0], ...X.CATEGORIAS.map(
      c => `${golpe(f[6], c[2], c[1])}  ×${acoes(c[1])}`)]),
    [16, 21, 21, 21, 21], { centerCols: [0,1,2,3,4], boldCols: [0] }));
  out.push(new Paragraph({ children: [new PageBreak()] }));
  out.push(FAIXA('Defesa, acerto e CD'));
  out.push(P('Esta escada muda em **marco**, e a de cima muda em **faixa de Classe**. Confira as duas separado.'));
  out.push(TBL(['nível', 'Defesa', 'acerto', 'CD do inimigo', 'refino'],
    X.DERIVADAS.map(r => [r[0], String(r[1]), `+${r[2]}`, String(r[3]), String(r[4])]),
    [22, 20, 19, 20, 19], { centerCols: [0,1,2,3,4], boldCols: [0] }));
  out.push(NOTA('Ele acerta um alvo que investiu em defesa em **50% a 55%**, e o Teste de Resistência treinado dele falha **35%**.'));

  out.push(GAP(150));
  out.push(FAIXA('Capanga e câmbio'));
  const [rLo, rHi] = X.RONDA_CONTRA_ALCATEIA.map(v => v.toFixed(2).replace('.', ','));
  out.push(P(`Um chefe de \`Alcateia\` vale **${X.CAMBIO} capangas** do mesmo nível. Quatro \`Ronda\` **não** valem uma \`Alcateia\`: elas cobram de \`${rLo}×\` a \`${rHi}×\` o que ela cobra.`));
  out.push(TBL(['nível do grupo', 'capanga: vida', 'o dado dele', `${X.CAMBIO} deles somam`],
    X.FAIXAS.map(f => {
      const [rot, , , , , , , kv, kd] = f;
      return kv == null
        ? [rot, '—', '—', 'a faixa não tem capanga']
        : [rot, String(kv), dado(kd), `${kv * X.CAMBIO} de vida somada`];
    }), [22, 20, 22, 36], { centerCols: [0,1,2], boldCols: [0] }));
  out.push(GAP(150));

  out.push(FAIXA('Um corpo ou vários'));
  out.push(P('O mesmo encontro cabe num corpo só ou repartido. **Cada capanga que entra tira um quarto do chefe** — a vida e o golpe dele.'));
  out.push(TBL(['a luta é…', 'o chefe fica com', 'capangas', 'e ela cobra'],
    X.SUBCATEGORIAS.map(([nome, n, cobra]) => {
      const frac = 1 - n / X.CAMBIO;
      return [nome, `${Math.round(frac * 100)}% da linha`, n === 0 ? '—' : String(n),
              `${cobra}% da vida do grupo`];
    }), [24, 26, 16, 34], { centerCols: [1,2], boldCols: [0] }));
  out.push(NOTA('Repartir sai um pouco **mais barato**, e não mais caro: o dano do inimigo despenca conforme os corpos caem, e um corpo único não despenca nunca.'));
  out.push(GAP(150));

  out.push(FAIXA('Resistência, imunidade e vulnerabilidade'));
  out.push(P('Resistir sobe a vida efetiva do inimigo, então ela **custa degrau de categoria**. Vulnerabilidade devolve na mesma moeda.'));
  out.push(TBL(['se ele resiste a…', 'resistência custa', 'imunidade custa'],
    X.RESISTENCIA.map(r => [r[0], r[5], r[6]]),
    [34, 33, 33], { centerCols: [1,2], boldCols: [0] }));
  out.push(NOTA('Imunidade a `Físicos` custa **mais** de um degrau, e não existe degrau acima da `Calamidade` — ela só cabe num inimigo que já esteja abaixo do topo.'));
  return out;
}

// ----------------------------------------------------------------- 2. BLOCO
// ⚠ O FORMATO E O DE BLOCO DE MONSTRO, e nao o de formulario. A primeira versao
// desta folha era uma planilha de construcao — quatro tabelas de consulta e um
// formulario para preencher —, e o Mizuki leu e disse que era confuso. O molde
// certo estava no Guia do Volo: um bloco vertical, lido de cima para baixo, com
// tudo ja calculado. Ninguem MONTA um monstro no 5e; a pessoa LE ele.
//
// A ordem e a de la, traduzida: nome, o que ele e, defesa e vida, deslocamento,
// os atributos numa linha so', o que ele resiste, o que ele carrega, e as acoes
// por ultimo — que e' o que se usa na rodada.
const { Paragraph: Pg } = d;

function regra(cor) {
  return new Pg({ spacing: { before: 60, after: 60 },
    border: { bottom: { style: d.BorderStyle.SINGLE, size: 10, color: cor || C.crimson } },
    children: [new TextRun({ text: '', size: 2 })] });
}
function stat(rotulo, valor, vazio) {
  const kids = [new TextRun({ text: rotulo + ' ', bold: true, size: 19, color: C.deep })];
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

function bloco(f, primeiro) {
  const v = (k) => (f ? (f[k] ?? '') : '');
  const vazio = !f;
  const out = [];
  if (!primeiro) out.push(new Pg({ children: [new PageBreak()] }));
  out.push(...titulo(f ? 'Ficha de inimigo — exemplo' : 'Ficha de inimigo'));
  if (vazio) out.push(P('Preencha de cima para baixo. **Defesa, vida, refino e o golpe você copia das tabelas do fim**; o resto você decide.'));
  out.push(GAP(120));

  out.push(...nomeGrande(v('nome'), f ? `${v('categoria')} ${v('sub')} · nível do grupo ${v('nivel')}` : 'categoria · sub-categoria · nível do grupo · grau'));
  out.push(regra());
  out.push(stat('Defesa', v('defesa'), vazio));
  out.push(stat('Vida e Integridade', f ? `${v('vida')} · ${v('vida')}` : '', vazio));
  out.push(stat('Deslocamento', f ? '9 m' : '', vazio));
  out.push(regra(C.linha));
  out.push(TBL(['FOR', 'DES', 'CON', 'INT', 'ESS'],
    [[v('forca'), v('destreza'), v('con'), v('int'), v('ess')]],
    [20, 20, 20, 20, 20], { centerCols: [0,1,2,3,4] }));
  out.push(regra(C.linha));
  out.push(stat('Testes de Resistência', f ? `${v('trs')} — os dois treinados` : '', vazio));
  out.push(stat('CD dele', v('cd'), vazio));
  out.push(stat('Refino', v('refino'), vazio));
  out.push(stat('Resistência · imunidade · vulnerabilidade', v('resist'), vazio));
  out.push(regra());

  out.push(new Pg({ spacing: { before: 60, after: 40 },
    children: [new TextRun({ text: 'AÇÕES', bold: true, size: 20, color: C.crimson,
                             characterSpacing: 40 })] }));
  out.push(stat('Por rodada', f ? `${v('acoes')} ações, e uma Reação` : '', vazio));
  out.push(stat('Golpe', f ? `${v('acerto')} para acertar, ${v('dano')} de dano` : '', vazio));
  out.push(regra());

  out.push(BLOCO('características — Passivas, aptidões e técnica', v('caracteristicas'), 3));
  out.push(BLOCO('pacto — o teto do permanente é metade da Essência dele', v('pacto'), 2));
  out.push(BLOCO('o que ele faz na mesa', v('notas'), 3));
  return out;
}

// O exemplo NAO tem nome nem ficcao de proposito: batizar maldicao e escolha
// de sabor do Mizuki, e o catalogo de prontas e a versao seguinte. O que este
// exemplo mostra e' o PREENCHIMENTO — de onde cada numero saiu.
const EXEMPLO = {
  nome: 'Maldição de nível 10',
  grau: '—', nivel: '10', categoria: 'Alcateia', sub: 'sozinho',
  forca: '3', destreza: '3', con: '2', int: '1', ess: '0',
  trs: 'Físico e Vigor',
  resist: 'resistência a Elementais — meio degrau, cobrado',
  vida: '475', dano: '1d8 + 4', acoes: '3',
  defesa: '16', acerto: '+6', cd: '14', refino: '4',
  caracteristicas: 'Escama (Passiva) · duas aptidões do catálogo da peça 11',
  pacto: 'nenhum — a Essência dele é 0, e o teto é metade dela',
  notas: 'Age três vezes por rodada, e rola o dado uma vez em cada. Quatro capangas de 70 de vida valem o mesmo encontro.',
};

const doc = new Document({
  creator: 'Projeto - M', title: 'Bloco de inimigo',
  styles: { default: { document: { run: { font: 'Calibri', size: 20, color: C.ink } } } },
  sections: [{
    // ⚠ 1153 nao e escolha: A4 tem 11906 twips e as tabelas tem 9600, entao
    // (11906 - 9600) / 2 = 1153 de cada lado. Com 760 a mancha ficava 786 twips
    // mais larga que as tabelas e o texto corria pra direita alem de todas elas.
    properties: { page: { margin: { top: 720, bottom: 640, left: 1153, right: 1153 } } },
    footers: { default: new Footer({ children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: 'Projeto - M · bloco de inimigo · peça 26',
                               size: 14, color: C.grey })] })] }) },
    children: [...bloco(null, true), ...bloco(EXEMPLO), ...tabelas()],
  }],
});

Packer.toBuffer(doc).then(b => {
  fs.writeFileSync('bloco-de-inimigo.docx', b);
  console.log(`gerado: bloco-de-inimigo.docx ${Math.round(b.length / 1024)} KB`);
});
