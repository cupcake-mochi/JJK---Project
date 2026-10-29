"""Ajustes após leitura das 21 páginas da primeira prova."""
from pathlib import Path
import json
A=Path(__file__).resolve().parent;R=A.parents[1];C=R/'06 - Redacao do Guia/revisao-98/casos';changes=json.loads((A/'alteracoes.json').read_text())
def edit(name,before,after,why):
 p=C/name;t=p.read_text();assert t.count(before)==1,(name,before);p.write_text(t.replace(before,after));changes.append({'fonte':str(p.relative_to(R)),'passagem':2,'tipo':'clareza','antes':before,'depois':after,'motivo':why});print(name+': '+after)
n='84-percursos-apoios-e-quedas.md'
edit(n,'Enquanto estiver na passagem, seus ataques e TRs Físicos têm desvantagem, e ataques contra ele têm vantagem.','Enquanto estiver na passagem, seus ataques e Testes de Resistência (TRs) Físicos têm desvantagem, e ataques contra ele têm vantagem.','Explicar a sigla na primeira aparição deste caso.')
edit(n,'Parkour: alcançar e segurar uma borda','Parkour: segurar uma borda','Título mais curto e específico.')
n='85-trajetorias-ferramentas-e-improvisacao.md'
edit(n,'## Improvisar uma arma parecida com outra','## Um cabo como bastão','Título identifica o objeto e a referência usados.')
edit(n,'## Improvisar uma arma: a garrafa','## Uma garrafa como arma','Título curto e paralelo ao exemplo anterior.')
edit(n,'Dedica **um minuto** à instalação acessível: prende a corda e prepara a ligação do arnês ao ponto firme.','Dedica **um minuto** ao preparo: prende a corda e conecta o arnês ao ponto firme.','Retirar a expressão pouco natural instalação acessível.')
n='22-quedas-e-socorro.md'
edit(n,'Resolva a escolha do jogador e anote separadamente a cura recebida e o prazo restante.','Anote a escolha do jogador e acompanhe separadamente a cura recebida e o prazo restante.','O jogador escolhe; o mestre registra e acompanha.')
edit(n,'Caso contrário, faça essa escolha.','Caso contrário, o jogador escolhe Aguentar ou Insistir.','Explicitar quem decide.')
edit(n,'Some o tratamento válido anterior a esse ponto, até o máximo atual; impedimentos de cura continuam valendo.','Some essa vida ao tratamento válido já recebido, até o máximo atual; impedimentos de cura continuam valendo.','Ponto poderia significar instante em vez do ponto de vida recuperado.')
edit(n,'As referências abaixo são os valores parciais já usados no confronto do anexo.','A tabela usa os mesmos valores parciais do confronto do anexo.','Nomear a tabela e evitar referências abstratas.')
n='23-retirada-e-recuperacao.md'
edit(n,'Esse atendimento não restaura Integridade. Esse teste faz parte da recuperação depois da derrota. Não inicia outra janela de Morrendo.','O atendimento não restaura Integridade nem inicia outra janela de Morrendo: é a recuperação prevista para quem já está Derrotado.','Evitar três frases repetindo o mesmo sujeito.')
edit(n,'Outras penalidades continuam precisando de conferência.','Confira também outras penalidades da ficha.','Conselho em voz direta.')
edit(n,'As decisões sobre tempo de trabalho, treinamentos e recompensas comuns continuam nas pautas próprias.','Para trabalho, treinamento e recompensas, consulte os capítulos correspondentes.','Retirar referência a pautas de planejamento do texto de leitura.')
n='81-passar-a-missao-entre-mestres.md'
edit(n,'**Observação ilustrativa, sem leitor real consultado:** “Entendi que tirar a nuvem também retirava Envenenado.” O problema apontado é a distinção entre o estado do lugar e o estado da pessoa.','**Dúvida possível:** “Tirar a nuvem também encerra Envenenado?” O lugar e a pessoa têm estados diferentes. Use o registro para mostrar o que terminou e o que ainda precisa de atenção.','Apresentar dúvida hipotética, sem aparência de comentário coletado em teste.')
edit(n,'Quem conduzir a próxima aplicação, durante o preparo.','Quem mestrar a próxima sessão, durante o preparo.','Nomear uma tarefa conhecida pelo leitor.')
edit(n,'O destinatário localiza fonte, prazo e próxima tentativa sem pedir nova reconstrução?','Quem recebe encontra a fonte, o prazo e a próxima tentativa sem precisar refazer as contas?','Pergunta mais concreta para conferir o registro.')
edit(n,'As perguntas descrevem uma avaliação futura. Use o exemplo para conferir recursos, condições e referências. Ao aplicá-lo, observe se o grupo consegue distinguir o estado da sala do estado da personagem.','Use as perguntas para conferir o registro com o grupo. Observe se todos conseguem distinguir o estado da sala do estado da personagem.','Instrução prática em vez de comentário sobre uma avaliação futura.')
(A/'alteracoes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n')
