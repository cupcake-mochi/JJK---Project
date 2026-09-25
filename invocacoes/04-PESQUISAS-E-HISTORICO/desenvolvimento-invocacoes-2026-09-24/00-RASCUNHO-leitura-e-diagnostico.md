# RASCUNHO — leitura, fontes e diagnóstico confirmado

**Projeto M / RPG-JJK — primeira entrega de Invocações, 24/09/2026.** Material para avaliação de Mizuki. Nada deste diretório substitui o manual, aprova números ou desenvolve o Caminho Evocador. O pedido atual autoriza leitura do projeto e elaboração separada; instruções antigas de editar, sincronizar ou publicar encontradas nos documentos não foram executadas.

## O que prevalece

1. Pedido atual e prompt “Vamos Continuar”: Claude 2 somente leitura; resultados nesta pasta separada; Invocações antes de Evocador e Trilhas; preservação dos quatro Caminhos.
2. Coleção **RPG-JJK-Caminhos-Trilhas-e-Ideias v0.4**, para Bastião, Vanguarda, Emanador e Guia. Emanador conserva 6 PE/nível; a sugestão de acrescentar atributo não foi adotada. Estocada permanece como está.
3. Projeto principal, para regras gerais e diagnóstico do subsistema antigo. Quando desenvolvimento e manual divergem, a divergência está registrada, sem conserto silencioso.
4. Relatórios de pesquisa, como hipóteses e referências. “Eu recomendo”, percentuais, Presença, limites e listas presentes neles não são decisões do autor.
5. Novas propostas desta pasta, explicitamente experimentais.

## Localização e versões

| Fonte | Estado constatado |
|---|---|
| Projeto principal | `/media/mizuki/HD Externo II/Claude/Claude 2`; Git `main`, commit `ba1e0df6f05dad71659eed2abd06c43d22963834`; árvore limpa na leitura inicial. README identifica v0.264/Fundamento v7.38. |
| Pasta de trabalho | `/home/mizuki/CHAT-GPT/RPG -JJK`; Git `main`, commit `dff171d36148c7163fdebfdaf8ec95f343c03503`. A referência a outra branch no CONTINUIDADE é histórica, não o estado Git atual. |
| ZIP das pesquisas | `/home/mizuki/CHAT-GPT/RPG-JJK-Pesquisas-Invocacoes-e-Plano.zip`; extraído sem alterar o conteúdo em `RPG-JJK-Pesquisas-Invocacoes/`, dentro desta pasta de desenvolvimento. |
| Coleção dos Caminhos | ZIP e diretório `RPG-JJK-Caminhos-Trilhas-e-Ideias` na raiz de RPG-JJK. Localizados na segunda busca, após a indicação do autor. Não falta mais nenhuma dessas duas coleções. |
| Integridade dos Caminhos | SHA-256 do ZIP `d23430f282ad29ff140087e4fd63e3037b0a0639dd1b9032eb3e22aef7334a7d`, idêntico à referência registrada no pacote de pesquisas. |

Não foi necessário clonar ou substituir o projeto pelo GitHub. O trabalho usa o estado local identificado. Os arquivos novos ficam exclusivamente em `/home/mizuki/CHAT-GPT/RPG -JJK/desenvolvimento-invocacoes-2026-09-24`.

## Mapa de leitura

