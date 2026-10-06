# Alterações de Aptidões e Refino

Candidata isolada. Nenhuma fonte publicada foi alterada. Mudanças mecânicas ficam identificadas para a revisão e para a sincronização autorizada do livro.

## A01 — apt-refino

**Tipo:** Editorial.

**Antes:** A abertura tratava vazamento e detecção a um quarteirão como universais.

**Depois:** A abertura apresenta treinamento e uso da ficha, distinguindo PE disponíveis de possuir energia.

**Motivo:** Evitar ensinar uma regra sensorial não comprovada e duplicar Sentir Energia.

**Fontes:** manual45: introdução/Refino; Regras Comuns: Sentir Energia.

## A02 — apt-marcos

**Tipo:** Esclarecimento.

**Antes:** O teto podia ser verificado antes do aumento básico do marco.

**Depois:** Aplicar primeiro o aumento básico; depois, resolver a escolha de Refino.

**Motivo:** Preservar as dez escolhas de aptidão da rota que sempre investe em Refino.

**Fontes:** peça11§3; conferir-aptidoes.py§5.2.

## A03 — apt-marcos

**Tipo:** Esclarecimento.

**Antes:** Compras encadeadas no mesmo marco não tinham ordem declarada.

**Depois:** Resolver as duas escolhas em ordem, exigindo o requisito quando cada uma for adquirida.

**Motivo:** Permitir uma compra válida sem usar um requisito que só viria de uma escolha futura.

**Fontes:** peça11§3/5.

## A04 — apt-catalogo

**Tipo:** Correção de divergência.

**Antes:** O índice chamava as melhorias de Kokusen de alternativas.

**Depois:** O catálogo contém quinze entradas; as duas melhorias de Kokusen funcionam juntas.

**Motivo:** A regra operacional e os 51% publicados com as duas melhorias demonstram que a exclusão era indevida.

**Fontes:** manual45§Catálogo; peça11§Kokusen Constante; conferir-aptidoes.py§11.

## A05 — apt-cobrir

**Tipo:** Esclarecimento.

**Antes:** A perda de proteção podia ser lida como exclusiva da aptidão.

**Depois:** Cobrir-se remove também a proteção de equipamento e escudo pelo prazo indicado.

**Motivo:** Preservar a decisão da v0.42, que impede usar equipamento para evitar o custo da Reação.

**Fontes:** peça11:285–297; R02 Defesa; R03 Redução de Dano.

## A06 — apt-canalizar

**Tipo:** Conciliação de fonte autoral.

**Antes:** A peça antiga começava em zero dados; o livro começava em 1d4.

**Depois:** Preservada a escala 1d4, 2d4, 3d4, 4d4 e 4d6, nas faixas publicadas no livro.

**Motivo:** O aumento inicial foi uma edição autoral expressa da v0.176, posterior à tabela matemática antiga.

**Fontes:** logs/CHANGELOG.md§0.176 tabela; manual45§Canalizar; manual47§Estímulo.

## A07 — apt-canalizar

**Tipo:** Esclarecimento.

**Antes:** Só arma parecia excluir o soco, embora os exemplos o incluíssem.

**Depois:** Canalizar beneficia ataques com arma e desarmados.

**Motivo:** O ataque desarmado conta como arma para essa regra; os Caminhos aprovados também usam essa interface.

**Fontes:** peça14§5.0.6; 35 Caminhos; peça11§6.9 exemplo soco.

## A08 — apt-canalizar

**Tipo:** Conciliação mecânica.

**Antes:** A prosa vedava Canalizar na rodada com conjuração; a caixa vedava apenas o mesmo ataque.

**Depois:** A exclusão vale para o ataque que transporta um feitiço de dano; outros ataques conservam suas regras.

**Motivo:** A versão aprovada de Contra a Parede explicita que o outro ataque continua normal. A vedação global contradizia essa decisão.

**Fontes:** manual35§Contra a Parede; caminhos/05-Edicao-Integrada/01-Bastião-Caminho-e-Trilhas.md; peça11§6.9.

## A09 — apt-canalizar

**Tipo:** Editorial.

**Antes:** Canalizar Energia, dano na arma e Canalizar em Golpe pareciam funções distintas.

**Depois:** Canalizar Energia é a aptidão; Canalizar em Golpe é seu dano adicional.

