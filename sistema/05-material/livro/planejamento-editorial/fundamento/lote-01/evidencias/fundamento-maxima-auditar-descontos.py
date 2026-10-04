from pathlib import Path
import re, itertools, json, hashlib
root=Path('/media/mizuki/HD Externo II/Claude/Claude 2')
p=root/'sistema/05-material/livro/manual/40-fundamento.md'
s=p.read_text()
rows={}
for line in s.splitlines():
 m=re.match(r'\| \*\*([1-7])\*\* \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|',line)
 if m:
  c,n,b,l,mid,h,r=map(int,m.groups());rows[c]={'nivel':n,'base':b,'L':l,'M':mid,'H':h,'refund':r}
assert set(rows)==set(range(1,8))
# Custo normal da Forma, mais até quatro Melhorias.
# Estados N/L significam família neutra ou livre; não indicam identidades.
# Isto inclui um superconjunto de perfis realizáveis com duas famílias livres.
# Prova de suficiência no superconjunto + testemunhas realizáveis dá mínimo.
opts=[(tier,status) for tier in 'LMH' for status in ('neutra','livre')]
profiles=[(form,parts) for form in '0LMH' for n in range(5) for parts in itertools.combinations_with_replacement(opts,n)]
def cost(c,prof):
 f,parts=prof;discount=(c+1)//2
 return (0 if f=='0' else rows[c][f])+sum(max(1,rows[c][tier]-discount) if status=='livre' else rows[c][tier] for tier,status in parts)
assert len(profiles)==840
budget={5:8,6:8,7:12}; steps=[]
for old,c in [(5,6),(6,7)]:
 legal=[pr for pr in profiles if cost(old,pr)<=budget[old]]
 minimum=max(cost(c,pr) for pr in legal)
 budget[c]=max(budget[c],minimum)
 steps.append({'de':old,'para':c,'numero_preexistentes':len(legal),'orcamento_minimo':budget[c],'testemunhas_de_custo':[pr for pr in legal if cost(c,pr)==minimum]})
models={}
for label,b in [('publicado',{5:8,6:8,7:12}),('primeiro_reparo_incompleto',{5:8,6:9,7:12}),('8_12_12',{5:8,6:12,7:12}),('8_12_15',{5:8,6:12,7:15}),('minimo_monotonico',budget)]:
 models[label]={'budget':b,'contagens':{c:sum(cost(c,pr)<=b[c] for pr in profiles) for c in b},'perdas':{f'{a}-{c}':[pr for pr in profiles if cost(a,pr)<=b[a] and cost(c,pr)>b[c]] for a,c in[(5,6),(6,7)]}}
examples=[
 {'nome':'Projétil com Troca, Perseguir, Fura e De Novo','familias_livres':['Alcance','Mira'],'profile':('0',(('M','livre'),)*4)},
 {'nome':'Apoio com Firmeza, Guarda, Pressa e Duradoura','familias_livres':['Auxiliares','Tempo'],'profile':('0',(('M','livre'),)*4),'ressalva':'Perfil de custo válido; quantidade de PV de Apoio Máximo tem lacuna independente no publicado.'},
 {'nome':'Projétil com Longe, Passo, Empurrão e Precisão','familias_neutras':['Alcance','Mira'],'profile':('0',(('L','neutra'),)*4)},
 {'nome':'Explosão com Longe, Passo e Precisão','familias_neutras':['Alcance','Mira'],'profile':('L',(('L','neutra'),)*3)},
]
for ex in examples:ex['custos']={c:cost(c,ex['profile']) for c in (5,6,7)}
checks={
 'orcamento_minimo_8_12_16':budget=={5:8,6:12,7:16},
 'ninguem_perde_perfil_5_6':not models['minimo_monotonico']['perdas']['5-6'],
 'ninguem_perde_perfil_6_7':not models['minimo_monotonico']['perdas']['6-7'],
 'testemunha_realizavel_12_necessario':examples[0]['custos']=={5:8,6:12,7:12},
 'testemunha_realizavel_16_necessario':examples[2]['custos']=={5:12,6:12,7:16},
 'classe5_inalterada':budget[5]==8,
 'classe7_respeita_piso12':budget[7]>=12,
}
out={'source':str(p),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'regra_desconto':'ceil(Classe/2), mínimo restante1; Formas sem desconto','perfil_count':len(profiles),'metodo':'Perfis de custo, superconjunto semântico; limites inferiores atestados por duas montagens concretas com até duas famílias livres. Inclui novas escolhas abertas na Classe6.','orcamento_minimo':budget,'transicoes':steps,'modelos':models,'testemunhas_concretas':examples,'checks':checks}
Path('/tmp/fundamento-maxima-descontos.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps({'orcamento':budget,'modelos':{k:{'contagens':v['contagens'],'numero_perdas':{t:len(pr) for t,pr in v['perdas'].items()}} for k,v in models.items()},'testemunhas':examples,'checks':checks},ensure_ascii=False,indent=2))
assert all(checks.values())
