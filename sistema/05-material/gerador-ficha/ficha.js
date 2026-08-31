// As tres paginas da ficha. Uma funcao so' monta a em branco e a preenchida —
// e' o mesmo layout, e o que muda e' o objeto `f` que chega. Se fossem dois
// arquivos, eles divergiriam: e a licao no 9 do README.
const { d, C, W, SEM_BORDA, NIL, P, FAIXA, LINHA, BLOCO, cell, TBL, NOTA, GAP,
        runs } = require('./helpers.js');
const X = require('./dados.js');
const { Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType,
        AlignmentType, BorderStyle } = d;

const V = (o, k, alt = '') => (o && o[k] != null ? String(o[k]) : alt);
const CX = (marcado) => (marcado ? '■' : '☐');

// ---------------------------------------------------------------- cabecalho
function titulo(sub) {
  return [
    new Paragraph({ spacing: { after: 20 },
      children: [new TextRun({ text: 'RPG DA GUILDA', bold: true, size: 16,
        color: C.grey, characterSpacing: 90, font: 'Georgia' })] }),
    new Paragraph({ spacing: { after: 40 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: C.crimson, space: 4 } },
      children: [new TextRun({ text: sub, bold: true, size: 34, color: C.deep, font: 'Georgia' })] }),
    GAP(120),
  ];
}