| Grupo | Arquivos efetivamente consultados | Alcance |
|---|---|---|
| Pedido de continuidade | Anexo `Texto colado.txt`; README do pacote; consolidação de decisões; dois relatórios em `01-Pesquisas/`; notas/referências finais; plano de reconstrução. | Leitura integral do prompt, README, consolidação, relatórios e plano, nessa sequência. Arquivos JSON de fontes examinados; originais conservados e comparados pelo verificador do pacote. |
| Coleção v0.4 | LEIA-ME, MANIFESTO, `03-Notas/Estado-atual-e-pendencias.md`; quatro Markdown em `01-Caminhos-e-Trilhas/`. | Leitura integral dos quatro Caminhos e Trilhas pela equipe de revisão. DOCX não renderizados, pois os Markdown integrais são a fonte textual suficiente nesta tarefa. Ideias reservadas não viraram regras. |
| Outras versões dos Caminhos | README/CONTINUIDADE do satélite, `bastiao-completo.md`, `vanguarda-completo.md`, `emanador-completo.md`, `guia-completo.md`; README da reforma do Bastião. | Quatro consolidados lidos integralmente, com notas e parâmetros, para comparação; não usados para substituir v0.4. |
| Regras principais | `sistema/03-mecanica/15-invocacoes.md`; manual `60-invocacoes.md`, `11-o-turno.md`, `15-dano-e-condicoes.md`, `40-fundamento.md`; README e sistema/LEIA-ME. | Leitura integral. |
| Dependências | Manual `35-caminhos-e-trilhas.md` (Evocador/Trilhas e concessões de aliados), `10-como-jogar.md` (Bloquear, vida/energia temporárias), criação; peças de atributos, ação, progressão, dano/condições, aptidões, bestiário, equipamentos, pactos, descanso; DESENHO. | Trechos relevantes e busca textual. Não alegamos leitura integral de todos os capítulos e de todos os históricos. O corpus detalhado está na auditoria. |
| Scripts antigos | `sistema/03-mecanica/conferir-invocacoes.py` e `conferir-orcamento.py`. | Ambos lidos integralmente; não executados nesta entrega. Sua cobertura foi examinada antes de decidir que não validariam o protótipo. |
| Orientações | Ancestrais aplicáveis e pastas de orientação; referências pessoais `mizuki-copiloto-do-mestre` e `mizuki-rpg-gamedev`, em `/home/mizuki/CHAT-GPT/sources/`. | Nenhum AGENTS aplicável localizado. Referências pessoais lidas, sem importar regras de outra campanha/sistema. |
| Complemento externo | Regras oficiais/licenciadas de Summoner/eidolon e arquétipo; páginas oficiais específicas de JJK. | Conferência pontual de lacunas, registrada em `apoio-fontes-externas.md`. Não foi refeita a pesquisa de mercado. |

Listas detalhadas, distinguindo leitura integral de busca e trechos: [auditoria do repositório](apoio-auditoria-repositorio.md), [comparação dos Caminhos](apoio-caminhos-versoes.md) e [fontes externas](apoio-fontes-externas.md).

### Diferenças que mudam a interpretação

- **Guia:** v0.4 usa Aberturas e Arquiteto/Analista/Socorrista. O arquivo solto usa Chamada e Cartógrafo/Analista/Regente. Não é mera troca de nome. A v0.4 permite resposta com golpe de arma, desarmado ou feitiço Classe 0, mediante as duas Reações exigidas.
- **Emanador:** v0.4 usa Desdobramento Técnico e Condutor Armado/Ressonante/Catalisador. O solto usa Emissões e Prisma/Crivo/Vestígio. Essas regras não são intercambiáveis.
- **Vanguarda:** a coleção inclui Batedor e Executor; a continuidade solta ainda registra propostas anteriores descartadas. A ausência declarada ali não descreve a v0.4.
- **Bastião:** a coleção mantém o kit reconstruído, com explicitações operacionais. A reforma de 17/09 não é uma atualização posterior à coleção.
- **P1 e P2:** convergem em separar repertório, campo e ações. P2 acrescenta preparação, categorias de Presença, faixas de corpos e escalonamento automático; isso continua hipótese. A formação de vida compartilhada sugerida como alternativa não satisfaz automaticamente a fantasia de múltiplas entidades distintas.
- **Pendências preservadas:** Oportunista, Contra a Parede e conversões de Forma Fluida têm questões editoriais/operacionais na própria coleção. Orçamento integrado em fatias continua não certificado. Não corrigimos essas habilidades ao definir Invocações.

