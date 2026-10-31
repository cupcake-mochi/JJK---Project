# Ciclo Maldito — R45

Integração das Origens v178 sobre a R44, concluída em 13/10/2026. **388 páginas.** R44 preservada; sem commit ou push. Comece por este arquivo: os LEIA-ME de versões anteriores são históricos.

## Entrega

- output/pdf/Ciclo-Maldito-R45.pdf — livro final.
- LIVRO-COMPLETO.md — texto consolidado editável.
- FICHAS-COMPLETAS-R45.md — modelos suplementares atualizados.
- ALTERACOES-R44-para-R45.json — 52 blocos com antes/depois, motivo e decisões.
- revisao-r45/ — mapa de decisões, fontes, testes, autorrevisão, pendências e prova visual.
- revisao-r45/ALTERACOES-DE-GERADOR-R45.json — diferenças dos scripts em relação à R44, incluindo as correções locais de continuidade.
- MANIFESTO-R45.json — hashes dos arquivos incluídos no ZIP. O SHA-256 do ZIP acompanha a entrega em arquivo separado.

## Ficha digital

Cópia com painel ORIGENS R45 e alerta de 30% do Híbrido:
https://docs.google.com/spreadsheets/d/1II2r3Yex_7H5BV2SVaU80XXyvPSqX6DNwYGmoSdBoOc/edit

A ficha original não foi alterada. As outras automações herdadas não foram integralmente convertidas; os campos do painel são registro e controle, e os demais bônus devem ser conferidos pelo livro. O link histórico existente no livro foi preservado.

## Reprodução

Python com ReportLab, Pillow, pypdf e pdfplumber. Poppler é usado na prova visual. Execute na pasta desta edição:

```sh
python gerar_livro.py --strict
python conferir_livro.py --strict
python revisao-r45/testar_origens.py
python revisao-r45/testar_integracao.py
```

Fontes editoriais congeladas e camadas anteriores são dependências ativas, não arquivos descartáveis. revisao_r45.py aplica o registro antes/depois após a R44, com conferência do texto anterior. A redação de trabalho está em revisao-r45/texto-final/. Não editar somente o Markdown consolidado esperando que sobreviva à geração. Os scripts históricos de preparação são registros; não os executar em lote. gerar_fichas.py é histórico e não exporta estes modelos R45 atualizados.

A conferência integral dos hashes da R44 depende da pasta original irmã e serve como auditoria local; o ZIP não duplica a edição anterior. O pacote contém fontes e ativos necessários à geração, mas não duplica PDFs e imagens de provas antigas.

## Limites

Veja revisao-r45/PENDENCIAS.md. Testes e leitura editorial são autorrevisão, sem playtest ou certificação de equilíbrio. PDF e Markdown são as exportações efetivas desta base; não há DOCX ativo.
