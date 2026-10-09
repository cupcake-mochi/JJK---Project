# Inventário da revisão do R41

*Passo 5a do `PLANO.md`. Feito em 09/10/2026, na v0.342. Revisão por modelo, não humana.*

Uma linha por decisão que mudou o livro na revisão de 07 a 09/10, dizendo o que ela pede das peças. As decisões estão em `../../ciclo-maldito-r41/revisao-de-regras/MUDANCAS-DE-REGRA.md` (seções A e B) e no `DECISOES-MIZUKI.md` da mesma pasta. O que o Mizuki mandou manter da reconstrução não está aqui: segue a migração normal de cada capítulo.

## O que já foi feito

- **v0.343:** itens 156, 157, 158 e a regra de não acumular (peças 19 e 14), 160 (peças 11 e 14), 171 (peça 16) e o cabeçalho da peça 15 (itens 16, 19 e 20). Conferidos pela sub-checagem 10.9 do `conferir-repositorio.py` e pela checagem 11 do `conferir-dano.py`.
- **v0.344:** as Bênçãos `Represália` e `Sangue Frio` (itens 180 a 185), na peça 11 §6.8, com a conta dos gates refeita. Conferidas pela sub-checagem 9.1 do `conferir-aptidoes.py`.
- **v0.345:** itens 113 (peça 13), 118 e 119 (peça 12). Conferidos pela mesma sub-checagem 10.9, que passou a cobrir nove regras.
- **v0.346:** a fonte dos validadores passou da candidata para o R41. **As 22 linhas `livro` passaram a ter o dono certo:** *o livro que os validadores leem já traz a regra decidida.* Isso não quer dizer que cada uma tem checagem própria; os validadores conferem o que já conferiam (o Catálogo entrada por entrada, as condições, e as frases que cada um cobra).
- **v0.347:** o capítulo de Dano sem o Morrendo (tipos de dano e exaustão; nenhuma linha deste inventário, porque as duas divergências eram anteriores à revisão).
- **v0.348:** o capítulo de Regras gerais (só lacunas; nenhuma linha deste inventário além do 158, que já tinha ido na v0.343).
- **v0.349:** o capítulo de Poderes avançados. **Correção deste inventário:** *as dez linhas `capítulo` da Expansão (1, 2, 3, 4, 5, 8, 11, 13, 152 e 153) são do tipo `livro`. A Expansão não tem peça; o dono era o manual v7 e hoje é o R41.* As decisões passaram a ser cobradas pela sub-checagem 12.7 do `conferir-expansao.py`, como frase do livro.
- **v0.350:** o capítulo de Ritual e Pactos, com as seis linhas `capítulo` que sobravam (34 a 36, 37, 39, 42, 47 e 50), nas peças 22 e 27. **Correção deste inventário:** *quatro delas mudaram regra de peça, e não só texto (34 a 36, 37, 42 e 50); a tabela da seção abaixo diz o que cada uma mudou.* Conferidas pelos sub-blocos 7.2 do `conferir-ritual.py` e 14.1 do `conferir-pactos.py`, e pela checagem 4 deste último.
- **Falta dos casos `nova` e `desfaz`:** só o 115, que espera a resposta do Mizuki. **O passo 5b fechou.**

## Os casos

| caso | o que quer dizer | linhas |
|---|---|---:|
| `nada` | a peça já está no valor decidido | 6 |
| `desfaz` | um passo da migração já levou a mudança para a peça, e ela volta | 6 |
| `nova` | regra nova: a peça dona muda | 8 |
| `capítulo` | o capítulo ainda não migrou; entra com ele, já no valor decidido | 16 |
| `livro` | não tem peça dona; o dono é o livro que os validadores leem | 22 |
| `travado` | espera a revisão do Morrendo | 2 |
| `texto` | só redação; não é regra de peça | 3 |
| | **total** | **63** |

**A coluna "conferido" diz quanto vale cada linha.** *`lido` é a peça aberta na linha citada. `experimento` é o que acendeu com os validadores lendo o R41 (seção abaixo). `pelo estado do capítulo` é dedução: o capítulo não migrou, então a peça ainda está no texto da v0.331, e isso precisa ser lido quando o capítulo entrar. `grep, sem leitura` e `não conferido` são o que dizem, e o traço é linha sem peça para ler.* As linhas citadas são as da v0.341.

