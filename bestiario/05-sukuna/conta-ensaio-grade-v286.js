// Ensaio de integração, não ficha final. Os números vêm do gerador atual.
const C = require('../../sistema/05-material/gerador-inimigo/conta.js');
const nivel = 30, pessoas = 6, categoria = 'Calamidade', papel = 'Artilheiro';
const f = C.X.FAIXAS.find(x => x[1] <= nivel && nivel <= x[2]);
const d = C.degrau(categoria), fp = C.fatorPapel(papel, d, pessoas);
const base = C.vidaCel(f, d, pessoas), comPapel = C.vidaCel(f, d, pessoas, fp.vida);
const comparar = pv => ({ pv, cura: Math.floor(pv / d[1] / pessoas), parte: Math.floor(pv / d[1] * 2 / pessoas) });
console.log(JSON.stringify({ nivel, pessoas, categoria, papel, rodadas: d[1], acoes: pessoas,
  golpe: C.golpe(f, d), derivadas: C.derivada(nivel), divisorIntervencao: C.precoIntervencao(d, pessoas),
  referenciaBase: comparar(d[1] * pessoas * (f[4] / 4)), apenasPapel: comparar(comPapel),
  decisao: "Cura e partes usam PV-base antes dos ajustes, com arredondamento apenas no resultado.",
  status: 'PV final ainda não fechado; referência PV-base aprovada; apenasPapel é alternativa rejeitada.'
}, null, 2));