// ============================================================ PAGINA 1 · FICHA
function pagina1(f) {
  const cam = X.CAMINHOS.find(c => c.nome === V(f, 'caminho')) || null;
  const at = (f && f.atributos) || {};
  const num = (k) => (f && f.numeros ? V(f.numeros, k) : '');

  const out = [...titulo('Ficha de personagem')];

  out.push(LINHA([['nome do personagem', V(f, 'nome')],
                  ['jogador', V(f, 'jogador')],
                  ['patente', V(f, 'grau', 'Grau 4')]], [46, 34, 20]));
  out.push(GAP(90));
  out.push(LINHA([['caminho', V(f, 'caminho')],
                  ['trilha', V(f, 'trilha')],
                  ['origem', V(f, 'origem')],
                  ['nível', V(f, 'nivel', String(X.NIVEL))],
                  ['xp', V(f, 'xp', '0')]], [24, 20, 28, 12, 16]));
  out.push(NOTA(`Toda ficha nasce no nível ${X.NIVEL} e Grau 4 — a patente é eixo social e sobe por feito, não por XP. ` +
                `O nível ${X.NIVEL} sobe com ${X.XP_PROXIMO} XP, que são duas missões padrão.`));

  // --- atributos
  out.push(FAIXA('Atributos'));
  out.push(new Table({
    rows: [new TableRow({ cantSplit: true, children: X.ATRIBUTOS.map(a => new TableCell({
      children: [
        new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 40, after: 30 },
          children: [new TextRun({ text: a.toUpperCase(), bold: true, size: 14, color: C.deep })] }),
        new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 30, after: 60 },
          children: [new TextRun({ text: V(at, a), bold: true, size: 40, color: C.crimson, font: 'Georgia' })] }),
      ],
      width: { size: Math.round(W / 5), type: WidthType.DXA },
      shading: { type: ShadingType.CLEAR, fill: C.bandBg, color: 'auto' },
      margins: { top: 60, bottom: 60, left: 60, right: 60 },
      borders: { top: NIL, bottom: NIL,
                 left: { style: BorderStyle.SINGLE, size: 4, color: 'FFFFFF' },
                 right: { style: BorderStyle.SINGLE, size: 4, color: 'FFFFFF' } },
    })) })],
    columnWidths: X.ATRIBUTOS.map(() => Math.round(W / 5)),
    width: { size: W, type: WidthType.DXA }, borders: SEM_BORDA,
  }));
  out.push(NOTA(`${X.PONTOS_ATRIBUTO} pontos entre os cinco, nenhum acima de ${X.TETO_ATRIBUTO}. ` +
                `O número é o modificador: não há valor separado nem tabela de conversão.`));

  // --- os numeros que caem sozinhos
  out.push(FAIXA('Os números — nada aqui é escolha'));
  const linhaVida = cam ? `(${cam.vida1} + Con) + (${cam.vidaNv} + Con)` : '(inicial + Con) + (por nível + Con)';
  const linhaPE = cam ? `${cam.peNv} × ${X.NIVEL}` : `PE do Caminho × ${X.NIVEL}`;
  out.push(TBL(['', 'a conta', 'valor', '', 'a conta', 'valor'], [
    ['Vida',        linhaVida,                    num('vida'),
     'Defesa',      `10 + Des + ${X.PROTECAO}`,   num('defesa')],
    ['Energia',     linhaPE,                      num('pe'),
     'Bloquear',    '2d10 + (Defesa − 11)',       num('bloquear')],
    ['Integridade', `${X.INTEGRIDADE_NV} + Essência`,  num('integridade'),
     'Iniciativa',  'd20 + Des',                  num('iniciativa')],
    ['Maestria',    '—',                          String(X.MAESTRIA),
     'Deslocamento','—',                          '9 m'],
    ['CD de feitiço', `8 + atr. + maestria`,      num('cd'),
     'Refino',      '—',                          String(X.REFINO)],
    ['Corpo a corpo', 'd20 + Força + maestria',   num('cac'),
     'Conjuração',  `d20 + atr. + maestria`,      num('conjuracao')],
    ['',            '',                           '',
     'À distância', 'd20 + Des + maestria',       num('distancia')],
  ], [15, 22, 11, 15, 22, 15], { boldCols: [0, 3], centerCols: [2, 5] }));
  out.push(NOTA(`A proteção ${X.PROTECAO} não é equipamento: ela é **cobrir-se de energia**, aptidão gratuita do refino ${X.REFINO} ` +
                `(\`1/3 do refino + 1\`). Ela vale sem uniforme, sem armadura e sem escudo — vestir qualquer um deles a desliga. ` +
                `Arredondamento: sempre para o lado que não te favorece, e o que você ganha nunca fica abaixo de 1.`));

  // --- testes de resistencia
  out.push(FAIXA('Testes de Resistência — dois treinados'));
  const trTreinados = (f && f.trs) || [];
  out.push(TBL(['', 'atributo', 'treinado', 'total'],
    X.TRS.map(([nome, attr]) => [nome, attr, CX(trTreinados.includes(nome)),
      trTreinados.includes(nome) ? 'd20 + atr + 2' : 'd20 + atr']),
    [18, 46, 14, 22], { boldCols: [0], centerCols: [2, 3] }));

  // --- pericias
  out.push(FAIXA('Perícias — 23, e você treina 8 (ou 9)'));
  const treinadas = (f && f.pericias) || [];
  const linhas = [];
  X.PERICIAS.forEach(([attr, lista]) => {
    lista.forEach((p, i) => linhas.push([i === 0 ? attr : '', `${CX(treinadas.includes(p))}  ${p}`]));
  });
  // tres colunas: 23 pericias cabem em 8 linhas em vez de 12
  const nCol = 3, alt = Math.ceil(linhas.length / nCol);
  const cols = Array.from({ length: nCol }, (_, c) => linhas.slice(c * alt, (c + 1) * alt));
  cols.forEach(c => { while (c.length < alt) c.push(['', '']); });
  out.push(TBL(null, Array.from({ length: alt }, (_, i) =>
    cols.flatMap(c => [c[i][0], c[i][1]])),
    [13, 21, 13, 21, 13, 19], { boldCols: [0, 2, 4] }));
  out.push(NOTA('Treinada: `d20 + atributo + maestria`. Sem treino: `d20 + atributo` — você tenta do mesmo jeito. Constituição não tem perícia; ela paga em vida.'));

  // --- oficios
  out.push(FAIXA('Ofícios — 11, e você treina 3 (ou 2)'));
  const of = (f && f.oficios) || [];
  const oAlt = Math.ceil(X.OFICIOS.length / 3);
  const oCols = Array.from({ length: 3 }, (_, c) => X.OFICIOS.slice(c * oAlt, (c + 1) * oAlt));
  oCols.forEach(c => { while (c.length < oAlt) c.push(null); });
  out.push(TBL(null, Array.from({ length: oAlt }, (_, i) =>
    oCols.map(c => (c[i] ? `${CX(of.includes(c[i]))}  ${c[i]}` : ''))), [34, 33, 33]));
  out.push(NOTA('Ofício **não tem atributo fixo**: o mestre escolhe na hora. E ofício sem treino você não tenta — ninguém forja uma lâmina por tentativa.'));

  return out;
}