## Poderes avançados

Peça 11 (a parte da Expansão), `RASCUNHO-expansao-sem-barreira.md` e o `conferir-expansao.py`, que ainda lê o `partE.js` do gerador v7. Capítulo do passo 5b, não migrado.

| nº | decisão | caso | onde, e o que achei | conferido |
|---|---|---|---|---|
| 1 | Acerto de dano volta a ser montado como feitiço pela régua do Inescapável | `capítulo` | a peça nunca recebeu o valor fixo da candidata | pelo estado do capítulo |
| 2 | Aliados no Acerto: fica, com a frase de que poupar alguém depende do Efeito | `capítulo` | — | pelo estado do capítulo |
| 3 | Acerto da Incompleta volta a resolver por rolagem, em três casos | `capítulo` | — | pelo estado do capítulo |
| 4 | Acerto garantido não tem crítico e ignora Redução de Dano, resistência e imunidade | `capítulo` | — | pelo estado do capítulo |
| 5 | Regra de ambiente não vale contra o dono | `capítulo` | — | pelo estado do capítulo |
| 8 | Barreira: uma reserva de vida só; sai o dano por dentro dividido por quatro | `capítulo` | a regra que saiu era da candidata e não chegou à peça | pelo estado do capítulo |
| 11 | Rescaldo volta | `capítulo` | — | pelo estado do capítulo |
| 12 | Acerto ao perder a disputa: fica, sem a frase vetada | `texto` | — | — |
| 13 | Manter a disputa volta (jogador testa a cada dano; inimigo, uma vez por jogador) | `capítulo` | o `conferir-manual.py` (4m) cobra do livro a frase da candidata, "compare o mesmo total à nova CD", e acende quando ler o R41 | experimento |
| 14 | Passar no TR corta o resultado do dano pela metade, e não os dados | `livro` | a peça 27 cita "metade dos dados"; conferir se é o mesmo caso | grep, sem leitura |
| 152 | Três ou mais barreiras: instáveis, disputa em pares, intruso derruba | `capítulo` | regra nova do autor, de 07/10 | pelo estado do capítulo |
| 153 | Duas barreiras e uma aberta volta | `capítulo` | — | pelo estado do capítulo |

## Invocações

A peça 15 se declara registro histórico desde a v0.331, e o cabeçalho dela aponta o livro como dono (passo 4).

| nº | decisão | caso | onde, e o que achei | conferido |
|---|---|---|---|---|
| 16 | Domínio da domada segue a regra do jogador; sai o `d8` fixo | `desfaz` | cabeçalho da peça 15, linha 11: ainda diz que na candidata o Acerto "causa Classe `d8`" (R11-32) | lido |
| 17 | Comandar especial não ocupa a conjuração do turno | `livro` | — | — |
| 19 | Especial com a Melhoria Reação custa só a Reação coletiva | `desfaz` | cabeçalho da peça 15, linha 8 (R11-19): descreve o custo da candidata | lido |
| 20 | Atrasar e Carregar cobram só da entidade | `desfaz` | cabeçalho da peça 15, linha 8 (R11-45) | lido |
| 21 | Capacidade reativa: sai o mesmo pagador; a Contramedida custa 2 PE | `livro` | — | — |
| 23 | Talismã: sai a frase do retorno da caída | `livro` | — | — |
| 30 | Ficha convertida da domada: o mestre pode deixar o jogador montar | `livro` | — | — |
| 143 | Restrição em especial de entidade: a devolução não cobre a Forma | `livro` | — | — |

## Ritual e Pactos

Peças 22 e 27, `conferir-pactos.py` e `conferir-ritual.py`. Capítulo do passo 5b, migrado na v0.350.