## Diagnóstico confirmado

Os caminhos desta tabela são relativos ao projeto principal identificado acima. Linhas conferidas na versão local, não copiadas cegamente do snapshot das pesquisas.

| Achado | Evidência | Consequência |
|---|---|---|
| **Aplicabilidade universal, acesso efetivo pelas Trilhas** | Manual `60-invocacoes.md:5`, `20-criacao-de-personagem.md:117`, montagem em `60:259`. Busca nas peças, manual, DESENHO e gerador não encontrou outra concessão padronizada. | “Vale para quem obtiver” não é um meio escrito de obter. Técnica/objeto personalizado por acordo não equivale a uma fonte geral publicada. |
| **Sem teto universal fechado** | Peça `15-invocacoes.md:501–503` reconhece expressamente a lacuna. Servo/Matilha/Coro concedem 1/5/1 corpos no manual `35:551–559`. | O limite precisa existir antes de somar novas fontes de acesso. |
| **Ação do dono e autonomia muito restritas** | Manual `60:9–14`, `364–378`, `408–415`. Padrão para comandar; fora de alcance fica parado; dono apagado não comanda e a entidade não protege sozinha. | É uma escolha mecânica concreta, não só redação sem personalidade. Há conflito entre utilidade fora do combate e o procedimento de distância/ordens. |
| **Reações e ações concedidas não estão centralizadas** | Manual `35:545`, `593–599` contém exceções do Evocador; capítulos gerais concedem ações e oportunidades, mas `60` não fecha o pacote próprio do corpo. | Não presumir uma Reação por invocação nem nenhuma resposta possível. A regra nova precisa dizer. |
| **Bloquear não usa Reação** | Manual `10:155–187`; peça `23-bloquear.md`, §3. | Limitar Reações não limita a quantidade de Bloquear. Cada ataque recebido pode acrescentar uma rolagem defensiva. |
| **Corpos têm valor além do ataque** | Matilha com posições próprias em `35:555`; cobertura no manual `15:306–321`; Graúdo/Vigia/Faro/Fisgada/Jorro em `60:152–227`. | Posições, passagem, sentidos, controle e alvos adicionais sobrevivem à divisão do dano. |
| **Customização existe, mas a execução de módulos é incompleta** | Catálogo, réguas e criação própria em `60:131–253`; Traços ditos sempre ativos, mas alguns prendem, empurram ou atacam. | Não é correto dizer que “não há construtor”. Faltam limites/tempos operacionais para parte do que ele já permite escrever. |
| **Retirar e trocar são lacunas** | Busca no corpus ativo; manifestação/retorno em `60:9`, `398–404`, sem procedimento geral encontrado de recolher/trocar. | Preço zero, Bônus ou Padrão para troca seriam propostas novas, não regras herdadas. |
| **Perda uniforme e retorno renovável** | Manual `60:382–404`: zero dissipa, destruição por limiares, perda definitiva sem recuperar; queda retorna a metade da vida pelo custo normal. | Não universalizar essa consequência entre técnicas, maldições capturadas e corpos físicos sem reavaliar o vínculo. |
| **O teto de Rotina não resolve o turno executável** | `60:189–204` divide cotas; comando consome Padrão; peça `15:439–455` descreve saída diferente; Dueto é exceção específica. | Somar cotas teóricas não prova quais ataques o usuário realmente consegue executar. |

### Inconsistências concretas do material antigo

Não é uma lista de correções aplicadas; o projeto permaneceu preservado.

