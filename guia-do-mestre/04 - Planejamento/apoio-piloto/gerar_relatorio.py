"""Escreve a leitura editorial dos resultados efetivamente concluídos."""
from pathlib import Path
import json,hashlib

HERE=Path(__file__).resolve().parent
data=json.loads((HERE/'base-inimigos.json').read_text())
result=json.loads((HERE/'resultado-validacao.json').read_text())
example=json.loads((HERE/'resultado-exemplo-guiado.json').read_text())
assert result['completo'] and example['conferido']
assert result['base_sha256']==hashlib.sha256((HERE/'base-inimigos.json').read_bytes()).hexdigest()
assert result['modelo_sha256']==hashlib.sha256((HERE/'validar_base.py').read_bytes()).hexdigest()
assert result['r53_sha256']==hashlib.sha256(Path(data['referencia']).read_bytes()).hexdigest()
def pct(x): return f'{x*100:.2f}'.replace('.',',')+'%'
def number(x): return str(int(x)) if x==int(x) else str(x).replace('.',',')
names={'rastejante':'Rastejante, trio','amontoado':'Amontoado, trio','vigia':'Vigia, trio','dois_rastejantes':'Dois Rastejantes, trio','amontoado_dupla':'Amontoado, dupla','amontoado_desgastado':'Amontoado, trio desgastado','amontoado_e_rastejante':'Amontoado e Rastejante, trio','amontoado_com_alma':'Amontoado, trio com Alma'}
total=sum(x['n'] for x in result['resultados'])
out=[f'''# Verificação da base pequena e do piloto

21 de outubro de 2026. A [base de três inimigos](14-base-pequena-de-inimigos-r53.md) foi conferida com a R53 e submetida a um ensaio restrito de confronto. O [piloto completo](13-piloto-editorial-ocorrencia-sobrenatural.md) pode ser avaliado e usado experimentalmente. A atualização integral do Bestiário permanece para depois.

**Resultado de trabalho:** manter um Amontoado isolado como introdução para três personagens de nível 2, com recursos disponíveis e sem Sequelas. Ele costuma ser neutralizado rapidamente pelos perfis usados, mas seus ataques ainda podem provocar quedas. Dupla, desgaste e inimigo adicional alteram bastante o risco; não são substituições automáticas. Os valores novos continuam candidatos desta base, sem pretensão de estabelecer uma escala geral de dificuldade.

## Base e método

Foram concluídas **{len(result['checagens'])} checagens de cálculos e estados**, **{total:,} confrontos abreviados simulados** e uma conferência separada do roteiro fixo de três rodadas. As simulações têm oito configurações, duas políticas de queda e duas políticas de defesa: 32 casos com 5.000 execuções cada. Não houve teste de mesa ou leitura com público externo.

O texto de referência é o [Livro do Jogador R53 editável](</home/mizuki/CHAT-GPT/RPG -JJK/entregas/livro-diagramado-r53/LIVRO-COMPLETO.md>). As fichas novas estão em uma fonte única; não foram calculadas a partir do Bestiário antigo. Os registros guardam a identificação dos arquivos usados, a semente de reprodução e os resultados completos.

## Referências de personagens usadas nas contas

São perfis parciais de cálculo, que deixam capacidades de fora; não substituem personagens completos nem medem todas as montagens possíveis dos Caminhos.

| Referência | Força Destreza Constituição Inteligência Essência | PV | PE | Defesa |
|---|---|---|---|---|
''']
for p in data['players']:
    out.append(f"| {p['nome']} | {' / '.join(str(x) for x in p['atributos'].values())} | {p['pv']} | {p['pe']} | {p['defesa']} |\n")