| nº | decisão | caso | onde, e o que achei | conferido |
|---|---|---|---|---|
| 34–36 | Pacto permanente volta: nunca valor numérico, e sim mecânica única | `capítulo` | **feito na v0.350.** A peça 22 §3.3 dava PE, aptidão ou espaço de feitiço e o §3.4 deixava o dano como escolha ruim; passaram a "modifica feitiço, energia, aptidão ou Estilo", "não existe pacto por dano" e pacto de energia em porcentagem | lido |
| 37 | Limite de pactos conta permanente, Promessa e restrição; a vaga volta quando o pacto se perde | `capítulo` | **feito na v0.350.** Regra nova na peça 22 §1, §1.1, §3.1 e §6: só o permanente contava, e para a campanha inteira | lido |
| 39 | Consentimento e quebra voltam; a punição pode ser definida na criação | `capítulo` | **feito na v0.350.** A peça 22 §2 e §5.3 já tinham o texto antigo; entrou a frase da punição | lido |
| 42 | Falhar o Ritual volta para o conjurador; o auxiliar perde a Classe em PE | `capítulo` | **feito na v0.350.** A peça 27 §3.2 ganhou a unidade (dados de dano, sem PE a mais) e o §6 a perda do auxiliar | lido |
| 47 | Ritual de Rerrolagem volta | `capítulo` | **feito na v0.350.** A peça 27 já estava no texto antigo; entrou "fica o segundo resultado" | lido |
| 50 | Ritual em dupla: sem limite de auxiliares, Ação Padrão, +2 por auxiliar | `capítulo` | **feito na v0.350.** Regra nova na peça 27 §6: era Ação Completa e 4 pontos | lido |

## Fundamento e Catálogo

Não têm peça dona desde a v0.337: o dono era o `.docx` e passou a ser o livro, que os validadores leem pelo `03-mecanica/livro.py`. Hoje esse livro é a candidata.

| nº | decisão | caso | onde, e o que achei | conferido |
|---|---|---|---|---|
| 51 | Certeiro volta (sem rolagem; TR para metade); sai a linha "Meio Acerto e Certeiro" | `livro` | — | — |
| 53 | Fica volta, com o limite de uma aplicação por criatura por rodada | `livro` | — | — |
| 56 | Empurrão volta, sem o limite de um alvo | `livro` | — | — |
| 57 | Troca sai do Catálogo | `livro` | aparece no experimento: o Catálogo lido do R41 tem uma Melhoria a menos | experimento |
| 63 | Classe 0 volta a aceitar uma Melhoria Leve e uma Restrição Leve; vale para a básica das entidades | `livro` | — | — |
| 65 | Técnica Máxima volta a aceitar Quebra Coisa | `livro` | — | — |
| 66 e 149 | Efeito Próprio e Aptidão Própria: quem define o preço é o mestre | `livro` | a peça 11 §6.7 guarda a escada antiga da Aptidão Própria; conferir junto | grep, sem leitura |
| 67 | Duas Melhorias escritas como uma: o mestre pode aprovar por menos | `livro` | o `conferir-manual.py` (4o) cobra do livro a frase contrária, da candidata, e acende quando ler o R41 | experimento |
| 70 | De Novo passa a Pesada, uma rerrolagem a cada uso | `livro` | aparece no experimento; a checagem 12 do `conferir-repositorio.py` compara o degrau com o livro v0.331 e vai acusar | experimento |
| 71 | Levanta: uma vez por cena, um aliado | `livro` | — | — |
| 75 | Segura e Armado voltam | `livro` | — | — |
| 79 | Assinatura mostra quem fez e onde você está | `livro` | — | — |
| 80 | Regra Própria e Talento Próprio: campos ficam, criação livre com o mestre | `texto` | — | — |
| 85 | Perseguir segue teleporte dentro da cena | `livro` | — | — |
| 86 | Desarma o Feitiço: cancela direto se a Classe for igual ou menor; senão, rolagem | `livro` | — | — |
| 141 | Técnica Máxima: uma vez por cena, ou de novo depois de 3 rodadas com o mestre | `livro` | — | — |
| 143 | Devolução de Restrição nunca passa do gasto em Melhorias; a Forma não entra | `livro` | o `conferir-orcamento.py` é o validador do orçamento; conferir se ele supõe a regra da candidata | não conferido |

