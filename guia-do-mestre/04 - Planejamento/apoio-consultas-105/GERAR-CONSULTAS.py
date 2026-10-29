"""Folhas curtas derivadas do manuscrito; mantém a edição integrada anterior."""
from pathlib import Path
from bs4 import BeautifulSoup
from weasyprint import HTML
from urllib.parse import urlsplit,unquote
import hashlib,json,markdown,os,re,sys
A=Path(__file__).resolve().parent
R=A.parents[1]
S=R/'06 - Redacao do Guia/revisao-98/consultas'
FILES=[('A1-preparar-a-missao.md','preparar','formulario'),('A2-conduzir-a-sessao.md','conduzir','consulta'),('A4-retomar-a-missao.md','retomar','formulario'),('A1-exemplo-despedida.md','exemplo-preparo','exemplo'),('A4-exemplo-sala-de-conservacao.md','exemplo-retomada','exemplo')]
OLD={str((R/x['fonte']).resolve()):x for x in json.loads((R/'07 - Edicao de Leitura/mapa-editorial.json').read_text())['fontes']}
LOCAL={str((S/name).resolve()):ident for name,ident,_ in FILES}
STAGED={str((R/'06 - Redacao do Guia/revisao-98/03-preparar-aventuras.md').resolve()):(R/'04 - Planejamento/apoio-mundo-e-preparo-101/capitulos-2-e-3.html','capitulo-3'),str((R/'06 - Redacao do Guia/revisao-98/04-na-mesa-de-jogo.md').resolve()):(R/'04 - Planejamento/apoio-conducao-102/capitulo-4.html','capitulo-4')}
for name,folder,number in [('06-inimigos-e-perigos.md','apoio-inimigos-106',6),('07-personagens-e-tecnicas.md','apoio-personagens-107',7),('08-entre-missoes.md','apoio-entre-missoes-108',8),('09-pactos-e-entidades.md','apoio-pactos-entidades-109',9),('10-jogar-em-guilda.md','apoio-guilda-110',10)]:
    STAGED[str((S.parent/name).resolve())]=(R/'04 - Planejamento'/folder/f'capitulo-{number}.html',f'capitulo-{number}')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def convert(p,prefix):
    soup=BeautifulSoup(markdown.markdown(p.read_text(),extensions=['tables','sane_lists','toc']),'html.parser')
    # Uma única página HTML pode conter títulos idênticos de folhas diferentes.
    for node in soup.find_all(id=True):node['id']=prefix+'--'+node['id']
    for c in list(soup.find_all(string=lambda x:isinstance(x,__import__('bs4').Comment))):
        if m:=re.search(r'espaco:\s*(\d+)',str(c)):
            block=soup.new_tag('div',attrs={'class':'linhas','aria-hidden':'true'})
            for _ in range(int(m[1])):block.append(soup.new_tag('span',attrs={'class':'linha'}))
            c.replace_with(block)
    for link in soup.find_all('a',href=True):
        u=urlsplit(link['href'])
        if u.scheme:continue
        if not u.path:
            if u.fragment:link['href']='#'+prefix+'--'+unquote(u.fragment)
            continue
        dest=(p.parent/unquote(u.path)).resolve();assert dest.is_file(),(p,link['href'])
        if str(dest) in LOCAL:
            ident=LOCAL[str(dest)];link['href']='#'+ident+('--'+u.fragment if u.fragment else '')
        elif str(dest) in STAGED:
            target,fallback=STAGED[str(dest)]
            frag='folha-despedida' if u.fragment=='antes-que-o-trem-parta' else (u.fragment or fallback)
            link['href']=os.path.relpath(target,A)+'#'+frag
        elif str(dest) in OLD:
            old=OLD[str(dest)];frag=old['ancoras'].get(u.fragment,u.fragment) if u.fragment else old['id']
            link['href']=os.path.relpath(R/'07 - Edicao de Leitura'/old['pagina'],A)+'#'+frag
        else:link['href']=os.path.relpath(dest,A)+('#'+u.fragment if u.fragment else '')
    return soup
