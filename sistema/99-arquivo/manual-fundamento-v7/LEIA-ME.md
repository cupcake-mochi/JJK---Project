# Manual do Fundamento v7 — arquivado

**Nada aqui é regra corrente.** O Fundamento (técnica, feitiço, Melhoria, Restrição, Liberação Máxima, Expansão de Domínio) é regra do livro `Ciclo Maldito`, em `sistema/05-material/livro/`.

- **De onde saiu:** `manual/gerador/`, `manual/Fundamento-MANUAL-v7.docx` e `manual/Fundamento-MANUAL-v7.pdf`.
- **O que o substituiu:** o livro. Os validadores leem o Fundamento, o Catálogo e os Poderes avançados pelo `sistema/03-mecanica/livro.py`.
- **Em que versão:** deixou de ser fonte na v0.337 (decisão do Mizuki de 05/10/2026: o Fundamento passa a ter um dono só, o livro). O último validador que lia o gerador, o `conferir-expansao.py`, saiu dele na v0.351. A pasta veio para cá na v0.352.
- **Por que morreu:** o livro reconstruído reescreveu o Fundamento inteiro, e a revisão de 07 a 09/10/2026 mudou regras que este manual ainda traz na forma antiga. Dois documentos dizendo o mesmo número divergem, e este já divergiu.

**Está congelado na v7.41.** O `conferir-repositorio.py` confere que a capa (`gerador/partA.js`), o `gerador/COMO-USAR.txt` e os documentos de entrada dizem a mesma versão, e que ninguém anuncia outra.

## Onde ele diverge do livro final

Conhecido, e sem pretensão de lista completa: o raio da Expansão sem Barreiras aberta (`200 m` aqui, `199,5 m` no livro); a Expansão sem as regras dos itens 2, 4, 5, 8 e 152 da revisão; o Catálogo com `Troca` e com `De Novo` como Média.

## Quem ainda abre estes arquivos

Vinte scripts de medição, nenhum na bateria de validadores: doze em `bestiario/`, seis em `sistema/01-pesquisa/` e dois em `manual/matematica/` (`casca-sem-barreira.py` e `sobrecarga.py`). O caminho deles foi trocado na v0.352, com a saída de cada um comparada antes e depois. **Eles medem contra este manual, e não contra o livro:** o que sair deles vale para a regra de antes da reconstrução.

Dez desses scripts, todos do `bestiario/`, têm a raiz do repositório escrita por extenso (o HD do Mizuki). Eles só acham esta pasta quando aquela cópia estiver nesta versão ou depois.

## Para regerar

```bash
cd sistema/99-arquivo/manual-fundamento-v7/gerador
npm install docx
node make.js
```
