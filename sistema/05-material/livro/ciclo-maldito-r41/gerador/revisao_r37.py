"""Correções autorizadas do pente fino: texto, hierarquia e destinos exatos."""
from pathlib import Path
import json,re
B=Path(__file__).resolve().parent;R=B/'correcoes-pente-fino'
def aplicar(textos,blocos,capitulos,meta):
    rows=json.loads((R/'ALTERACOES-TEXTO.json').read_text())
    for row in rows:
        assert textos[row['bloco']]==row['antes'],row['bloco']
        textos[row['bloco']]=row['depois']
    old=json.loads(json.dumps(meta))
    for key in ['geral--testes','geral--pericias','geral--resistencia']:
        meta[key]['contexto']=re.sub(r'^#+ ','',textos[key].splitlines()[0])
    contexts={
        'vanguarda--van-yumi':'Vanguarda / Batedor',
        'rotas--rota-invocacoes':'Invocações nas rotas',
        'rotas--rota-cura':'Sem Técnica / Cura',
        'campo--inv-corpos':'Corpos amaldiçoados',
        'campo--inv-reparo':'Cura e reparo',
        'campo--inv-liberacao':'Trunfos das domadas',
        'campo--inv-maxima':'Trunfos das domadas',
        'campo--inv-dominio':'Trunfos das domadas',
        'construcao--entidades-ampliacao':'Ampliar uma especial',
        'evocador--ev-principal-continuidade':'Evocador / Invocação Principal / Intervenções da principal',
    }
    for k,v in contexts.items():meta[k]['contexto']=v
    meta['vanguarda--van-yumi']['contextos_por_titulo']={'Batedor: Yumi':'Vanguarda / Batedor: Yumi'}
    meta['evocador--ev-principal-continuidade']['contextos_por_titulo']={'Nível 19 — Especial de Continuidade':'Evocador / Invocação Principal / Especial de Continuidade'}
    for row in rows:
        k=row['bloco'];cfg=meta[k];original={h['titulo']:h for h in cfg['titulos']};heads=[]
        for line in textos[k].splitlines():
            m=re.match(r'^(#{1,6}) (.+)$',line)
            if m:heads.append({**original.get(m[2],{'papel':'subtópico'}),'titulo':m[2],'nivel':len(m[1])})
            elif cfg.get('marcador') and line=='**'+cfg['marcador']+'**':heads.append({'titulo':cfg['marcador'],'papel':'marcador temático','nivel':0})
        cfg['titulos']=heads
        first=re.match(r'^(#{1,6}) (.+)',textos[k])
        if first:cfg['nivel_primeiro']=len(first[1])
    extras=json.loads((R/'DESTINOS-INDICE.json').read_text());p=B/'revisao-de-estrutura/DESTINOS-INDICE.json'
    p.write_text(json.dumps(json.loads(p.read_text())+extras,ensure_ascii=False,indent=2)+'\n')
    (R/'ALTERACOES-CONTEXTO.json').write_text(json.dumps([{'bloco':k,'antes':old[k],'depois':v} for k,v in meta.items() if old[k]!=v],ensure_ascii=False,indent=2)+'\n')
    (B/'revisao-de-estrutura/HIERARQUIA.json').write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n')
    return rows
