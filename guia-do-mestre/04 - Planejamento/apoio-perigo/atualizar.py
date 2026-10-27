from pathlib import Path
import hashlib,json,shutil
H=Path(__file__).resolve().parent;R=H.parent.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
state=json.loads((H/'estado-inicial.json').read_text(encoding='utf-8'))
matrix='04 - Planejamento/03-matriz-dos-130-pontos.md'
assert sha(R/matrix)==state['manifesto_inicial'][matrix]
d=H/'historico/antes-do-perigo'/matrix;d.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(R/matrix,d)
state['snapshot'][matrix]=sha(R/matrix)
(H/'estado-inicial.json').write_text(json.dumps(state,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
status='Perigo completo da passarela entregue no registro67 e seção64: sinais, três rodadas experimentais, interrupção, queda publicada, alternativas, socorro e interdição. Sem escala universal ou aprovação numérica nova.'
nxt='**Próxima tarefa recomendada:** preparar a comparação de um confronto com objetivo e uma fonte ambiental de pressão, usando o Carregador como base e conferindo espaço, ações, informação e retirada. Não somar automaticamente o perigo da passarela nem presumir equilíbrio. **GPT-6 Astra, esforço extra alto** para interações; **GPT-6.1 Sol, esforço alto** para redação. Bestiário integral e treinamentos continuam adiados.'
link='[67 — Perigo da passarela](67-perigo-da-passarela-e-do-guincho.md)'
def edit(rel,f):
 p=R/rel;assert sha(p)==state['snapshot'][rel],f'Alteração concorrente: {rel}'
 s=p.read_text(encoding='utf-8');new=f(s);assert new!=s
 p.write_text(new,encoding='utf-8',newline='\n')
def version(s,n):
 lines=s.splitlines();assert lines[2].startswith('Versão ');lines[2]=f'Versão {n}, de 23 de outubro de 2026. '+status
 return '\n'.join(lines)+'\n'
edit('04 - Planejamento/01-plano-completo-do-guia.md',lambda s:version(s,57)+'\n## C04 — perigo com evolução e encerramento\n\n'+link+' e [seção64](<../06 - Redacao do Guia/64-a-passarela-e-o-guincho.md>): mecanismo sinalizado, rotas, parada e ruptura, com dano publicado de queda. Cronograma de três rodadas e dispositivo são propostas locais. M017/M129 ampliados, sem fechamento integral. Conferência documental e aritmética, sem sessão humana.\n\n'+nxt+'\n')
def pauta(s):
 s=version(s,51)
 start=s.index('**Desenvolvimento atual:**',s.index('## D12 Perigos ambientais'))
 end=s.index('\n\n',start)
 return s[:start]+'**Desenvolvimento atual:** a seção58 oferece a ferramenta; registro66/seções62–63 apresentam terreno e arrasto. O '+link+' e seção64 completam um perigo sem autor: passarela com sinais, ruptura única, interrupção, rotas e socorro. Dano de queda e ações são publicados; cronograma e dispositivo são propostas locais. M017/M129 continuam parciais para outros danos, doenças e efeitos não tabelados.'+s[end:]
edit('04 - Planejamento/02-decisoes-para-conversar.md',pauta)
def mat(s):
 old='M017/M129 têm campos de preparação, mas ainda precisam de exemplos ambientais completos; cobertura não concluída.'
 assert old in s
 return s.replace(old,'M017/M129 receberam terreno no registro66 e um exemplo ambiental completo no [registro67](67-perigo-da-passarela-e-do-guincho.md)/seção64, com sinais, ritmo, queda, intervenção e encerramento. Outros danos, doenças e efeitos não tabelados continuam em desenvolvimento; cobertura não concluída.',1)
edit(matrix,mat)
def roteiro(s):
 start=s.index('**Próxima tarefa recomendada:** preparar um perigo ambiental completo')
 end=s.index('\n\n',start)
 return s[:start]+'**Continuação entregue:** '+link+' e seção64 completam o perigo proposto. Cronograma local e limites de verificação identificados.\n\n'+nxt+s[end:]
edit('04 - Planejamento/19-roteiro-pre-1-e-modelos.md',roteiro)
edit('04 - Planejamento/apoio-piloto/RETOMADA.md',lambda s:s+'''\n## Retomada — 23/10/2026: perigo da passarela

Autorização “Pode seguir” após P66. P67/G64 completam perigo ambiental sem inimigo, com acionamento deliberado precedido de informação, apoio móvel3m e piso inferior6m abaixo. Contagem local proposta0–3, um avanço ao fim da rodada completa; ruptura única no terceiro. Parada antes impede; depois não restaura. Sem ativação não há contagem secreta. Interrupção por alavanca/Padrão no Leste ou dano em pino de transmissão madeiraDef14/PV5 no Oeste; freio independente é fato ficcional declarado, não regra de cortar qualquer cabo.

Superior9m; inferior27m físicos/39m de movimento (andar15+escalar12×2). Via inferior turno1Mov+Bônus convertida+Correr27; turno2faltam12, doisMov18 preservam Padrão para parada. Queda6m=2d6Concussão sem Bloquear, Derrubado se dano. Sem nova chance gratuita de borda, dano de escombros, soterramento, parcelas recorrentes ou ação no ar. Saltos e escadas seguem R53; rota de socorro e transporte dependem de posições, mãos, apoios e carga.

221/221 arquivos do manifesto inicial íntegros. R53 mesmo hash7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d. Plano57/pauta51, matriz, roteiro, índice e referências atualizados; registro06 e entregas anteriores preservados. Snapshot apoio-perigo/historico/antes-do-perigo; QA apoio-perigo/verificacao.json. Salvamento local, sem commit/push, sessão humana, simulação integral ou validação de dificuldade. Cronograma e dispositivo experimentais. M017/M129 ampliados, não concluídos integralmente.
\n'''+nxt+'\n')
edit('06 - Redacao do Guia/LEIA-ME.md',lambda s:s.replace('Próximo: perigo ambiental completo com escalada, intervenção e encerramento, **GPT-6 Astra, esforço extra alto**; prosa **GPT-6.1 Sol alto**.','O [perigo da passarela](64-a-passarela-e-o-guincho.md) completa o exemplo com evolução e encerramento. Próximo: comparar confronto e pressão ambiental, **GPT-6 Astra extra alto**; prosa **GPT-6.1 Sol alto**.',1)+'\n## C04 — perigo ambiental completo\n\n[A passarela e o guincho](64-a-passarela-e-o-guincho.md) ensina sinais, evolução do risco, interrupção, queda e socorro, com rotas alternativas e interdição. Regras publicadas e escolhas de cenário são identificadas. O [registro67](<../04 - Planejamento/67-perigo-da-passarela-e-do-guincho.md>) documenta a conferência. Depois deste caso, a próxima tarefa é comparar um confronto com objetivo e pressão ambiental, **GPT-6 Astra extra alto**, com prosa **GPT-6.1 Sol alto**.\n')
edit('06 - Redacao do Guia/REFERENCIAS.md',lambda s:s+'''\n## Seção64 — A passarela e o guincho

Fonte primária: a [R53 recuperada](<../04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md>), SHA-2567311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d. Leitura dirigida de Turnos/conversões, Preparar, Movimento/escalada, Saltos, Quedas e Queda sobre uma criatura, Danificar objetos/Objetos e efeitos, Estudar, manipulação de itens, Carga/transporte e Vida a zero/Socorro. O [registro67](<../04 - Planejamento/67-perigo-da-passarela-e-do-guincho.md>) identifica a aplicação de cada fonte.

Guincho, freio, geometria e três rodadas são elaboração local experimental. MadeiraDef14/peça5PV e queda6m/2d6 aplicam tabelas publicadas, sem tabela universal nova de perigo. Não houve consulta externa de engenharia, auditoria do acervo, teste humano ou validação de dificuldade. Cenário e cronograma permanecem revisáveis.
''')
print('Planejamento, pauta, matriz, roteiro, retomada, índice e referências atualizados.')
