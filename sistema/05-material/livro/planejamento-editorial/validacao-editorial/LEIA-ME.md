# Validador de títulos e localização

Diretriz expressa de03/10/2026: evitar títulos “Como ler...” e não repetir explicações de Caminhos, Trilhas ou habilidades em capítulos que não sejam seus donos.

`conferir_editorial.py` detecta títulos Markdown/Setext/HTML, reconhece nomes cadastrados inclusive com acentos ou quebra de linha, e procura sequências de24 palavras copiadas de prosa dos Caminhos. Arquivo sem domínio cadastrado é erro. O diagnóstico informa arquivo, linha quando identificável, termo e dono.

A chamada `assert_exportable(manuscrito)` foi ligada aos três geradores correntes desta rodada, antes da construção do PDF. Exige também o `LOCALIZACAO-EDITORIAL.json` da pasta de evidências de cada unidade, com hash do texto e declaração de revisão contextual. Um texto alterado invalida essa leitura. Não basta mudar o título e conservar uma explicação alheia sem nome.

## Execução

Da raiz do projeto:

```bash
python3 sistema/05-material/livro/planejamento-editorial/validacao-editorial/testar_editorial.py
python3 sistema/05-material/livro/planejamento-editorial/validacao-editorial/conferir_editorial.py --saida /tmp/diagnostico-editorial.json
```

Sem arquivos, examina todos os manuscritos correntes de MANUSCRITOS.json e retorna código1 se houver achado. Com caminhos posicionais, examina apenas esses arquivos. `--exportacao` também exige a leitura contextual atualizada. Nunca usar uma saída anterior verde depois de mudar o texto.

## Escopo e limites

DONOS.json tem nomes, aliases e fontes de Caminhos/Trilhas e um conjunto inicial de aptidões/efeitos com dono próprio. Esse cadastro precisa acompanhar os novos capítulos e renomes. Termos ambíguos, como o verbo carregar e nomes curtos usados como palavras comuns, exigem contexto marcado ou título, para não acusar a frase “Carregar uma mochila”.

Menção marcada e cópia são sinais objetivos; uma ligação mecanicamente indispensável pode exigir exame contextual. Não apagar custos ou requisitos só para zerar avisos. A correção é mover a explicação, preservar a regra no dono e verificar a interface. Não declarar toda ocorrência encontrada um erro de regra.

Paráfrases completas sem nome nem trecho idêntico não são reconhecidas de forma confiável. A leitura contextual continua obrigatória. O parecer registrado não é prova automática de compreensão, nem substitui leitor independente.

Os22 testes incluem casos positivos e negativos, nomes com quebra de linha, texto comum que não deve ser bloqueado, domínio correto, cópia sem nome e falha efetiva da exportação por título, nome ou parecer desatualizado. Uma falha inicial para nome entre linhas foi corrigida. As fontes de testes são temporárias e não alteram o livro.

## Auditoria retroativa

DIAGNOSTICO-CORRENTE.json inclui as candidatas anteriores e o Incursor de trabalho. Elas ainda têm alertas; a conferência global NÃO está verde. As três provas novas passam individualmente e podem ser exportadas. As versões publicadas/históricas não foram editadas só para cumprir essa norma nova. Antes de integrar a edição completa, tratar todos os achados pertinentes e conferir o conjunto novamente. A interface mecânica aprovada do Incursor fica no manuscrito do próprio Caminho.

## Atualização: vocabulário e provas correntes

VOCABULARIO.json acrescenta sinais contextuais de palavras ambíguas/pouco familiares. E005 aponta o trecho e uma alternativa; não faz substituição automática. Exceções justificadas são registradas por linha e termo em LOCALIZACAO-EDITORIAL.json, válidas somente para o hash examinado. E006 exige vocabulario_revisto antes da exportação. A leitura deve examinar palavras fora do cadastro, preservar termos necessários e evitar explicações repetidas.

São agora 29 testes do validador. Os geradores de Equipamento lote-01-r3, Proteção lote-02-r2 e Munição lote-03 usam a verificação atual. Manuscritos anteriores ainda precisam revisão retroativa; não considerar o conjunto aprovado. A conferência compartilhada conferir_pdf_candidato.py também examina texto, tabelas, navegação, fontes e hash das evidências.

## Atualização: títulos diretos e E007

A diretriz atual também evita títulos iniciados pelos artigos **A, O, As ou Os**. E007 verifica títulos ATX, Setext e HTML, inclusive numeração e formatação interna. Não remove acentos: **À** e **Às** não acionam essa regra. Blocos de citação, comentários e código ficam fora da leitura. A ocorrência gera um bloqueio em `assert_exportable`, mesmo quando o parecer contextual estiver atualizado. Não foram criadas exceções para esconder títulos pendentes.

A regra encontra o padrão; a escolha do novo título exige leitura. “O que...” normalmente pede nomear o assunto, em vez de apenas retirar o artigo. O script abaixo inventaria todos os Markdown do planejamento, separando os **17 manuscritos cadastrados** das versões históricas/pilotos e da documentação/evidências:

```bash
python3 sistema/05-material/livro/planejamento-editorial/validacao-editorial/inventariar_titulos.py --saida /tmp/r07-titulos-auditoria.json
```

O número de manuscritos acompanha MANUSCRITOS.json; o inventário informa a contagem real em cada execução. Ele não altera títulos, arquivos antigos ou hashes de pareceres. As sugestões são entregues por arquivo e linha para edição manual. Ao trocar apenas cabeçalhos, preservar um backup e provar que o restante do texto é idêntico antes de atualizar o hash da leitura anterior. Depois de exportar um PDF, inspecionar as páginas alteradas e comparar as demais com a exportação anterior.

Os **53 testes** agora incluem artigos, capitalização, links, numeração, HTML em várias linhas, À/Às, palavras como Ação/Onda, citações, código e bloqueio real de exportação. O diagnóstico histórico DIAGNOSTICO-CORRENTE.json não passa a ser atual por essa mudança: produzir uma saída nova ao auditar o conjunto. Geradores novos devem usar `assert_exportable`; um script antigo que ainda não o invoque depende também da conferência explícita antes da entrega.

## Cadastro: Mão Firme

Mão Firme pertence ao **Fundamento**, onde aparece no catálogo de Talentos. A conferência do catálogo completo de Aptidões não encontrou aptidão autônoma homônima: as três menções são incompatibilidades, registradas como referências contextuais exatas. O cadastro anterior atribuía dois donos por engano. Identificar Feitiço e Leitura de Feitiços distinguem a Melhoria e o Talento antes chamados Aviso. `aliases_historicos` conserva as equivalências nominais; conceitos compartilhados (Talento, Categoria de Efeito, Guarda Aberta) não são tratados como capacidade de caminho por mera menção.
