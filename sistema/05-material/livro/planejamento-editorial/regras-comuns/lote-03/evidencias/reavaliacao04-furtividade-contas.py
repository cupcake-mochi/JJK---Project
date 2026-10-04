from fractions import Fraction as F
from collections import Counter
from itertools import product
import json, hashlib
from pathlib import Path
src=Path(__file__).resolve().parents[1]/'03-PERCEPCAO-E-FURTIVIDADE.md'

def packed(x):
    if x is None:return None
    if isinstance(x,F):return {'fraction':str(x),'value':float(x)}
    if isinstance(x,dict):return {k:packed(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [packed(v) for v in x]
    return x

def pmf(mode):
    if mode=='normal':return {i:F(1,20) for i in range(1,21)}
    c=Counter((min if mode=='disadvantage' else max)(a,b) for a,b in product(range(1,21),repeat=2))
    return {i:F(n,400) for i,n in c.items()}

def prob(dc,s,mode='normal'):
    return sum((w for r,w in pmf(mode).items() if r+s>=dc),F())

def search_stats(s,p,dc,mode):
    eligible={r+s:w for r,w in pmf(mode).items() if r+s>=dc}
    den=sum(eligible.values(),F())
    if not den:return None
    eligible={t:w/den for t,w in eligible.items()}
    return {
      'stored_cd_conditional_pmf':{str(t):w for t,w in sorted(eligible.items())},
      'search_success_first_action':sum((w*prob(t,p) for t,w in eligible.items()),F()),
      'search_success_in_3_actions_same_total':sum((w*(1-(1-prob(t,p))**3) for t,w in eligible.items()),F()),
      'impossible_search_probability':sum((w for t,w in eligible.items() if t>20+p),F()),
      'expected_stored_cd':sum((t*w for t,w in eligible.items()),F()),
    }
rows=[]
for base,s,p in product([8,10],[4,7,10,12],[0,4,8,10]):
    dc=base+p
    h=prob(dc,s);q=prob(dc,s,'disadvantage')
    assert q==h*h
    r=q+(1-q)*h
    st=h/(1-q*(1-h)) if 1-q*(1-h) else None
    rows.append({'base':base,'stealth_bonus':s,'perception_bonus':p,'dc':dc,
     'hide_normal':h,'maintenance_disadvantage':q,'maintenance_advantage_cancels':h,
     'still_hidden_after_n_attacks':{str(n):q**n for n in [1,2,3,4,6]},
     'all_n_attacks_start_hidden':{str(n):q**(n-1) for n in [1,2,3,4,6]},
     'expected_hidden_attacks_first4_given_initial_hidden':sum((q**i for i in range(4)),F()),
     'expected_hidden_attack_run_until_reveal':1/(1-q) if q<1 else 'infinite_without_external_discovery',
     'end_hidden_after_attack_then_legal_normal_rehide_if_needed_given_initial_hidden':r,
     'stationary_start_hidden_one_attack_per_turn_free_rehide_at_end':st,
     'stationary_bonus_rehide_attempts_per_turn_if_used_only_when_not_hidden':1-st*q if st is not None else None,
     'search_after_successful_initial_hide':search_stats(s,p,dc,'normal'),
     'search_after_successful_maintenance':search_stats(s,p,dc,'disadvantage'),
     'observer_passive_advantage_p_hide':prob(dc+5,s),
     'observer_passive_disadvantage_p_hide':prob(dc-5,s),
    })
# Direct enumeration independently confirms formula and chained geometric event counts.
for row in rows:
    brute=sum(1 for a,b in product(range(1,21),repeat=2) if min(a,b)+row['stealth_bonus']>=row['dc'])
    assert F(brute,400)==row['maintenance_disadvantage']
    for mode in ['normal','disadvantage','advantage']:assert sum(pmf(mode).values())==1

def equal(base):
    h=prob(base,0);q=h*h
    return {'base':base,'p':h,'q':q,'after3':q**3,'after4':q**4,'4_attacks_all_hidden':q**3,
      'expected_hidden_attacks4':sum(q**i for i in range(4)),
      'run':1/(1-q),'rehide_composite':q+(1-q)*h,
      'stationary_with_rehide':h/(1-q*(1-h)),
      'ordinary_full_hide_actions_per_hidden_attack_no_maintenance':1/h,
      'ordinary_full_hide_actions_per_hidden_attack_with_maintenance':(1-q)/h,
      'ordinary_attack_action_fraction_always_aims_for_hidden_no_maintenance':h/(h+1),
      'ordinary_attack_action_fraction_always_aims_for_hidden_with_maintenance':h/(h+1-q),
      'maintenance_cancelled_disadv_chain4':h**4}
obj={'source':str(src),'source_sha256':'6b84a92c296d46bfc8ad5a41621e60a4e74921e35542019ce8ab51a11adb7765',
 'source_note':'Modelo comparativo da candidata anterior; fórmulas explícitas, não extraídas automaticamente da versão corrente. Revisão posterior removeu manutenção; números não a descrevem.',
 'assumptions':['d20 uniform; tie reaches CD','No automatic skill success/failure on natural 20/1; project CD26 example supports this','Valid hide geometry, available signals, one observer unless stated; no external interruption in chain examples','Advantage and disadvantage cancel; maintenance with its disadvantage alone = p^2','Free rehide model assumes integrated Assassin11 legal attack, movement and hiding endpoint each turn; counterplay and unavailable endpoints break model','A failed search keeps the same stored DC; repeated searches conditional on legality and cost'],
 'matrix':rows,'equal_bonuses':[equal(8),equal(10)],
 'accuracy_examples':[{'base_hit':F(h,100),'advantage_hit':1-(1-F(h,100))**2,'gain':F(h,100)*(1-F(h,100))} for h in [20,50,55,65,90]],
 'critical_probability':{'normal':F(1,20),'advantage':1-F(19,20)**2},
 'opposed_equal_bonus_tie_hider':F(210,400),'opposed_equal_bonus_tie_observer':F(190,400)}
Path(__file__).with_name('reavaliacao04-furtividade-matematica.json').write_text(json.dumps(packed(obj),ensure_ascii=False,indent=2))
print(json.dumps(packed({'equal':obj['equal_bonuses']}),ensure_ascii=False,indent=2))
for base in [8,10]:
 print('\nBASE',base)
 for s in [4,7,10,12]:
  rr=[r for r in rows if r['base']==base and r['stealth_bonus']==s]
  print(s,' | '.join(f"P{r['perception_bonus']}: {float(r['hide_normal'])*100:g}%/{float(r['maintenance_disadvantage'])*100:g}%" for r in rr))
for base,s,p in [(8,4,4),(10,4,4),(8,12,4),(10,12,4),(8,12,0),(10,12,0),(8,12,10),(10,12,10)]:
 r=next(r for r in rows if (r['base'],r['stealth_bonus'],r['perception_bonus'])==(base,s,p))
 print('\nSELECT',base,s,p)
 for k in ['all_n_attacks_start_hidden','still_hidden_after_n_attacks','expected_hidden_attacks_first4_given_initial_hidden','expected_hidden_attack_run_until_reveal','end_hidden_after_attack_then_legal_normal_rehide_if_needed_given_initial_hidden','stationary_start_hidden_one_attack_per_turn_free_rehide_at_end','search_after_successful_initial_hide','search_after_successful_maintenance']:
  v=r[k]
  if isinstance(v,dict):v={k:v for k,v in v.items() if k!='stored_cd_conditional_pmf'}
  print(k,packed(v))