// =========================================================== PAGINA 2 · TECNICA
function pagina2(f) {
  const t = (f && f.tecnica) || {};
  const out = [...titulo('A técnica')];

  out.push(BLOCO('a Regra — uma frase, verificável pela mesa, sem número',
    V(t, 'regra'), 2));
  out.push(NOTA('É o que você carrega a campanha inteira: **a técnica nunca muda**, o que evolui é o que você consegue fazer com ela. ' +
                'A Regra é lida por outra pessoa antes de entrar em jogo — quem escreveu sabe o que quis dizer; quem vai arbitrar, não.'));

  out.push(BLOCO('o atributo da técnica — um dos cinco, escolhido na criação e travado',
    V(t, 'atributo'), 1));
  out.push(NOTA('É ele que entra no **ataque de conjuração** e na **CD dos seus feitiços**, na página 1. ' +
                'Se ele ficar para trás, a sua técnica fica junto.'));

  out.push(BLOCO('descrição — de onde ela veio, como ela aparece, o que as pessoas veem',
    V(t, 'descricao'), 2));

  out.push(FAIXA('Famílias — duas Livres, três Fechadas'));
  const livres = (t.livres || []), fechadas = (t.fechadas || []);
  out.push(TBL(['família', 'Livre', 'Fechada', 'família', 'Livre', 'Fechada'],
    (() => {
      const metade = Math.ceil(X.FAMILIAS.length / 2);
      const a = X.FAMILIAS.slice(0, metade), b = X.FAMILIAS.slice(metade);
      while (b.length < a.length) b.push(null);
      return a.map((fam, i) => [fam, CX(livres.includes(fam)), CX(fechadas.includes(fam)),
        b[i] || '', b[i] ? CX(livres.includes(b[i])) : '', b[i] ? CX(fechadas.includes(b[i])) : '']);
    })(),
    [22, 12, 12, 22, 12, 20], { boldCols: [0, 3], centerCols: [1, 2, 4, 5] }));
  out.push(NOTA('Melhoria de família **Livre** custa metade da Classe a menos. De família **Fechada** você nunca compra nada. ' +
                'É aqui que duas técnicas com a mesma Regra viram personagens diferentes.'));

  out.push(LINHA([['selo — o gesto, a condição ou o objeto que a técnica exige', V(t, 'selo')]], [100]));
  out.push(NOTA('O Selo não custa nem devolve ponto: ele é identidade. Mas Restrição que o Selo já obriga **não devolve ponto**.'));

  out.push(BLOCO('Passiva Livre — uma, de graça. Não rola dado, não muda número, não faz ninguém rolar',
    V(t, 'passiva'), 2));

  out.push(FAIXA(`Feitiços de Classe 0 — ${X.CLASSE_0}, grátis, não ocupam espaço`));
  const c0 = t.classe0 || [];
  out.push(TBL(['', 'nome', 'Forma', 'o que faz'],
    Array.from({ length: X.CLASSE_0 }, (_, i) => [String(i + 1),
      V(c0[i], 'nome'), V(c0[i], 'forma'), V(c0[i], 'efeito')]),
    [7, 24, 20, 49], { centerCols: [0] }));
  out.push(NOTA('Classe 0 não gasta PE, não ocupa espaço e não se monta: escolha uma Forma e pronto. ' +
                'Cabe uma Melhoria Leve, tirando um dado para pagar.'));

  out.push(FAIXA(`Feitiços conhecidos — ${X.CONHECIDOS} de Classe ${X.CLASSE}, ${X.PONTOS_POR_FEITICO} pontos e ${X.PONTOS_POR_FEITICO} PE cada`));
  const fs = t.feiticos || [];
  for (let i = 0; i < X.CONHECIDOS; i++) {
    const fe = fs[i] || {};
    out.push(LINHA([['nome do feitiço', V(fe, 'nome')],
                    ['forma', V(fe, 'forma')],
                    ['pontos', V(fe, 'pontos', String(X.PONTOS_POR_FEITICO))],
                    ['pe', V(fe, 'pe', String(X.PONTOS_POR_FEITICO))]], [42, 30, 14, 14]));
    out.push(LINHA([['melhorias', V(fe, 'melhorias')],
                    ['restrições', V(fe, 'restricoes')],
                    ['o que ele faz', V(fe, 'efeito')]], [30, 30, 40]));
    out.push(GAP(55));
  }
  out.push(NOTA('Restrição devolve ponto; Melhoria gasta. **A Liberação Máxima chega no nível 10** e a Técnica Máxima no 17 — nenhuma das duas existe ainda.'));

  return out;
}

