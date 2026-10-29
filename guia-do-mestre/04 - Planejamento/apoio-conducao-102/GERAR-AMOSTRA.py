"""Capítulo 4 da nova estrutura; não modifica o livro integrado."""
from pathlib import Path
from bs4 import BeautifulSoup
from weasyprint import HTML
import markdown,json,hashlib,os,re
A=Path(__file__).resolve().parent
R=A.parents[1]
F=R/'06 - Redacao do Guia/revisao-98/04-na-mesa-de-jogo.md'
B=R/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def estilo():
    ref=R/'04 - Planejamento/apoio-primeira-missao-100/capitulo-1.html'
    css=BeautifulSoup(ref.read_text(),'html.parser').style.string
    css=css.replace("content:'SUA PRIMEIRA MISSÃO'","content:'NA MESA DE JOGO'")
    css+='''
    .numero{font:700 18px Barlow,sans-serif;letter-spacing:.08em;color:#6f5867;margin:0 0 8px}
    .folha>header>h1{margin-top:0}.folha>header{break-after:avoid}.consulta-regra{border-top:1px solid #ded4d9;margin-top:25px;padding-top:15px}
    @media print{.numero{font-size:10pt;margin-bottom:7pt}.folha>header>h1{margin-bottom:12pt}.colunas h2{font-size:17pt;margin:11pt 0 7pt}.colunas h3{font-size:12.5pt}.colunas ol{padding-left:14pt;margin:5pt 0 9pt}.colunas h2:first-child{margin-top:0}table{font-size:9pt;line-height:11.5pt}p:has(>strong:first-child){break-inside:auto}.colunas p.bloco-curto{break-inside:avoid!important}}
    '''
    return css

def regra_blocos():
    lines=B.read_text().splitlines()
    nomes=['Testes','Testes de grupo','Iniciativa','Recursos do turno','Ajudar','Influenciar','Reações e ataques de oportunidade','Vasculhar','Vasculhar com Sentir Energia','Estudar','Vida a zero','Descansos','Mestrar uma sessão']
    blocos=[]
    for nome in nomes:
        matches=[(i,len(m.group(1))) for i,l in enumerate(lines) if (m:=re.match(r'^(#{2,5}) '+re.escape(nome)+r'\s*$',l))]
        assert matches,nome
        # Selecionar a regra de Turnos antes de invocações e glossários. Descansos já inclui Cena e usos de habilidades.
        assert len(matches)==1 or nome in ['Iniciativa','Recursos do turno'],(nome,matches)
        start,level=matches[0];end=len(lines)
        for i in range(start+1,len(lines)):
            m=re.match(r'^(#{1,5}) ',lines[i])
            if m and len(m.group(1))<=level:end=i;break
        slug=f'regra-{len(blocos)+1}'
        raw='\n'.join(lines[start:end])
        ancora = None
        for prev in reversed(lines[max(0,start-6):start]):
            if prev.startswith('#'):break
            m=re.search(r'<a id="([^"]+)"',prev)
            if m:ancora=m.group(1);break
        blocos.append({'titulo':nome,'id':slug,'ancora_original':ancora,'inicio_linha':start+1,'fim_linha':end,'texto':raw})
    return blocos

def regras(css):
    blocos=regra_blocos()
    corpo=''.join(f'<section class="consulta-regra" id="{b["id"]}">{markdown.markdown(b["texto"],extensions=["tables","sane_lists"])}</section>' for b in blocos)
    soup=BeautifulSoup(corpo,'html.parser');ids={x['id'] for x in soup.find_all(id=True)}
    destinos={b['ancora_original']:b['id'] for b in blocos if b['ancora_original']}
    for link in soup.find_all('a',href=True):
        if link['href'].startswith('#'):
            alvo=link['href'][1:]
            if alvo in destinos:link['href']='#'+destinos[alvo]
            elif alvo not in ids:link['href']='../apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'+link['href']
    menu=''.join(f'<li><a href="#{b["id"]}">{b["titulo"]}</a></li>' for b in blocos)
    doc=f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Livro de Regras 1.0 | Consulta de condução</title><style>{css}main{{max-width:900px;background:white;padding:30px}}h4{{font-family:Bree,serif;font-size:22px}}h5{{font-size:19px}}table{{font-size:16px}}body{{background:white}}</style></head><body><main><p><a href="capitulo-4.html">Voltar ao capítulo</a></p><h1>Livro de Regras 1.0</h1><p>Trechos da referência do sistema, sem reescrita. Os casos do Guia e as orientações de condução são consultados no capítulo.</p><ul>{menu}</ul>{soup}</main></body></html>'
    (A/'consulta-de-regras.html').write_text(doc)
    return [{k:v for k,v in b.items() if k!='texto'} for b in blocos]

