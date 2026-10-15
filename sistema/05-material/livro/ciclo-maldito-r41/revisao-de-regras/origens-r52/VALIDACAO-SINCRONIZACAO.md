# Sincronização do sistema com a R52 — 15/10/2026

O livro foi comparado integralmente com a R51 do último commit: só as três substituições do bloco `origens--legado-criar` mudaram. O PDF e o texto são cópias exatas da entrega R52. O resumo da peça 9, o gerador, as decisões e as referências da montagem R45 acompanham a retificação. As capacidades publicadas não mudaram.

Passaram os 27 validadores de regra, os dois validadores matemáticos e o `conferir-repositorio.py`. A primeira conferência acusou o recorte desatualizado; após sincronizá-lo pelo mapa do publicador, a conferência passou. Nenhum erro foi ocultado ou transformado em aviso.

Três testes negativos modificaram só a leitura do livro no processo de teste, sem gravar nos arquivos: recolocar a permissão geral de criar marcantes, recolocar o pacote próprio de família sem a delimitação e retirar a exceção expressa da Restrição corporal. Os três foram rejeitados na verificação 10.10. A cópia real do livro permaneceu idêntica antes/depois dos testes.

Os testes e seus códigos de saída estão em `VALIDACAO-SINCRONIZACAO.json`. A revisão visual da entrega está em `REVISAO-VISUAL.md`. A ficha digital não foi alterada, conforme decisão do autor.
