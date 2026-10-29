"""Capítulo 7 reorganizado; não altera a edição integrada ou as fichas antigas."""
from pathlib import Path
from bs4 import BeautifulSoup
from weasyprint import HTML
from urllib.parse import urlsplit,unquote
import hashlib,json,markdown,os,re
A=Path(__file__).resolve().parent
R=A.parents[1]
F=R/'06 - Redacao do Guia/revisao-98/07-personagens-e-tecnicas.md'
B=R/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'
ESTILO=R/'04 - Planejamento/apoio-conducao-102/capitulo-4.html'
OLD={str((R/x['fonte']).resolve()):x for x in json.loads((R/'07 - Edicao de Leitura/mapa-editorial.json').read_text())['fontes']}
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def regras(css):
    lines=B.read_text().splitlines();blocks=[]
    for name in ['Ficha pronta','Personalizar sua Origem','Conselho Interior','Disputa pelo corpo','Reparo do corpo','Reserva Condensada','Pontos e preços','Toque, Aura e proximidade','Efeito Próprio','Talento Próprio','Regra Própria','Aptidão Própria','Bênção Própria','Liberação Máxima','Técnica Máxima','Expansão de Domínio','Criar um domínio','Acerto do domínio','Atualizar a ficha']:
        hits=[(i,len(m[1])) for i,l in enumerate(lines) if (m:=re.match(r'^(#{2,5}) '+re.escape(name)+r'\s*$',l))];assert hits and (len(hits)==1 or name in ['Aptidão Própria','Liberação Máxima']),(name,hits)
        start,level=hits[0];end=len(lines)
        for i in range(start+1,len(lines)):
            m=re.match(r'^(#{1,5}) ',lines[i])
            if m and len(m[1])<=level:end=i;break
        blocks.append({'titulo':name,'id':f'regra-{len(blocks)+1}','inicio_linha':start+1,'fim_linha':end,'texto':'\n'.join(lines[start:end])})
    body=''.join(f'<section class="consulta-regra" id="{b["id"]}">{markdown.markdown(b["texto"],extensions=["tables","sane_lists"])}</section>' for b in blocks)
    soup=BeautifulSoup(body,'html.parser');ids={x['id'] for x in soup.find_all(id=True)}
    for a in soup.find_all('a',href=True):
        if a['href'].startswith('#') and a['href'][1:] not in ids:a['href']='../apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'+a['href']
    menu=''.join(f'<li><a href="#{b["id"]}">{b["titulo"]}</a></li>' for b in blocks)
    doc=f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Regras de personagens e técnicas | Ciclo Maldito</title><style>{css}main{{max-width:900px;background:white;padding:30px}}h4{{font:22px Bree,serif}}h5{{font-size:19px}}</style></head><body><main><p><a href="capitulo-7.html">Voltar ao capítulo</a></p><h1>Livro de Regras 1.0</h1><p>Trechos da base sem reescrita. Aquisições e permissões conservam seus limites publicados; os acordos por personagem e os exemplos do Guia permanecem identificados.</p><ul>{menu}</ul>{soup}</main></body></html>'
    (A/'consulta-de-regras.html').write_text(doc)
    return [{k:v for k,v in b.items() if k!='texto'} for b in blocks]
def main():
    css=BeautifulSoup(ESTILO.read_text(),'html.parser').style.string.replace("content:'NA MESA DE JOGO'","content:'PERSONAGENS E TÉCNICAS'")
    css+='@media print{.colunas p:has(>strong:first-child){break-inside:auto}.colunas table{font-size:9.2pt;line-height:11.5pt}.colunas th,.colunas td{padding:4pt 5pt}.golpes td:nth-child(n+2){white-space:nowrap}.golpes th:nth-child(1){width:40%}.golpes th:nth-child(2){width:14%}.golpes th:nth-child(3),.golpes th:nth-child(4){width:23%}}'
    consulta=regras(css)
    soup=BeautifulSoup(markdown.markdown(F.read_text(),extensions=['tables','sane_lists','toc']),'html.parser');title=soup.h1.get_text();soup.h1.extract()
    for table in soup.find_all('table'):
        if [h.get_text() for h in table.find_all('th')]==['Golpe','Ataque','Dano','Crítico']:table['class']='golpes'
    for a in soup.find_all('a',href=True):
        u=urlsplit(a['href'])
        if u.scheme or not u.path:continue
        dest=(F.parent/unquote(u.path)).resolve();assert dest.is_file(),(a['href'],dest)
        if str(dest) in OLD:
            old=OLD[str(dest)];frag=old['ancoras'].get(u.fragment,u.fragment) if u.fragment else old['id'];target=R/'07 - Edicao de Leitura'/old['pagina']
        elif dest.name=='04-na-mesa-de-jogo.md' and dest.parent==F.parent:
            target=R/'04 - Planejamento/apoio-conducao-102/capitulo-4.html';frag=u.fragment or 'capitulo-4'
        elif dest.name=='A4-retomar-a-missao.md' and dest.parent.name=='consultas':
            target=R/'04 - Planejamento/apoio-consultas-105/folhas-para-a-mesa.html';frag='retomar'
        else:target=dest;frag=u.fragment
        a['href']=os.path.relpath(target,A)+('#'+frag if frag else '')
    nav=''.join(f'<a href="#{h["id"]}">{h.get_text()}</a>' for h in soup.find_all('h2',id=True))
    doc=f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} | Ciclo Maldito</title><style>{css}</style></head><body><nav>{nav}</nav><p class="aviso-edicao">Amostra do capítulo 7 na nova estrutura. <a href="consulta-de-regras.html">Consultar regras</a> · <a href="../apoio-consultas-105/casos-completos.html#B3">Casos completos</a>.</p><main><article class="folha" id="capitulo-7"><header><p class="numero">CAPÍTULO 7</p><h1>{title}</h1></header><div class="colunas">{soup}</div></article></main><p class="rodape-tela"><a href="../107-personagens-tecnicas-e-escolhas.md">Registro de revisão</a></p></body></html>'
    (A/'capitulo-7.html').write_text(doc)
    out=A/'output/pdf/Ciclo-Maldito-Personagens-e-Tecnicas-Amostra.pdf';out.parent.mkdir(parents=True,exist_ok=True)
    render=HTML(string=doc,base_url=str(A)).render();render.write_pdf(str(out),pdf_identifier=b'personagens-107')
    d={'registro':107,'fonte':str(F.relative_to(R)),'fonte_sha256':sha(F),'palavras_markdown':len(F.read_text().split()),'livro_de_regras':str(B.relative_to(R)),'livro_de_regras_sha256':sha(B),'consultas':consulta,'estilo_base':str(ESTILO.relative_to(R)),'estilo_base_sha256':sha(ESTILO),'pdf':str(out.relative_to(R)),'pdf_sha256':sha(out),'paginas':len(render.pages),'limite':'Capítulo reorganizado sem nova regra de treinamento, poder ou estoque de energia. Exemplos próprios mantêm sua identificação e as decisões existentes foram preservadas.'}
    (A/'amostra.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in d.items() if k!='consultas'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