def main():
    style=R/'04 - Planejamento/apoio-conducao-102/capitulo-4.html'
    css=BeautifulSoup(style.read_text(),'html.parser').style.string.replace("content:'NA MESA DE JOGO'","content:'FOLHAS PARA A MESA'")
    css+='''
    .linhas{margin:3pt 0 6pt}.linha{display:block;height:5mm;border-bottom:.4pt solid #ded4d9}
    .indice{background:white;padding:36px 48px;max-width:1000px;margin:24px auto}.indice h1{font-size:34px}
    @media print{.folha>h1{font-size:26pt}.folha p{margin:0 0 6pt}.folha h2{font-size:15pt;margin:9pt 0 4pt}.folha h3{font-size:12pt}.formulario{column-count:1}.formulario h2{font-size:15pt;margin:8pt 0 3pt}.formulario .colunas{column-count:1}.formulario p{margin-bottom:4pt}.formulario .linhas{break-inside:avoid}.consulta .colunas,.exemplo .colunas{column-count:2;column-gap:7mm;column-fill:balance}.colunas p:has(>strong:first-child){break-inside:auto}ol,ul{padding-left:14pt;margin:5pt 0 8pt}li{margin-bottom:4pt}table{font-size:9.5pt;line-height:12pt;margin:6pt 0 9pt}th,td{padding:4pt 5pt}blockquote{margin:6pt 0 8pt;padding:6pt 8pt}.indice{display:none}}
    '''
    parts=[];meta=[]
    for name,ident,kind in FILES:
        p=S/name;soup=convert(p,ident);title=soup.h1.get_text();soup.h1.extract()
        parts.append(f'<article class="folha {kind}" id="{ident}"><h1>{title}</h1><div class="colunas">{soup}</div></article>')
        meta.append({'fonte':str(p.relative_to(R)),'sha256':sha(p),'id':ident,'tipo':kind,'titulo':title})
    guia=convert(S/'LEIA-ME.md','escolher')
    # Atualiza só o guia de escolha; corpo e links da edição impressa permanecem históricos.
    for link in guia.find_all('a',href=True):
        path,sep,frag=link['href'].partition('#')
        if path=='../apoio-conducao-102/capitulo-4.html':
            anchor='c04' if frag=='capitulo-4' else 'c04--'+frag
            link['href']='../apoio-revisao-textual-113/prova-textual.html#'+anchor
        elif path in ['../apoio-inimigos-106/capitulo-6.html','../apoio-personagens-107/capitulo-7.html']:
            number=6 if 'inimigos-106' in path else 7
            anchor=f'c0{number}' if frag==f'capitulo-{number}' else f'c0{number}--'+frag
            link['href']='../apoio-revisao-textual-114/prova-textual.html#'+anchor
        elif path in ['../apoio-entre-missoes-108/capitulo-8.html','../apoio-pactos-entidades-109/capitulo-9.html','../apoio-guilda-110/capitulo-10.html']:
            number=8 if 'entre-missoes-108' in path else 9 if 'entidades-109' in path else 10
            anchor=f'c{number:02}' if frag==f'capitulo-{number}' else f'c{number:02}--'+frag
            link['href']='../apoio-revisao-textual-115/prova-textual.html#'+anchor
        elif path=='../apoio-mundo-e-preparo-101/capitulos-2-e-3.html':
            anchor='c03' if frag=='capitulo-3' else 'c03--antes-que-o-trem-parta' if frag=='folha-despedida' else 'c03--'+frag
            link['href']='../apoio-revisao-textual-112/prova-textual.html#'+anchor

    nav=''.join(f'<a href="#{x["id"]}">{x["titulo"]}</a>' for x in meta)+'<a href="#escolher">Escolher uma consulta</a><a href="casos-completos.html">Casos por assunto</a>'
    doc=f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Folhas para a mesa | Ciclo Maldito</title><style>{css}</style></head><body><nav>{nav}</nav><p class="aviso-edicao">Três folhas curtas e dois exemplos. Os campos com linhas são para impressão ou preenchimento no texto editável; este PDF não tem campos interativos.</p><main>{"".join(parts)}</main><section id="escolher" class="indice">{guia}</section><p class="rodape-tela"><a href="../105-folhas-para-a-mesa-e-acesso-aos-casos.md">Registro desta entrega</a></p></body></html>'
    if '--somente-html' in sys.argv:
        previous=BeautifulSoup((A/'folhas-para-a-mesa.html').read_text(),'html.parser')
        current=BeautifulSoup(doc,'html.parser')
        assert str(previous.main)==str(current.main),'As folhas impressas mudariam; requer regeneração e revisão do PDF.'
        assert previous.style.get_text()==current.style.get_text(),'O estilo de impressão mudaria.'
        data=json.loads((A/'amostra.json').read_text());assert data['fontes']==meta
        assert sha(R/data['pdf'])==data['pdf_sha256']
        (A/'folhas-para-a-mesa.html').write_text(doc)
        data['guia_de_escolha']['sha256']=sha(S/'LEIA-ME.md')
        data['revisao_da_navegacao']=115
        data['html_sha256']=sha(A/'folhas-para-a-mesa.html')
        data['limite']='Folhas e PDF da entrega 105 preservados; guia de escolha aponta as revisões 112 a 115. Integração do livro ainda pendente.'
        (A/'amostra.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps({'somente_html':True,'pdf_preservado':data['pdf_sha256']},ensure_ascii=False))
        return
    (A/'folhas-para-a-mesa.html').write_text(doc)
    output=A/'output/pdf/Ciclo-Maldito-Folhas-para-a-Mesa.pdf';output.parent.mkdir(parents=True,exist_ok=True)
    render=HTML(string=doc,base_url=str(A)).render();render.write_pdf(str(output),pdf_identifier=b'consultas-105')
    data={'registro':105,'fontes':meta,'guia_de_escolha':{'fonte':str((S/'LEIA-ME.md').relative_to(R)),'sha256':sha(S/'LEIA-ME.md')},'estilo':str(style.relative_to(R)),'estilo_sha256':sha(style),'html':str((A/'folhas-para-a-mesa.html').relative_to(R)),'pdf':str(output.relative_to(R)),'pdf_sha256':sha(output),'paginas':len(render.pages),'limite':'Primeiro lote da etapa 5. Reorganização dos capítulos técnicos e consolidação final de remissões ainda pendentes.'}
    (A/'amostra.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'paginas':data['paginas'],'pdf_sha256':data['pdf_sha256']},ensure_ascii=False))
if __name__=='__main__':main()
