# Revisão do Incursor

A candidata reúne o Caminho e as três Trilhas em 26 páginas. O manuscrito tem SHA-256 `cd608cb7a2ad671becaef2da0b56ee77229a24f8212df1dbbbf7b002e9f268d4`. Revisão textual, modelos dirigidos, leitura independente, exportação e inspeção visual das 26 páginas concluídos. A conferência final do PDF aprovou 201 verificações.

## Escopo conferido

A edição integrada e a seção correspondente do manual35 são idênticas. O inventário associa 65 entradas da fonte às páginas da candidata; 41 nomes operacionais foram preservados e conferidos. A candidata incorpora a alteração já aprovada de Movimento Acrobático: atravessar criaturas de qualquer tamanho desde o nível2.

O texto conserva a vida, energia, progressão, dados, distâncias e preços aprovados. Antes/depois e justificativas de 20 decisões estão em ALTERACOES.md/.json. Publicados e arquivos dos outros donos não foram editados.

## Armas do Assassino

A propriedade **Leve** é separada de Volume, Oculta e Discreta. A comparação enumera as 52 armas: 22 eram elegíveis; 21 permanecem. A única retirada é Taco. Faca, Punhal e Sai passam a ter Leve por coerência de classificação, sem ganhar acesso novo, pois já tinham Fineza. Wakizashi e manoplas conservam o acesso. Katana e Rapieira permanecem pela Fineza.

Besta de Uma Mão, Pistola e Revólver foram preservados deliberadamente. A regra aprovada permitia arma leve ou Fineza sem limitar todos os usos a corpo a corpo. Parkour, Estudar a Guarda e Brecha Fatal continuam com suas exigências próprias de contato. O ajuste não concede ataque bônus, Destreza no dano, recarga ou redução de carga.

**A sincronização ainda precisa entrar em R05.** SINCRONIZACOES.md contém texto da propriedade e lista completa. Também identifica explicações de habilidades que podem sair das regras comuns depois de migradas ao Incursor.

## Execução dos testes

Comando, a partir desta pasta:

`python3 auditar.py`

Resultado: **249 verificações**, incluindo âncoras, integridade, cobertura e estrutura; **76 casos dirigidos**; **46.875 sequências** curtas de Fluidez; **70 perfis** de atributo/Refino para Golpe Cirúrgico; **400 trajetórias** de Ricochete; **364 perfis** de resistência; **5 comparações** de pressão ofensiva. O validador editorial passou sem achados.

Esses são modelos de especificação com valores e requisitos ligados ao manuscrito. Não executam um motor completo de jogo. O número de verificações não representa esse mesmo número de partidas ou de situações reais independentes.

Foram exercitados: ganho com reserva cheia, evento já processado, limite por ciclo, perda por Incapacitado, Retomar fora do começo, Reflexo sem Fluidez anterior, reação compartilhada, cota acrobática e salto, imobilidade por rodada, custo por atributo, crítico e combinação, bloqueios de alcance, continuação já usada e quatro alvos distintos na Trajetória Perfeita.

## Resultados numéricos

Com Destreza5 e Canalizar3d4, Golpe Cirúrgico custa4PE e acrescenta4d4. Uma arma1d8 causa1d8 + atributo do ataque +7d4; no crítico,2d8 + atributo +14d4. Com atributo de ataque5, a média do crítico é49. Instante Decisivo eleva o custo para8PE e mantém esses dados.

No extremo conferido, atributo6 e Refino10 produzem nove dados adicionais totais: quatro de Canalizar e cinco do Golpe. Com arma1d8, são42 de média normal ou78 no crítico, antes das defesas. O custo próprio é5PE e Fluidez; outros requisitos continuam presentes. Esses picos não foram reduzidos nesta revisão, pois decorrem de decisões aprovadas.

Pugilista faz até três ataques próprios com Atacar e Rajada. Guarda troca um ataque da Bônus pela defesa; no nível27, Harmonia combina dois ataques da Bônus e Esquivar por6PE. Projeção continua sendo um TR que substitui um ataque: não produz crítico, Fluidez por acerto ou Quebrar o Compasso.

