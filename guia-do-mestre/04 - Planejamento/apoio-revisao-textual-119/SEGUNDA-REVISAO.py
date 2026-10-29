"""Ajustes após leitura das 18 páginas da primeira prova."""
from pathlib import Path
import json
A=Path(__file__).resolve().parent;R=A.parents[1];C=R/'06 - Redacao do Guia/revisao-98/casos';changes=json.loads((A/'alteracoes.json').read_text())
def edit(name,before,after,why):
 p=C/name;t=p.read_text();assert t.count(before)==1,(name,before);p.write_text(t.replace(before,after));changes.append({'fonte':str(p.relative_to(R)),'passagem':2,'tipo':'clareza','antes':before,'depois':after,'motivo':why});print(after)
n='59-recursos-e-ritmo-dos-inimigos.md'
edit(n,'| Você quer… | Examine… | Confira antes de usar |','| Você quer… | Limite de uso | O que conferir |','Cabeçalhos diretos para a consulta.')
edit(n,'O ensaio acima compara outra forma de interrupção;','O exemplo acima compara outra forma de interrupção;','Nomear o exemplo sem termo de processo editorial.')
edit(n,'Ela explica a diferença entre o custo-base da Classe e o que se paga ao usar o feitiço.','A seção explica a diferença entre o custo-base da Classe e o que se paga ao usar o feitiço.','Dar referente claro à remissão.')
n='60-montar-habilidades-de-inimigos.md'
edit(n,'**Para ler depois de [PE, recarga e limites de uso]','**Leia depois de [PE, recarga e limites de uso]','Abertura em voz direta, mantendo o link.')
edit(n,'Trançar placas, a proteção proposta no ensaio anterior.','Trançar placas, a proteção proposta no exemplo anterior.','Mesmo nome de remissão no quadro e na explicação.')
edit(n,'## Defina o tipo de ação','## Tipo de capacidade','O trecho distingue feitiço, manobra e aptidão; não Padrão, Bônus e Reação.')
edit(n,'**Classe de Dificuldade (CD), 8 + 3 + 1 = 12**','**Classe de Dificuldade (CD)**, calculada como **8 + 3 + 1 = 12**','Separar o nome da CD de sua conta; fórmula curta pode permanecer inteira.')
edit(n,'Conferir o texto e as contas prepara a habilidade para um teste em mesa. Só o uso em jogo permite avaliar sua clareza e seu equilíbrio. Apresente-a como experimental enquanto esses testes não forem feitos.','A conferência de texto e contas prepara a habilidade para a mesa. Testes em jogo ainda são necessários para observar sua clareza e seu equilíbrio em uso. Mantenha a identificação de experimental enquanto esses testes não forem feitos.','Distinguir revisão documental de observação em jogo sem negar a utilidade da revisão.')
n='74-regua-inicial-de-inimigos.md'
edit(n,'Use esta seção para montar os primeiros valores da ficha e reconhecer o que precisa de revisão.','Use esta seção para montar os primeiros valores da ficha e reconhecer o que precisa de revisão. Aqui, **PV** significa pontos de vida.','Definir a sigla antes das tabelas.')
edit(n,'Reduzir ambos a uma coluna de vida apagaria suas diferenças.','Comparar os dois apenas pela vida apagaria suas diferenças.','Não tratar vida como descrição completa do inimigo.')
edit(n,'não devem ser interpolados como escala aprovada.','não formam uma escala aprovada para calcular os níveis ausentes.','Trocar interpolados por uma explicação direta.')
edit(n,'A terceira pode orientar uma aplicação de nível 6; não importa automaticamente os dois ataques ou o restante da ficha do Sineiro.','A terceira pode orientar um golpe de nível 6; ela não concede os dois ataques nem as outras capacidades do Sineiro.','Nomear golpe e concessão em vez de importação de dados.')
edit(n,'Para uma criatura adquirível, prepare separadamente a ficha de entidade e seus custos','Se o grupo puder adquirir a criatura como entidade, prepare sua ficha e seus custos separadamente','Trocar adquirível por condição concreta.')
n='100-comparar-inimigos-em-outras-faixas.md'
edit(n,'| Vivo após dois conjuntos | Dano médio: misto | Vivo após dois conjuntos |','| PV positivos após dois conjuntos | Dano médio: misto | PV positivos após dois conjuntos |','A tabela mede vida positiva, não confirma morte ou duração do combate.')
edit(n,'## Use as comparações para preparar o encontro','## Levar os resultados à mesa','Título curto para o uso dos resultados.')
n='67-preparar-chefes-e-confrontos-maiores.md'
edit(n,'Em campanha fechada, inclua o desgaste anterior.','Em qualquer campanha, inclua o desgaste anterior.','O desgaste anterior também importa na guilda.')
edit(n,'Ao oferecer partes atacáveis, indique se são criaturas, objetos separados ou alvos de uma regra específica.','Se o grupo puder atacar partes do inimigo, diga se cada parte é uma criatura, um objeto separado ou um alvo com regra própria.','Explicar o que partes atacáveis exige definir.')
(A/'alteracoes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2)+'\n');print({'registros':len(changes)})