## Dano e recuperação

Peça 01 §5.5 e as remissões das peças 12, 15, 20 e 24. Travado pela revisão do Morrendo.

| nº | decisão | caso | onde, e o que achei | conferido |
|---|---|---|---|---|
| 94 | Cicatriz: o jogador escolhe se ela dá a vantagem e a desvantagem | `travado` | — | — |
| 96 | Insistir não custa Ação Padrão (resposta final dele, em 08/10) | `travado` | o `MUDANCAS-DE-REGRA.md` ainda traz a redação anterior, com o custo; o `DECISOES-MIZUKI.md`, Leva 17, tem a final | lido |

## Origens, Progressão e Criação

Peças 09, 12, 13 e 18. Progressão migrou no passo 5 (v0.337) e Origens no 5b (v0.340).

| nº | decisão | caso | onde, e o que achei | conferido |
|---|---|---|---|---|
| 113 | Sangue que Não é Sangue volta, sem a necessidade corporal | `desfaz` | peça 13: a entrada (linha 911) e o registro da migração (linha 1169), da v0.340; conferir o `conferir-legados.py` | lido |
| 115 | Legado personalizado sem o limite de um | `nova` | peça 13 §6 ("Um Legado Próprio por ficha", desde a v0.39) e linha 1171 (v0.340). **A trava é da peça e é mais velha que a candidata; o livro v0.331 não a trazia.** Confirmar com o Mizuki antes de tirar. | lido |
| 118 | XP guardado no limiar vira, de uma vez, quantos níveis pagar | `desfaz` | peça 12, linha 476 (PRO04, v0.337): "não paga dois níveis de uma vez". O §7 da mesma peça já dizia "destrava de uma vez". | lido |
| 119 | Subir de nível: com o mestre, pode recuperar tudo | `nova` | peça 12, uma frase | pelo estado da peça |
| 120 | Troca de Trilha: fica, deixando claro que substitui tudo | `nada` | a peça 06 já tem a troca (PRO20, v0.335) | pelo registro do passo 4 |
| 147 | Rolar a vida como variante | `nada` | peça 01, linha 202, já traz a variante | lido |
| 177 | Vida inicial da Vanguarda, 8 + Constituição | `nada` | peça 06: vida por nível 5, do d8; faltava só no livro | lido |

## Equipamento, Aptidões e Bênçãos

Peças 11, 14, 16 e 19. Equipamento migrou no passo 4 (v0.335) e Aptidões e Rotas no 5b (v0.340).

| nº | decisão | caso | onde, e o que achei | conferido |
|---|---|---|---|---|
| 156 | Arma sem a Força exigida: desvantagem nos ataques e deslocamento pela metade; não tira mais a Destreza da Defesa | `nova` | peça 19 §6 (linha 488), peça 14 (linhas 10, 1389 e 1431) e o `conferir-dano.py` (linha 1145), que cobra a frase antiga | lido |
| 157 | Traje, Revestimento ou escudo sem a Força: veste e protege, com deslocamento pela metade e desvantagem em TR Físico | `nova` | peça 14, linhas 1800 e 1801 ("não pode ser preparada", v0.335) | lido |
| 158 | Carga acima do limite, até o dobro: a mesma penalidade | `nova` | peça 14, linha 1689 ("é um muro") e linha 1702 (v0.335) | lido |
| 157/158 | As três penalidades não acumulam | `nova` | entra junto das três | — |
| 160 | A Reação de Cobrir-se e a de Defesa sem Armadura tiram só a proteção passiva | `nova` | peça 11 (linhas 290 e 1188) e peça 14 (linha 1839, a decisão da v0.42 que esta desfaz); conferir o `conferir-aptidoes.py` | lido |
| 171 | Insondável volta a alcançar na cena, na ordem de 100 m | `desfaz` | peça 16, linhas 364, 377 e 393 (`18 m`, v0.335) | lido |
| 180 a 185 | Bênçãos novas, `Represália` e `Sangue Frio`, na forma final do R41 | `nova` | peça 11, na tabela das Bênçãos (por volta da linha 1100); sem teste de mesa | lido |
| 179 | Frase do PE a zero em Sentir Energia | `texto` | — | — |

