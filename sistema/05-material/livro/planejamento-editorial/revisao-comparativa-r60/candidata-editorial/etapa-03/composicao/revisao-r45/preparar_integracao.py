from pathlib import Path
import json,re
B=Path(__file__).resolve().parents[1];R=B/'revisao-r45'
base=json.loads((R/'BLOCOS-BASE.json').read_text());after=dict(base);new={}
for f in sorted((R/'texto-final').glob('*.md')):
 for k,t in re.findall(r'<!-- bloco:([^>]+) -->\s*(.*?)(?=<!-- bloco:|\Z)',f.read_text(),re.S):
  assert k not in new,k
  new[k]=t.strip().replace('#campo--inv-recuperar','#campo--inv-reparo')
# Ordem de leitura: catálogo, opção de rota, personalização e exemplos.
order=[k for k in new if k not in ['origens--legado-criar','origens--legados-exemplos']]+['origens--legado-criar','origens--legados-exemplos']
# Híbrido vem após Encarnado; conservar ordem das primeiras Origens do livro.
start=order.index('origens--origem-encarnado');end=order.index('origens--origem-descendente')
enc=order[start:end]; del order[start:end]
pos=order.index('origens--origem-feto');order[pos:pos]=enc
for k in list(after):
 if k.startswith('origens--') and k not in new:after.pop(k)
after.update(new)
def rep(k,a,z):
 assert a in after[k],(k,a)
 after[k]=after[k].replace(a,z)
rep('ab--ab-criacao','Escolha sua história inicial, seus Legados e os treinos concedidos.','Escolha sua história, a marcante, duas menores e os treinos da Origem.')
rep('ab--ab-origem','Leia sua entrada inteira e anote o traço, os dois Legados iniciais e os treinos que ela concede. Pelo menos um dos Legados deve ser narrativo.','Leia sua entrada inteira e registre a base de treinos, o traço, uma capacidade marcante e duas menores elegíveis. Legados de história sem benefício não consomem essas escolhas; Sem Técnica é uma opção separada, disponível somente às Origens indicadas.')
rep('ab--ab-origem','Portanto, antes de trocas específicas, a criação reúne','Portanto, antes de capacidades que concedam treinos adicionais e de trocas específicas, a criação reúne')
rep('ab--ab-conferencia','Origem e Legados.','Origem, marcante, duas menores e Legados de história.')
rep('progressao--prog-atualizar','Origem e Legados são escolhas da criação; a subida não oferece novos Legados. Efeitos de Origem que dependam de nível acompanham sua própria regra.','A Origem, sua marcante e as duas menores são escolhas da criação; subir de nível não concede novas vagas. Efeitos que dependam de nível acompanham sua própria regra. Uma perda duradoura pode permitir rever a escolha afetada entre missões, com jogador e mestre, conforme [Rever a Origem](#origens--legado-criar), sem troca livre ou vagas extras.')
for k in ['rotas--rotas','rotas--rota-sem-tecnica']:rep(k,'**Origens e Legados**','**Origens**')
rep('rotas--rotas','Personagem com essa sub-origem.','Latente, Receptáculo, Descendente, Encarnado ou Híbrido que escolha essa opção separada.')
rep('rotas--rota-sem-tecnica','Esta rota conserva PE de energia, refino e aptidões.','A opção não consome a marcante nem uma das duas menores da Origem. Esta rota conserva PE de energia, refino e aptidões.')
rep('aptidoes--apt-reversa','Suas formas de reparo estão na Origem.','Suas formas de recuperação estão na Origem, com o procedimento compartilhado em [Cura e reparo](#campo--inv-reparo).')
# Regra compartilhada: preservar integralmente a tabela e números R44.
rep('campo--inv-reparo','No descanso curto, uma pessoa treinada','## Reparar\n\nNo descanso curto, uma pessoa treinada')
rep('campo--inv-reparo','O corpo precisa estar acima de zero.','Para uma entidade, o corpo precisa estar acima de zero. O personagem de Origem Corpo Amaldiçoado usa o mesmo teste e tabela; vida a zero segue Socorro e as curas compatíveis, sem permitir religá-lo pelo retorno pago de uma entidade.')
after['campo--inv-reparo']+='\n\nO ofício compatível do personagem é escolhido na criação e fica registrado na ficha. **Manutenção Precisa** permite uma repetição diária do teste falho durante descanso curto, na mesma tentativa e sem cura dupla. **Reparo Autônomo** conserva sua Ação Padrão, frequência diária e recuperação de 30%, conforme a Origem; não consome a tentativa de uma pausa futura.'
# M1: exceção local expressa; nenhuma reescrita dos gatilhos de derrota.
after['dano--derrota']+='\n\n**Núcleo Dependente.** Um Corpo Amaldiçoado com essa menor não possui Integridade; a exigência de recuperar essa reserva não se aplica a ele. Queda por vida, outras causas de inconsciência e as demais condições de recuperação continuam valendo. Receber PE encerra a inatividade por energia, não essas outras causas.'
rep('consulta--consulta-glossario-4','[Legado](#origens--origens). Escolha da Origem que registra uma capacidade ou vínculo, conforme sua entrada.','[Legado de história](#origens--legados). Relação ou detalhe da história; sem benefício mecânico, não ocupa escolha de marcante ou menor.')
rep('consulta--consulta-glossario-4','Escolha de criação que reúne traço, Legados, treinos e opções de rota.','Escolha de criação que reúne base de treinos, história, uma marcante, duas menores elegíveis e opções de rota.')
# Novos termos junto da entrada pertinente, preservando as demais definições.
after['consulta--consulta-glossario-4']=after['consulta--consulta-glossario-4'].replace('[Marco]', '[Marcante e menores](#origens--origem-escolhas). Uma capacidade central e duas escolhas elegíveis da Origem, sem trocar suas vagas entre si.\n\n[Marco]')
# Índice: nomenclatura vigente e novas entradas localizáveis.
for k in list(after):
 if k.startswith('consulta--consulta-indice-'):
  after[k]=after[k].replace('[Feto]', '[Híbrido]').replace('[Origens e Legados]','[Origens]')
