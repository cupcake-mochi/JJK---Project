# Integração dos validadores R53

O texto e os dois PDFs correspondem à R53 publicada, com 411 páginas. BLOCOS-R53.json preserva os 576 blocos finais. O registro de alterações contém 202 blocos com antes e depois, incluindo as remoções. FONTE-PUBLICADA.json guarda a impressão digital do texto completo, incluindo títulos.

A revisão local atualiza a leitura de catálogo, as contas comuns e as interfaces com Emanador, Ritual, Sem Técnica, Técnica Marcial e entidades. A edição do livro permanece intacta nesta tarefa.

## Executar

Na raiz do repositório, execute:

```sh
python3 sistema/03-mecanica/conferir-fundamento.py
python3 conferir-repositorio.py
python3 sistema/05-material/livro/ciclo-maldito-r41/revisao-de-regras/fundamento-r53/testar-integridade.py
bash bestiario/ferramentas-claude-2/valida.sh
```

O último comando executa a bateria inteira em série, sem commit. Os comandos pac7.py e v7.py são entradas de compatibilidade para a conferência atual.

## Conta em JSON

EXEMPLO-MONTAGEM-R53.json contém uma montagem com dano e cura. Execute:

```sh
python3 manual/matematica/validador-feiticos.py sistema/05-material/livro/ciclo-maldito-r41/revisao-de-regras/fundamento-r53/EXEMPLO-MONTAGEM-R53.json
```

O campo funcoes informa os efeitos registrados. distribuicao reserva pontos inteiros para cada função variável: dano, cura e vida_temporaria. A saída apresenta as parcelas, o saldo sem uso e as bases pagas. Melhorias e Restrições precisam usar nomes publicados. Longe e Maior exigem modalidade; Condição exige a condição escolhida. As famílias publicadas são lidas do livro.

Esta conta cobre Classes 1 a 7. Classe 0 e as máximas têm procedimentos próprios. A validade da conta depende também da revisão dos requisitos e dos procedimentos de cada peça. A ferramenta não arbitra a compatibilidade narrativa de uma criação própria. Mesclas com Controle limitado e parcelas de outras funções pedem revisão da origem dos pontos descartados.

## Conferência editorial legada

O verificador de voz ainda lê o manuscrito antigo. Seus 34 achados preexistentes foram conferidos contra a base R52, sem alteração dos arquivos desse manuscrito. VOZ-LEGADA-R52.json registra cada achado. O modo --legado-sem-regressao reprova qualquer mudança nesse inventário e mantém as demais guardas estritas. O modo --estrito continua acusando as 34 pendências.

O resultado legado não certifica o texto ou a diagramação da R53. A tarefa atual não modifica os PDFs nem a cadeia antiga de composição. A ficha digital está sendo atualizada em outro chat.

Os resultados completos estão em VALIDACAO-LOCAL.json.
