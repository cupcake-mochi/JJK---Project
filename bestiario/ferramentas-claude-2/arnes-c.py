# Arnes de perturbacao das checagens novas do commit C (v0.221):
#   conferir-bestiario  3.3 (tamanho) · 9.5 (as prontas) · 9.6 (a area natural)
#   conferir-ficha      bloco 7: 7a · 7b-bis · 7c-bis · 7c-ter
#
# As tres regras do §7 da peca 26: copia isolada; base conferida verde, com PULADA
# zero, antes de perturbar; e o arquivo perturbado tem de diferir do original antes
# de rodar. O veredito e lido da MENSAGEM da checagem testada — nunca do codigo de
# retorno —, e cada perturbacao que acende imprime a mensagem, para conferir que
# acendeu pelo motivo certo.
#
#   python3 arnes-c.py            (ARNES_COPIA=<pasta> muda onde a copia mora)
import os, re, shutil, subprocess, filecmp, sys

REPO = '/media/mizuki/HD Externo II/Claude/Claude 2'
CP = os.environ.get('ARNES_COPIA', '/tmp/claude-1000/-media-mizuki-HD-Externo-II-Claude-Bestiario/'
                    '8caa82d6-467d-4d5d-bdd6-3e44a9933b71/scratchpad/arnes-c')
PECA = 'sistema/03-mecanica/26-bestiario.md'
DJ = 'sistema/05-material/gerador-inimigo/dados.js'
PC = 'manual/gerador/partC.js'
CB, CF = 'conferir-bestiario.py', 'conferir-ficha.py'
EXCL = ['.git', 'finalizado', 'node_modules', 'PDFs - Sistemas Extras', '_to_delete', '_backup',
        '.claude', 'Fichas - Teste']


def copia():
    shutil.rmtree(CP, ignore_errors=True)
    subprocess.run(['rsync', '-a'] + [a for e in EXCL for a in ('--exclude', e)] + [REPO + '/', CP + '/'],
                   check=True)


def restaura():
    for r in (PECA, DJ, PC):
        shutil.copy2(os.path.join(REPO, r), os.path.join(CP, r))
        assert filecmp.cmp(os.path.join(REPO, r), os.path.join(CP, r), shallow=False), r


def roda(v):
    r = subprocess.run(['python3', v], cwd=os.path.join(CP, 'sistema/03-mecanica'),
                       capture_output=True, text=True)
    o = r.stdout + r.stderr
    errs = [l.strip()[3:] for l in o.split('\n') if l.strip().startswith('!! ')]
    pul = [l for l in o.split('\n') if re.search('pulad', l, re.I)
           and not re.match(r'^\s*~*\s*PULADA\.?\s*$', l)]
    return errs, pul, 'Traceback' in o, r.returncode


def aplica(ops):
    tocados = set()
    for op in ops:
        if op[0] == 're':
            _, rel, pat, rep, n = op
            f = os.path.join(CP, rel)
            t = open(f, encoding='utf-8').read()
            achou = len(re.findall(pat, t))
            assert achou == n, ('re', rel, pat[:70], achou)
            t = re.sub(pat, rep, t)
        else:
            rel, old, new = op
            f = os.path.join(CP, rel)
            t = open(f, encoding='utf-8').read()
            assert t.count(old) == 1, (rel, old[:80], t.count(old))
            t = t.replace(old, new)
        open(f, 'w', encoding='utf-8').write(t)
        tocados.add(rel)
    for rel in tocados:
        assert not filecmp.cmp(os.path.join(CP, rel), os.path.join(REPO, rel), shallow=False), \
            f'a perturbacao nao mudou {rel}'