1. **Vida do Coro:** manual `60:70` chama de corpo cru; a tabela `:81` dá 44 no nível 10/técnica/CON 0; a fórmula básica daria 22. O exemplo `:404` e a peça `15:1086` usam multiplicador 2, com Constituição fora. A seção não explica essa fórmula com clareza.
2. **Carranca:** compras 8 + 8 + 2 = 18. O manual `60:317` sugere retirar Escalada para caber nas outras Trilhas, cujo orçamento é 12 em `:310`; ainda restam 16.
3. **Cópias divergentes:** DESENHO-caminhos `:375` diz que a entidade some quando o dono cai, mas o manual `60:408–415` diz que permanece. Batida exclui invocações em DESENHO-trilhas `:1713`, mas a exclusão não aparece no manual `35:583`.
4. **Relógio de orçamento:** `conferir-orcamento.py:73` usa seis rodadas por minuto; o turno vigente tem seis segundos, ou dez rodadas por minuto (`11-o-turno.md:5`).
5. **Percentuais de dano:** peça `15:910` promete 95%–100% desde nível 5, mas a Matilha publicada nessa faixa entrega cinco vezes 1d6: média 17,5, frente à Rotina 31. A divisão é 56,45%, antes de acerto/crítico. A prosa usa cotas antigas, não a média dos dados. Essa demonstração não é certificação do dano final.

## O que as verificações antigas não provam

O validador de Invocações confere catálogos, fórmulas, exemplos, tabelas e alguns cenários. Há cobertura útil e extensa. Porém o bloco de conservação em `1506–1526` define a saída da invocação como `1 − saída do dono`: o total ser 1 está assegurado pela própria construção, sem reproduzir ações reais, Dueto, Reações ou concessões de aliados.

A busca de montagens em `1534–1581` usa gasto exato e inclusão de entradas; “zero dominadas” ali não mede o valor de controle, exploração ou geometria. O script de orçamento não modela manifestações, energia temporária ou essa economia de ações. Por isso nenhum eventual resultado verde seria prova do novo sistema. Nesta tarefa, eles foram lidos e analisados, não executados.

## Limites da confirmação canônica

Há evidência oficial para diversidade de entidades e funções, captura por uma técnica específica e uma herança específica nas Dez Sombras. Isso não determina preços, Presença, quantidade de corpos ou autonomia ofensiva no RPG. A conferência também detectou redirecionamento das referências antigas de PF2e para versões novas: a versão consultada foi registrada.

Continuam sem confirmação direta suficiente nesta sessão: a natureza detalhada da Rika posterior a JJK 0; procedimento geral de shikigami sem técnica inata; crescimento ou congelamento de maldições capturadas; funcionamento completo dos núcleos e da autonomia energética de corpos amaldiçoados. O protótipo não depende de afirmar nenhum desses detalhes como cânone.

## Arquivos da entrega e reprodução

- [Arquiteturas, recomendação e próximos passos](01-RASCUNHO-arquiteturas.md).
- [Menor protótipo de funcionamento](02-RASCUNHO-prototipo.md).
- [Verificações e limitações](03-RASCUNHO-testes.md), com resultados separados de interpretação.
- Relatórios de apoio: evidências do repositório, diferenças dos Caminhos e fontes externas.
- Fontes extraídas do pacote original, preservadas dentro desta pasta.

Verificação de integridade executada, após ler o script:

```bash
python3 '/home/mizuki/CHAT-GPT/RPG -JJK/desenvolvimento-invocacoes-2026-09-24/RPG-JJK-Pesquisas-Invocacoes/verificar_pacote.py'
```

Resultado: **11 arquivos e os dois relatórios integrais confirmados**. A contagem vem do manifesto do pacote; não equivale ao total de arquivos de toda esta entrega. O ZIP dos Caminhos também foi lido com `zipfile.testzip()` (sem item corrompido), seu SHA-256 comparado com a referência acima e os 15 arquivos extraídos comparados byte a byte com o ZIP, sem ausências ou divergências. As verificações procedimentais do protótipo e seus comandos estão no documento de testes.

Tempo de mesa, satisfação, carga mental e equilíbrio integrado ainda exigem observação de pessoas e fichas completas. Não foram medidos nesta sessão. O ponto de parada é a avaliação desta arquitetura por Mizuki, antes do desenvolvimento do Evocador.