**Motivo:** Relacionar os termos existentes sem criar um novo benefício ou renomear habilidades aprovadas.

**Fontes:** PAUTA-DE-DECISOES.md N06; manual35 Incursor.

## A10 — apt-projetar

**Tipo:** Conciliação de fonte autoral.

**Antes:** A peça mantinha Projetar gratuito e fixo; o livro cobrava PE por d6 e ainda prometia funcionar sem PE.

**Depois:** Preservado o disparo pago, de 1 PE a Refino, com um d6 por PE.

**Motivo:** A regra paga pertence à revisão autoral da v0.176. A prosa gratuita era uma sobra da versão anterior.

**Fontes:** manual45:165; logs/CHANGELOG.md§0.176; peça11§Projetar.

## A11 — apt-projetar

**Tipo:** Mecânica: fechamento de lacuna.

**Antes:** Projetar não declarava ação, atributo, resolução ou alvo completos.

**Depois:** Ação Padrão, um alvo visível, ataque de conjuração habitual, alcance 18 ou 36 m e gasto antes da rolagem.

**Motivo:** Impor Essência criaria uma segunda exigência de atributo. Na comparação indicada, reduziria o acerto de 55% a 25%.

**Fontes:** R02 Ataques/Crítico; R06 Projétil alcance; manual45§Projetar.

## A12 — apt-projetar

**Tipo:** Sincronização.

**Antes:** Projetar não tinha um tipo de dano definido na entrada.

**Depois:** Projetar causa dano de Força.

**Motivo:** Sincronizar o pedido do usuário já aplicado em Dano e Condições, sem criar outro tipo chamado Energético.

**Fontes:** R03 DanoeCondições§Força.

## A13 — apt-reversa

**Tipo:** Sincronização.

**Antes:** Energia Reversa omitira a incompatibilidade de cura do Corpo Amaldiçoado.

**Depois:** O alvo próprio e a incompatibilidade ficam explícitos; reparos continuam com a Origem.

**Motivo:** Preservar a decisão da v0.318 sem transformar uma incompatibilidade de alvo em veto a aprender aptidões.

**Fontes:** peça09§Corpo Amaldiçoado; manual40§Cura; peça11§Energia Reversa.

## A14 — apt-energia-positiva

**Tipo:** Restauração e esclarecimento.

**Antes:** A exceção ofensiva de Cura desaparecera na candidata do Fundamento.

**Depois:** Forma Cura exige Energia Reversa, ataque contra Defesa e alvo maldição; converte os dados em dano com 50% adicional.

**Motivo:** Restaurar a regra publicada, impedindo dano automático e uso ofensivo contra pessoas.

**Fontes:** manual40:549–553; R03 tiposEspeciais; peça11§Ferir maldição.

## A15 — apt-energia-positiva

**Tipo:** Esclarecimento mecânico.

**Antes:** O uso ofensivo da aptidão fora de um feitiço só aparecia na peça de design.

**Depois:** Aptidão aplicada por contato exige uma permissão expressa de alcançar outra criatura.

**Motivo:** Não conceder cura externa gratuitamente nem criar uma aptidão nova a partir de um ponteiro órfão.

**Fontes:** peça11§Ferir maldição; manual43 referênciaúnicaórfã; R10 coordenação.

## A16 — apt-circulacao

**Tipo:** Esclarecimento.

**Antes:** A opção de Ação Bônus podia ser estendida à reconstrução de membro.

**Depois:** Reconstruir exige Ação Padrão e o teto de PE, sem recuperar vida nesse uso.

**Motivo:** A Ação Bônus foi precificada para cura em d4; reconstrução possui finalidade e custo próprios.

**Fontes:** peça11§Circulação e membro; manual45§Circulação.

## A17 — apt-kokusen

**Tipo:** Esclarecimento.

**Antes:** Melhor de dois d100 e contagem de falhas não explicavam todas as etapas.

**Depois:** Usa o menor resultado; uma tentativa falhada acrescenta +2, mesmo com dois dados. Sucesso não apaga o acumulado.

**Motivo:** A fonte só determina o descanso longo como encerramento desse bônus. A vantagem não duplica o número de tentativas.

**Fontes:** manual45 Kokusen; peça11§KokusenConstante/Melhorado.

## A18 — apt-protecao-dominios

