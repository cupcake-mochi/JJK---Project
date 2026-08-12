# RASCUNHO — Equipamento

**Não é peça.** Sem número na frente de propósito: meia peça não é peça, e um arquivo com dois dígitos quebraria a contagem do `conferir-repositorio.py`. Vira a peça 14 quando fechar, junto do validador dela — que ainda não existe e por isso não é citado pelo nome aqui.

Peça 2 da fila decidida na v0.36. Destrava a Vanguarda, a Técnica Marcial e **quatro das sete vagas de Desliga** da peça 13.

---

## 1. O que travava, e por que a resposta óbvia não servia

`Defesa = 10 + Destreza + proteção`, e a peça 11 §9 deixou o recado: *"um uniforme precisa valer mais que proteção 4, senão ele nasce morto."*

**Esse recado é orientação, não invariante, e tratá-lo como invariante trava a peça.** Proteção 1 é o que está assado dentro dos 50% de acerto que a peça 1 §6 promete. Cada ponto acima disso custa 5 pontos percentuais:

| proteção | acerta, em todo nível | rodadas de combate |
|---|---|---|
| **1** | **50%** | **3,7** — a linha da peça 1 |
| 3 | 40% | 4,6 |
| 5 | 30% | 6,2 |

Passar de 4 para não nascer morto põe o acerto 20 pontos abaixo do que o sistema promete.

**E a colisão de verdade é a lição nº 1:** cobrir-se cresce `+2` no refino passivo e `+3` no especialista; armadura de número fixo cresce `0`. Um número chapado só pode estar certo num nível.

> **Decisão do Mizuki:** o uniforme **não precisa ganhar** de cobrir-se. Precisa *alcançar e ter chance de passar*. Quem investiu Destreza e refino chegar a Defesa 20 é build, não defeito.

## 2. Duas classes, e o corte é o do 4e

A peça 6 §8 já tinha escrito *"leve e pesada, com requisito de Força e limite de Destreza na Defesa"*, e o levantamento confirmou que ela estava certa.

**O modo de falha da classe do meio é documentado.** Na 5e a armadura média é *"the worst-of-both-worlds of the best light armor and the best heavy armor"*, e o conserto oficial é gastar um feat só para ela funcionar. A 4e foi para duas classes de propósito, com o corte exatamente aqui: *"light armors let you add the better of your Dex or Int modifiers to your AC. Heavy armors do not have any ability score adjustment."*

A matriz de dominância deste projeto tinha achado o mesmo por outro caminho: com três classes, a média come a pesada sempre que a Destreza passa de 2.

**A régua do 3.x, que o levantamento também confirmou:** *"armor bonus + Max Dex adds up to either +7 or +8"* — proteção e teto de Destreza são um orçamento só.

## 3. A escada — nomes escolhidos pelo Mizuki

**`Traje`** (leve) e **`Revestimento`** (pesada). Os dois saíram `LIVRE` na triagem e não aparecem no manual nenhuma vez.

| degrau | **Traje** proteção | teto de Destreza | **Revestimento** proteção | teto de Destreza | requisito de Força |
|---|---|---|---|---|---|
| 1 | 1 | — | 4 | 0 | **3** |
| 2 | 2 | — | 5 | 0 | **5** |
| 3 | 3 | — | 6 | 0 | **6** |

**Sem gate de nível.** O orçamento de atributo faz o trabalho sozinho: o teto da criação é 3, e Força 5 só chega no nv6, Força 6 no nv10. Medido:

| requisitos | degrau 3 abre no | acerto lá |
|---|---|---|
| 3 / 4 / 5 | nv6 | 40% — cedo demais |
| **3 / 5 / 6** | **nv10** | **45%** |

*O motivo de não haver gate de nível é do Mizuki, e é de mesa:* sistema de "Custo 1 a 4" travado por nível força o personagem parrudo a usar uniforme leve porque é o que ele pode pegar, e ninguém gosta disso. Orçamento de como conseguir o item entra depois, não como trava de nível.

**O cruzamento cai em Destreza 3, igual nos três degraus** — Revestimento ganha de 0 a 3, Traje ganha de 4 pra cima. Sem classe do meio, ninguém espremido.

**E as duas rotas topam no mesmo lugar:** no nv30 com Destreza 6, cobrir-se com refino 10 dá Defesa **20**, e Traje degrau 3 + escudo dá **20**. Uma paga com sete escolhas de marco; a outra com a mão ocupada. Isso caiu da régua, não foi calibrado.

## 4. O escudo é `+1`, e agora é derivado

O custo do escudo é **a mão**, e a mão vale o que a arma de duas mãos entrega — a peça 5 mede isso em `+2` por golpe.

