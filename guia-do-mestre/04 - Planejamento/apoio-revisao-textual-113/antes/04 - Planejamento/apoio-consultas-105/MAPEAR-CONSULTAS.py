"""Conserva os destinos do mapa 99 e a localização da cobertura já existente."""
from pathlib import Path
from html import escape
import hashlib,json,os
A=Path(__file__).resolve().parent
R=A.parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(name,data):(A/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
def main():
    mapa=R/'04 - Planejamento/apoio-estrutura-99/estrutura-e-fontes.json'
    cobertura=R/'04 - Planejamento/apoio-edicao-leitura/cobertura-atualizada.json'
    m=json.loads(mapa.read_text());c=json.loads(cobertura.read_text())
    old={x['fonte']:x for x in json.loads((R/'07 - Edicao de Leitura/mapa-editorial.json').read_text())['fontes']}
    config=R/'04 - Planejamento/apoio-conferencia-111/rotas-de-consulta.json'
    routes=json.loads(config.read_text()) if config.is_file() else None
    by={x['fonte']:x for x in m['fontes']};assert len(by)==104
    data={'registro':105,'etapa_5':'Em andamento; primeiro lote de consultas. Capítulos técnicos 6–10 e conferência final das remissões ainda pendentes.','fontes':[],'casos':{k:[] for k in ['B1','B2','B3','B4','B5']},'limite':'Os destinos são herdados do mapa 99; a movimentação do conteúdo ainda não foi executada. Alguns textos têm método e exemplo em partes diferentes.'}
    if routes:
        data.update({'revisao_das_rotas':111,'etapa_5':'Conferência conjunta das consultas no registro 111; métodos 6–10 reorganizados, ainda sem integração ao PDF completo.','rotas':routes,'limite':'Casos preservados na edição anterior; os métodos da nova estrutura têm acesso próprio. A revisão textual integral e a integração são posteriores.'})
    for f in m['fontes']:
        p=R/f['fonte'];assert p.is_file();assert sha(p)==f['sha256'],p
        ds=list(dict.fromkeys([f['destino_principal']]+f['usos_complementares']))
        row={'id':f['id'],'fonte':f['fonte'],'sha256':sha(p),'titulo':f['titulo_atual'],'exposicao_principal':f['destino_principal'],'usos':f['usos_complementares'],'recortes':[x for x in m['recortes'] if x['fonte_id']==f['id']]}
        data['fontes'].append(row)
        for code in ds:
            if code in data['casos']:
                original=old[f['fonte']]
                data['casos'][code].append({'id':f['id'],'titulo':f['titulo_atual'],'fonte':f['fonte'],'consulta_atual':str(Path('07 - Edicao de Leitura')/original['pagina'])+'#'+original['id'],'exposicao_principal':f['destino_principal'],'orientacao':f['orientacao']})
    dump('destinos-e-fontes.json',data)
    evidence={'registro':105,'mapa_99_sha256':sha(mapa),'cobertura_anterior_sha256':sha(cobertura),'tipo_conferencia':'Localização dos arquivos, hashes atuais e destinos; sem nova validação semântica dos 130 pontos, aprendizagem ou equilíbrio.','pontos':[],'competencias':[]}
    for kind in ['pontos','competencias']:
        for item in c[kind]:
            linked=[]
            for e in item.get('evidencias',[]):
                f=by[e['arquivo']];linked.append({'fonte':e['arquivo'],'sha256_atual':sha(R/e['arquivo']),'destino_principal':f['destino_principal'],'usos_complementares':f['usos_complementares']})
            assert linked,item['id']
            evidence[kind].append({'id':item['id'],'assunto':item.get('assunto',item.get('competencia')),'estado_anterior':item['estado'],'fontes_preservadas':linked})
    assert len(evidence['pontos'])==130 and len(evidence['competencias'])==20
    dump('conferencia-de-cobertura.json',evidence)
    groups={'B1':'Testes, percepção e movimento','B2':'Confrontos e perigos','B3':'Personagens e técnicas','B4':'Objetos e recompensas','B5':'Pactos e entidades'}
    nav=''.join(f'<a href="#{code}">{title}</a>' for code,title in groups.items())
    sections=[]
    md='# Destino dos casos completos — registro 105\n\n'
    md+=('Navegação conferida no registro 111. Os métodos 6–10 estão reorganizados; os casos completos continuam preservados na edição anterior até a integração. O mapa 99 determina seus destinos.\n\n' if routes else 'Primeiro lote da etapa 5. Capítulos técnicos ainda pendentes de reorganização.\n\n')
    for code,title in groups.items():
        cards=[];intro='';md+=f'## {title}\n\n'
        if routes:
            def local(path):return os.path.relpath(R/path,A)
            route=routes['grupos'][code]
            intro=f'<p><a href="{escape(local(route["metodo"]),quote=True)}">Ler a explicação principal</a></p>'
            refs=[]
            for ident in route['folhas']:
                f=next(x for x in m['fontes'] if x['id']==ident);o=old[f['fonte']]
                refs.append(f'<a href="{escape(local(str(Path("07 - Edicao de Leitura")/o["pagina"])))}#{o["id"]}">{escape(f["titulo_atual"])}</a>')
            intro+='<p>Folhas: '+' · '.join(refs)+'.</p>'
            if route.get('consulta_publicada'):
                f=next(x for x in m['fontes'] if x['id']==route['consulta_publicada']);o=old[f['fonte']]
                intro+=f'<p><a href="{escape(local(str(Path("07 - Edicao de Leitura")/o["pagina"])))}#{o["id"]}">Reserva Condensada: conferir os campos publicados</a></p>'
            md+=f'[Explicação principal](<{local(route["metodo"])}>)\n\n'
        md+='| Consulta | Exposição principal | Uso posterior |\n|---|---|---|\n'
        for f in data['casos'][code]:
            path,frag=f['consulta_atual'].split('#',1);link=os.path.relpath(R/path,A)+'#'+frag
            notice=routes.get('avisos',{}).get(f['id']) if routes else None
            warn=f'<p class="pendencia">{escape(notice)}</p>' if notice else ''
            cards.append(f'<li><a href="{escape(link,quote=True)}">{escape(f["titulo"])}</a>{warn}</li>')
            md+=f'| [{f["titulo"]}](<{os.path.relpath(R/f["fonte"],A)}>) | {m["destinos"][f["exposicao_principal"]]} | {title} |\n'
        sections.append(f'<section id="{code}"><h2>{title}</h2>{intro}<h3>Casos completos</h3><ul>{"".join(cards)}</ul></section>')
    (A/'destinos-dos-casos.md').write_text(md+'\nOs dois estudos históricos de chefe excluídos no mapa 99 continuam fora da leitura. O aprofundamento da obra conserva aviso de revelações e acesso separado. Nenhum campo de socorro, projeto, Pacto, entidade ou avaliação foi eliminado nesta entrega.\n')
    css='body{font:18px/1.55 Georgia,serif;color:#251727;background:#eee9ed;margin:0}main{max-width:960px;background:white;padding:32px 44px;margin:auto}h1,h2{color:#9e2358}nav{padding:16px;background:#251727}nav a{color:white;display:inline-block;margin:5px 16px}a{color:#9e2358}li{margin:8px 0}section{scroll-margin-top:16px}'
    css+='.pendencia{border-left:3px solid #9e2358;padding:8px 12px;background:#faf2f5;font-size:.92em}h3{font-size:1.05em}section{border-top:1px solid #ded4d9;padding-top:16px;margin-top:24px}'
    guild=f'<a href="{escape(os.path.relpath(R/routes["guilda"],A))}">Jogar em guilda</a>' if routes else ''
    intro='Comece pela explicação principal, escolha a folha que precisa levar à mesa e abra um caso para acompanhar a aplicação. Os casos completos ainda estão na edição de leitura anterior, até a integração. Exemplos experimentais conservam seus limites e avisos.'
    (A/'casos-completos.html').write_text(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Casos por assunto | Ciclo Maldito</title><style>{css}</style></head><body><nav><a href="folhas-para-a-mesa.html#escolher">Escolher uma folha</a>{nav}{guild}</nav><main><h1>Casos por assunto</h1><p>{intro}</p>{"".join(sections)}</main></body></html>')
    print(json.dumps({'fontes_preservadas':len(data['fontes']),'consultas_por_grupo':{k:len(v) for k,v in data['casos'].items()},'pontos_localizados':len(evidence['pontos']),'competencias_localizadas':len(evidence['competencias'])},ensure_ascii=False))
if __name__=='__main__':main()