Malabarista faz até três ataques próprios com Ofensiva e uma continuação. Os custos são6PE com Cruzado,7PE com Retorno ou9PE com Finta, além da Fluidez. Uma reação ofensiva válida pode levar a quatro ataques no ciclo, mas depende do gatilho, do alcance e da reserva pessoal. Trajetória Perfeita com Ofensiva custa15PE e permite até cinco ataques no turno: quatro alvos distintos na trajetória e o outro ataque da Ação Atacar. Uma mesma vítima pode receber dois desses cinco, não quatro da trajetória.

## Comparação de pressão e limites

O modelo comparativo usa acerto de60%, crítico de5%, sem vantagem, bloqueios, técnicas, Kokusen ou ações concedidas por aliados. Golpe Cirúrgico pressupõe uma oportunidade válida; a continuação do Malabarista só ocorre quando pelo menos um dos dois ataques iniciais acerta. Assim, sua chance de disponibilizar essa continuação é84%, em vez de tratar o terceiro ataque como garantido.

| Perfil | Assassino: um Golpe | Pugilista: Rajada | Malabarista: continuação condicional |
|---|---:|---:|---:|
| Nível7, atributo4, Refino3 | 12,80 | 23,03 | 21,80 |
| Nível19, atributo5, Refino7 | 16,65 | 33,23 | 27,76 |
| Nível30, atributo6, Refino10 | 26,35 | 48,68 | 40,54 |

Esses valores são dano médio por sequência restrita, não uma classificação final de força. O Assassino investe em ocultação, escolha do momento e crítico; o modelo acima não inclui suas vantagens nem Sentença Final. O Malabarista paga mais PE para preservar a Bônus e depende da geometria. O Pugilista compromete a Bônus, mas tem dano contínuo elevado. A comparação identifica a necessidade de observar **consistência do dano do Assassino entre seus picos** em testes de mesa, sem provar que a Trilha inteira está fraca.

A reserva de energia cresce bastante: Ofensiva3PE consome25% dos12PE do nível2, mas apenas1,67% dos180PE do nível30. A economia nos níveis altos depende mais de ações, Fluidez, alvo e oportunidade do que de esgotar esse custo básico. Isso corresponde à direção aprovada de um Caminho com energia abundante; não foi usado como justificativa para aumentar custos silenciosamente.

## Leitura e apresentação

As 26 páginas receberam parecer contextual de clareza, suficiência, vocabulário, voz e localização. O PHB2024 local foi usado como comparação de organização: quadro da ficha, progressão e habilidade com nível, ação, custo e efeito identificáveis. Não foram importados recursos, números, armaduras ou condições daquele sistema.

Não há nova afirmação canônica sobre Jujutsu Kaisen que dependa de validação em mangá. Os percursos e poderes descritos são regras do Projeto-M. Não foi criada ou usada imagem de IA.

## Etapas restantes

1. Revisão de outro agente ou da raiz, com leitura do manuscrito e dos limites deste relatório.
2. Aplicar a propriedade Leve no dono de equipamento e remover duplicações externas indicadas.
3. Exportar e conferir todas as páginas, tabelas, títulos e navegação do PDF.
4. Na revisão global, testar técnicas, ações concedidas por outros Caminhos e defesas específicas que não foram enumeradas aqui.

V12–V14 foram concluídos pela raiz após a autoria. Evidências independentes e hashes das 26 imagens constam na pasta evidencias.

## Prova exportada

PDF de26 páginas exportado com quatro grupos recolhidos. A pré-conferência documental passou198 verificações, sem executar ou alegar inspeção visual. Imagens para a raiz em `/tmp/incursor-qa-final/pagina-01.png` até `pagina-26.png`. O registro visual foi concluído, e CONFERENCIA.json aprovou as 201 verificações integrais. Gerador requer o Python do runtime com ReportLab/PyPDF; o Python do sistema não possui ReportLab.
