"""Amostra isolada do capítulo 5; fontes anteriores permanecem preservadas."""
from pathlib import Path
from bs4 import BeautifulSoup
from weasyprint import HTML
import markdown,json,hashlib,os,re
A=Path(__file__).resolve().parent
R=A.parents[1]
F=R/'06 - Redacao do Guia/revisao-98/05-criar-uma-campanha.md'
B=R/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'
ESTILO=R/'04 - Planejamento/apoio-conducao-102/capitulo-4.html'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def agrupar(soup):
    for p in soup.find_all('p'):
        primeiro=next((c for c in p.contents if str(c).strip()),None)
        if getattr(primeiro,'name',None)=='strong':p['class']=['bloco-curto']
    for table in list(soup.find_all('table')):
        prev=table.find_previous_sibling();itens=[table]
        if prev and prev.name=='p':
            cabecalho=prev.find_previous_sibling()
            if cabecalho and cabecalho.name in ['h2','h3']:itens=[cabecalho,prev,table]
        elif prev and prev.name in ['h2','h3']:itens.insert(0,prev)
        grupo=soup.new_tag('div',attrs={'class':'grupo-tabela'});itens[0].insert_before(grupo)
        for item in itens:grupo.append(item.extract())
def regras(css):
    lines=B.read_text().splitlines();blocos=[]
    for nome in ['Campanhas e guildas','Primeira sessão','Legados de história']:
        matches=[(i,len(m.group(1))) for i,l in enumerate(lines) if (m:=re.match(r'^(#{2,5}) '+re.escape(nome)+r'\s*$',l))]
        assert len(matches)==1,(nome,matches)
        start,level=matches[0];end=len(lines)
        for i in range(start+1,len(lines)):
            m=re.match(r'^(#{1,5}) ',lines[i])
            if m and len(m.group(1))<=level:end=i;break
        blocos.append({'titulo':nome,'id':f'regra-{len(blocos)+1}','inicio_linha':start+1,'fim_linha':end,'texto':'\n'.join(lines[start:end])})
    body=''.join(f'<section id="{b["id"]}" class="consulta-regra">{markdown.markdown(b["texto"],extensions=["tables","sane_lists"])}</section>' for b in blocos)
    soup=BeautifulSoup(body,'html.parser');ids={t['id'] for t in soup.find_all(id=True)}
    for a in soup.find_all('a',href=True):
        if a['href'].startswith('#') and a['href'][1:] not in ids:a['href']='../apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'+a['href']
    menu=''.join(f'<li><a href="#{b["id"]}">{b["titulo"]}</a></li>' for b in blocos)
    doc=f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Livro de Regras 1.0 | Campanha</title><style>{css}main{{max-width:900px;background:white;padding:30px}}h4{{font-family:Bree,serif;font-size:22px}}h5{{font-size:19px}}body{{background:white}}</style></head><body><main><p><a href="capitulo-5.html">Voltar ao capítulo</a></p><h1>Livro de Regras 1.0</h1><p>Trechos da referência do sistema, sem reescrita. As situações de festa, facções e relações são exemplos do Guia.</p><ul>{menu}</ul>{soup}</main></body></html>'
    (A/'consulta-de-regras.html').write_text(doc)
    return [{k:v for k,v in b.items() if k!='texto'} for b in blocos]
def main():
    css=BeautifulSoup(ESTILO.read_text(),'html.parser').style.string.replace("content:'NA MESA DE JOGO'","content:'CRIAR UMA CAMPANHA'")
    consultas=regras(css)
    soup=BeautifulSoup(markdown.markdown(F.read_text(),extensions=['tables','sane_lists','toc']),'html.parser');titulo=soup.h1.get_text();soup.h1.extract()
    agrupar(soup)
    for a in soup.find_all('a',href=True):
        u=a['href']
        if re.match(r'^(https?:|#)',u):continue
        p,sep,frag=u.partition('#');dest=(F.parent/p).resolve();assert dest.is_file(),dest
        a['href']=os.path.relpath(dest,A)+(sep+frag if sep else '')
    menu=''.join(f'<a href="#{h["id"]}">{h.get_text()}</a>' for h in soup.find_all('h2',id=True))
    doc=f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{titulo} | Ciclo Maldito</title><style>{css}</style></head><body><nav aria-label="Conteúdo">{menu}</nav><p class="aviso-edicao">Amostra do capítulo 5 da nova estrutura. <a href="../apoio-conducao-102/capitulo-4.html">Na mesa de jogo</a>. <a href="consulta-de-regras.html">Consultar as regras</a>. A edição integrada anterior continua preservada.</p><main><article class="folha" id="capitulo-5"><header><p class="numero">CAPÍTULO 5</p><h1>{titulo}</h1></header><div class="colunas">{soup}</div></article></main><p class="rodape-tela"><a href="../103-campanha-e-conferencia-do-nucleo.md">Registro de revisão</a></p></body></html>'
    (A/'capitulo-5.html').write_text(doc)
    out=A/'output/pdf/Ciclo-Maldito-Criar-uma-Campanha-Amostra.pdf';out.parent.mkdir(parents=True,exist_ok=True)
    HTML(string=doc,base_url=str(A)).write_pdf(str(out),pdf_identifier=b'campanha-103')
    d={'registro':103,'fonte':str(F.relative_to(R)),'fonte_sha256':sha(F),'palavras_markdown':len(F.read_text().split()),'livro_de_regras':str(B.relative_to(R)),'livro_de_regras_sha256':sha(B),'consultas':consultas,'estilo_base':str(ESTILO.relative_to(R)),'estilo_base_sha256':sha(ESTILO),'pdf':str(out.relative_to(R)),'pdf_sha256':sha(out),'limite':'Amostra isolada. Integração e consultas gerais continuam nas etapas seguintes.'}
    (A/'amostra.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in d.items() if k!='consultas'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
