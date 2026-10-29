"""Conjunto de inspiração e exemplos originais; não recompõe o livro integrado."""
from pathlib import Path
from bs4 import BeautifulSoup
from weasyprint import HTML
import markdown,json,hashlib,os,re
A=Path(__file__).resolve().parent
R=A.parents[1]
F=R/'06 - Redacao do Guia/revisao-98/03a-ideias-para-aventuras.md'
B=R/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'
ESTILO=R/'04 - Planejamento/apoio-conducao-102/capitulo-4.html'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
MAPA='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 600" role="img" aria-labelledby="titulo descricao">
<title id="titulo">O canal das hortas: travessia e apoio na margem inicial</title>
<desc id="descricao">As margens estão separadas por quatro metros e meio. Há três metros livres para impulso na margem inicial e apoio firme na oposta. A corrente segue para baixo no desenho. Uma grade fica junto à margem inicial, um metro e meio adiante no sentido da corrente. O caminho pela passarela fica fora do recorte.</desc>
<defs><marker id="seta" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto-start-reverse"><path d="M1,1 L7,4 L1,7" fill="none" stroke="#9e2358" stroke-width="1.4"/></marker></defs>
<style>text{font-family:Arial,sans-serif;font-size:24px;fill:#251727}.titulo{font-size:28px;font-weight:bold}.menor{font-size:23px}.cota{fill:none;stroke:#9e2358;stroke-width:2}.margem{fill:#f8f1f4;stroke:#a8909c;stroke-width:2}</style>
<rect width="1100" height="600" fill="white"/>
<text x="550" y="35" text-anchor="middle" class="titulo">UM TRECHO DE 4,5 m ENTRE APOIOS FIRMES</text>
<rect x="50" y="100" width="380" height="390" class="margem"/>
<rect x="430" y="100" width="240" height="390" fill="#e7eff2"/>
<rect x="670" y="100" width="380" height="390" class="margem"/>
<text x="240" y="78" text-anchor="middle" class="titulo">MARGEM INICIAL</text>
<text x="860" y="78" text-anchor="middle" class="titulo">MARGEM OPOSTA</text>
<path d="M430 140 H670" class="cota" marker-start="url(#seta)" marker-end="url(#seta)"/>
<rect x="502" y="120" width="96" height="31" fill="white"/><text x="550" y="143" text-anchor="middle">4,5 m</text>
<path d="M270 200 H430" class="cota" stroke-dasharray="7 6"/>
<circle cx="430" cy="200" r="7" fill="#9e2358"/><circle cx="670" cy="200" r="7" fill="#9e2358"/>
<path d="M440 200 H660" class="cota" marker-end="url(#seta)"/>
<text x="250" y="166" text-anchor="middle" class="menor">3 m livres para impulso</text>
<text x="820" y="166" text-anchor="middle" class="menor">Chegada no mesmo nível</text>
<path d="M550 285 V420" class="cota" marker-end="url(#seta)"/>
<text x="550" y="260" text-anchor="middle" class="menor">Corrente</text>
<path d="M450 200 V280 M444 200 H456 M444 280 H456" class="cota"/>
<text x="416" y="244" text-anchor="end" class="menor">1,5 m</text>
<g stroke="#251727" stroke-width="3"><path d="M409 267 H435 V293 H409 Z" fill="white"/><path d="M415 267 V293 M422 267 V293 M429 267 V293 M409 280 H435"/></g>
<path d="M270 338 L410 286" class="cota"/>
<text x="75" y="353" class="titulo">Grade firme</text>
<text x="75" y="386">Junto à margem inicial;</text><text x="75" y="418">permite manter a cabeça</text><text x="75" y="450">fora d’água neste caso.</text>
<text x="860" y="337" text-anchor="middle">Após cruzar:</text><text x="860" y="373" text-anchor="middle" class="titulo">5 min até o coreto</text>
<text x="550" y="540" text-anchor="middle">Pela passarela pública: 20 min até o coreto, fora deste recorte.</text>
<text x="550" y="577" text-anchor="middle" class="menor">Esquema sem escala. As medidas indicam as distâncias da travessia.</text>
</svg>'''
def regras(css):
    lines=B.read_text().splitlines();blocos=[]
    for nome in ['Testes','Ajudar','Terreno, escalada e natação','Saltos','Carga','Percepção de energia']:
        m=[(i,len(h.group(1))) for i,l in enumerate(lines) if (h:=re.match(r'^(#{2,5}) '+re.escape(nome)+r'\s*$',l))]
        assert m,nome
        assert len(m)==1 or nome=='Carga',(nome,m)
        start,level=m[0];end=len(lines)
        for i in range(start+1,len(lines)):
            h=re.match(r'^(#{1,5}) ',lines[i])
            if h and len(h.group(1))<=level:end=i;break
        blocos.append({'titulo':nome,'id':f'regra-{len(blocos)+1}','inicio_linha':start+1,'fim_linha':end,'texto':'\n'.join(lines[start:end])})
    corpo=''.join(f'<section class="consulta-regra" id="{b["id"]}">{markdown.markdown(b["texto"],extensions=["tables","sane_lists"])}</section>' for b in blocos)
    soup=BeautifulSoup(corpo,'html.parser');ids={x['id'] for x in soup.find_all(id=True)}
    for a in soup.find_all('a',href=True):
        if a['href'].startswith('#') and a['href'][1:] not in ids:a['href']='../apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'+a['href']
    menu=''.join(f'<li><a href="#{b["id"]}">{b["titulo"]}</a></li>' for b in blocos)
    doc=f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Regras para os exemplos | Ciclo Maldito</title><style>{css}main{{max-width:900px;background:white;padding:30px}}h4{{font-family:Bree,serif;font-size:22px}}h5{{font-size:19px}}body{{background:white}}</style></head><body><main><p><a href="ideias-para-aventuras.html">Voltar às ideias</a></p><h1>Livro de Regras 1.0</h1><p>Trechos da base, sem reescrita. Os horários, as pessoas e as condições do canal são preparo local dos exemplos.</p><ul>{menu}</ul>{soup}</main></body></html>'
    (A/'consulta-de-regras.html').write_text(doc)
    return [{k:v for k,v in b.items() if k!='texto'} for b in blocos]
def main():
    (A/'canal-das-hortas.svg').write_text(MAPA)
    css=BeautifulSoup(ESTILO.read_text(),'html.parser').style.string.replace("content:'NA MESA DE JOGO'","content:'IDEIAS PARA AVENTURAS'")
    css+='''
    figure{margin:18px 0;break-inside:avoid}figcaption{font-size:15px;line-height:1.4;color:#6f5867;margin-top:8px}.colunas .cartao h3{margin-top:0}
    @media print{.cartao{break-inside:avoid;margin:0 0 9pt}.cartao h3{margin-top:8pt}.mapa-canal{column-span:all;margin:9pt 0;break-inside:avoid}.mapa-canal img{width:100%;max-height:85mm;object-fit:contain}figcaption{font-size:8.8pt;line-height:11pt;margin-top:5pt}.colunas h2{font-size:18pt}.colunas h3{font-size:12.5pt}}
    '''
    consultas=regras(css)
    soup=BeautifulSoup(markdown.markdown(F.read_text(),extensions=['tables','sane_lists','toc']),'html.parser');titulo=soup.h1.get_text();soup.h1.extract()
    for p in list(soup.find_all('p')):
        if p.find('img'):
            fig=soup.new_tag('figure',attrs={'class':'mapa-canal'});p.insert_before(fig);fig.append(p.find('img').extract())
            nxt=p.find_next_sibling()
            if nxt and nxt.name=='p' and nxt.find('em'):
                cap=soup.new_tag('figcaption');cap.string=nxt.get_text();fig.append(cap);nxt.extract()
            p.extract()
    # As quatro listas funcionam como cartões; exemplos completos seguem em fluxo.
    for h2 in list(soup.find_all('h2'))[:4]:
        stop=h2.find_next_sibling('h2');cur=h2.find_next_sibling()
        while cur is not None and cur is not stop:
            nxt=cur.find_next_sibling()
            if cur.name=='h3':
                p=cur.find_next_sibling();assert p and p.name=='p'
                box=soup.new_tag('section',attrs={'class':'cartao'});cur.insert_before(box);box.append(cur.extract());nxt=p.find_next_sibling();box.append(p.extract())
            cur=nxt
    for a in soup.find_all(['a','img']):
        attr='href' if a.name=='a' else 'src';u=a.get(attr,'')
        if re.match(r'^(https?:|#)',u):continue
        path,sep,frag=u.partition('#');dest=(F.parent/path).resolve();assert dest.exists(),dest
        a[attr]=os.path.relpath(dest,A)+(sep+frag if sep else '')
    menu=''.join(f'<a href="#{h["id"]}">{h.get_text()}</a>' for h in soup.find_all('h2',id=True))
    doc=f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{titulo} | Ciclo Maldito</title><style>{css}</style></head><body><nav aria-label="Conteúdo">{menu}</nav><p class="aviso-edicao">Complemento de Preparar aventuras. <a href="../apoio-mundo-e-preparo-101/capitulos-2-e-3.html">Ler o método de preparo</a>. <a href="consulta-de-regras.html">Consultar as regras dos exemplos</a>.</p><main><article class="folha" id="ideias"><header><p class="numero">PREPARAR AVENTURAS</p><h1>{titulo}</h1></header><div class="colunas">{soup}</div></article></main><p class="rodape-tela"><a href="../104-ideias-combinaveis-e-exemplos.md">Registro de revisão</a></p></body></html>'
    (A/'ideias-para-aventuras.html').write_text(doc)
    out=A/'output/pdf/Ciclo-Maldito-Ideias-para-Aventuras-Amostra.pdf';out.parent.mkdir(parents=True,exist_ok=True)
    HTML(string=doc,base_url=str(A)).write_pdf(str(out),pdf_identifier=b'inspiracao-104')
    d={'registro':104,'fonte':str(F.relative_to(R)),'fonte_sha256':sha(F),'palavras_markdown':len(F.read_text().split()),'livro_de_regras':str(B.relative_to(R)),'livro_de_regras_sha256':sha(B),'consultas':consultas,'estilo_base':str(ESTILO.relative_to(R)),'estilo_base_sha256':sha(ESTILO),'mapa':str((A/'canal-das-hortas.svg').relative_to(R)),'mapa_sha256':sha(A/'canal-das-hortas.svg'),'pdf':str(out.relative_to(R)),'pdf_sha256':sha(out),'limite':'Amostra isolada. Ideias curtas requerem preparo; dois exemplos têm escopo definido. Sem novo equilíbrio de combate.'}
    (A/'amostra.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:v for k,v in d.items() if k!='consultas'},ensure_ascii=False,indent=2))
if __name__=='__main__':main()
