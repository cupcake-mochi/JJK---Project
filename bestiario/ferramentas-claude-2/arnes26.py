import os, shutil, subprocess, glob, filecmp
REPO = '/media/mizuki/HD Externo II/Claude/Claude 2'
CP = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'arnes')
PECA = 'sistema/03-mecanica/26-bestiario.md'
def monta():
    shutil.rmtree(CP, ignore_errors=True)
    fs = [os.path.relpath(f, REPO) for f in glob.glob(os.path.join(REPO, 'sistema/03-mecanica/*.md'))]
    fs += ['sistema/03-mecanica/conferir-bestiario.py', 'manual/Fundamento-MANUAL-v7.docx',
           'sistema/05-material/gerador-inimigo/dados.js', 'sistema/05-material/bloco-de-inimigo.docx']
    for f in fs:
        os.makedirs(os.path.dirname(os.path.join(CP, f)), exist_ok=True)
        shutil.copy2(os.path.join(REPO, f), os.path.join(CP, f))
def roda():
    o = subprocess.run(['python3', 'conferir-bestiario.py'], cwd=os.path.join(CP, 'sistema/03-mecanica'),
                       capture_output=True, text=True).stdout
    return [l.strip()[3:] for l in o.split('\n') if l.strip().startswith('!! ')], ('PULADA' in o)