| nível | golpe de chefe | +1 de proteção poupa | duas mãos rende |
|---|---|---|---|
| 6 | 17 | 0,9 | 2,0 |
| 14 | 36 | 1,8 | 2,0 |
| 22 | 54 | 2,7 | 2,0 |
| 30 | 72 | 3,6 | 2,0 |

Escudo `+1` empata no meio da campanha e erra para os dois lados nas pontas. **Escudo `+2` domina:** poupa de 1,7 a 7,2, e do nv14 em diante ninguém larga o escudo.

**Duas suposições que precisam de playtest:** a conta supõe **um ataque de inimigo por rodada** — se a ameaça típica bate duas vezes, o escudo dobra de valor — e mede contra **golpe de chefe**, não capanga.

### O que o escudo NÃO custa, e eu tinha escrito errado

`Gesto` é uma Restrição **Leve**, e Leve devolve `teto(Classe/2)`. **Mas Gesto é uma de treze Leve** — Parado, Tudo ou Nada, Uma Vez, Frágil, Barulho, Assinatura, Aquecer, Peso Morto, Condicional, Fraqueza e mais. Trocar Gesto por Parado devolve exatamente o mesmo. **Perder Gesto não custa quase nada.**

**A exceção é o Selo**, e ela é de graça: o manual define Selo como *"Gesto ou condição obrigatória pra conjurar, **igual pra todos os seus feitiços**"*. Quem escolheu Gesto como Selo e pega um escudo **desliga a técnica inteira**. Trava que se aplica sozinha, sem regra nova.

## 5. Armas — o preço mora na classe

A peça 5 já provou que **o dado não é alavanca**: trocar d6 por d12 move três pontos numa lacuna de cem contra a coluna Rotina. Isso deixa o catálogo grande imune à armadilha clássica (*"o problema da longsword"*, opção-armadilha) — **porque a armadilha do hobby é sempre medida em dano.**

**A régua que fechou:** o preço é a **classe**, não a arma. O nome é sabor, e gêmea dentro da classe é de graça — decisão do Mizuki: *"não tem problema ter arma idêntica, tem vezes que a pessoa só quer um flavor diferente."*

| classe | Força mín | dado | propriedades | armas |
|---|---|---|---|---|
| **Oculta** | 0 | d4 | Oculta · Arremesso | Tanto, Punhal, Kunai, Shuriken, Tekko, Tessen, Canivete |
| **Curta** | 0 | d6 | Par | Sai, Tonfa, Nunchaku, Cassetete, Soqueira |
| **Uma mão** | 1 | d8 | — | Kama, Machete, Marreta, Machado, Taco, Wakizashi, Foice |
| **Versátil** | 2 | d8 | Versátil | Katana, Bastão, Espada Longa |
| **Haste** | 2 | d10 | Alcance · Duas mãos | Naginata, Corrente, Kusarigama, Yari, Bō |
| **Pesada** | 3 | d12 | Duas mãos | Odachi, Nodachi, Kanabō, Marreta de Obra, Machado de Bombeiro |
| **Tiro leve** | 1 | d6 | Distância · Munição · Oculta | Pistola, Revólver, Submetralhadora |
| **Tiro pesado** | 2 | d10 | Distância · Munição · Duas mãos | Espingarda, Rifle, Besta, Yumi |

**Oito classes, 39 armas. Matriz de dominância: zero classes dominadas.**

### A régua que separa arma de Caminho

> **A arma dá acesso e restrição. O Caminho dá o que você faz com ela.**

O `ESTADO-ATUAL` diz que a árvore da Vanguarda é *"o que se faz com a arma: alcance, reposicionamento forçado, troca de alvo, exceção na economia de ação"*. **Nenhuma propriedade de arma concede manobra, reposicionamento nem exceção de ação** — senão a peça 4 da fila nasce sem ter o que dar. A naginata *tem* alcance (fato do objeto); a Vanguarda *estende* o alcance (ação).

### `Precisa` (Destreza no corpo a corpo) foi rejeitada, com conta

A peça 5 §1 já mediu: `+1` de Destreza evita 2 a 7 de dano num combate de três rodadas, e um dado maior rende `+2` por golpe. Mesmo com o menor dado do catálogo, a ficha de Destreza faria 5,5 de dano contra 8,5 da arma pesada — perde 3 e ganha Defesa, iniciativa e quatro perícias. **A diferença de dado inteira vale menos que a Defesa sozinha.**

E o agravante: a peça 1 §9 tem aberto *"se Força precisa de um segundo trabalho, ela tem uma perícia só"*. `Precisa` **tira o primeiro trabalho da Força** e piora a pergunta. Corpo a corpo é Força, ponto.

