# Projeto M · construir a ficha digital

Documento de passagem para uma conversa nova. Ele existe para que alguém que nunca viu este sistema consiga sair do zero até uma ficha de personagem funcionando, sem ter que reconstruir o contexto lendo repositório inteiro.

---

## 1 · O que é o Projeto M

Sistema de RPG de mesa de Jujutsu Kaisen, base d20, feito para **um servidor de guilda com cinco a sete mestres ativos e personagem persistente entre mesas**. Esse detalhe é o que decide quase tudo: a mesma ficha senta em mesas diferentes, com mestres que nunca conversaram, e precisa produzir o mesmo número nas duas.

Toda ficha nasce no **nível 2**, com **Grau 4** de patente. O teto é o nível 30.

---

## 2 · Onde está cada coisa

| fonte | o que é | quando usar |
|---|---|---|
| `Projeto-M-Manual-da-Guilda.pdf` | o manual jogável, 199 páginas, 16 capítulos | **é a referência principal.** Regra que vale na mesa está aqui |
| `github.com/cupcake-mochi/JJK---PDF---RPG` | pacote de entrega: `regra/` (19 peças), `desenho/`, `manual/`, `ficha/` | quando o PDF não bastar, ou para conferir número |
| `github.com/cupcake-mochi/JJK---Project` | repositório de trabalho, com CHANGELOG de 700 KB | **evite.** É argumento de design e histórico de decisão |
| ficha-em-branco.docx | a ficha de papel, que é a especificação de layout. Fica em ficha/, no pacote de entrega | **é o molde a digitalizar** |
| ficha-exemplo-kaori.docx | uma ficha preenchida de nível 2. Fica em ficha/, no pacote de entrega | caso de teste pronto |

> **Regra de ouro ao ler o repositório.** As peças de `regra/` **não são texto de mesa**: são argumento de design, com mais parágrafo de justificativa do que de regra. Texto riscado, bloco começando com "Corrigido na vX" e nota em itálico são **história** — registram o que a regra era. O PDF já fez essa transposição; prefira ele.

---

## 3 · Divergências conhecidas entre a ficha de papel e o manual

**Isto é o mais importante deste documento.** A `ficha-em-branco.docx` é mais antiga que o manual, e diverge em três pontos. Onde os dois discordam, **o manual vence**.

| assunto | a ficha .docx diz | o manual v7.10 diz | use |
|---|---|---|---|
| **Famílias de Melhoria** | Ataque · Área · Controle · Castigo · Amparo · Corpo · Movimento · Auxiliares · Percepção | Alcance · Área · Mira · Controle · Auxiliares · Castigo · Tempo · Marca · Amparo | **o manual** |
| **Ofícios** | 10 | 11 | **o manual** |
| **Legados por ficha** | "um só, na criação" | **dois**: um Destranca obrigatório, mais um de qualquer formato | **o manual** |

Se aparecer uma quarta divergência durante o trabalho, **pergunte antes de escolher um lado**. Não decida sozinho qual está certo.

---

## 4 · A anatomia da ficha

A ficha de papel tem quatro blocos, e a digital deve manter a mesma divisão.

### Bloco 1 · Identidade e números

Campos de escolha: nome, jogador, patente (começa Grau 4), Caminho, Trilha, Origem, nível (começa 2), XP.

**Os cinco atributos**, escala 0 a 6. Na criação: **nove pontos entre os cinco, nenhum acima de 3**. O número *é* o modificador; não existe valor separado nem tabela de conversão.

**Os números derivados — nada aqui é escolha, tudo é fórmula:**

| campo | fórmula |
|---|---|
| Vida | `(inicial do Caminho + Con) + (por nível do Caminho + Con) × (nível − 1)` |
| Energia (PE) | `PE por nível do Caminho × nível` |
| Integridade | `20 + (Essência + 5) × (nível − 1)` |
| Defesa | `10 + Destreza + proteção` |
| Iniciativa | `d20 + Destreza` |
| Deslocamento | `9 m` |
| Maestria | `1`, e sobe `+1` a cada oito níveis (chega a 4) |
| CD de feitiço | `10 + atributo da técnica` |
| Ataque de conjuração | `d20 + atributo da técnica + maestria` |
| Ataque corpo a corpo | `d20 + Força` |
| Ataque à distância | `d20 + Destreza` |
| Perícia treinada | `d20 + atributo + maestria` |
| Perícia sem treino | `d20 + atributo` |
| Teste de Resistência | `d20 + atributo do TR`, mais `2` se treinado |

