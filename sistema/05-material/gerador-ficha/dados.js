// Os catalogos que a ficha imprime.
//
// ATENCAO: nenhum destes valores e' autoridade. A autoridade e' a peca de
// 03-mecanica, e o conferir-ficha.py compara os dois — se alguem acrescentar
// uma pericia na peca 7 e esquecer daqui, o validador falha. Foi por nao existir
// uma checagem assim que a peca 8 passou sete versoes com a Defesa errada.

// as 23 pericias, por atributo (peca 7, secao 4)
const PERICIAS = [
  ['Força',        ['Atletismo']],
  ['Destreza',     ['Acrobacia', 'Furtividade', 'Pontaria', 'Prestidigitação']],
  ['Inteligência', ['Investigação', 'Intuição', 'Ocultismo', 'Religião', 'História',
                    'Hierarquia', 'Medicina', 'Sobrevivência', 'Natureza',
                    'Lidar com Animais', 'Tecnologia']],
  ['Essência',     ['Sentir Energia', 'Percepção', 'Persuasão', 'Enganação',
                    'Intimidação', 'Atuação', 'Provocar']],
];

// os 11 oficios (peca 7, secao 5). Oficio NAO tem atributo fixo: o mestre
// escolhe na hora, conforme o que voce faz com ele.
const OFICIOS = ['Condução', 'Arrombamento', 'Herbalismo', 'Forja', 'Caligrafia',
                 'Burocracia', 'Entalhador', 'Alfaiate', 'Culinária', 'Instrumento', 'Jogatina'];

// os 5 Caminhos (peca 8, passo 3) — vida no nv1, vida por nivel, PE por nivel.
// Sem oficio fixo desde a v0.105: o Caminho da dois oficios LIVRES.
const CAMINHOS = [
  { nome: 'Bastião',   dado: 'd12', vida1: 12, vidaNv: 7, peNv: 4,
    pericias: ['Atletismo', 'Intimidação'],
    trilhas: ['Muro', 'Punho', 'Brasa'] },
  { nome: 'Vanguarda', dado: 'd8',  vida1: 8,  vidaNv: 5, peNv: 5,
    pericias: ['Acrobacia', 'Percepção'],
    trilhas: ['Estocada', 'Batedor', 'Executor'] },
  { nome: 'Guia',      dado: 'd8',  vida1: 8,  vidaNv: 5, peNv: 5,
    pericias: ['Persuasão', 'Medicina'],
    trilhas: ['Elo', 'Sutura', 'Perímetro'] },
  { nome: 'Evocador',  dado: 'd6',  vida1: 6,  vidaNv: 4, peNv: 6,
    pericias: ['Religião', 'Lidar com Animais'],
    trilhas: ['Servo', 'Matilha', 'Coro'] },
  { nome: 'Emanador',  dado: 'd6',  vida1: 6,  vidaNv: 4, peNv: 6,
    pericias: ['Ocultismo', 'Investigação'],
    trilhas: ['Torrente', 'Explosivo', 'Arremate'] },
];

// as Origens (peca 9)
const ORIGENS = ['Latente', 'Receptáculo', 'Descendente', 'Reencarnado', 'Feto'];
const ORIGENS_ESPECIAIS = ['Corpo Amaldiçoado', 'Restrição Celestial'];
const SUB_ORIGEM = 'Sem Técnica';

// os 4 Testes de Resistencia (peca 1)
const TRS = [
  ['Físico',    'Força ou Destreza — travado na criação'],
  ['Vigor',     'Constituição'],
  ['Intelecto', 'Inteligência'],
  ['Espírito',  'Essência'],
];

const ATRIBUTOS = ['Força', 'Destreza', 'Constituição', 'Inteligência', 'Essência'];

// as 9 Familias do Fundamento — 2 Livres e 3 Fechadas na criacao (manual, secao 3)
const FAMILIAS = ['Ataque', 'Área', 'Controle', 'Castigo', 'Amparo',
                  'Corpo', 'Movimento', 'Auxiliares', 'Percepção'];

// o nivel padrao da ficha, e o que ele implica
const NIVEL = 2;
const MAESTRIA = 1;
const REFINO = 1;
const PROTECAO = Math.floor(REFINO / 3) + 1;   // cobrir-se de energia, peca 11
const CLASSE = 1;                               // manual, tabela de progressao
const PONTOS_POR_FEITICO = 3 * CLASSE;
const CONHECIDOS = 2 + Math.floor(NIVEL / 2);   // peca 8, formula da v0.27
const CLASSE_0 = 2;                             // manual
const XP_PROXIMO = 100;                         // peca 12, faixa "2 a 4"
const INTEGRIDADE = 20 + 8 * (NIVEL - 1);
const PONTOS_ATRIBUTO = 9;
const TETO_ATRIBUTO = 3;

module.exports = { PERICIAS, OFICIOS, CAMINHOS, ORIGENS, ORIGENS_ESPECIAIS,
  SUB_ORIGEM, TRS, ATRIBUTOS, FAMILIAS, NIVEL, MAESTRIA, REFINO, PROTECAO,
  CLASSE, PONTOS_POR_FEITICO, CONHECIDOS, CLASSE_0, XP_PROXIMO, INTEGRIDADE,
  PONTOS_ATRIBUTO, TETO_ATRIBUTO };
