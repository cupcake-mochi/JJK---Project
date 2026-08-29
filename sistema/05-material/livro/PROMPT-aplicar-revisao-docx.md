# Aplicar a revisão do Mizuki no `Projeto-M-Manual-da-Guilda-REVISAO.docx`

Pasta: `/media/mizuki/HD Externo II/Claude/Claude 2/`
⚠ Trabalhe na pasta PRINCIPAL, não em worktree. **Você não commita** — deixa a mensagem em
`mensagem-de-commit.txt` na raiz e avisa. Leia `README.md` (seção *"Nove lições que custaram
erro"*) e `sistema/05-material/livro/README.md` antes de mexer.

## O que aconteceu

O Mizuki abriu `sistema/05-material/livro/Projeto-M-Manual-da-Guilda-REVISAO.docx` no Word e
revisou o texto — comentários, correções, reescrita de frase, cortes. **Esse `.docx` é saída,
não fonte**: ele é gerado de `sistema/05-material/livro/manual/*.md` (18 capítulos numerados +
3 peças de frente) pelo `build_docx.py`. As edições dele precisam voltar para o markdown, e daí
os quatro artefatos são regerados.

**Pergunte a ele onde está o arquivo editado** — se sobrescreveu o mesmo `.docx` ou salvou uma
cópia — antes de começar.

## O mapa: qual arquivo `.md` é qual capítulo

*A ordem e os títulos são de `build/build.py`, que é o dono — se este mapa e aquele arquivo
discordarem um dia, `build.py` vence.*

**Frente, sem número:**
`05-introducao.md` (Bem-vindo à Guilda) · `07-glossario.md` (O vocabulário do sistema) ·
`08-inicio-rapido.md` (Antes da primeira sessão)

**Capítulos 1 a 18, nesta ordem:**
`10-como-jogar.md` · `11-o-turno.md` · `12-pericias-e-oficios.md` ·
`15-dano-e-condicoes.md` · `70-descanso-e-recuperacao.md` · `20-criacao-de-personagem.md` ·
`25-origens.md` · `35-caminhos-e-trilhas.md` · `40-fundamento.md` · `42-tecnica-marcial.md` ·
`43-sem-tecnica.md` · `45-aptidoes-e-refino.md` · `47-bencaos-e-lapidacao.md` ·
`50-equipamento.md` · `55-ferramenta-amaldicoada.md` · `60-invocacoes.md` · `65-pactos.md` ·
`80-experiencia-e-progressao.md`

## O método

1. **Extraia o `.docx` editado para texto**, para poder ler o que mudou sem abrir Word:
   ```bash
   cd sistema/05-material/livro/build
   python3 docx2md.py <caminho-do-docx-editado> /tmp/revisado.md
   ```
   *Isso não substitui ler os comentários do Word se houver — comentário pode carregar uma
   instrução que não vira texto corrido ("trocar isso por aquilo", "cortar este parágrafo").
   Se o Mizuki usou Track Changes ou comentários, você vai precisar abrir o `.docx` de outro
   jeito para lê-los (é um `.zip`; *word/comments.xml* dentro dele tem os comentários, se
   existirem) — pergunte a ele se usou.*

2. **Para cada capítulo que mudou, ache o arquivo `.md` correspondente pelo mapa acima**, e
   **salve o "antes" ANTES de editar**:
   ```bash
   cp manual/<arquivo>.md /tmp/antes-<arquivo>.md
   ```

3. **Aplique a edição do Word no `.md`**, preservando a sintaxe que o `.md` já usa — negrito
   `**assim**`, blocos de regra `>`, tabelas com `{: .tab-titulo }` embaixo, `` `crases` `` em
   termo de sistema. *O texto extraído do `.docx` pelo `docx2md.py` não tem essa sintaxe de
   volta perfeita — leia a INTENÇÃO da edição (o que o Mizuki queria dizer) e escreva ela na
   sintaxe do markdown, não copie o texto extraído literalmente.*

4. **Depois de cada arquivo editado, rode a guarda de números**, e leia CADA diferença contra a
   linha que a carregava antes de aceitar:
   ```bash
   python3 build/guard_numeros.py /tmp/antes-<arquivo>.md manual/<arquivo>.md
   ```
   **Isto é o que existe para pegar erro que ninguém vê**, e a régua do projeto é dura sobre
   isso — ver `METODO-passada-de-texto.md` na mesma pasta. Número que aparece é acréscimo,
   número que **some** é regra apagada sem querer. Se uma diferença não bater com o que você
   sabe que o Mizuki pediu, pare e pergunte antes de aceitar.

5. **Uma revisão de texto NUNCA muda número de regra.** Se a extração do `.docx` sugerir que
   um valor mudou (um dado, uma porcentagem, um preço), **isso não é revisão de texto — é
   mudança de mecânica**, e não deve ser aplicado sem confirmar com o Mizuki que era essa a
   intenção. A `pesquisa-antes-de-propor` e o `design-mecanicas-rpg` são as skills para esse
   caso, não este prompt.

6. **Depois de todos os arquivos editados, rode os quatro builds:**
   ```bash
   cd sistema/05-material/livro/build
   python3 build.py            # PDF coluna única
   python3 build.py --duas     # PDF duas colunas
   python3 build_docx.py       # regera o .docx de revisão — o mesmo arquivo que o Mizuki editou
   python3 build_txt.py        # texto corrido
   ```

7. **Confira a voz e os validadores:**
   ```bash
   cd sistema/05-material/livro && python3 conferir-voz.py --estrito
   cd ../../.. && python3 conferir-repositorio.py
   ```
   *`conferir-voz.py --estrito` tem de sair `0`. `conferir-repositorio.py` provavelmente vai
   acender a 7.5 (builds atrasados) até você rodar os quatro builds do passo 6 — depois disso
   ele deve sair limpo ou só com o aviso de sempre (a lista branca da 7.2, se aplicável).*

8. **Reporte página e palavra antes/depois**, e **mande o PDF de duas colunas para o Mizuki**
   antes de ele fechar a versão — é o hábito da casa.

## O que NÃO fazer

- Não corte narrativa ou material de mestre por conta própria — isso é passada de texto, e tem
  método próprio (`METODO-passada-de-texto.md`). Este prompt é para **aplicar** as edições que
  o Mizuki já fez, não para fazer uma passada nova.
- Não rode git desta pasta — a mensagem de commit fica em `mensagem-de-commit.txt` na raiz.
- Não mexa no manual do Fundamento (`manual/`, fora de `sistema/05-material/`) — é outro
  arquivo, gerado de código (`manual/gerador/part*.js`) e não tem relação com este `.docx`.
