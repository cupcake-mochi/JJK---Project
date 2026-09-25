# Relatório e auditoria — revisão 5

## Execução

**212 verificações passaram; zero falhas.** São 178 regressões executadas no modelo ampliado e 34 verificações novas. Em 98 verificações exige-se que a consulta ou recusa não altere o estado. `ensaio/resultados.json` registra cada caso e seus estados; `ensaio/execucao.json` reúne as contagens.

A criação da bancada nova não chegou a iniciar antes da interrupção. Na retomada, foram preservadas as cópias já salvas e criada a bancada r5; sua primeira execução completa passou. Nenhuma decisão autoral foi alterada para obter os resultados.

## Auditoria de interações

- Básica/especial: conversão para Bônus não cria segunda básica, não concede especial autônoma e não permite preterir antecipada já válida. R5-09–10, 17 e 22; regressões preservam os gastos distintos das especiais.
- Substituição/entrada adicional, mesmo corpo/corpo novo e Movimento/básica transferível: regressões anteriores repetidas; R5-20 verifica que retorno e novo ciclo não restauram uso próprio limitado.
- Preparação/deslocamento: R5-01 verifica a ordem passagem → resultado → cobertura; R5-02–08 verificam impedimento, falha, continuidade voluntária e ausência de armazenamento.
- Coletiva: R5-25–31 distinguem Avançar sem gasto, Avançar que gasta e dispensa expressa; as preparações e a resposta de outro corpo respeitam a mesma reserva.
- Intenção persistente/primeira intenção/orientação posterior: os casos executáveis anteriores continuam passando; a nova opção não dispensa coerência (R5-16). O programa não interpreta a intenção em linguagem natural.
- Proibição de Bônus: R5-11–13 recusam a opção convertida sem apagar a básica para outras ações permitidas.
- Preparada/antecipada: a janela da porta foi adicionada somente à preparada; a antecipada conserva seu método e suas regressões.

Não foi identificada contradição nos cruzamentos exercitados. Isso não prova exaustividade, equilíbrio ou fidelidade a toda situação possível de mesa. Fichas incompletas, exceções específicas e parâmetros não foram inventados para fechar cenários.

## Preservação e leitura

A r5 incorpora §§41–45 no corpo do texto e remove marcações obsoletas de pendência. Para leitura corrente substitui r4 + complemento 24 + bloco 23; todo o histórico permanece.

Os três scripts herdados e as referências copiadas são conferidos por hash com a r4. A preservação dos arquivos da r4 é comparada ao ZIP histórico, cujo hash coincide com o registrado na entrega r4; o resultado está em `VERIFICACAO-INTEGRIDADE.json`. O manifesto identifica cada arquivo da entrega.

O projeto principal, manual, regras gerais e Caminhos não foram editados. Não houve commit ou push. Nenhuma regra de Evocador, Trilha, construtor, catálogo, preço ou orçamento foi criada. Energia própria e custo de substituição permanecem futuros.

## Próximo uso

Pronta para continuidade da integração delimitada e ensaio em mesa, sem decisão autoral bloqueante para este conjunto. Ainda não é aprovação integral da candidata, autorização de migração ao principal ou fechamento equilibrado do subsistema. Astra médio é suficiente para a continuidade delimitada; auditoria estrutural ampla pode justificar esforço alto.
