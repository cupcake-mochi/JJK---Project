from pathlib import Path
p=Path('/home/mizuki/JJK-v0.341-para-subir/conferir-repositorio.py');t=p.read_text();a=t.index("bloco('12. FONTE R53");b=t.index('# --------------------------------------------------------------------------',a)
old=t[a:b]
new=old.replace('12. FONTE R53 E REGISTRO DE ALTERAÇÕES','12. FONTE R57 E CADEIA DE ALTERAÇÕES')
new=new.replace("_fonte53 = _json53.load(open(os.path.join(_REV53, 'FONTE-PUBLICADA.json'), encoding='utf-8'))","_atual57 = os.path.join(_BASE53, 'revisao-de-regras', 'editorial-r57')\n    _fonte53 = _json53.load(open(os.path.join(_atual57, 'FONTE-PUBLICADA.json'), encoding='utf-8'))")
new=new.replace('fonte R53 difere','fonte R57 difere')
a1=new.index('    if set(_fim53)');b1=new.index('    _esperados53',a1)
comparison=new[a1:b1].replace('integração R53','edição R57')
new=new[:a1]+new[b1:]
marker="    print(f'  {len(_publicados53)} blocos finais e {len(_reg53)} registros antes/depois conferidos.')"
assert marker in new
chain='''    _registros57 = len(_reg53)
    for _n57 in range(54, 58):
        _proximo57 = _json53.load(open(os.path.join(_atual57, f'BLOCOS-R{_n57}.json'), encoding='utf-8'))
        _registro57 = _json53.load(open(os.path.join(_BASE53, 'revisao-de-regras', 'alteracoes', f'R{_n57-1}-para-R{_n57}.json'), encoding='utf-8'))
        _mudados57 = {k for k in set(_fim53) | set(_proximo57) if _fim53.get(k, '') != _proximo57.get(k, '')}
        if {r['bloco'] for r in _registro57} != _mudados57 or len(_registro57) != len(_mudados57):
            erro(f'12: registro R{_n57-1}-para-R{_n57} tem omissão ou repetição')
        for _r57 in _registro57:
            _k57 = _r57['bloco']
            if _r57['antes'] != _fim53.get(_k57, '') or _r57['depois'] != _proximo57.get(_k57, ''):
                erro(f'12: antes/depois divergente na R{_n57}: {_k57}')
        _registros57 += len(_registro57)
        _fim53 = _proximo57
'''+comparison+'''    print(f'  {len(_publicados53)} blocos finais e {_registros57} registros da cadeia R52 a R57 conferidos.')'''
new=new.replace(marker,chain).replace('registros da R53','registros da R57')
p.write_text(t[:a]+new+t[b:])
# The current guard regression retains the historical integration snapshots.
q=p.parent/'sistema/05-material/livro/ciclo-maldito-r41/revisao-de-regras/editorial-r57/testar-integridade.py'
s=(q.parent.parent/'fundamento-r53/testar-integridade.py').read_text()
s=s.replace("revisao-de-regras/alteracoes/R52-para-R53.json","revisao-de-regras/alteracoes/R56-para-R57.json")
s=s.replace("bloco('12. FONTE R53","bloco('12. FONTE R57")
q.write_text(s)
print('Guarda e regressões atualizadas para a cadeia R52 a R57.')