**Vida e PE por Caminho:**

| | Bastião | Vanguarda | Guia | Evocador | Emanador |
|---|---|---|---|---|---|
| Vida por nível | 7 | 5 | 5 | 4 | 4 |
| PE por nível | 4 | 5 | 5 | 6 | 6 |

Duas travas que a ficha digital precisa respeitar:

> **Arredondamento é sempre para o lado que não te favorece.** Custo sobe, ganho desce, e o que você ganha nunca fica abaixo de 1.
>
> **A proteção 1 inicial não é equipamento.** Ela é `cobrir-se de energia`, aptidão gratuita do refino 1, e vale `1/3 do refino + 1`. Vestir Traje, Revestimento ou escudo **desliga** ela.

### Bloco 2 · Perícias, ofícios e Testes de Resistência

**23 perícias**, cada uma com atributo fixo. Constituição não tem perícia. Uma ficha treina **oito** (Caminho dá duas fixas mais quatro à escolha; Origem dá mais duas).

**11 ofícios**, e ofício **não tem atributo fixo**: o mestre escolhe na hora, conforme o que você está fazendo. Ofício sem treino você não tenta.

**Quatro Testes de Resistência**, dois treinados: Físico (Força **ou** Destreza, travado na criação), Vigor (Constituição), Intelecto (Inteligência), Espírito (Essência).

### Bloco 3 · A técnica (Fundamento)

É a camada mais complexa e a que mais se ganha em digitalizar, porque tem aritmética de verdade.

- **A Regra**: uma frase, verificável pela mesa, sem número. Nunca muda.
- **Descrição** e **tipo de dano**.
- **Famílias**: duas Livres (Melhoria custa metade da Classe a menos, mínimo 1) e três Fechadas (não compra nada delas). Use a lista do manual, não a do .docx.
- **Selo**: o gesto ou condição obrigatória. Não custa nem devolve ponto.
- **Passiva Livre**: uma, de graça.
- **Feitiços**: `Pontos = 3 × Classe`; cada ponto não gasto vira `1d8` de dano; `Custo em PE = 3 × Classe`. Melhoria custa (`Leve` = metade da Classe, `Média` = a Classe, `Pesada` = Classe e meia, arredondando para cima); Restrição devolve, no máximo `2 × Classe`, e **só paga Melhoria, nunca vira dano**.
- No nível 2: Classe 1, **dois feitiços de Classe 0** (grátis, não ocupam espaço) e **três feitiços conhecidos**.

> **A validação de feitiço é a melhor coisa que uma ficha digital faz aqui.** As oito regras de ouro do capítulo de Fundamento são checáveis por código: orçamento fechado, teto de dano, limite de Melhorias e Restrições por Classe, devolução máxima, nada de duas Restrições de frequência, e Restrição que o Selo já obriga não devolve ponto.

### Bloco 4 · Quem é essa pessoa

Aparência, história, o que a Origem deu, o traço, **os dois Legados**, laços, o que a instituição sabe, pacto (opcional). **Nada aqui rola dado**, e é a página que faz o personagem ser reconhecido numa mesa em que nunca jogou. Numa guilda com sete mestres, ela não é enfeite.

---

## 5 · Escolher a plataforma

**Isto se decide na conversa, com o dono do sistema.** Não presuma. As opções realistas, com o trade-off de cada uma:

