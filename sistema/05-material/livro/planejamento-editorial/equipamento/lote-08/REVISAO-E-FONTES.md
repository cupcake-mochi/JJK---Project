# Equipamento amaldiçoado: reformulação candidata

03/10/2026. Pedido: refazer o capítulo, com poderes por grau, poucos benefícios numéricos e armas, Trajes, Revestimentos, roupas sem proteção e escudos. O lote-08 substitui o lote-07 **na fila de candidatas**. Livro v0.331, peças mecânicas, PDFs publicados e candidatas anteriores continuam preservados.

## Resultado

Onze páginas; dezessete ferramentas de exemplo; seis tipos de base. Quatro grupos principais recolhidos no PDF: Ferramentas, Catálogo, Desgaste e Objetos. O texto usa função, ativação, resultado e limites; as justificativas de design ficam neste relatório. Não há arte de IA.

Confirmado pelo usuário na rodada seguinte: grau 3 já admite efeitos especiais; grau 4 apenas permite ferir maldições. A candidata já seguia essa leitura; a pendência de interpretação está encerrada. Grau 2/1/especial comporta capacidades mais marcantes. Requisitos próprios 7/13 mantidos, sem Refino e sem sintonização. Grau 4 sem poder especial. Não se importou a progressão numérica de raridade de outro sistema.

## Mudanças de regra, além da escrita

| Entrada anterior | Resultado candidato |
|---|---|
| Fiel | Retorno depois do próprio arremesso, com mão livre e percurso físico; retirada a imunidade absoluta a desarme. Usa Longo Alcance, propriedade existente; Arremesso é uma categoria de armas. |
| Aferido | Acerto com arma identifica o grau da maldição; acessório usa Ação Padrão e, contra resistência, ataque desarmado sem dano. |
| Presságio | Presença de maldição em 9 m, sem direção, quantidade ou identificação; barreira física fechada e ocultação apropriada impedem aviso. |
| Perene | Conservação e reparo superficial; retirada a indestrutibilidade absoluta, que invalidaria regras de objetos. |
| Quebranto | Reação antes de um TR contra feitiço: sucesso comum, uma vez por cena. Não se aplicam a versão de anular todo feitiço nem a versão de sucesso de Bloquear. Conciliação por redesign autorizada no pedido. |
| Avulsa | Mantidas Reação e duas vezes por cena; gatilho após terminar ataque recebido, exige capacidade de agir, empunhadura e alcance normal. |
| Cisão | Dano do ataque, inclusive adicionais próprios, substitui Vida por Integridade; não afeta ambas. Mantida a dependência das regras de alma, com alerta abaixo. |
| Insondável | Alcance indefinido “na cena” substituído por 18 m apenas nos ataques do próprio turno; não amplia oportunidades. Ponta escondida e caminho físico continuam necessários. |
| Contrapeso | Dispensa somente a Força exigida pela peça, ampliado a Revestimento e escudo. Não dispensa carga, mãos ou teto de Destreza. |
| Anátema | Contato indefinido vira Ação Padrão e TR para abertura local em barreira de feitiço. Defesa por Reação/TR limitada a uma vez por cena e somente ao portador. Não elimina área inteira, Domínio, energia ou poderes do alvo. Mudança efetiva do poder antigo, não equivalência numérica. |

Sete efeitos novos cobrem necessidades ausentes: Aparência Mutável, Costura de Fuga, Passagem, Âncora, Retirada, Suspensão e Reserva de Ar. As ferramentas são criações do Projeto M, mesmo quando uma função lembra poderes da obra. Seus nomes não afirmam ser fichas oficiais de relíquias canônicas.

Roupa sem proteção preserva a defesa por energia. Traje/Revestimento preserva o substituto de proteção, o teto e a situação onde couber. Dois itens vestidos com efeito, sendo no máximo uma vestimenta; escudo flutuante ocupa uma dessas vagas. Mãos continuam limitando armas e escudos normais. São limites ampliados para acomodar novas bases sem somar três camadas de roupa e dois acessórios.

Cópias compartilham a frequência por personagem, além do contador do próprio item. Guardar, emprestar ou trocar não recupera usos. Essa trava é nova; não deve ser confundida com sintonização. O item precisa acompanhar o descanso para recuperar seus próprios usos. O custo para vestir/retirar roupa ou acessório com poder é Ação Padrão; proteção mantém seu tempo próprio.

## Nome e superfícies afetadas