# (validador, checagem, descricao, operacoes, acende?, trecho da mensagem esperada)
# Contra-teste (acende = False): no conferir-bestiario, NADA novo pode acender; no
# conferir-ficha, nada novo pode acender no bloco 7.
P = [
    # ---- 3.3 · o tamanho ------------------------------------------------------------
    (CB, '3.3', 'o alcance do `Grande` vira `4,5 m`',
     [(PECA, '| **`Grande`** | `2×2` *(3 × 3 m)* | `3 m` |', '| **`Grande`** | `2×2` *(3 × 3 m)* | `4,5 m` |')],
     True, 'publica alcance'),
    (CB, '3.3', 'o `Médio` passa a pegar metade num vizinho',
     [(PECA, '| `1,5 m` | só o alvo |', '| `1,5 m` | o alvo, e metade em `1` vizinho |')],
     True, 'a coluna dos alvos diz'),
    (CB, '3.3', 'a peça para de declarar que o tamanho não cobra nada',
     [(PECA, '**o tamanho não cobra nada.**', '**ele é de graça.**')],
     True, 'parou de declarar que o tamanho nao cobra nada'),
    (CB, '3.3', 'CONTRA-TESTE: o `Colossal` vira `5×5`, com alcance `7,5 m` — coerente',
     [(PECA, '| **`Colossal`** | `4×4` *(6 × 6 m)* | `6 m` |', '| **`Colossal`** | `5×5` *(7,5 × 7,5 m)* | `7,5 m` |')],
     False, None),
    # ---- 9.5 · as prontas -------------------------------------------------------------
    (CB, '9.5', 'a `Kitsune` volta para a `Dupla`, que morreu',
     [(DJ, "nome: 'Kitsune', faixa: '9 a 12', categoria: 'Ameaça',", "nome: 'Kitsune', faixa: '9 a 12', categoria: 'Dupla',")],
     True, 'que nao existe na escada'),
    (CB, '9.5', 'o `Oni` sobe para `Catástrofe`, que exige seis pessoas',
     [(DJ, "nome: 'Oni', faixa: '5 a 8', categoria: 'Desastre',", "nome: 'Oni', faixa: '5 a 8', categoria: 'Catástrofe',")],
     True, 'tem de caber na mesa padrao'),
    (CB, '9.5', 'o `Betobeto` ganha Ações Múltiplas agindo uma vez',
     [(DJ, 'quando a luta começa."}],\n    acoes_multiplas: null,',
       'quando a luta começa."}],\n    acoes_multiplas: "O Betobeto faz dois ataques de Pisada.",')],
     True, 'Acoes Multiplas dela nao bate'),
    (CB, '9.5', 'a `Tsuchigumo` perde a terceira `Intervenção`',
     [(DJ, ', {"nome": "Subir", "texto": "A Tsuchigumo escala até {deslocamento} pela parede ou pelo teto. '
           'Esse movimento não provoca ataque de oportunidade."}] },', '] },')],
     True, 'carrega 2 Intervencao'),
    (CB, '9.5', 'a `Hitotsume` vai para uma faixa que não existe, `6 a 8`',
     [(DJ, "nome: 'Hitotsume', faixa: '5 a 8',", "nome: 'Hitotsume', faixa: '6 a 8',")],
     True, 'que nao existe nas FAIXAS'),
    (CB, '9.5', 'uma pronta volta a guardar a vida',
     [(DJ, "nome: 'Betobeto', faixa: '2 a 4', categoria: 'Ameaça',", "nome: 'Betobeto', faixa: '2 a 4', categoria: 'Ameaça', vida: 38,")],
     True, "as PRONTAS guardam ['vida']"),
    (CB, '9.5', 'a peça passa a dar duas `Intervenções` por luta',
     [(PECA, 'carrega três `Intervenções` por luta', 'carrega duas `Intervenções` por luta')],
     True, 'pede 2'),
    (CB, '9.5', 'CONTRA-TESTE: a `Kitsune` desce para `5 a 8` — a derivação do seis morreu',
     [(DJ, "nome: 'Kitsune', faixa: '9 a 12',", "nome: 'Kitsune', faixa: '5 a 8',")],
     False, None),
    (CB, '9.5', 'CONTRA-TESTE: o `Oni` vira `Ameaça`, sem Ações Múltiplas e sem Intervenções',
     [(DJ, "nome: 'Oni', faixa: '5 a 8', categoria: 'Desastre',", "nome: 'Oni', faixa: '5 a 8', categoria: 'Ameaça',"),
      (DJ, 'acoes_multiplas: "O Oni faz três ataques de Kanabō, ou usa Pancada no Chão e faz dois ataques de Kanabō.",',
       'acoes_multiplas: null,'),
      ('re', DJ, r'    intervencoes: \[\{"nome": "Kanabō", "texto": "O Oni faz um ataque de Kanabō\..*?\] \},',
       '    intervencoes: [] },', 1)],
     False, None),
    # ---- 9.6 · a area natural -------------------------------------------------------
    (CB, '9.6', 'a cobertura do nível `9`–`16` vira `29` quadrados',
     [(PECA, '| `9`–`16` | `28` quadrados |', '| `9`–`16` | `29` quadrados |')],
     True, 'e a tabela publica 29'),
    (CB, '9.6', 'o `Cone` do nível `2`–`8` vira `9 m`',
     [(PECA, '| `13` quadrados | raio `3 m` | `7,5 m` |', '| `13` quadrados | raio `3 m` | `9 m` |')],
     True, 'o cone cobre 18'),
    (CB, '9.6', 'um retângulo `12×1` vira `16×1`',
     [(PECA, '`7×2` · `12×1` |', '`7×2` · `16×1` |')],
     True, 'o retangulo 16×1 cobre 16'),
    (CB, '9.6', 'a faixa `17`–`24` passa a começar no `18`',
     [(PECA, '| `17`–`24` |', '| `18`–`24` |')],
     True, 'nao comeca onde a anterior terminou'),
    (CB, '9.6', 'a escada de esfera do manual troca o segundo degrau para `5 m`',
     [(PC, "['Esfera (raio)', '3 m → 4,5 m → 6 m → 9 m → 15 m'],", "['Esfera (raio)', '3 m → 5 m → 6 m → 9 m → 15 m'],")],
     True, 'a escada de esfera do manual comeca em'),
    (CB, '9.6', 'a tolerância declarada cai para `5,0%`',
     [(PECA, 'nas doze células é `12,5%`', 'nas doze células é `5,0%`')],
     True, 'que a peca declara'),
    (CB, '9.6', 'a área natural para no nível `28`',
     [(PECA, '| `25`–`30` |', '| `25`–`28` |')],
     True, 'a area natural para no nivel 28'),
    (CB, '9.6', 'CONTRA-TESTE: o `12×1` vira `13×1`, que dá a cobertura exata',
     [(PECA, '`7×2` · `12×1` |', '`7×2` · `13×1` |')],
     False, None),
    (CB, '9.6', 'CONTRA-TESTE: mexer na prosa da área natural sem mexer em número',
     [(PECA, '**Nem todo ataque em área vem de técnica.**', '**Nem todo ataque em área sai de técnica.**')],
     False, None),
    # ---- conferir-ficha, bloco 7 ------------------------------------------------------
    (CF, '7a', 'a `Catástrofe` do dados.js age `4` vezes',
     [('re', DJ, r"\['Catástrofe',\s*6,\s*1\.50,\s*5,\s*true\]", "['Catástrofe', 6, 1.50, 4, true]", 1)],
     True, 'as categorias do dados.js nao batem'),
    (CF, '7a', 'o `Desastre` do dados.js perde a `Intervenção`',
     [('re', DJ, r"\['Desastre',\s*4,\s*1\.00,\s*3,\s*true\]", "['Desastre', 4, 1.00, 3, false]", 1)],
     True, 'as categorias do dados.js nao batem'),
    (CF, '7b-bis', 'a vida do capanga da faixa `13 a 16` vira `46` — faixa que o §4.1 não publica',
     [('re', DJ, r"(\['13 a 16',\s*13,\s*16,\s*4,\s*180,\s*540,\s*111,\s*)45(,\s*28\])", r"\g<1>46\g<2>", 1)],
     True, 'o capanga do dados.js nao e o da escada'),
    (CF, '7b-bis', 'o dano do capanga da faixa `21 a 25` vira `45`',
     [('re', DJ, r"(\['21 a 25',\s*21,\s*25,\s*6,\s*275,\s*825,\s*183,\s*68,\s*)46\]", r"\g<1>45]", 1)],
     True, 'o capanga do dados.js nao e o da escada'),
    (CF, '7c-bis', 'o chefe do `com dois` fica com `83,5%` no dados.js',
     [('re', DJ, r"\['com dois',\s*2,\s*83\.0,\s*67\.4\]", "['com dois', 2, 83.5, 67.4]", 1)],
     True, 'a sub-categoria do dados.js'),
    (CF, '7c-ter', 'o fator da `Intervenção` vira `0,95` no dados.js',
     [(DJ, 'const FATOR_INTERVENCAO = 0.923;', 'const FATOR_INTERVENCAO = 0.95;')],
     True, 'o fator da Intervencao:'),
    (CF, '7c-ter', 'o dados.js passa a dar `2` `Intervenções` por luta',
     [(DJ, 'const INTERVENCOES = 3;', 'const INTERVENCOES = 2;')],
     True, 'quantas Intervencoes por luta:'),
    (CF, '7c-ter', 'o teto de empilhamento vira `4` no dados.js',
     [(DJ, 'const TETO_EMPILHAMENTO = 3;', 'const TETO_EMPILHAMENTO = 4;')],
     True, 'o teto de empilhamento:'),
    (CF, '7c-ter', 'o deslocamento vira `12 m` no dados.js',
     [(DJ, "const DESLOCAMENTO = '9 m';", "const DESLOCAMENTO = '12 m';")],
     True, 'o deslocamento:'),
    (CF, '7c-ter', 'o alcance do `Projétil` vira `24 m` no dados.js',
     [(DJ, "const ALCANCE_PROJETIL = '18 m';", "const ALCANCE_PROJETIL = '24 m';")],
     True, 'o alcance do Projetil'),
    (CF, '7c-ter', 'a razão do §4.3 vira `0,75 ×` a `0,80 ×` no dados.js',
     [(DJ, 'const AMEACA_CONTRA_DESASTRE = [0.75, 0.77];', 'const AMEACA_CONTRA_DESASTRE = [0.75, 0.80];')],
     True, 'a razao de quatro Ameaca'),
    (CF, '7c-ter', 'o `Grande` ocupa `3` quadrados de lado no dados.js',
     [('re', DJ, r"\['Grande',\s*2,\s*true\]", "['Grande', 3, true]", 1)],
     True, 'o tamanho do dados.js'),
    (CF, '7c-ter', 'o `Cone` do nível `9` a `16` vira `12 m` no dados.js',
     [(DJ, "'10,5 m'", "'12 m'")],
     True, 'a area natural do dados.js'),
    (CF, '7c-ter', 'CONTRA-TESTE: o deslocamento vira `12 m` na peça E no dados.js',
     [(PECA, '| deslocamento | `9 m` |', '| deslocamento | `12 m` |'),
      (DJ, "const DESLOCAMENTO = '9 m';", "const DESLOCAMENTO = '12 m';")],
     False, None),
    (CF, '7c-ter', 'CONTRA-TESTE: a peça E o dados.js passam a dar duas `Intervenções` por luta',
     [(PECA, 'carrega três `Intervenções` por luta', 'carrega duas `Intervenções` por luta'),
      (DJ, 'const INTERVENCOES = 3;', 'const INTERVENCOES = 2;')],
     False, None),
    (CF, '7a', 'CONTRA-TESTE: a `Calamidade` age `7` vezes na peça E no dados.js',
     [(PECA, '| **`Calamidade`** | 8 | `× 2,00` | `6` | sim |', '| **`Calamidade`** | 8 | `× 2,00` | `7` | sim |'),
      ('re', DJ, r"\['Calamidade',\s*8,\s*2\.00,\s*6,\s*true\]", "['Calamidade', 8, 2.00, 7, true]", 1)],
     False, None),
]