| plataforma | a favor | contra |
|---|---|---|
| **Planilha** (Google Sheets / Excel) | fórmula é nativa; qualquer mestre edita; compartilhar é trivial; zero hospedagem | fica feia; validação de feitiço é limitada; catálogo grande vira aba difícil de navegar |
| **HTML de arquivo único** | roda offline no navegador; cabe num arquivo; visual sob controle; dá para embutir catálogo inteiro | salvar exige `localStorage` ou exportar JSON; sem sincronizar entre pessoas |
| **Bot de Discord** | o servidor é o lugar onde a guilda já vive; rolagem no mesmo canal da mesa; o dono já tem experiência com isso | ficha em chat é ruim de ler inteira; precisa de banco e de hospedagem |
| **Foundry VTT** | é VTT de verdade: mapa, rolagem, automação; sistema custom é suportado | curva alta; exige licença; só serve quem já usa Foundry |
| **Roll20** | popular, baixo atrito para jogador | ficha custom é limitada e chata de manter |

**O que perguntar antes de escolher**, porque cada resposta elimina opções:

1. A guilda joga por onde? Discord, VTT, presencial?
2. A ficha precisa ser **preenchível pelo jogador** ou **gerada** a partir de escolhas?
3. Precisa **validar** as regras (recusar ficha ilegal) ou só guardar o que foi digitado?
4. Precisa **sincronizar** entre mestres, já que o personagem atravessa mesas?
5. Precisa **imprimir** bonito, ou é só de tela?

> Se a resposta for "o personagem atravessa mesas e vários mestres precisam ver", isso empurra forte para uma coisa com estado compartilhado, e derruba o HTML solto.

---

## 6 · Ordem de construção sugerida

Independente da plataforma, esta ordem evita retrabalho:

1. **Os números derivados primeiro.** São fórmula pura e não dependem de catálogo nenhum. Uma ficha que só calcula Vida, PE, Defesa, CD e ataques já é útil.
2. **Perícias, ofícios e Testes de Resistência.** Listas fechadas, com atributo fixo.
3. **A camada de escolha**: Origem, Caminho, Trilha, os dois Legados. Aqui entram catálogos, e é onde a plataforma começa a doer.
4. **O Fundamento e a montagem de feitiço.** Deixe por último: é a parte com aritmética e validação, e a que mais se beneficia de já ter tudo o resto funcionando.
5. **A página de ficção.** Campos de texto livre, sem regra.

**Teste com a Kaori.** A `ficha-exemplo-kaori.docx` é uma ficha de nível 2 já preenchida e conferida: Força 3, Constituição 2, Destreza 2, Inteligência 1, Essência 1, com o TR Físico travado em Força. Se a sua ficha digital reproduzir os números dela, a base está certa.

---

## 7 · Coisas que ainda não têm regra fechada

Não invente regra para nenhuma delas. Deixe o campo aberto, ou marque como pendente.

- **O nível 27 da Trilha `Arremate`**: casa vaga de propósito.
- ~~**`Parrudo`**, a segunda opção da `Sintonia` do Evocador: diz "mais vida" sem número.~~ ***FECHADO na v0.185:*** ele vale **`5 ×` a sua maestria**, e o número está no `DESENHO-caminhos.md` e no capítulo 35, com o `conferir-catalogo.py` comparando os dois.

> **Esta lista tinha cinco itens e três fecharam, em versões diferentes.** *As três Trilhas do Evocador — `Servo`, `Matilha` e `Coro` — fecharam na **v0.164**, e com elas as quinze Trilhas. **Pactos** fechou na **v0.134**, e é a peça 22. E a última das nove rotas de Origem fechou na **v0.168**: a `Técnica Marcial` é a peça 20, desde a v0.122, e `Sem Técnica` é a peça 25.*
>
> **O `Estilo da Sombra` nunca virou peça** — ele virou a semente `Domínio Simples` da peça 25, que a peça 11 §6.5 já publicava desde a v0.29.

---

## 8 · Como trabalhar com o dono do sistema

- **Escolha de sabor é dele**: quantos itens numa lista, como se chamam, em que ordem aparecem. Traga opções com o trade-off calculado e pergunte, em rodadas curtas. Não entregue uma proposta grande pronta.
- **Não pergunte o que a conta responde.** Se dá para medir, meça e mostre o resultado.
- **Mostre o resultado no chat**, não só no arquivo.
- **Português informal do Brasil.** Nunca português de Portugal.
- **Nunca edite nem comite nos repositórios.** Trabalho vai em diretório próprio; entrega é por envio de arquivo.