**Proposta local: Estigma → efeito especial.** Usada neste rascunho para dispensar um termo abstrato. O conceito antigo permanece no mapa de revisão, sem substituição global. Antes da integração definitiva, confirmar a nomenclatura e atualizar manual, peça 16, fichas, validadores antigos e índice. Nomes dos dez poderes foram mantidos, embora suas fichas possam ter mudado.

## Comparação dirigida com outros livros

D&D apresenta equipamentos com funções concretas, incluindo roupas, escudos e acessórios. Foram examinados escudo animado, armadura de mithral e manto de deslocamento: a referência é descrever quando o item funciona e o que permite fazer. Não foram importados bônus universais por raridade nem sintonização. [D&D 2024, itens mágicos](https://www.dndbeyond.com/sources/dnd/br-2024/magic-items-a-z), [equipamento](https://www.dndbeyond.com/sources/dnd/br-2024/equipment).

O GM Core distingue uso contínuo de ativação e explicita frequência, gatilho e requisitos. Isso orientou os cabeçalhos e procedimentos, sem importar seu limite de itens investidos. [Pathfinder 2, uso de itens](https://2e.aonprd.com/Rules.aspx?ID=3135).

Cairn oferece outra solução, com cargas e recargas particulares para relíquias. Preferiu-se aproveitar os relógios já existentes do Projeto M, sem acrescentar uma nova economia de recarga. [Cairn SRD, relíquias](https://cairnrpg.com/first-edition/cairn-srd/#relics).

Cotejo dirigido de regras públicas e das fontes locais do projeto; não representa leitura integral dos livros enviados nem opinião de leitores externos. As evidências canônicas sobre uso por Maki, dedos de Sukuna e selos permanecem em `../lote-07/evidencias/fontes-canone.json` e no relatório daquele lote. O capítulo distingue convenções de campanha de alegações sobre a obra.

## Validação funcional e numérica

`validar_modelos.py` enumera 6.561 distribuições de equipamentos representativas de duas mãos e duas vagas vestidas. Os 74 conjuntos permitidos não excedem quatro efeitos. A exceção do escudo suspenso mantém esse teto. Múltiplas cópias não acrescentam usos; Avulsa ainda compete pela Reação com defesa e oportunidades. Casos negativos retiram travas para confirmar que o modelo os detecta.

O modelo exato de d20 usa CD = 8 + bônus adversário: em igualdade, 65%; quatro pontos atrás, 45%. Contra dano 40 reduzido à metade por sucesso, com TR de 65%, a média sem ferramenta é 27. Quebranto reduz essa aplicação a 20: prevenção média 7. Anátema, também com 65% no teste próprio, previne em média 17,55 nessa aplicação e não protege os aliados. A diferença é de grau, alcance de efeito e risco; não prova dominância universal.

**Cisão não está certificado como equilibrado.** Com Integridade inimiga igual à metade da Vida, um usuário isolado esgota essa barra em metade do tempo do dano comum, antes de considerar resistências e estágios. Num grupo de quatro com contribuições iguais e dano dividido, o tempo até uma barra esgotar passa de 1/4 para 1/3 da unidade de referência. Isso mostra sensibilidade à composição, não resolve o efeito dos estágios nem o desfecho de Integridade zero. Não se deve chamar o efeito de “sem aumento de dano” e concluir daí que não tem ganho de poder. Revisar com Alma; Morrendo permanece adiado.

Alcance de 18 m, teleporte, detecção e utilidade não têm preço comum confiável com dano. Permanecem alvos de mesa: corredores e campo aberto; inimigo que recua; três cenas antes de um descanso; usuário sem energia; dupla de armas; grupo com e sem cura de Integridade. Especialmente verificar se Contrapeso merece grau 1 nas fichas em que sua vantagem de manejo é pequena.

A revisão editorial verificou títulos convencionais, termos definidos, ausência de explicação duplicada de Caminhos, sequência de uso e fronteiras entre os capítulos. A conferência visual abrange as onze páginas. Os testes são do autor e não equivalem a validação independente ou playtest humano. `CONFERENCIA.json` e a auditoria registram hashes do material efetivamente examinado.

## Fila

Catálogo e base de ferramentas concluídos como candidata. Próximo item solicitado executado em `../revisao-carga-r5`: proteção, itens comuns, transporte de criaturas e exemplos de compra. Depois segue **Perícias e Ofícios**, incluindo a fabricação/reparo de ferramentas, sem tratar a montagem de uma ficha como fabricação automática.