copia()
restaura()
for v in (CB, CF):
    e, p, tb, rc = roda(v)
    print(f'base na copia, {v}: {len(e)} erro(s), PULADA {len(p)}, traceback {tb}, codigo {rc}')
    for x in e[:5]:
        print('   ', x[:150])
    assert not e and not p and not tb and rc == 0, 'a base da copia nao esta verde — nao perturbo'

ok = 0
for v, chk, desc, ops, acende, marca in P:
    restaura()
    aplica(ops)
    errs, pul, tb, rc = roda(v)
    if acende:
        bate = [e for e in errs if marca in e]
        acendeu = bool(bate)
    else:
        bate = errs if v == CB else [e for e in errs if e.startswith('7:')]
        acendeu = bool(bate)
    certo = (acendeu == acende) and not pul and not tb
    ok += certo
    print(f'  {v[9:13]} {chk:<7} {desc:<86} esperado {"acende" if acende else "verde ":<6}  '
          f'deu {"acende" if acendeu else "verde ":<6}{"" if certo else "   <-- ERRADO"}')
    if bate:
        print(f'{"":15}| {bate[0][:170]}')
    if not certo:
        for x in (errs[:4] + pul[:2]):
            print(f'{"":15}! {x[:170]}')
        if tb:
            print(f'{"":15}! TRACEBACK')
restaura()
print(f'  == {ok} de {len(P)} perturbacoes deram o esperado')
sys.exit(0 if ok == len(P) else 1)