**Tipo:** Mecânica: fechamento de lacuna.

**Antes:** A manutenção por rodada não tinha instante de cobrança nem encerramento operacional completo.

**Depois:** Cobrança na ativação e no começo de cada turno, com encerramento por falta de pagamento, decisão ou inconsciência.

**Motivo:** Evitar ativações gratuitas entre turnos e reproduzir os totais de 77 e 117 PE da Extensão.

**Fontes:** peça11§6.5 tabelas de custo; R01 durações; R08 coordenação.

## A19 — apt-cesta

**Tipo:** Esclarecimento.

**Antes:** Soltar e retomar o símbolo da Cesta não tinha tratamento completo.

**Depois:** Retomar não apaga falhas. Golpe que acerta exige teste, mesmo reduzido a zero; Acerto anulado pela Cesta não é golpe recebido.

**Motivo:** Preservar o gatilho de acerto sem permitir reiniciar a barreira gratuitamente.

**Fontes:** peça11§Cesta; R03 Acertoedano.

## A20 — apt-simples

**Tipo:** Mecânica: padronização de medidas.

**Antes:** O raio do Domínio Simples produzia medidas como 3,5 e 6,5 m.

**Depois:** A tabela usa o múltiplo de 1,5 m mais próximo do resultado antigo.

**Motivo:** Cumprir a diretriz de medidas do usuário, registrando também a mudança de área geométrica.

**Fontes:** manual45§DomínioSimples; pedido humano múltiplos1,5.

## A21 — apt-simples-duracao

**Tipo:** Esclarecimento.

**Antes:** Rodadas, Acertos e piso de duração podiam ser confundidos.

**Depois:** A capacidade total é comparada com o número de Acertos já impedidos; falhas reduzem capacidade, não restauram saldo.

**Motivo:** Reproduzir o modelo matemático publicado e impedir duração infinita por interpretação do piso.

**Fontes:** conta-dominio-simples.py função simples V; peça11§DomínioSimples.

## A22 — apt-simples-duracao

**Tipo:** Mecânica: fechamento de lacuna.

**Antes:** Não havia procedimento para mudar de Expansão durante a mesma ativação.

**Depois:** Um contador global por ativação; sair e voltar não o zera. Um novo adversário pode reduzir a capacidade, nunca aumentá-la.

**Motivo:** Fechar a renovação indevida por movimento e evitar cobrar várias vezes por um único Acerto que afete o grupo.

**Fontes:** R08 disputa de domínios; peça11§6.5.

## A23 — apt-cesta/apt-simples

**Tipo:** Mecânica: fechamento de lacuna.

**Antes:** As consequências de queda tratavam principalmente falhas e voto.

**Depois:** Encerramentos precoces da Cesta ou do Domínio Simples provocam o Acerto imediato. Esgotamento do contador do Simples deixa passar apenas o Acerto atual.

**Motivo:** Cancelar voluntariamente antes da queda não pode evitar a consequência. O mesmo Acerto não deve ser aplicado duas vezes.

**Fontes:** decisão v0.274 Acertoextra; R08 coordenação.

## A24 — apt-petala

**Tipo:** Mecânica: resolução simultânea.

**Antes:** Queda da Pétala e contra-ataque podiam competir pelo mesmo gatilho.

**Depois:** A Pétala precisa estar ativa no acerto. O golpe é resolvido primeiro; a queda da proteção não apaga a resposta já desencadeada.

**Motivo:** Preservar a função da habilidade, sem permitir agir depois de ficar incapaz de usar a Reação.

**Fontes:** manual45§Pétala; R02 Resolução.

## A25 — apt-barreira

**Tipo:** Mecânica.

**Antes:** Um minuto de preparação não especificava ações nem quantidade de barreiras simultâneas.

**Depois:** Dez turnos com Ação Padrão no ponto; uma Barreira Simples ou Cortina ativa por criador.

**Motivo:** Impedir reservas ilimitadas de PV por preparação, mantendo os valores de cada barreira.

**Fontes:** peça11§6.6; R01 rodada6segundos.

## A26 — apt-barreira

**Tipo:** Mecânica: fechamento de lacuna.

**Antes:** Barreiras tinham PV sem um procedimento para receber ataques ou TRs.

**Depois:** Ataques que alcançam a superfície acertam sem crítico; barreiras falham nos TRs de efeitos capazes de afetá-las.

