# Prompt para retomar o RPG da Guilda em conversa nova

*Atualizado ao fim da v0.42. Copie daqui para baixo.*

---

Este é o RPG da Guilda — um sistema de RPG de mesa de Jujutsu Kaisen para um
server de guilda com 5 a 7 mestres ativos e personagem persistente entre mesas.
Você está pegando o projeto no meio de uma peça.

Antes de escrever qualquer coisa, faça esta sequência inteira e me relate cada passo.

## 1. LEIA, NESTA ORDEM

- `README.md`, em especial "Nove lições que custaram erro". Elas são a fonte
  única e não têm cópia em lugar nenhum.
- `sistema/ESTADO-ATUAL.md` INTEIRO. Ele é grande e a leitura pode truncar — se
  vier aviso de leitura parcial, continue do offset em vez de responder pela
  primeira página.
- `logs/CHANGELOG.md` de cima até a v0.33. A entrada do topo é a mais recente, e
  ele carrega o PORQUÊ de cada decisão — é a única parte do projeto que não dá
  para reconstruir lendo o resto.

## 2. RODE OS VALIDADORES

De dentro de `sistema/03-mecanica/`, que é o que o `subir.sh` faz. Depois o
`conferir-repositorio.py` da raiz. São **treze + um**, e mais dois em
`manual/matematica/` (`pac7.py` e `v7.py`) = dezesseis.

Me diga quantos passaram e se algum imprimiu PULADA — verde que pulou checagem
não prova nada. Sem `python-docx`, três deles pulam e saem com código 0:
`conferir-nomes` pula 3 de 5, `conferir-manual` pula 4 de 4 (todas, ele sai no
`except ImportError`) e `conferir-pericias` pula 1 de 8.

## 3. NÃO RODE GIT

Deste sandbox o git sai com "loose object is corrupt" e o repositório está
inteiro — é o mount. Pior: `git status` cria um `.git/index.lock` que você não
consegue apagar, e lock preso trava o `./subir.sh`. Commit é sempre meu.

**E o mount às vezes some com um arquivo que ele mesmo acabou de gravar.**
Sintoma: `ls` e `stat` mostram tamanho e inode certos, `open()` devolve ENOENT,
os vizinhos abrem normalmente. Aconteceu duas vezes na v0.42. O conteúdo nunca
está em risco — **qualquer escrita nova reconcilia**, e uma edição de uma linha
basta.

---

# ONDE O TRABALHO PAROU

**EQUIPAMENTO está em andamento**, e o estado dela mora em
`sistema/03-mecanica/RASCUNHO-equipamento.md`. **LEIA ESSE ARQUIVO INTEIRO**
antes de propor qualquer coisa — ele tem as decisões já tomadas com o número de
cada uma, o que foi rejeitado e por quê, e a lista do que falta. Não refaça nada
que está lá; a conta já rodou.

## Fechado na v0.42

- **O teto de Defesa tem dono, e não é o que o rascunho supunha.** O `20` é
  **derivado** de três números que já têm dono — `10` (peça 1 §5), teto de
  atributo `6` e teto de refino `10` (peça 2 §3), e a fórmula de cobrir-se
  (peça 11 §5). Zero parâmetros livres, então **ninguém escreve o número**.
  Equipamento é dona do **invariante**: *nenhuma montagem de equipamento passa
  da Defesa que a rota sem equipamento alcança.* **Equipamento topa em 19**, por
  decisão.
- **Duas classes de uniforme** com escadas de Força **separadas** — `Traje`
  `— / — / 3`, `Revestimento` `3 / 4 / 6`.
- **O Traje é sob medida**: proteção 1/2/3 mais **vantagem numa situação**, com
  lista fechada de oito e **uma vaga aberta** para o jogador inventar a dele,
  governada pela mesma régua de três itens. O ofício **`Alfaiate`** entrou para
  fabricar (os ofícios foram de dez para onze).
- **Escada de escudos** com proteção, requisito de Força e teto de Destreza. O
  degrau 3 é o primeiro item do catálogo a cobrar ponto de marco.
- **Treze categorias, 52 armas.** A categoria carrega **uma coisa só: a fonte do
  dano**. Se carregasse número próprio, o valor viraria `classe + categoria +
  propriedade` e a matriz teria de rodar sobre o produto dos três.