## Seção B do documento

Decisões anteriores à revisão, que faltavam no R28a.

| nº | decisão | caso | onde, e o que achei | conferido |
|---|---|---|---|---|
| D43 | Condição, Prende e Cerca sempre pedem TR | `nada` | nas peças e na candidata desde `65afa3c` | pelo histórico |
| D44 | Execução Preparada impõe −2 | `nada` | peça 06, v0.336 | pelo histórico |
| Projetar | Projetar Energia: 1 PE até metade do refino, 2d6 por PE | `nada` | peça 11, v0.340; a candidata ainda tem o antigo | pelo histórico |

## O experimento: os validadores lendo o R41

*Feito numa cópia isolada, fora do repositório.* O `LIVRO-COMPLETO.md` do R41 guarda os mesmos identificadores de página dos manuscritos da candidata, agora como âncora de bloco (`catalogo--cat-alcance` no lugar de `<!-- page:cat-alcance|… -->`), e os títulos dois níveis abaixo. Com uma função de umas trinta linhas no `livro.py`, que remonta cada unidade a partir das âncoras, os 27 validadores rodaram contra o R41.

**22 passaram sem mudança nenhuma. 5 reprovaram**, por dois motivos diferentes:

- **Forma do texto, e não regra.** O `conferir-dano.py` e o `conferir-nomes.py` não acham o título `Condições leves` no nível que esperam (a diagramação nova o desceu um nível); o `conferir-acao.py` e o `conferir-manual.py` não leem `Concentrada` e `Duradoura`, que passaram a dividir um título; o `conferir-ritual.py` não lê os Pontos, o Teto e a Liberação Máxima do Fundamento, e o `conferir-dano.py` não acha a frase do `Calado`. *Nesses dois não fui atrás da causa: pode ser forma ou pode ser regra.*
- **Regra decidida na revisão.** O `conferir-manual.py` cobra do livro duas frases da candidata que a revisão tirou: a do combo de Melhorias (item 67) e a de manter a disputa de domínios (item 13).

**Lido direto, o Catálogo do R41 difere do da candidata em duas coisas, e as duas são decisão:** `Troca` saiu (item 57) e `De Novo` passou de Média para Pesada (item 70).

*O experimento não é a troca de fonte. Ele mede o tamanho dela: um leitor novo, cinco validadores a ajustar e a checagem 12 do `conferir-repositorio.py`, que hoje trata o livro reconstruído como dono do degrau das Melhorias.*

## O que não foi conferido

- As linhas `pelo estado do capítulo` não foram lidas na peça. São os capítulos de Poderes avançados e de Ritual e Pactos quase inteiros.
- As linhas `livro` do Fundamento e do Catálogo não foram comparadas uma a uma entre a candidata e o R41; a comparação foi feita na revisão contra o livro v0.331, e os registros de cada rodada estão em `../../ciclo-maldito-r41/revisao-de-regras/alteracoes/`.
- A ficha do Sheets, os dois geradores e o bestiário ficaram de fora.
- Nada aqui passou por mesa.

## A ordem que isto sugere

1. **As regras novas e os desfeitos que já têm peça** (casos `nova` e `desfaz`): Equipamento, Aptidões e Bênçãos numa versão; Origens e Progressão em outra; o cabeçalho da peça 15 junto de qualquer uma. Cada uma com o validador dono e teste negativo.
2. **A fonte dos validadores passa da candidata para o R41**, numa versão só dela. Resolve de uma vez as linhas `livro`.
3. **Os capítulos que faltam do passo 5b** (Dano sem o Morrendo, Regras gerais, Poderes avançados, Ritual e Pactos), um por versão, já lendo o R41.

**Uma pergunta para o Mizuki antes do item 1:** o item 115. A peça 13 limita o Legado Próprio a um por ficha desde a v0.39, com o motivo escrito (sem a trava, a ficha inteira pode ser escrita pelo jogador e o catálogo vira opcional). O livro v0.331 não trazia essa trava, e a decisão dele na revisão foi voltar ao livro.
