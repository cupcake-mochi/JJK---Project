"""Provas de registro, preservação, exemplos e regressões da integração R50.

Os roteiros numéricos são os do estudo v0.14, com resultados esperados já fixados
antes desta integração. Não representam uma missão ou teste humano.
"""
from pathlib import Path
import hashlib, json, re, runpy, sys

B=Path(__file__).resolve().parents[1]
R=B/'revisao-r50'
STUDY=B.parents[1]/'desenvolvimento-morrendo'
def read(p): return json.loads(p.read_text())
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
old=read(R/'BLOCOS-R49.json'); expected=read(R/'BLOCOS-ESPERADOS.json')
rows=read(B/'ALTERACOES-R49-para-R50.json')
checks=[]
def check(label,condition):
    assert condition,label
    checks.append(label)
check('Identificadores únicos no registro',len({r['id'] for r in rows})==len(rows))
check('Um registro por bloco alterado',len({r['bloco'] for r in rows})==len(rows))
rebuilt=dict(old)
for r in rows:
    check('Antes exato: '+r['bloco'],r['antes']==old[r['bloco']])
    check('Formato e alteração real: '+r['bloco'],set(r)=={'id','bloco','antes','depois','motivo','item'} and r['antes']!=r['depois'])
    rebuilt[r['bloco']]=r['depois']
check('Registro reconstrói integralmente os 511 blocos',rebuilt==expected)
diff=[k for k in old if old[k]!=expected[k]]
check('Nenhuma diferença textual sem registro',set(diff)=={r['bloco'] for r in rows})
sys.path.insert(0,str(B))
ns=runpy.run_path(str(B/'ler_fontes.py'),run_name='auditoria_r50')
actual=ns['enriched']
check('Fonte carregada pelo gerador corresponde à revisão esperada',actual==expected)

# Verificações de regressão textual: núcleo antigo e propostas rejeitadas.
core='\n'.join(actual[k] for k in actual if k.startswith('dano--'))
check('Sem limiar antigo de 20% no capítulo de Dano',not re.search(r'20\s*%',core))
check('Sem custos antigos fracionários de vida máxima',not re.search(r'1/8|1/6|1/5',core))
check('Sem base de cálculo limitada a 210/30C',not re.search(r'210|30 ×.*Classe',actual['dano--insistir']))
check('Recomposição recupera 3C', '3 × sua maior Classe' in actual['catalogo--cat-passivas-2-recursos'])
check('Sem frases vetadas pelo autor', all(t not in '\n'.join(actual.values()).lower() for t in ['suas fichas','não tem como recusar']))

sys.path.insert(0,str(STUDY/'ensaios'))
from validar_teto_v14 import deterministic_checks
from motor_socorro_v14 import requisito
scenarios=deterministic_checks()
examples=[(23,1,[6,8,12]),(93,3,[24,31,45]),(395,7,[99,105,105])]
for hp,c,values in examples:
    check(f'Exemplos de tratamento {hp}PV/C{c}',
          [requisito(hp,'Aguentar',0,c),requisito(hp,'Insistir',0,c),requisito(hp,'Insistir',1,c)]==values)
check('Mei: 3+3 conclui Aguentar, mas ainda faltam 2 no primeiro Insistir',3+3==requisito(23,'Aguentar',0,1) and requisito(23,'Insistir',0,1)-6==2)
check('Exemplo de dano: 31−18=13 de tratamento; 2−1=1 rodada',31-18==13 and 2-1==1)

# Preservação é medida sobre todos os arquivos originais, não só o PDF.
base=read(STUDY/'referencia/BASE.json')
base_root=Path(base['origem'])
changed_base=[]
for rel,sha in base['arquivos_base_sha256'].items():
    p=base_root/rel
    if not p.exists() or digest(p)!=sha:changed_base.append(rel)
check('Todos os arquivos inventariados da R49 permanecem intactos',not changed_base)
check('Texto integral da R49 preservado',digest(base_root/'LIVRO-COMPLETO.md')==base['sha256_texto'])
style_names=['ARTES-APLICADAS.json','CAPA-E-ABERTURAS.json']
preserved=[]
for rel in base['arquivos_base_sha256']:
    if rel in style_names or Path(rel).suffix.lower() in {'.ttf','.otf','.woff','.woff2'}:
        if (B/rel).exists():
            check('Arte/configuração/fonte preservada: '+rel,digest(B/rel)==base['arquivos_base_sha256'][rel])
            preserved.append(rel)
report=dict(edicao='R50',blocos_total=len(expected),blocos_alterados=len(diff),
    blocos_inalterados=len(expected)-len(diff),checagens=len(checks),aprovadas=checks,
    cenarios_deterministicos_v014=len(scenarios),cenarios_aprovados=scenarios,
    arquivos_R49_conferidos=len(base['arquivos_base_sha256']),arquivos_R49_alterados=changed_base,
    arte_configuracoes_fontes_preservadas=preserved,
    sha256_registro=digest(B/'ALTERACOES-R49-para-R50.json'),
    sha256_texto=digest(B/'LIVRO-COMPLETO.md'),
    escopo='Conferência de integração, exemplos e regressões do estudo; não simula uma missão e não substitui teste humano.')
(R/'VALIDACAO-INTEGRACAO.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if isinstance(v,(int,str))},ensure_ascii=False,indent=2))