### Nomes que morreram na triagem

| nome | por quê |
|---|---|
| `Lança` | está dentro de **Lança Negra**, feitiço pronto |
| `Chicote` | é feitiço pronto no manual |
| `Guarda` | é **Melhoria** no manual |
| `Faca` | a uma letra de **Fica** (Melhoria) |
| `Lastro` | a uma letra de **Rastro** (Melhoria) |
| `Proteção` | sai `LIVRE` na substring e é o **termo da fórmula da Defesa**. Batizar a categoria com o nome do valor que ela produz é "uma coisa por nome", literal |
| `Carapaça` | colide em sentido com a **Escama** e com a **Casca** que morreu |

*Controle da triagem:* `Marca`, `Passo` e `Salto` foram passados de propósito e voltaram `OCUPADO` os três — prova de que a triagem estava mesmo rodando naquela passada.

---

## 6. A dívida que esta peça deve à peça 11

**O preço da Reação de cobrir-se tem de virar agnóstico de fonte.** Hoje ela cobra *"você fica sem **a proteção passiva**"* — e quem está de Revestimento não paga isso, porque não tira o colete no meio do golpe.

O tamanho, pelos números da própria peça 11:

| nível | RD | custo hoje | saldo hoje | saldo se o preço sumir |
|---|---|---|---|---|
| 6 | 4 | 1,7 | +2,3 | +4,0 |
| 14 | 10 | 5,3 | +4,7 | +10,0 |
| 22 | 15 | 10,8 | +4,2 | +15,0 |
| 30 | 15 | 14,4 | **+0,6** | **+15,0** |

A peça 11 escolheu o `1,5 ×` com critério escrito: *"o saldo **encolhe** em vez de virar"*. Sem o preço ele sobe e trava no teto — inverte o critério.

> **Conserto decidido:** trocar *"você fica sem a proteção passiva"* por *"você fica sem proteção"*, venha ela de onde vier. Uma palavra a menos.

**Vai junto com esta peça, na mesma versão** — decisão do Mizuki. E a linha *"sem uniforme, sem armadura e sem escudo"* muda junto, porque sob duas classes ela vira `Traje`, `Revestimento` e escudo.

## 7. Em aberto

1. **A `Pesada` paga dois pontos de Força a mais que a `Uma mão` e entrega o mesmo valor líquido.** Não saiu dominada porque o `d12` é exclusivo dela, e o teste de dominância compara dado e propriedade, **não o total** — é um furo do próprio teste, e o validador desta peça precisa fechá-lo. *O argumento que a salva, e que não foi validado:* o requisito de Força é **compartilhado com o Revestimento**, então quem comprou Força 6 para vestir o mais pesado já pagou por toda arma do catálogo.
2. **Ferramenta amaldiçoada fica fora desta peça.** Decisão do Mizuki: canalizar energia já faz arma comum ferir maldição, e ferramenta amaldiçoada entra em tópico próprio, com graus e forja. A peça 5 §9 tem a pendência nomeada; a `Armaria` do Descendente e o `Enterrado` do Reencarnado a citam e são as primeiras a reler.
3. **As quatro vagas de Desliga da peça 13** que esperam equipamento — Descendente, Reencarnado, Corpo Amaldiçoado e Restrição Celestial. A peça 13 fecha dizendo *"quando equipamento fechar, a primeira coisa a fazer é voltar aqui"*.
4. **Munição:** quantos tiros, e como recarrega. Nenhum número ainda.
5. **`Versátil`:** os dois dados de cada arma versátil não estão escritos.
6. **O validador.** Checagens que ele precisa ter: a régua do orçamento por classe, dominância **por valor total** (o furo acima), a escada de proteção contra a peça 11, o requisito de Força contra a peça 2, e que todo nome do catálogo passe na triagem.

## 8. O que já foi conferido, e como

- **Regressão da régua das Restrições contra o manual:** 18 feitiços com Classe deduzida, **zero divergências**. `Leve = teto(Classe/2)`, `Média = Classe`.
- **Achado de caminho:** o `conferir-acao.py` **não abre o `.docx`** — a faixa de cada Restrição está escrita à mão dentro dele, e ele cobre **11 das 18** do manual. Ficam sem conferência: `Aquecer`, `Assinatura`, `Barulho`, `Condicional`, `Dívida`, `Fraqueza`, `Uma Vez`. Hoje não há erro; o que não há é trava. É a lição nº 9, e o conserto é uma checagem no validador dono.
- **A curva de refino do modelo reproduz sozinha o "refino 5, 4 e 3"** que a peça da Expansão usou no nv10 para escolher o gate — regressão contra número já publicado.