**Motivo:** Evitar que cada mestre invente Defesa e testes, alinhando Anteparo e a barreira da Expansão.

**Fontes:** R07 Anteparo; R08 barreira; R02 ataque.

## A27 — apt-cortina

**Tipo:** Conciliação + mudança mecânica.

**Antes:** Cortina tinha 20 vezes Refino no dono antigo, 40 no livro e área sem teto.

**Depois:** Preservados 40 vezes Refino de PV; o local escolhido deve caber a até 90 m do ponto de conclusão.

**Motivo:** O aumento de PV veio do usuário na v0.176. O limite territorial impede tratar uma cidade ou país como um único local gratuito.

**Fontes:** logs/CHANGELOG.md§0.176; manual45§Cortina.

## A28 — apt-cortina

**Tipo:** Esclarecimento mecânico.

**Antes:** A Cortina podia ser interpretada como uma Barreira Simples com oito vezes mais vida.

**Depois:** Ela regula passagem de criaturas e ocultação visual; não herda a vedação completa de ataques.

**Motivo:** Preservar funções distintas e tornar seu custo de oportunidade real.

**Fontes:** peça11§Cortina tabela de condições; RegrasComuns barreiras/sinais.

## A29 — apt-propria

**Tipo:** Mecânica/editorial.

**Antes:** Frequência e permanência determinavam a Classe sozinhas; a rerrolagem de exemplo não tinha ação.

**Depois:** A comparação considera magnitude, ação, alvos e alcance. A rerrolagem exige Reação e conserva o segundo resultado.

**Motivo:** Alinhar a criação própria com R07 e fechar um benefício antes incompleto, sem proclamar que todo efeito permanente é Classe 3.

**Fontes:** R07 PassivaPrópria; manual45 AptidãoPrópria.


## A30 — Passagem da rota sem energia

A vedação de Barreira Simples e Cortina conserva a exceção da Origem para personagens sem energia. Objetos carregados seguem os requisitos da Origem. Isso não permite atravessar estruturas físicas nem estende a exceção a Anteparo. Sincronização pedida na revisão cruzada de R10, sem alterar o capítulo de Origem.

## A31 — Critério de dano e raio

Troca editorial: “Acerto letal” por “Acerto que causa dano” e explicitação de que o raio protegido é o do Domínio Simples. Não altera custos ou frequência.

## A32 — Ritual no índice de aptidões

O índice agora inclui Ritual com seus requisitos e referência ao capítulo próprio. A regra completa não foi reproduzida.

## A33 — retirada a pedido do autor

**Antes:** | Nível | Nunca escolhe Refino | Sempre escolhe Refino | Aptidões recebidas pela escolha nesse marco |
|---|---:|---:|---:|
| Início | 1 | 1 | — |
| 6 | 2 | 3 | 1 |
| 10 | 3 | 5 | 1 |
| 14 | 4 | 7 | 1 |
| 18 | 5 | 9 | 1 |
| 22 | 6 | 10 | 2 |
| 26 | 7 | 10 | 2 |
| 30 | 8 | 10 | 2 |

A última coluna acompanha quem sempre escolheu Refino. Em outra sequência, verifique seu valor naquele marco.

**Depois:** (retirado)

**Motivo:** Pedido do autor (04/10/2026): retirar do livro do jogador projeções de projetista (tempo de campanha, como o personagem termina seguindo sempre a mesma escolha). A regra do marco fica.

## A34 — decisão do autor

**Antes:** A Expansão incompleta não tem Acerto garantido. Cesta, Domínio Simples e a proteção de Pétala contra Acerto não a anulam. Extensão declara a própria exceção. As capacidades descritas aqui são regras do Projeto - M para representar essas defesas.

**Depois:** A Expansão incompleta não tem Acerto garantido. Cesta, Domínio Simples e a proteção de Pétala contra Acerto não a anulam. Extensão declara a própria exceção. As capacidades descritas aqui são regras do Ciclo Maldito para representar essas defesas.

**Motivo:** Decisão do Mizuki em 05/10/2026, depois de mandar o livro final (Ciclo Maldito R28a): o sistema se chama Ciclo Maldito no repositório inteiro, e a candidata acompanha o nome do livro publicado. Só o nome muda; nenhuma regra muda.