out.append('''
A vida é calculada pelo Caminho, com Constituição nos dois níveis. A Defesa usa Traje 1 e Destreza 2. Integridade de jogador usa a fórmula própria, **20 + (Essência + 5) × (nível − 1)**; não a metade da vida dos inimigos. As reservas de energia seguem os máximos dos Caminhos, antes de benefícios específicos.

As aplicações ofensivas têm Classe 1, 3 PE e 3d8: Toque na frente, Projétil nos outros dois. São montagens sem Melhorias ou Restrições, saldo 3. A frente usa Força; a referência Emanador usa Inteligência; a Guia usa Essência. Ataque +4. Os danos usados são Concussão; a variação de sensibilidade a Alma substitui apenas o tipo da aplicação da conjuradora quando permitido por sua ficha. O perfil Guia também conhece cura individual: Classe 1, 3 PE, Amparo disponível, base Média 1, saldo 2, **2d8**, alcance 9 m.

Para a demonstração, os Selos são uma palavra dita pela frente, encostar as palmas pela conjuradora e um gesto de mão pelo apoio. A frente mantém uma mão livre para Toque e a espada longa na outra. A técnica do apoio permite comprimir para ferir e sustentar para curar, com Amparo e Alcance Livres; a conjuradora usa Mira e Alcance Livres; a frente, Mira e Castigo. Não há desconto necessário nas montagens usadas. As outras escolhas de criação não foram preenchidas: são referências parciais, como indica o roteiro.

As três referências têm energia amaldiçoada e Refino 1. Canalizar Energia permite que os ataques mundanos e desarmados firam maldições sem custo separado e acrescenta 1d4 por Canalizar em Golpe. Sem PE para conjurar, a frente usa espada longa: +4, 1d8 + 3 + 1d4. Os outros dois usam ataque desarmado: +1, 2d4, sendo um dado básico e um adicional. No crítico, somente o dado básico dobra; Canalizar não acompanha feitiços. A composição de dois personagens conserva frente e apoio. Todos dispõem de meios de atendimento; o Guia usa Medicina +3. O teste é o de Estabilizar da R53, com alvo Inconsciente e Morrendo, Padrão, alcance 1,5 m, mão livre e meios adequados.

São usados os valores de Caminho e o efeito ofensivo gratuito de Canalizar Energia, mas não as outras capacidades de Origem, Caminho, Trilha ou Aptidões. A reação paga de Cobrir-se de Energia não é usada. Por isso, estes resultados não classificam o desempenho de Bastião, Guia ou Emanador completos. Também não medem Evocador, Vanguarda, Incursor, todas as técnicas livres ou diferentes equipamentos.

## Condições do confronto simulado

- Iniciativa rolada uma vez por confronto, com Destreza e desempates da R53. Um turno por participante e Reação renovada no próprio turno.
- As duas políticas de defesa são manter a Defesa estática ou escolher Bloquear em todo ataque em que seja possível. A segunda inclui Aparar, Brecha e os revides físicos pagos por Reação.
- Nas políticas de queda, a pessoa sempre escolhe Aguentar ou sempre escolhe Insistir. O apoio prioriza cura de quem ainda está Morrendo; sem PE, tenta estabilizar outra pessoa, que passa a Aguentar quando necessário. Estável e sem cura disponível, o apoio volta ao ataque. Isso é uma política do ensaio, não a melhor decisão em toda mesa.
- Aliados concentram ataques num inimigo por vez. O inimigo prioriza a frente consciente; troca de alvo quando ela Aguenta ou fica Derrotada. Não golpeia inconscientes. O Amontoado tenta suas conjurações antes da Pancada. As duas escolhas de queda mudam também quem continua sendo alvo dessa conduta.
- Todos começam em situação de alcance viável; a linha de visão é livre. Os ataques pessoais de Toque e os revides são a 1,5 m; os disparos são a 6 m. Aproximação, retomada de alcance e acesso para atendimento são concedidos ao modelo. Não há obstáculos, contenção ou oportunidade por retirada nesse ensaio.
- Sem vida temporária, resistência, Redução de Dano, domínio, surpresa, invocações ou recursos adicionais. Há crítico e gasto de PE; dano de Alma inclui perda de Integridade e seus estágios. O caso desgastado começa com metade dos PV, para baixo, duas Sequelas e PE disponíveis.
- A execução para ao neutralizar todos os inimigos ou quando não há personagem consciente capaz de continuar. Pessoas inconscientes podem ainda estar Morrendo e recuperáveis: esse resultado não significa morte nem necessariamente todos Derrotados. Casos que passam de 20 rodadas são separados como não resolvidos no limite.

Essas simplificações isolam a interação entre dano, recursos e queda. Não reproduzem o mapa inteiro, improviso, informação dos jogadores, proteção completa do Bastião, Aberturas do Guia ou uma missão com vários encontros. Os números não são uma garantia nem uma estimativa precisa do risco de uma mesa real.

## Probabilidades exatas

Um ataque +4 contra Defesa 13 acerta em **60%** dos d20; contra Defesa 11, em **70%**. O crítico natural continua em 5% nos ataques normais deste exemplo. Contra Bloquear, incluindo duplo 10, duplo 1 e a prevalência de 20 natural, essas chances iniciais são **59,85%** e **69,30%**, respectivamente. Revides têm contas e requisitos próprios; essa pequena diferença inicial não resume o valor da escolha de defesa.

Uma cura de 2d8 consegue atingir, numa aplicação e sem impedimentos:

| Tratamento exigido para máximo 23 | Chance exata de 2d8 bastar |
|---|---|
''')
for threshold,label in ((6,'Aguentar: 6'),(8,'Primeiro Insistir: 8'),(12,'Segundo Insistir: 12')):
    out.append(f"| {label} | {pct(example['chance_exata_2d8_atingir'][str(threshold)])} |\n")