def main():
    css=estilo();consultas=regras(css)
    soup=BeautifulSoup(markdown.markdown(F.read_text(),extensions=['tables','sane_lists','toc']),'html.parser')
    titulo=soup.h1.get_text();soup.h1.extract()
    for p in soup.find_all('p'):
        if p.get_text().startswith('Na condução.'):p['class']='comentario'
        if p.get_text().startswith(('Helena:','Jogadora:')):p['class']='fala'
        primeiro=next((c for c in p.contents if str(c).strip()),None)
        if getattr(primeiro,'name',None)=='strong':
            classes=p.get('class',[])
            if isinstance(classes,str):classes=[classes]
            p['class']=[*classes,'bloco-curto']
    # Cabeçalho e tabela devem continuar juntos. Demais seções fluem entre páginas.
    for table in list(soup.find_all('table')):
        prev=table.find_previous_sibling()
        itens=[table]
        if prev and prev.name=='p':
            itens.insert(0,prev);prev=prev.find_previous_sibling()
        if prev and prev.name in ['h2','h3']:itens.insert(0,prev)
        grupo=soup.new_tag('div',attrs={'class':'grupo-tabela'})
        itens[0].insert_before(grupo)
        for item in itens:grupo.append(item.extract())
    for link in soup.find_all('a',href=True):
        u=link['href']
        if re.match(r'^(https?:|#)',u):continue
        p,sep,frag=u.partition('#');dest=(F.parent/p).resolve();assert dest.exists(),dest
        link['href']=os.path.relpath(dest,A)+(sep+frag if sep else '')
    menu=''.join(f'<a href="#{h["id"]}">{h.get_text()}</a>' for h in soup.find_all('h2',id=True))
    doc=f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{titulo} | Ciclo Maldito</title><style>{css}</style></head><body><nav aria-label="Conteúdo">{menu}</nav><p class="aviso-edicao">Amostra do capítulo 4 da nova estrutura. <a href="../apoio-mundo-e-preparo-101/capitulos-2-e-3.html">Mundo e preparação de aventuras</a>. A edição integrada anterior continua preservada.</p><main><article class="folha" id="capitulo-4"><header><p class="numero">CAPÍTULO 4</p><h1>{titulo}</h1></header><div class="colunas">{soup}</div></article></main><p class="rodape-tela"><a href="../102-conducao-participacao-e-ritmo.md">Registro de revisão</a></p></body></html>'
    (A/'capitulo-4.html').write_text(doc)
    out=A/'output/pdf/Ciclo-Maldito-Na-Mesa-de-Jogo-Amostra.pdf';out.parent.mkdir(parents=True,exist_ok=True)
    HTML(string=doc,base_url=str(A)).write_pdf(str(out),pdf_identifier=b'conducao-102')
    dados={'registro':102,'fonte':str(F.relative_to(R)),'fonte_sha256':sha(F),'palavras_markdown':len(F.read_text().split()),'livro_de_regras':str(B.relative_to(R)),'livro_de_regras_sha256':sha(B),'consultas':consultas,'pdf':str(out.relative_to(R)),'pdf_sha256':sha(out),'limite':'Amostra isolada. Etapa 3 em andamento; PDF integrado anterior preservado.'}
    (A/'amostra.json').write_text(json.dumps(dados,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in dados.items() if k!='consultas'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
