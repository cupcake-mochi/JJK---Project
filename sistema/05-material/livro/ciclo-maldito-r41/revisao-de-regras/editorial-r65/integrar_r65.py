from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import hashlib,json,shutil,sys

H=Path(__file__).resolve().parent
R=Path(sys.argv[1]).resolve()
L=R/'sistema/05-material/livro'
B=L/'ciclo-maldito-r41'
E=B/'revisao-de-regras/editorial-r65'
V=H/'revisao'
D=H/'composicao/output/pdf'

def load(p):return json.loads(p.read_text())
def write(p,text):
    t=p.with_suffix(p.suffix+'.novo')
    t.write_text(text)
    t.replace(p)
def dump(p,x):write(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def copy(a,b):
    b.parent.mkdir(parents=True,exist_ok=True)
    t=b.with_suffix(b.suffix+'.novo')
    shutil.copy2(a,t)
    t.replace(b)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def edit(p,a,b):
    old=p.read_text()
    assert old.count(a)==1,(p,a)
    write(p,old.replace(a,b,1))

validation=load(V/'VALIDACAO.json')
comparison=load(V/'COMPARACAO-R64.json')
visual=load(V/'REVISAO-VISUAL.json')
ops=load(H/'TROCAS-R65.json')
assert validation['resultado']==visual['resultado']=='aprovado'
assert validation['paginas']==425
assert (B/'LIVRO-COMPLETO.md').read_bytes()==(H/'LIVRO-CANDIDATA.md').read_bytes()
assert load(E/'FONTE-PUBLICADA.json')['sha256_texto']==sha(B/'LIVRO-COMPLETO.md')
meta=load(L/'EDICAO-ATUAL.json')
assert meta['revisao']=='R64'
meta.update(revisao='R65',paginas=425,revisado_em=datetime.now(ZoneInfo('America/Sao_Paulo')).isoformat())
names=[]
for pal in ('claro','noturno'):
    assert comparison['paletas'][pal]['paginas']==425
    assert comparison['paletas'][pal]['paginas_com_imagem_alterada']==visual['paginas_vistas'][pal]
    name=meta[pal]['arquivo'];names.append(name)
    assert sha(D/name)==visual['sha256'][pal]
    copy(D/name,L/name)
    meta[pal]['sha256']=sha(L/name)
dump(L/'EDICAO-ATUAL.json',meta)
dump(L/'REVISAO-R65.json',{
    'revisao':'R65','base':'R64','resultado':'aprovado','paginas':425,
    'blocos_alterados':sorted({x['bloco'] for x in ops}),'trocas':len(ops),
    'descricao':'Linguagem simples em Caminhos e Trilhas. Rótulos de Requisito e conteúdo de regra preservados.',
    'conferencia_pdf':validation,'revisao_visual':{**comparison,'revisao_visual':visual},
    'sha256':{**{k:meta[k]['sha256'] for k in ('claro','noturno')},'texto':sha(B/'LIVRO-COMPLETO.md')},
})
for f in ['COMPARACAO-R64.json','COLUNAS-R64-R65.json','REVISAO-VISUAL.json','AUDITORIA-PAGINAS-INDICE.json','ANCORAS-R64-R65.json']:
    copy(V/f,E/f)
copy(V/'VALIDACAO.json',E/'VALIDACAO-PDFS.json')
for f in ['conferir.py','comparar_r64.py','medir_colunas.py','DESTINOS-INDICE-REVISAO.json','TROCAS-R65.json','integrar_texto_r65.py','integrar_r65.py','PLANO-LINGUAGEM.md','COMPOSICAO.md']:
    copy(H/f,E/f)
for p in sorted((H/'propostas').iterdir()):
    if p.is_file():copy(p,E/p.name)
for f in ['gerar_livro.py','gerar_noturno_r57.py','ler_fontes.py','fluxo_continuo.py']:
    copy(H/'composicao'/f,E/'composicao'/f)
for f in names+['EDICAO-ATUAL.json','REVISAO-R65.json']:
    copy(L/f,R/'finalizado/livro'/f)

count=len(visual['paginas_vistas']['claro'])
ncheck=len(validation['verificacoes'])
movidas=len(load(V/'ANCORAS-R64-R65.json')['deslocadas'])
summary=f'Os dois PDFs têm 425 páginas. Foram revisadas {count} páginas em cada paleta. A composição passou em {ncheck} verificações e a auditoria do Índice conferiu 453 verbetes. A comparação registrou {movidas} âncoras que mudaram de página.'
p=R/'README.md'
edit(p,'**Versão v0.374**','**Versão v0.375**')
edit(p,'[Ciclo Maldito R64,','[Ciclo Maldito R65,')
text=p.read_text()
i=text.index('\n---\n')
paragraph='\nA R65 simplifica a redação de Caminhos e Trilhas. São 181 trocas em 96 blocos, com os rótulos de Requisito preservados. O antes e depois fica em `sistema/05-material/livro/ciclo-maldito-r41/revisao-de-regras/editorial-r65/`.\n'
write(p,text[:i]+paragraph+text[i:])
p=R/'sistema/LEIA-ME.md'
edit(p,'**v0.374.**','**v0.375.**')
edit(p,'O livro atual é a R64','O livro atual é a R65')
p=B/'LEIA-ME.md'
old=p.read_text()
i=old.index('\n',old.index('Os PDFs ficam'))
write(p,'''# Fonte corrente R65

LIVRO-COMPLETO.md é a edição R65 de 425 páginas usada pelos validadores. Ela simplifica “conceder”, “conservar” e “requisito” em Caminhos e Trilhas.

O snapshot e a impressão digital atual ficam em revisao-de-regras/editorial-r65/. O antes e depois está em revisao-de-regras/alteracoes/R64-para-R65.json. Os PDFs ficam na pasta acima, com seus hashes em EDICAO-ATUAL.json.'''+old[i:])
p=R/'sistema/ESTADO-ATUAL.md'
old=p.read_text()
assert old.startswith('# Edição corrente R64\n\n**Versão v0.374.**')
old=old.replace('# Edição corrente R64\n\n**Versão v0.374.**','# Edição anterior R64\n\n*Versão v0.374.*',1)
assert old.count('Registro em `editorial-r64/PUBLICACAO.json`.')==1
old=old.replace('Registro em `editorial-r64/PUBLICACAO.json`.','Registro em `05-material/livro/ciclo-maldito-r41/revisao-de-regras/editorial-r64/PUBLICACAO.json`.',1)
write(p,f'''# Edição corrente R65

**Versão v0.375.**

A R65 revisa Caminhos e Trilhas, com 181 trocas em 96 blocos. Os dez rótulos de Requisito e o título Requisitos da aplicação foram preservados. O exemplo de Cobrir o Parceiro passou a usar o título Reações na cobertura.

{summary}

Fonte, trocas e validações em `05-material/livro/ciclo-maldito-r41/revisao-de-regras/editorial-r65/`. A cadeia de integridade cobre R52 a R65. A candidata está pronta para publicação.

'''+old)
p=R/'logs/CHANGELOG.md'
edit(p,'## [0.374] - 04/11/2026',f'''## [0.375] - 04/11/2026

### Alterado

- R65 do Livro de Regras. Revisão de “conceder”, “conservar” e “requisito” no capítulo 6. As 181 trocas preservam regras, números, rótulos, âncoras e destinos.
- {summary}
- A guarda da fonte reaplica o registro R64-para-R65. A checagem de Fundamento acompanha a nova redação de Queima-Roupa em Manifestação Técnica.

→ Continua em `sistema/ESTADO-ATUAL.md`, com a candidata R65 pronta para publicação.

## [0.374] - 04/11/2026''')
p=R/'finalizado/README.md'
old=p.read_text().splitlines()[4]
assert '**Livro atual: Ciclo Maldito R64**' in old
edit(p,old,old.replace('R64','R65').replace('0.374','0.375').replace('que simplifica “registre” e “conforme”.','que simplifica a redação de Caminhos e Trilhas.'))
print('R65 instalada na cópia',R,meta['claro']['sha256'],meta['noturno']['sha256'])
