# Revisão editorial do capítulo 1

26 de outubro de 2026. Registro 93. Pré-1.0, revisão dirigida após o registro 92.

## Recuperação e comparação

Recuperado o commit b8b518cbb4111673de4c01970d505913b3cb970b da branch codex/guia-do-mestre-pre-1-2026-10-23. O prompt de continuidade foi lido integralmente. A produção foi localizada no Windows em `E:/Claude/Pesquisa de Campo - Mestragem/`; a pasta Linux de salvamento não estava disponível neste sistema. A cópia Git de trabalho foi criada separadamente neste chat.

Comparados 1399 itens do inventário remoto: 1397 arquivos presentes na produção tinham SHA-256 idêntico; README.md e CONFERIR-COPIA-GIT.py eram exclusivos do pacote Git. Nenhuma divergência de conteúdo foi encontrada. O acervo externo e os demais projetos não participaram da sincronização. A R53 mantém SHA-256 `7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d`.

## Correções concretas

| Trecho | Antes | Depois e motivo |
|---|---|---|
| Entrada de testes | Ensinava a conta sem explicar quando pedir a rolagem; “você” podia indicar o mestre | Apresenta incerteza e consequência; distingue porta destrancada de arrombamento; identifica quem rola e demonstra igualdade à CD com a conta publicada na R53 |
| Vocabulário | Jujutsu, energia e Cortina pressupostos; NPC sem apresentação | Contexto breve dos termos; a frase sobre negociação passa a falar diretamente de autoridade |
| Técnica de fios | Pergunta aberta sobre aplicações diferentes | Intenção de puxar a chave, consulta de efeito/alcance/custo e limite de uma aplicação que apenas corta |
| Guilda | Mina e organização real apareciam numa explicação ambígua | Personagem encaminha chamado na história; comunidade organiza inscrição e registro fora dela |
| Apoio institucional | Nara alternava entre oficina e coordenação; Davi entre testemunha e motorista | Sílvia coordena e Otávio dirige neste exemplo; Nara e Davi conservam suas funções nos pilotos |
| Depósito | “Preparo preenchido” podia parecer investigação completa sem causa preparada | Delimita o exemplo a relatos, apoio e acesso e remete ao preparo da investigação para causa e vestígios |
| Sessão zero | Percurso espalhado; conferência de ficha e dúvidas com destinos genéricos | Roteiro de entrada, remissão a Conferir personagens e âncora específica de dúvidas de regra |
| Acordos preenchidos | Conhecimento reduzido à ficha; atividades pareciam depender de procedimento ainda inexistente | Distingue história e capacidades; remete à dedicação por ficha já escrita, mantendo aberta apenas a implantação local na campanha fechada |

As 20 substituições editoriais exatas estão em [alterações textuais](apoio-revisao-c01/alteracoes-textuais.json). Não foram alteradas regras de teste, custos, fichas de inimigos, Origens ou decisões autorais. Não houve questão mecânica nova que exigisse consulta. A ficha 08 foi conferida e permaneceu adequada ao percurso.

## Composição e inspeção

A prova inicial de 358 páginas ainda dividia parágrafos curtos de forma ruim nas páginas 6, 11 e 13 e deixava uma introdução de tabela isolada numa coluna. A composição do capítulo 1 passou a conservar parágrafos completos. Três introduções de tabela recebem largura útil e acompanham o cabeçalho. Foi corrigida também a reserva de altura da introdução ilustrada de Sociedade, que gerava espaço vazio desnecessário. O procedimento foi limitado ao capítulo em revisão; não mudou globalmente a composição dos demais capítulos.

O PDF final tem **359 páginas**; o capítulo 1 ocupa **4–17**, e o capítulo 2 começa na **18**. O acréscimo resulta da preservação das unidades de leitura, sem aumentar a fonte ou preencher espaço com texto artificial. As tabelas com continuação repetem cabeçalho. Espaços ao fim de blocos preservam parágrafos e títulos completos.

Todas as 359 páginas foram renderizadas com Poppler e inspecionadas em 60 pranchas. O capítulo 1 foi examinado em páginas ampliadas. Os cinco mapas foram revistos nas páginas 114, 125, 133, 144 e 164; a rota do Carregador mantém três trechos de 6 m e a lateral de 24 m entre os mesmos pontos. A página 189 foi ampliada para conferir as seis linhas de preenchimento de Reserva. A biblioteca Markdown atual deixou de interpretar os sublinhados como ênfase, sem mudar os campos ou a habilidade.

Verificações complementares: 2380 links PDF e 1047 links HTML sem destinos inválidos; 104 fontes com hashes correspondentes; 497 amostras textuais do capítulo localizadas no PDF; nenhum problema no verificador de geometria. A [revisão visual](<../08 - Diagramacao do Guia/revisao/revisao-visual.json>) registra as imagens e o alcance.

SHA-256 do PDF: `e44fa4c294c9994096330ff37038a4380ec6792cd77b43082d8196ae8e7cf864`.

## Reprodução e preservação

Os geradores foram executados sobre as fontes numeradas. GERAR-EDICAO.py agora produz URLs com barras portáveis, escreve UTF-8/LF e resolve o antigo caminho absoluto da R53 para a cópia de referência incluída. No Windows, executar Python com `-X utf8`. Bibliotecas usadas: ReportLab, BeautifulSoup, Markdown, Pillow e PyMuPDF; Poppler para as provas. Os registros anteriores permanecem no histórico, sem atribuir suas verificações ao PDF novo.

Manifestos atualizados por união; fontes externas omitidas do salvamento remoto continuam omitidas. A comparação prévia e a sincronização seletiva preservam outros trabalhos locais. Não houve teste com leitores ou sessão de mesa. A revisão textual desta entrega cobre o capítulo 1; as demais páginas receberam inspeção de apresentação e navegação após a repaginação.

## Próxima tarefa

Revisar o capítulo 2, “Preparar missões e campanhas”, a partir da página 18: acompanhar a preparação e seus exemplos, verificar informação oferecida, opções dos jogadores, consequências e remissões. **GPT-6.1 Sol, esforço alto**, conforme a direção do projeto. Se surgir contradição mecânica ampla, preparar comparação com **GPT-6 Astra, esforço extra alto** antes de pedir decisão autoral.

A recomendação é aplicada a este trabalho; não foi feito teste comparativo entre modelos. A [orientação de seleção da OpenAI](https://developers.openai.com/api/docs/guides/model-selection), consultada nesta entrega, recomenda escolher pelo resultado e pelos critérios de qualidade. A recomendação não muda o seletor automaticamente.