monta(); BASE, pul = roda()
print(f'base na copia: {len(BASE)} erro(s), PULADA={pul}')
for b in BASE: print('   ', b[:110])
assert len(BASE) == 1 and BASE[0].startswith('5: o capanga da tabela') and not pul, 'a base da copia nao e a esperada'
P = [
 ('3', 'a vida do Capanga no §4.1 vira 33', '| `Capanga` | `32` vida · `19` dano |', '| `Capanga` | `33` vida · `19` dano |', True),
 ('3', 'o fator da Calamidade vira 2,10', '| **`Calamidade`** | 8 | `× 2,00` | `6` | sim |', '| **`Calamidade`** | 8 | `× 2,10` | `6` | sim |', True),
 ('4', 'o Desastre publica 4 acoes', '| **`Desastre`** | 4 | `× 1,00` | `3` | sim |', '| **`Desastre`** | 4 | `× 1,00` | `4` | sim |', True),
 ('4', 'a Catastrofe publica 0 acoes', '| **`Catástrofe`** | 6 | `× 1,50` | `5` | sim |', '| **`Catástrofe`** | 6 | `× 1,50` | `0` | sim |', True),
 ('5', 'a peca publica o cambio em sete', '> **Um `Desastre` vale oito capangas do mesmo nível.**', '> **Um `Desastre` vale sete capangas do mesmo nível.**', True),
 ('5', 'a derivacao da vida do capanga some', '**Vida do capanga = o dano do grupo por rodada dividido por quatro, arredondado para baixo.**', '**Vida do capanga = um pedaço do dano do grupo.**', True),
 ('5.1', 'o `com dois` passa a cobrar 67,9%', '| **`com dois`** | `83,0%` | `2` | `67,4%` |', '| **`com dois`** | `83,0%` | `2` | `67,9%` |', True),
 ('5.1', 'o chefe do `com um apoio` fica com 92,0%', '| **`com um apoio`** | `91,5%` | `1` | `67,5%` |', '| **`com um apoio`** | `92,0%` | `1` | `67,5%` |', True),
 ('7.1', 'a Catastrofe com Expansao vira 12,0', '| **`Catástrofe`** | `6` | `11,5` |', '| **`Catástrofe`** | `6` | `12,0` |', True),
 ('8', 'resistir aos Fisicos vira 1,60', 'multiplica o fator da categoria por `1,43`.**', 'multiplica o fator da categoria por `1,60`.**', True),
 ('8', 'a peca para de declarar a moeda', '> **Resistência ao grupo `Físicos` multiplica o fator da categoria por `1,43`.**', '> **Resistência ao grupo `Físicos` custa caro.**', True),
 ('9.1', 'o Desastre do nivel 20 vira 11,1', '| nível 20 | `8,2` | `8,2` | `10,1` | `9,0` | `10,1` |', '| nível 20 | `8,2` | `8,2` | `11,1` | `9,0` | `10,1` |', True),
 ('9.1', 'o fator da Intervencao vira 0,950', 'é multiplicado por `0,923`.**', 'é multiplicado por `0,950`.**', True),
 ('9.2', 'CONTRA-PROVA: o Desastre volta aos 16% da cota crua', '| `Domínio Simples` e `Pétala` · `1 ×` maior Classe | `65%` | `18%` |', '| `Domínio Simples` e `Pétala` · `1 ×` maior Classe | `65%` | `16%` |', True),
 ('9.4', 'uma porta troca a moeda por "o mestre decide"', '| **o que dá vida efetiva** | **multiplica o fator** da categoria, pelo §6.3 |', '| **o que dá vida efetiva** | o mestre decide |', True),
 ('*', 'CONTRA-TESTE: mexer em prosa sem mexer em numero', '**O `Desastre` é a linha do manual sem tocar em nada.**', '**O `Desastre` é a linha do manual, e nada nela muda.**', False),
 ('*', 'CONTRA-TESTE: a Calamidade vira 10 pessoas, coerente em todas as tabelas', None, None, False),
]
ok = 0
for chk, desc, old, new, acende in P:
    monta(); f = os.path.join(CP, PECA); t = open(f, encoding='utf-8').read()
    if old is None:   # a Calamidade de 10 pessoas: fator 2,50, e as tabelas que dependem dele
        reps = [('| **`Calamidade`** | 8 | `× 2,00` | `6` | sim |', '| **`Calamidade`** | 10 | `× 2,50` | `6` | sim |'),
                ('| `Calamidade` | `780` · `150` | `1320` · `294` | `1890` · `438` |', '| `Calamidade` | `975` · `188` | `1650` · `368` | `2362` · `548` |'),
                ('| **`Calamidade`** | `8` | `15,4` |', '| **`Calamidade`** | `10` | `19,2` |'),
                ('| nível 10 | `4,2` | `4,2` | `5,1` | `4,5` | `5,1` |', '| nível 10 | `4,2` | `4,2` | `5,1` | `4,5` | `6,6` |'),
                ('| nível 15 | `6,2` | `6,2` | `7,6` | `6,9` | `7,6` |', '| nível 15 | `6,2` | `6,2` | `7,6` | `6,9` | `9,4` |'),
                ('| nível 20 | `8,2` | `8,2` | `10,1` | `9,0` | `10,1` |', '| nível 20 | `8,2` | `8,2` | `10,1` | `9,0` | `12,5` |'),
                ('| nível 25 | `10,2` | `10,2` | `12,5` | `11,2` | `12,5` |', '| nível 25 | `10,2` | `10,2` | `12,5` | `11,2` | `15,7` |'),
                ('| nível 30 | `12,2` | `12,2` | `15,0` | `13,5` | `15,0` |', '| nível 30 | `12,2` | `12,2` | `15,0` | `13,5` | `18,8` |')]
    else:
        reps = [(old, new)]
    for a, b in reps:
        assert t.count(a) == 1, (desc, a)
        t = t.replace(a, b)
    open(f, 'w', encoding='utf-8').write(t)
    assert not filecmp.cmp(f, os.path.join(REPO, PECA), shallow=False), 'a perturbacao nao mudou o arquivo'
    errs, pul = roda()
    novos = [e for e in errs if e not in BASE]
    acendeu = any(e.split(':')[0] == chk for e in novos) if chk != '*' else bool(novos)
    certo = (acendeu == acende) and not pul
    ok += certo
    print(f'  {chk:<4} {desc:<68} esperado {"acende" if acende else "verde ":<6}  deu {"acende" if acendeu else "verde ":<6} {"" if certo else "  <-- ERRADO"}')
    if not certo:
        for e in novos[:4]: print('         ', e[:120])
print(f'  == {ok} de {len(P)} perturbacoes deram o esperado')