for name,target,k,before in [
 ('Híbrido','origens--origem-feto','consulta--consulta-indice-6','Identificar Feitiço'),
 ('Marcante e menores','origens--origem-escolhas','consulta--consulta-indice-7','Marco'),
 ('Talento de Categoria de Efeito 4','origens--restricao-ce4','consulta--consulta-indice-10','Talento Próprio'),
 ('Reparar','campo--inv-reparo','consulta--consulta-indice-9','Ressonante')]:
 assert '['+before+']' in after[k]
 after[k]=after[k].replace('['+before+']','['+name+'](#'+target+')\n['+before+']')
rep('consulta--consulta-indice-6','[Legado](#origens--origens)','[Legado de história](#origens--legados)')
# Mapear cada bloco à evidência, sem inventar novos itens da lista de regras geral.
def decision(k):
 if k in ['origens--origens','origens--origem-escolhas','origens--legados','origens--legado-criar','origens--legados-exemplos','origens--origem-sem-tecnica']:return 'A001–A015, A047'
 if 'latente' in k:return 'A032–A047'
 if 'receptaculo' in k:return 'A063–A070'
 if 'descendente' in k:return 'A077–A087'
 if 'encarnado' in k:return 'A071–A076'
 if 'feto' in k:return 'A048–A050'
 if 'corpo' in k and not 'restricao' in k or 'origem-reparo' in k or k=='campo--inv-reparo' or k=='dano--derrota':return 'A051–A062; I002'
 if k in ['origens--restricao-sem-energia','origens--restricao-prenuncio','origens--restricao-beneficios']:return 'A016–A031'
 if 'restricao' in k:return 'A088–A100; I001'
 return 'A007–A015, A047; remissões das decisões de Origem'
rows=[]
for k in list(base)+[k for k in after if k not in base]:
 a=base.get(k,'');z=after.get(k,'')
 if a!=z:rows.append(dict(id=f'R45-{len(rows)+1:03}',bloco=k,antes=a,depois=z,motivo='Integrar a montagem aprovada e sua redação final.' if k.startswith('origens--') else 'Conciliar referência ou procedimento compartilhado afetado pelas novas Origens; demais frases preservadas.',item=decision(k)))
(R/'ORDEM-ORIGENS.json').write_text(json.dumps(order,ensure_ascii=False,indent=2)+'\n')
(B/'ALTERACOES-R44-para-R45.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
(R/'BLOCOS-ESPERADOS.json').write_text(json.dumps(after,ensure_ascii=False,indent=2)+'\n')
# Modelo separado continua editável e rastreado.
supp=json.loads((R/'FICHAS-BASE.json').read_text());sr=[]
k='consulta--consulta-ficha-personagem';old=supp[k]
supp[k]=old.replace('Origem, traço e Legados','Origem, traço e Legados de história').replace('| Caminho, Trilha e nível |','| Marcante, modalidade/ramo | ________________________________________ |\n| Menor 1 e escolhas fixas | ________________________________________ |\n| Menor 2 e escolhas fixas | ________________________________________ |\n| Ofício compatível, quando aplicável | ________________________________________ |\n| Caminho, Trilha e nível |')
supp[k]+='\n\n**Híbrido — Regeneração Orgânica:** limiar = piso(30% da vida máxima atual): ______; usos por cena = piso(Constituição/2) + 1: ______; usos restantes: ______. Faixa válida: de 1 PV ao limiar, sem vida temporária. Confira PE, turno, Ação Bônus e impedimentos antes de ativar.\n\n**Restrições e capacidades de Origem:** limites, cuidados, escolhas e estoques: ________________________________________'
for k,z in supp.items():
 a=json.loads((R/'FICHAS-BASE.json').read_text())[k]
 if a!=z:sr.append(dict(id=f'R45-F-{len(sr)+1:03}',bloco=k,antes=a,depois=z,motivo='Atualizar campos da ficha e registro manual do Híbrido.',item='A008/A048; I001/I002'))
(R/'ALTERACOES-FICHAS.json').write_text(json.dumps(sr,ensure_ascii=False,indent=2)+'\n')
(R/'FICHAS-ATUALIZADAS.json').write_text(json.dumps(supp,ensure_ascii=False,indent=2)+'\n')
(B/'FICHAS-COMPLETAS-R45.md').write_text('\n\n'.join(supp.values())+'\n')
print(len(rows),'blocos registrados;',len(new),'blocos de Origens;',len(sr),'modelo de ficha atualizado')

notes=json.loads((B/'DESTAQUES-CATALOGO.json').read_text())
changed={r['bloco'] for r in rows}
notes=[x for x in notes if x['bloco'] not in changed]
for row in rows:
 for i,para in enumerate(row['depois'].split('\n\n')):
  if para.startswith('> '):
   text=' '.join(line.removeprefix('> ') for line in para.splitlines())
   notes.append(dict(id=f"R45-N-{len(notes)+1}",bloco=row['bloco'],capitulo='5. Origens' if row['bloco'].startswith('origens--') else 'Criação',texto=text,palavras=len(text.split()),paginas_base=[],tipo='exemplo' if text.startswith('**Exemplo') else 'recurso digital',motivo='R45: exemplo ou recurso preserva tratamento vigente.'))
(B/'DESTAQUES-CATALOGO.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
