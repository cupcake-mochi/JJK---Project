# o contra-teste da Calamidade de 10 pessoas, com cada numero calculado pela regra da peca
import os, sys, math, shutil, subprocess
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'proto26.py')).read().split("print('MANUAL'")[0])
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import importlib.util
spec = importlib.util.spec_from_file_location('arn', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'arnes26.py'))
src = open(spec.origin, encoding='utf-8').read().split('monta(); BASE, pul = roda()')[0]
exec(src)
F = 2.5
def cel41(nv): s, cv, cd, _, _ = MAN[nv]; return f'`{mb(cv * F)}` · `{mb(cd * F)}`'
def pts(nv):
    s, cv, cd, _, _ = MAN[nv]; p = dado(arred(cd * F) / 6)[1] * 0.923 / 4.5
    return 'seco' if p < 3 - 1e-9 else f'`{p:.1f}`'.replace('.', ',')
reps = [('| **`Calamidade`** | 8 | `× 2,00` | `6` | sim |', '| **`Calamidade`** | 10 | `× 2,50` | `6` | sim |'),
        ('| `Calamidade` | `780` · `150` | `1320` · `294` | `1890` · `438` |', f'| `Calamidade` | {cel41(10)} | {cel41(20)} | {cel41(30)} |'),
        ('| **`Calamidade`** | `8` | `15,4` |', f'| **`Calamidade`** | `10` | `{round(10 * 1.92, 1):.1f}` |'.replace('.', ','))]
T0 = open(os.path.join(REPO, PECA), encoding='utf-8').read()
for ln in T0.split('\n'):
    if ln.startswith('| nível ') and ln.count('|') == 7 and ('seco' in ln or '`' in ln):
        nv = int(ln.split('nível ')[1].split(' ')[0]); cels = ln.split('|')
        cels[6] = f' {pts(nv)} '
        reps.append((ln, '|'.join(cels)))
monta(); BASE, _ = roda()
f = os.path.join(CP, PECA); t = open(f, encoding='utf-8').read()
for a, b in reps:
    assert t.count(a) == 1, a
    t = t.replace(a, b); print('  ', b[:100])
open(f, 'w', encoding='utf-8').write(t)
errs, pul = roda(); novos = [e for e in errs if e not in BASE]
print('  CONTRA-TESTE Calamidade de 10 pessoas, coerente:', 'VERDE' if not novos and not pul else 'ACENDEU', *[n[:110] for n in novos[:4]], sep='\n    ')
