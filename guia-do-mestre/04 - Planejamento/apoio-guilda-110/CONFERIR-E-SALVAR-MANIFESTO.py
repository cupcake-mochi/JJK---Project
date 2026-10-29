"""Conferir entradas anteriores e acrescentar a entrega 110 por união."""
from pathlib import Path
import hashlib,json

A=Path(__file__).resolve().parent
R=A.parents[1]
MANIFEST=R/'04 - Planejamento/apoio-piloto/manifesto-entrega.json'
CONTROLS=[
    'LEIA-ME.md','RETOMADA-CODEX-2026-10-23.md',
    '04 - Planejamento/01-plano-completo-do-guia.md',
    '04 - Planejamento/19-roteiro-pre-1-e-modelos.md',
    '04 - Planejamento/98-plano-de-melhoria-e-validacao-do-guia.md',
    '04 - Planejamento/99-sumario-comentado-e-caminhos-de-leitura.md',
    '06 - Redacao do Guia/LEIA-ME.md',
    '06 - Redacao do Guia/revisao-98/LEIA-ME.md',
    '04 - Planejamento/apoio-piloto/RETOMADA.md'
]
NEW=[
    '06 - Redacao do Guia/revisao-98/10-jogar-em-guilda.md',
    '04 - Planejamento/110-guilda-registros-e-passagem.md'
]

def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()

def main():
    old=json.loads((A/'antes/04 - Planejamento/apoio-piloto/manifesto-entrega.json').read_text())
    current=json.loads(MANIFEST.read_text())
    assert set(old)<=set(current),'Entradas anteriores ausentes'
    allowed=set(CONTROLS)
    changed=[];fail=[]
    for rel,expected in old.items():
        p=R/rel
        if not p.is_file():fail.append({'arquivo':rel,'problema':'ausente'});continue
        actual=sha(p)
        if actual!=expected:
            if rel in allowed:changed.append(rel)
            else:fail.append({'arquivo':rel,'problema':'alteração fora do lote'})
    assert not fail,fail
    assert set(changed)==allowed,(changed,allowed)
    result={'registro':110,'entradas_anteriores':len(old),'entradas_anteriores_preservadas':len(old)-len(changed),'controles_atualizados':changed,'arquivos_ausentes_ou_alterados_fora_do_lote':fail,'metodo':'Todas as entradas anteriores conferidas; atualização por união restrita aos nove controles e aos arquivos da entrega 110.','limite':'Verificação de integridade documental, não teste de aprendizagem ou equilíbrio.'}
    (A/'conferencia-do-manifesto.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    candidates=[R/rel for rel in CONTROLS+NEW]+[p for p in A.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
    updated=dict(current)
    for p in candidates:updated[str(p.relative_to(R))]=sha(p)
    assert set(old)<=set(updated)
    MANIFEST.write_text(json.dumps(updated,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'entradas_anteriores':len(old),'entradas_finais':len(updated),'novas_entradas':len(set(updated)-set(old)),'controles_atualizados':len(changed),'falhas':len(fail)},ensure_ascii=False))

if __name__=='__main__':main()
