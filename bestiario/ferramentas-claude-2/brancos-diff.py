# Itemiza a lista branca da checagem 7.2 do conferir-repositorio entre duas arvores da
# entrega. As tres regex sao lidas do proprio conferir-repositorio.py (ast), e o laco
# e o mesmo da checagem — nenhuma copia a mao.
import ast, re, os, sys
from collections import Counter
R = '/media/mizuki/HD Externo II/Claude/Claude 2'
env = {'re': re}
for node in ast.walk(ast.parse(open(R + '/conferir-repositorio.py', encoding='utf-8').read())):
    if (isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name)
            and node.targets[0].id in ('RX_MD', 'IGNORAR', 'BRANCOS_RX') and node.targets[0].id not in env):
        env[node.targets[0].id] = eval(compile(ast.Expression(node.value), '<rx>', 'eval'), env)
RX_MD, IGNORAR, BRANCOS_RX = env['RX_MD'], env['IGNORAR'], env['BRANCOS_RX']
def brancos(ENT):
    nomes = set()
    for _b, d, f in os.walk(ENT):
        d[:] = [x for x in d if x != '.git']; nomes.update(f)
    out, vistos = Counter(), 0
    for base, dirs, arqs in os.walk(ENT):
        dirs[:] = [x for x in dirs if x != '.git']
        for f in sorted(arqs):
            if not f.endswith('.md'):
                continue
            c = os.path.join(base, f)
            for m in RX_MD.finditer(open(c, encoding='utf-8', errors='ignore').read()):
                alvo = m.group(1).strip()
                if IGNORAR.search(alvo) or ' ' in alvo:
                    continue
                vistos += 1
                if '/' in alvo and (alvo.endswith('/') or re.search(r'\.\w{2,4}$', alvo)):
                    achou = any(os.path.exists(x) for x in (os.path.join(base, alvo), os.path.join(ENT, alvo)))
                elif '/' in alvo:
                    continue
                else:
                    achou = alvo in nomes
                if not achou and BRANCOS_RX.match(alvo):
                    out[(os.path.relpath(c, ENT), alvo)] += 1
    return out, vistos
a, va = brancos(sys.argv[1]); b, vb = brancos(sys.argv[2])
print(f'antes: {sum(a.values())} brancas de {va} citacoes · depois: {sum(b.values())} brancas de {vb}')
for k in sorted(set(a) | set(b)):
    if a[k] != b[k]:
        print(f'  {a[k]} -> {b[k]}   {k[0]}   `{k[1]}`')