- **As oito propriedades escritas.** `Alcance` e `Longo Alcance` com número em
  metros; `Par` (role dois dados de dano, fique com o melhor); `Versátil` (o
  dado sobe um passo); `Oculta` (camada 1 · Permissão); `Munição` (1–2 natural
  ou a cada X, **recarregar é Ação Bônus**); `Fineza`; `Duas mãos`.
- **Dado do tiro**: 3d10 no topo, descendo até 2d8 na pistola.
- **A dívida da peça 11 e da peça 8 foi APLICADA** — o escudo **soma** com
  cobrir-se em vez de desligar, e o preço da Reação virou agnóstico de fonte.
  Três checagens novas no `conferir-criacao.py` guardam as duas.

## Em aberto, e é por aí que se retoma

1. **A classe das doze armas novas** — Rapieira, Espadão, Maça, Machadinha,
   Manriki, Chakram, Chicote, Hankyū, Daikyū, Besta de Uma Mão, Rifle de
   Precisão, Metralhadora Pesada. Nenhuma tem dado nem Força mínima.
2. **A pergunta que a `Fineza` abriu: o preço mora na classe ou na arma?** O §5
   fecha com *"o preço mora na classe"*, e uma propriedade que a Rapieira tem e o
   Machete não **põe preço na arma** — troca 8 classes para conferir por 52
   armas. Ou a régua ganha exceção escrita, ou as propriedades soltas viram
   classes próprias. **A matriz por valor total não roda até isso fechar.**
   *E a `Fineza` deve ir para mais armas — Lâmina Curta inteira e boa parte do
   Arremesso.*
3. **O validador da peça.** Ele precisa rodar dominância **por valor total e uma
   vez por rota de proteção — e são TRÊS, não duas**: cobrir-se, uniforme, e
   **sem energia nenhuma** (Restrição Celestial pelo ramo da Maki, que não tem
   cobrir-se para desligar).
4. **As quatro vagas de Desliga da peça 13**, que esperam esta peça desde a v0.39.

## E uma ideia em validação, fora da peça

**Rolagem de defesa ("bloquear") em sinergia com a Defesa estática** — em vez da
sua Defesa, você rola `1d20 + Destreza + proteção`. Já foi medido:

- Vale **+2,5pp** no parelho, e o ganho **encolhe sozinho** conforme a proteção
  cresce (zero em proteção 5). Auto-regulado, que é a melhor propriedade dele.
- **De graça vira automático** (reprova no teste do bônus automático);
  **custando a Reação vira letra morta** (perde de 8× a 12× para a RD de
  cobrir-se). A janela é estreita dos dois lados.
- Como balanceamento **reprova**; como **textura passa**: 25% de tráfego, um em
  cada quatro golpes muda de resultado por causa do dado.
- **Proposta em aberto: bloquear é o que o escudo faz.** Deixa de ser grátis sem
  custar Reação (você pagou na criação, com Força e teto de Destreza), corta o
  custo de mesa, e dá ao escudo a identidade ativa que o §4 procurou e não achou.
- **Lacuna que a regra precisa fechar:** um 20 natural pode ser bloqueado?

---

# COMO EU GOSTO DE TRABALHAR

- **Escolha de sabor é minha**: quantos itens numa lista, quais são, como se
  chamam. Traga as opções com número e trade-off já calculados, e pergunte.
  Rodadas curtas, nunca uma proposta grande pronta.
- **Mas não me pergunte o que a conta responde.** Se dominância, deriva ou o
  filtro multi-mestre já decidem, rode a conta e me mostre o resultado.
- **Me mostre no chat o que você escreveu**, não só no arquivo.
- **Antes de entrar numa peça ou numa Origem, me mostre o que ela já tem.**
- **Número vem de conta rodada, nunca de intuição.** Escreva o script, rode,
  mostre a tabela.
- **Pesquise antes de inventar**: como outros sistemas resolvem o mesmo problema,
  e qual o modo de falha documentado de cada um.
- **Revisão cética antes de fechar, inclusive contra o que você mesmo escreveu.**
- **Português informal, nunca de Portugal.** Documento não pode ter cara de saída
  de IA: seções de tamanhos diferentes, sem simetria forçada.

O repositório está em `https://github.com/cupcake-mochi/JJK---Project.git`.

Comece pelos três passos e me diga o que você entendeu do estado atual.