// ================================================ PAGINA 3 · LORE E REFERENCIA
function pagina3(f) {
  const l = (f && f.lore) || {};
  const out = [...titulo('Quem é essa pessoa')];

  out.push(NOTA('Esta é a página que atravessa as mesas: numa guilda com sete mestres, é ela que faz o seu personagem ser reconhecido numa mesa em que nunca jogou. Nada aqui rola dado.'));

  out.push(BLOCO('aparência — o que se vê antes de você abrir a boca', V(l, 'aparencia'), 2));
  out.push(BLOCO('história — como você chegou aqui', V(l, 'historia'), 4));

  out.push(FAIXA('O que a Origem te deu'));
  out.push(BLOCO('o traço — um acesso, uma obrigação, um contato, uma marca no corpo, alguém atrás de você',
    V(l, 'traco'), 2));
  out.push(BLOCO('o Legado Destranca — obrigatório, zero no dado, e é quem você é', V(l, 'legado'), 2));
  out.push(BLOCO('o segundo Legado — de qualquer lista da sua Origem', V(l, 'legado2'), 2));

  out.push(FAIXA('Laços'));
  out.push(BLOCO('quem você conhece, quem te deve, quem te cobra', V(l, 'lacos'), 2));
  out.push(BLOCO('a instituição — o que ela sabe de você, e o que ela não sabe', V(l, 'instituicao'), 2));

  out.push(BLOCO('pacto — opcional, e a maioria começa sem', V(l, 'pacto'), 2));
  out.push(NOTA('**Provisório:** pacto entre personagens ainda não tem regra, e **na criação ele não entra** — quem quiser começar com um usa a `Regra Própria` do manual ou um `Legado`, que é onde essa ficção já mora.'));

  // --- a tira de referencia: SO' o que e estrutural e nao envelhece
  out.push(FAIXA('Referência rápida'));
  out.push(TBL(['', ''], [
    ['O turno', 'movimento 9 m + ação padrão + ação bônus + reação'],
    ['Arredondamento', 'sempre para o lado que não te favorece. Custo sobe, ganho desce, e o que você ganha nunca fica abaixo de 1'],
    ['Crítico', '20 natural, e dobra os dados — só onde há rolagem de acerto'],
    ['Os dois golpes', 'canalizado = os dados da Classe e nada mais, um por turno. Simples = arma + Força'],
    ['Os dois descansos', 'curto devolve 25% do PE máximo em ambiente propício; longo zera o relógio e a exaustão'],
  ], [22, 78], { boldCols: [0] }));
  out.push(NOTA('Isto é só o que não muda. **CDs, condições, exaustão e o resto da mesa estão na quick-start** — repetir número em dois documentos é como eles divergem. Nota de campanha vai no verso.'));

  return out;
}

module.exports = { pagina1, pagina2, pagina3 };
