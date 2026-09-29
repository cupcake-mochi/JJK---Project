// A CONTA do bloco de inimigo — pura, sem o pacote `docx`.
//   node conta.js --json     as seis prontas calculadas, para o capitulo 8 do livro do Bestiario
//
// v0.282: separada do make.js para o livro poder ler as prontas numa copia do repositorio sem
// node_modules. O make.js monta o .docx em cima destas funcoes; o livro formata o --json. A conta
// mora aqui, e so aqui: duas contas do mesmo numero sao dois donos.
const X = require('./dados.js');

const NUM = { 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco', 6: 'seis', 7: 'sete', 8: 'oito' };
const lista = (xs) => (xs.length > 1 ? `${xs.slice(0, -1).join(', ')} e ${xs[xs.length - 1]}` : xs[0]);
const virg = (x) => String(x).replace('.', ',');

// [nome, rodadas, orcamento] — peca 26 §4
function degrau(nome) {
  const c = X.DEGRAUS.find((x) => x[0] === nome);
  if (!c) throw new Error(`a categoria "${nome}" nao existe na grade da peca 26 §4`);
  return c;
}
const RODADAS_DESASTRE = degrau('Desastre')[1];
// a pressao: o orcamento do degrau x as rodadas do Desastre ÷ as rodadas dele
const pressao = (dg) => (dg[2] * RODADAS_DESASTRE) / dg[1];
// a porta da Intervencao: N x orcamento >= 4, e o Capanga nao tem
const temIntervencao = (dg, n) => dg[0] !== 'Capanga' && n * dg[2] >= X.PORTA_INTERVENCAO;
// e o preco dela, na vida: 1 + 0,75 ÷ (rodadas × N) — peca 26 §6.5
const precoIntervencao = (dg, n) => 1 + X.INTERVENCAO_EXTRA / (dg[1] * n);

// ⚠ meio para BAIXO, e a regra e' declarada na peca 26 §4.1. Nao e' cosmetica:
// os fatores 0,25 e 1,50 poem doze das sessenta e tres celulas desta escala
// exatamente em ,5. O Math.round do JS arredonda meio para cima e o round do
// Python arredonda para o par — tres lugares com duas convencoes seria a licao
// no 9 num numero que o mestre le em voz alta.
const arred = (x) => Math.ceil(x - 0.5);
// v0.228: a Integridade do inimigo e metade da vida maxima, para baixo (peca 24 SS3.3).
const integridadeDe = (vida) => (/^\d+$/.test(String(vida)) ? String(Math.floor(Number(vida) / 2)) : vida);

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
// A celula, peca 26 §4. f e a linha de FAIXAS: f[4] e o dano do grupo por rodada e f[6]
// o dano do chefe. A saida de um personagem e f[4] ÷ 4, e o golpe-base e f[6] ÷ 4.
const vidaCel = (f, dg, n, fv = 1) => arred(dg[1] * n * (f[4] / 4) * fv);
const golpeAlvo = (f, dg) => (dg[0] === 'Capanga' ? arred(f[6] / 8) : arred(pressao(dg) * f[6] / 4));
function golpe(f, dg) { return dado(golpeAlvo(f, dg)); }
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
// a maestria — peca 1 §2: 1 do nivel 2 ao 9, e +1 a cada oito niveis
const maestria = (nv) => Math.floor((nv - 2) / 8) + 1;
const NOMES_AT = ['Força', 'Destreza', 'Constituição', 'Inteligência', 'Essência'];

// ------------------------------------------------------ 3. AS SEIS PRONTAS
// Cada numero aqui e COMPUTADO de FAIXAS, CATEGORIAS e DERIVADAS, e nenhum e
// lido das PRONTAS: elas guardam so escolha e texto. O texto traz marcadores, e
// esta funcao enche cada um pela mesma regra que o livro do Bestiario usa — um
// marcador que ninguem conhece mata a geracao em vez de sair em branco.
const FEM = { Minúsculo: 'Minúscula', Pequeno: 'Pequena', Médio: 'Média', Grande: 'Grande', Imenso: 'Imensa', Colossal: 'Colossal' };
const TR_TODOS = ['Físico', 'Vigor', 'Intelecto', 'Espírito'];
const rotNv = (a, b) => (a === b ? `nível ${a}` : `nível ${a} a ${b}`);

// O papel da peca 26 §3.4. Ele REDISTRIBUI a base: o que ganha num eixo paga no
// outro, e o produto fecha em 1,000 — o encontro nao muda de tamanho, muda de
// forma. Os tres de fator fixo saem da tabela; os tres variaveis saem das ACOES,
// porque o preco deles e UMA acao, e o `Capanga` se le por esquadrao.
function fatorPapel(nome, dg, n) {
  if (!nome) return { vida: 1, defesa: 0 };
  const p = X.PAPEIS.find((x) => x[0] === nome);
  if (!p) throw new Error(`papel desconhecido: ${nome}`);
  if (dg[0] === 'Capanga' && X.PAPEIS_FORA_DO_CAPANGA.includes(nome)) {
    throw new Error(`o Capanga nao aceita ${nome}: um corpo que nao cai num golpe deixa de ser Capanga`);
  }
  if (p[1] !== null) return { vida: p[1], defesa: p[2] };
  if (p[3] === 'alcance') return { vida: 1 / (1 + X.GANHO_ALCANCE / dg[1]), defesa: 0 };
  const acoes = dg[0] === 'Capanga' ? X.CORPOS_POR_PESSOA * n : n;
  const ganha = p[3] === 'vantagem' ? (acoes - 1 + X.MULT_VANTAGEM) / acoes : 1 + 1 / acoes;
  return { vida: 1 / ganha, defesa: 0 };
}

function montaPronta(p) {
  const f = X.FAIXAS.find((x) => x[0] === p.faixa);
  if (!f) throw new Error(`a faixa "${p.faixa}" de ${p.nome} nao existe em FAIXAS`);
  const dg = degrau(p.categoria);
  const n = p.n;
  if (!(n >= 1 && n <= X.N_MAXIMO)) throw new Error(`${p.nome}: o N ${n} fica fora de ×1 a ×${X.N_MAXIMO}`);
  const chefe = temIntervencao(dg, n);
  // v0.234: o arranjo cabe na criação — nove pontos, dez para o chefe (quem carrega Intervenção), teto 3
  const arr = p.arranjo.split('·').map(Number);
  if (arr.some((x) => x > 3) || arr.reduce((s, x) => s + x, 0) !== (chefe ? 10 : 9)) {
    throw new Error(`${p.nome}: o arranjo ${p.arranjo} nao e ${chefe ? 'dez' : 'nove'} pontos com teto 3`);
  }
  // v0.235: a pronta declara o atributo de ataque, e cada ponto de marco com o atributo dele
  const iAtk = NOMES_AT.indexOf(p.ataque);
  if (iAtk < 0) throw new Error(`${p.nome}: o ataque "${p.ataque}" nao e um dos cinco atributos`);
  const pontosMarco = Object.entries(p.marcos || {}).flatMap(([mk, ats]) => {
    if (!Array.isArray(ats)) throw new Error(`${p.nome}: o marco ${mk} tem de ser uma lista de atributos`);
    return ats.map((a) => {
      if (!NOMES_AT.includes(a)) throw new Error(`${p.nome}: o marco ${mk} leva "${a}", que nao e atributo`);
      return [Number(mk), a];
    });
  });
  const atNv = (nv) => arr.map((v, i) => v + pontosMarco.filter(([mk, a]) => mk <= nv && a === NOMES_AT[i]).length);
  const fp = fatorPapel(p.papel, dg, n);
  const [lo, hi] = [f[1], f[2]];
  const seg = [];
  for (let nv = lo; nv <= hi; nv++) {
    const dv = derivada(nv);
    // v0.234: a Defesa sai do arranjo — 10 + Destreza + proteção, e o papel por fora (peça 26 §3.4).
    // v0.235: o acerto e a CD saem do atributo de ataque, com a maestria. Os dois têm de ser os da
    // curva; só o chefe pode ter 1 a mais, e é um ponto só, na Destreza ou no ataque.
    const at = atNv(nv);
    const exDes = at[1] - (dv[1] - 10 - protecao(dv[4]));
    const exAtk = at[iAtk] - (dv[2] - maestria(nv));
    const acima = exDes + (iAtk === 1 ? 0 : exAtk);
    if (exDes < 0 || exAtk < 0 || acima > (chefe ? 1 : 0)) {
      throw new Error(`${p.nome} no nivel ${nv}: Destreza ${at[1]} e ${p.ataque} ${at[iAtk]}, e a tabela pede ${dv[1] - 10 - protecao(dv[4])} e ${dv[2] - maestria(nv)}${chefe ? ' (ou 1 a mais num deles, de chefe)' : ''}`);
    }
    const ch = [dv[1] + fp.defesa + exDes, dv[2] + exAtk, dv[3] + exAtk, dv[4]];
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
  const g = golpe(f, dg);
  const pontos = media(g) / ((8 + 1) / 2);   // o d8 do Fundamento: o golpe e o orcamento (peca 26 §6.5)
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
  // as travas do molde: Acoes Multiplas so em quem age mais de uma vez, com o numero de
  // ataques igual ao N, e Intervencoes so onde a porta abre — e entao as tres
  if ((n > 1) !== Boolean(p.acoes_multiplas)) {
    throw new Error(`${p.nome} age ${n} vez(es) e ${p.acoes_multiplas ? 'traz' : 'nao traz'} Acoes Multiplas`);
  }
  const mAt = p.acoes_multiplas ? /faz (\w+) ataques/.exec(p.acoes_multiplas) : null;
  if (p.acoes_multiplas && (!mAt || mAt[1] !== NUM[n])) {
    throw new Error(`${p.nome} age ${n} vezes, e as Acoes Multiplas dizem "${mAt ? mAt[1] : '?'}" ataques`);
  }
  if (chefe !== (p.intervencoes.length > 0) || (chefe && p.intervencoes.length !== X.INTERVENCOES)) {
    throw new Error(`${p.nome} (${dg[0]} ×${n}) com ${p.intervencoes.length} Intervencoes`);
  }
  const fInt = chefe ? 1 / precoIntervencao(dg, n) : 1;
  return { f, dg, n, chefe, lo, hi, seg, alcance, g, pontos, enche, atNv, iAtk, vida: String(vidaCel(f, dg, n, fp.vida * fInt)) };
}

function prontasJson() {
  return X.PRONTAS.map((p) => {
    const m = montaPronta(p);
    const atr = [];
    for (let nv = m.lo; nv <= m.hi; nv++) atr.push(m.atNv(nv));
    return {
      nome: p.nome, linha: p.linha, notas: p.notas, tamanho: p.tamanho, categoria: p.categoria, n: m.n,
      papel: p.papel || null, corpos: p.corpos_na_mesa, lo: m.lo, hi: m.hi, faixa: p.faixa,
      seg: m.seg.map(([a, b, v]) => [a, b, v, protecao(v[3])]), vida: Number(m.vida), golpe: m.g,
      pontos: m.pontos, atributos: atr, iAtk: m.iAtk, trs: p.trs, movimentos: p.movimentos,
      tracos: p.tracos.map((x) => ({ nome: x.nome, texto: m.enche(x.texto) })),
      acoes_multiplas: p.acoes_multiplas ? m.enche(p.acoes_multiplas) : null,
      acoes: p.acoes_nomeadas.map((x) => ({ nome: x.nome, texto: m.enche(x.texto) })),
      intervencoes: p.intervencoes.map((x) => ({ nome: x.nome, texto: m.enche(x.texto) })),
    };
  });
}


module.exports = { X, NUM, lista, virg, degrau, RODADAS_DESASTRE, pressao, temIntervencao, precoIntervencao,
                   arred, integridadeDe, DADOS, dado, media, vidaCel, golpeAlvo, golpe, fmtGolpe, derivada,
                   protecao, maestria, NOMES_AT, FEM, TR_TODOS, rotNv, fatorPapel, montaPronta, prontasJson };

if (require.main === module && process.argv.includes('--json')) {
  console.log(JSON.stringify(prontasJson()));
}