out.append('''
São contas sobre uma única cura e um máximo de referência específico. Curas válidas podem acumular, mas o prazo não se renova por uma cura insuficiente. O custo do segundo socorro importa mesmo quando a vida máxima não mudou.

## Resultados com Insistir e Defesa estática

“Rodadas” é a mediana, contando a rodada em que o confronto termina. A faixa P10–P90 contém os percentis 10 e 90, sem prometer um mínimo ou máximo. “Queda” é pelo menos um jogador chegar a zero de vida; “Derrotado” é pelo menos um encerrar sua participação pelo procedimento. “Neutralização” mede apenas todos os inimigos derrotados, sem garantir que todos os jogadores estejam socorridos.

| Caso | Rodadas e P10–P90 | Alguma queda | Algum Derrotado | Neutralização e intervalo de 95% |
|---|---|---|---|---|
''')
for r in result['resultados']:
    if r['politica']=='Insistir' and not r['bloquear']:
        interval=f"{pct(r['ic95'][0])}–{pct(r['ic95'][1])}"
        out.append(f"| {names[r['caso']]} | {number(r['mediana_rodadas'])}; {r['p10_rodadas']}–{r['p90_rodadas']} | {pct(r['alguma_queda'])} | {pct(r['algum_derrotado'])} | {pct(r['neutralizacao'])}; {interval} |\n")
out.append('''
Os intervalos usam Wilson, com 5.000 execuções por caso, e expressam apenas a variação da amostragem deste modelo. Não incluem a incerteza das simplificações. Resultado observado de 100% não é impossibilidade de falha. Os [resultados completos](apoio-piloto/resultado-validacao.json) incluem os casos com Bloquear e Aguentar e os limites não resolvidos.

## O efeito das escolhas de queda

| Caso com Defesa estática | Escolha fixa | Mediana de rodadas | Algum Derrotado | Morrendo no encerramento |
|---|---|---|---|---|
''')
for r in result['resultados']:
    if r['caso'] in ('amontoado','amontoado_dupla','amontoado_desgastado') and not r['bloquear']:
        out.append(f"| {names[r['caso']]} | {r['politica']} | {number(r['mediana_rodadas'])} | {pct(r['algum_derrotado'])} | {pct(r['morrendo_ao_encerrar'])} |\n")
