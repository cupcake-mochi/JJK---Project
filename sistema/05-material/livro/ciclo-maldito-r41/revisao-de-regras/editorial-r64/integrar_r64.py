from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import hashlib,json,shutil
H=Path(__file__).resolve().parent
S=Path('/home/mizuki/JJK-v0.341-para-subir')
L=S/'sistema/05-material/livro'
B=L/'ciclo-maldito-r41'
E=B/'revisao-de-regras/editorial-r64'
V=H/'revisao'
D=H/'composicao/output/pdf'

def load(p):return json.loads(p.read_text())
def dump(p,x):
    temp=p.with_suffix(p.suffix+'.novo')
    temp.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
    temp.replace(p)
def copy(src,dst):
    dst.parent.mkdir(parents=True,exist_ok=True)
    temp=dst.with_suffix(dst.suffix+'.novo')
    shutil.copy2(src,temp)
    temp.replace(dst)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()

validation=load(V/'VALIDACAO.json')
comparison=load(V/'COMPARACAO-R63.json')
visual=load(V/'REVISAO-VISUAL.json')
ops=load(H/'TROCAS-R64.json')
assert validation['resultado']==visual['resultado']=='aprovado'
assert validation['paginas']==425
assert (B/'LIVRO-COMPLETO.md').read_bytes()==(H/'LIVRO-CANDIDATA.md').read_bytes()
assert load(E/'FONTE-PUBLICADA.json')['sha256_texto']==sha(B/'LIVRO-COMPLETO.md')
meta=load(L/'EDICAO-ATUAL.json')
meta.update(revisao='R64',paginas=425,revisado_em=datetime.now(ZoneInfo('America/Sao_Paulo')).isoformat())
pdfs=[]
for pal in ('claro','noturno'):
    assert comparison['paletas'][pal]['paginas']==425
    assert comparison['paletas'][pal]['paginas_com_imagem_alterada']==visual['paginas_vistas'][pal]
    name=meta[pal]['arquivo'];pdfs.append(name)
    assert sha(D/name)==visual['sha256'][pal]
    copy(D/name,L/name)
    meta[pal]['sha256']=sha(L/name)
dump(L/'EDICAO-ATUAL.json',meta)
dump(L/'REVISAO-R64.json',{
    'revisao':'R64','base':'R63','resultado':'aprovado','paginas':425,
    'blocos_alterados':sorted({o['bloco'] for o in ops if o['bloco']!='capitulo-6'}),
    'aberturas_alteradas':['capitulo-6'],'trocas':len(ops),
    'descricao':'Linguagem simples. 139 ocorrências de registre e registrem, 163 de conforme e dois títulos. Números, regras, rótulos de Requisito, âncoras e destinos preservados.',
    'conferencia_pdf':validation,'revisao_visual':{**comparison,'revisao_visual':visual},
    'sha256':{**{p:meta[p]['sha256'] for p in ('claro','noturno')},'texto':sha(B/'LIVRO-COMPLETO.md')},
})
for f in ['COMPARACAO-R63.json','COLUNAS-R63-R64.json','REVISAO-VISUAL.json','AUDITORIA-PAGINAS-INDICE.json','ANCORAS-R63-R64.json']:
    copy(V/f,E/f)
copy(V/'VALIDACAO.json',E/'VALIDACAO-PDFS.json')
for f in ['conferir.py','comparar_r63.py','medir_colunas.py','DESTINOS-INDICE-REVISAO.json','TROCAS-R64.json','trocas_r64.py','conferir_trocas.py','integrar_texto_r64.py','integrar_r64.py','PLANO-LINGUAGEM.md','COMPOSICAO.md']:
    copy(H/f,E/f)
for f in ['TROCAS-R64-01-REGISTRE.md','TROCAS-R64-02-CONFORME.md']:
    copy(H/'propostas'/f,E/f)
for f in ['gerar_livro.py','gerar_noturno_r57.py','ler_fontes.py','fluxo_continuo.py']:
    copy(H/'composicao'/f,E/'composicao'/f)
for f in pdfs+['EDICAO-ATUAL.json','REVISAO-R64.json']:
    copy(L/f,S/'finalizado/livro'/f)
print(meta['revisao'],meta['paginas'],meta['claro']['sha256'],meta['noturno']['sha256'])