out.append('''
O mesmo valor de mediana pode ocultar ações durante Insistir, mais socorros ou personagens ainda Morrendo ao neutralizar o inimigo. A escolha não torna todos os encontros mais longos nem sempre reduz o risco. Com a política de alvo usada, quem Insiste continua consciente e pode continuar exposto. Quem Aguenta deixa de agir e deixa de ser escolhido por esses inimigos. Outros comportamentos podem mudar bastante os resultados.

## Por que estes valores foram escolhidos

O Rastejante tem 12 PV, menos que o dano médio de um acerto de 3d8, 13,5. O Vigia tem 24 PV e uma ameaça inicial à distância, mas se esgota e é frágil quando alcançado. O Amontoado tem 48 PV, entre os danos médios de três e quatro acertos de 3d8, 40,5 e 54. Isso permite alguma resistência aos três personagens sem multiplicar suas ações. O acerto, o crítico, a cura e as escolhas fazem a duração variar.

A reserva de 6 PE permite dois ataques concentrados pelo custo normal; depois, resta a Pancada. Isso dá ao mestre uma mudança de condução baseada em recursos conhecidos. A perda de Integridade pode aumentar o custo e reduzir esses usos. São escolhas para os exemplos, sem fórmula geral de vida ou energia de inimigo.

Os três perfis não são opções de compra pelo mesmo orçamento; não faz sentido declarar um vencedor universal ou atribuir o mesmo preço a eles. A comparação útil é sua função, quantidade de turnos, alcance, resistência e custo em recursos para aquele grupo. Dois Rastejantes e Amontoado com Rastejante foram ensaiados como encontros diferentes, sem supor equivalência por soma de níveis.

## Conferência do exemplo comentado

O roteiro fixo confirma duas quedas, tratamento 8 no primeiro Insistir, tratamento 12 no segundo, a janela reduzida pela Sequela e o consumo de uma rodada no ponto correto da iniciativa. No ramo principal, o estado final da frente é 12 PV, 2 PE e duas Sequelas. O apoio conserva 1 PE e a conjuradora 3 PE. O inimigo chega a zero.

No ramo alternativo, uma Pancada causa dano positivo à frente quando resta uma rodada. Ela fica Derrotada antes do socorro seguinte. Na campanha padrão, estando viva, os 7 de tratamento acumulado viram vida e a cura posterior de 5 a leva a 12 PV; sua participação continua encerrada naquela cena. Vida positiva não apaga Derrotado. O [registro desse roteiro](apoio-piloto/resultado-exemplo-guiado.json) separa os ramos.

A conferência também recalculou os exemplos publicados de tratamento com máximos 23, 93 e 395, o teto por Classe, o momento de expiração, o efeito de dano posterior, estabilização, fim de contagem após socorro e derrota por Integridade. Ela cobre os procedimentos usados aqui; não audita todas as tabelas ou combinações das 411 páginas da R53.

## Continuação recomendada

Revisar com Mizuki a clareza e o papel dos exemplos e recolher uma aplicação em mesa com as fichas reais. Registrar ações, recursos, socorros, retiradas e consultas demoradas. Se a missão for usada por dois personagens, com desgaste ou com uma composição muito diferente, reavaliar antes da sessão; os dados não sustentam tratá-la como a mesma introdução.

O piloto completo pode orientar essa revisão. Esta base não substitui o futuro procedimento geral de criação e avaliação de inimigos do Guia, nem atualiza o catálogo inteiro. A ampliação dependerá de faixas de nível, composições, técnicas, entidades e condições de missão que ainda não foram cobertas.
''')
(HERE.parent/'15-verificacao-da-base-e-do-piloto.md').write_text(''.join(out).replace(f'{total:,}',f'{total:,}'.replace(',','.')))
print('Relatório gerado somente a partir de verificações concluídas.')
