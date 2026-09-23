# Como o hobby de RPG de mesa resolve contra-jogo contra efeito que não erra

Pesquisa de campo — 22/09/2026
Alvo: preço e forma das quatro aptidões anti-domínio num RPG homebrew de Jujutsu Kaisen.

---

## Como ler este arquivo

Cada achado vem marcado assim:

| Marca | O que quer dizer |
|---|---|
| **[REGRA]** | Texto de regra publicado, copiado literal da fonte. Confiança alta. |
| **[NÚMERO]** | Número derivado por mim a partir de regra publicada. A conta está escrita. |
| **[FÓRUM]** | Opinião de comunidade. Vale como sintoma, não como prova. |
| **[MESA]** | Relato de playtest / post-mortem de mesa real. É o mais valioso. |
| **[NÃO ACHEI]** | Buraco declarado. |

Três coisas que valem o preço do arquivo inteiro, se você só ler uma parte:

1. **Três sistemas de JJK independentes convergiram na mesma faixa de preço** para as anti-domínio: entre **1/4 e 1/6** do custo do Domínio. Nenhum deles cobra ação cheia, nenhum deles cobra uso por dia.
2. **A Exalted 2e é o seu caso, com vinte anos de vantagem, e ela quebrou.** E depois foi consertada oficialmente com dois movimentos exatos e mensuráveis: **dobrar o preço** e **pôr teto de usos por cena**. Os números estão na seção 3.
3. **O preço real das anti-domínio de JJK, nos três sistemas, não é energia — é a ação e o pé no chão.** Todos cobram concentração, imobilidade ou proibição de usar a própria técnica. A energia é o rótulo; o custo é o turno.

---

# PARTE 1 — Homebrews de RPG de Jujutsu Kaisen, um por um

## 1.1 — D&D Wiki, *Jujutsu Kaisen Supplement* (o maior e mais completo)

- Fontes: `https://www.dandwiki.com/wiki/Domain_Expansion_(Jujutsu_Kaisen_Supplement)`, `https://www.dandwiki.com/wiki/Feats_(Jujutsu_Kaisen_Supplement)`, `https://www.dandwiki.com/wiki/Jujutsu_Sorcerer_(Jujutsu_Kaisen_Supplement)`
- Base: D&D 5e. Classe própria (Jujutsu Sorcerer), sistema de feats, Discord de manutenção ativo (link na talk page da classe).
- É de longe o material mais denso que existe. Tem as **quatro** anti-domínio com texto completo, tem refino de domínio de 1 a 1000 pontos, e tem discussão de balanceamento pública.

### O recurso base

**[REGRA]** *"You have a number of cursed energy points equal to twice your Jujutsu sorcerer Level + your Charisma modifier."*

### Como ele modela o Domínio e o acerto garantido

**[REGRA]** *"All domains require a specific hand sign for its expansion to be activated, taking a Full Turn Action to activate. All domains cost 30 Cursed Energy unless specified, and traps all creatures of your choice within range, within your barrier for 1 minute."*

**[REGRA]** Sure Hit — *"While inside your domain radius, all of your cursed techniques from the imbued innate technique will be affected by the sure hit feature. No matter what your cursed energy attack roll is, it will be considered a hit. Creatures will automatically count as having failed saving throws for your cursed technique for the purposes of dealing damage (though not for conditions or additional effects). Additionally, the range of any imbued cursed technique feature is expanded to cover the entire domain, even if it is normally touch range (…). Finally any feature which negates, reduces, or avoids attacks, saving throws, damage, or conditions do not work against a feature affected by this unless it specifically states otherwise."*

> **Isto é a lição de redação mais direta do arquivo.** O sure-hit dele traz uma cláusula de fecho: *nada que reduza ou anule funciona contra isto, a não ser que o próprio texto diga que funciona.* Ou seja, a lista de contra-jogo é **fechada e nomeada**, não é derivada. As quatro anti-domínio funcionam porque cada uma diz explicitamente que funciona. Qualquer outra defesa do livro, por mais que pareça caber, não entra. Isso mata na origem a discussão de mesa "mas minha habilidade X não deveria também…".

**[REGRA]** E o sure-hit é separado em duas coisas, que é uma distinção que o seu sistema talvez não tenha:
- **sure hit *feature*** = as técnicas do conjurador não erram.
- **sure hit *effect*** = o pulso passivo do domínio. *"Lethal sure hit effects require a Saving Throw or an Attack Roll to generally happen at the beginning of each round after they are cast."*
Domínio cujo efeito passivo não causa dano nem condição é classificado **Não-Letal** e simplesmente **não tem** sure-hit ofensivo — ele impõe uma regra de espaço. Duas categorias, duas curvas de preço.

**[REGRA]** Punição de uso — *Technique Burnout*: ao fechar o domínio, *"roll a d10 + 5. You will enter Technique Burnout for a number of rounds equal to the amount rolled. During this time, you gain 2 levels of exhaustion (…) you must pay Cursed Energy equal to the cost of the feature (before reductions) alongside its regular cost and you must make a DC 30 Constitution saving throw."* → 6 a 15 rodadas de inutilidade. O domínio é caro **depois**, não só na hora.

### As quatro anti-domínio — texto literal

**NEW SHADOW STYLE: SIMPLE DOMAIN** — pré-requisito: feat *Basic Barrier*.

**[REGRA]** *"Vow. In order to use simple domain properly, a Jujutsu Sorcerer must use the Simple Domain Binding Vow."*
**[REGRA]** *"As an action or reaction (S-2) against a cursed energy attack roll or saving throw, or domain expansion opening, or being affected by the sure hit effect of a Domain Expansion, for 5 Cursed Energy, you surround yourself with a 5 ft. barrier for 1 minute, though said barrier does not impede movement. The circle has an amount of hit points equal to half of your proficiency bonus (rounded down) times your refinement points. While inside of a Domain Expansion, the sure-hit feature and sure-hit effect is negated against creatures inside the simple domain but at the start of your turn the simple domain will take 3d12 force damage per 100 refinement the domain has. If the simple domain is reduced to 0 hit points, this technique ends."*
**[REGRA]** *"To use this technique, you must maintain concentration as if you were concentrating on a spell. You cannot react to the effects of a Domain Expansion with this feat the first time you would get the opportunity after your simple domain ends or is broken."*
**[REGRA]** O voto, na página da classe: *"While using New Shadow Style: Simple Domain you cannot move from where the simple domain was cast and you cannot use any innate technique features while concentrating on simple domain, otherwise it ends immediately."*

**HOLLOW WICKER BASKET** — pré-requisito: feat *Basic Barrier*.

**[REGRA]** *"As an action, bonus action, or reaction (S-2, V-1) against being affected by a sure hit effect of a Domain Expansion, or seeing a Domain Expansion open, for 5 Cursed Energy, you surround yourself with a barrier that only takes up your space for 1 minute. Within that radius, the sure-hit feature and sure-hit effect of the domain is negated; any one of your choice inside of the barrier is unaffected. Additionally the barrier has an amount of hit points equal to 50 times half of your proficiency bonus (rounded down), and at the start of your turn inside a domain it takes 3d12 force damage per 100 refinement the domain has. If at any point the barrier disappears or breaks anyone who was protected by it (including you) is immediately struck by the sure hit effect of the domain they're inside of if they're inside one."*
**[REGRA]** *"When you activate this feat or as a free action while it is active you may choose to continuously maintain the barrier, requiring concentration but making the barrier no longer take damage at the start of your turn. To do so you must also have two free hands and while you are concentrating those hands are occupied. You must also continuously chant to concentrate on this feat, meaning you cannot activate anything that requires you to speak while concentrating."*

**FALLING BLOSSOM EMOTION** — pré-requisito: background *Sorcerer Family*.

**[REGRA]** *"As an action or reaction (S-2) against being affected by a sure hit effect of a Domain Expansion, or seeing a Domain Expansion open, for 10 Cursed Energy, you will shroud yourself in cursed energy for 1 minute. The sure-hit feature of the Domain Expansion targetting or affecting you is negated. This prevents any Cursed Energy attack rolls from automatically hitting you and prevents you from automatically failing any Cursed Energy saves caused by the Domain Expansion. You gain a special damage reduction equal to your Charisma modifier times your proficiency bonus added twice plus your Charisma modifier times 4 that applies to the sure hit effect for the duration of this technique. If the damage from the Domain Expansion does not exceed the damage reduction, its damage will be negated (…). This feature cannot prevent the effects or damage of anything non-physical, such as a mental attack which does psychic damage."*
**[REGRA]** *"You must maintain concentration on Falling Blossom Emotion to keep it active."*

**DOMAIN AMPLIFICATION** — exige domínio completo.

**[REGRA]** *"As an action for up to half of your level (rounded up) in cursed energy, you can cover your body to 'wear' your domain in order to neutralize cursed techniques for 1 minute. (…) While active, you gain a damage reduction to Innate Techniques equal to the amount spent times 10. In addition, conditions and effects from Innate Techniques are negated against you, unless they possess an original cost (before reductions) higher than the amount spent on Amplification, or are under Maximum Output. (…) Domain Amplification works on contact with your body, and as such ranged attacks and your features that do not make physical contact will not gain the benefits (…). You cannot use Domain Amplification while your Domain Expansion is active."*
**[REGRA]** *"When you activate amplification, and while it is active, you cannot use your Innate Technique, and any active durations or effects will be stopped and interrupted."*

### O que ele cobra por ligar a defesa (o resumo que importa)

| | Energia | Ação | Trava real |
|---|---|---|---|
| Simple Domain | 5 | Ação **ou reação** (bônus a 70 de refino) | Concentração + **não pode se mover** + **não pode usar a técnica inata** + após quebrar, perde a primeira reação seguinte |
| Hollow Wicker Basket | 5 | Ação, bônus **ou reação** | Concentração + **duas mãos ocupadas** + **cantando** (não pode falar/usar nada verbal) |
| Falling Blossom Emotion | 10 | Ação **ou reação** | Concentração; **não cobre dano não-físico** (psíquico passa) |
| Domain Amplification | metade do nível | Ação | **Não pode usar a técnica inata enquanto ativo**; só funciona em contato corpo a corpo; não coexiste com domínio próprio |

**[NÚMERO]** Razão de preço em energia, contra o Domínio de 30:
- Simple Domain e Hollow Wicker Basket: **6:1**
- Falling Blossom Emotion: **3:1**
- Domain Amplification no nível 20: 10 CE → **3:1**

**[NÚMERO]** Fração do reservatório (pool = 2×nível + mod CHA):
- Nível 8 (nível mínimo do feat de Domínio), CHA 20: pool = 21. **O Domínio custa 30, ou seja, 143% do reservatório — ele é literalmente inconjurável sem ajuda.** O Simple Domain custa 24% do pool.
- Nível 20, CHA 24: pool = 47. Domínio = 64% do pool; Simple Domain = 11%; Falling Blossom = 21%.

> Lê-se: **neste sistema, abrir o domínio é o seu turno E o seu tanque. A anti-domínio é troco.** E o desenho está consciente disso — ele não tenta equilibrar pelo preço em energia, equilibra pela **barra de vida da barreira** contra o **refino do domínio**.

### O mecanismo que faz a anti-domínio não ser permanente: refino contra pontos de vida

Este é o miolo do desenho e é o que eu levaria para o seu sistema. A anti-domínio **não é um interruptor liga/desliga** — ela é uma barreira com HP que está sendo comida pelo domínio a cada rodada.

**[REGRA]** Dano por rodada que o domínio causa à anti-domínio: **3d12 de força por 100 pontos de refino do domínio** (média 19,5 por 100 de refino).
**[REGRA]** HP do Simple Domain = `(bônus de proficiência ÷ 2, arredondado para baixo) × pontos de refino do SD`, com refino do SD **limitado a 100** (125 na subclasse especialista).
**[REGRA]** HP do Hollow Wicker Basket = `50 × (bônus de proficiência ÷ 2, arredondado para baixo)` — **fixo**, não escala com refino.

**[NÚMERO]** Com proficiência +6 (níveis 17-20), metade = 3:
- Simple Domain no teto (100 de refino): 300 HP.
- Hollow Wicker Basket: 150 HP.
- Contra um domínio de 500 de refino: 15d12/rodada, média 97,5. → Simple Domain aguenta **~3 rodadas**; Hollow Wicker aguenta **~1,5 rodada**.
- Contra um domínio de 1000 de refino (o teto): 30d12, média 195. → Simple Domain aguenta **~1,5 rodada**; Hollow Wicker, **menos de uma**.

> **Este é o achado de desenho mais aproveitável da Frente 1.** A anti-domínio não anula o domínio; ela **compra rodadas**, e quantas rodadas ela compra é função de quem treinou mais. O domínio caro e refinado *vence* a anti-domínio barata — só que leva alguns turnos, e esses turnos são a janela em que o grupo tem que resolver a luta. O contra-jogo vira um **relógio**, não um **botão**.

E o sistema ainda fecha o loop nos dois sentidos:
**[REGRA]** *"Usage. The most effective way to refine your simple domain is by putting it to the test against the barrier of a Domain. Whenever your simple domain's hit points are reduced by a Domain Expansion, you will gain 1 refinement point for every 10 damage it takes."*
**[REGRA]** E o domínio ganha refino por **quebrar** anti-domínio: *"Whenever your domain breaks or overcomes a domain countermeasure from a hostile creature, it gains refinement depending on if it was Hollow Wicker Basket, Falling Blossom Emotion or Simple Domain"* → **1, 2 e 4 pontos respectivamente**.

> Esse `1 / 2 / 4` é o **ranking oficial de dificuldade do próprio autor**: Hollow Wicker é a mais fácil de furar, Simple Domain é a mais dura. Se você quiser uma ordem de preço para as suas quatro, esse é um voto publicado.

### Economia de reação — o ponto que quase ninguém olha

**[REGRA]** *"at 5th level, you have two reactions instead of one in each round of combat."*
**[REGRA]** Várias features do livro dão **reações extras dedicadas**: *"you gain 1 additional reaction only for using said reaction"* (escola Ainu, para barreiras), e a subclasse Limitless dá *"a number of additional Reactions equal to your Charisma modifier + your proficiency bonus that can be used exclusively for this feature"*.

> Ou seja: este sistema **percebeu que defesa por reação sufoca a economia de reação** e resolveu **abrindo o orçamento de reação**, em vez de baratear a defesa. É uma alavanca diferente da que você provavelmente está considerando.

### O que quebrou / o que a comunidade criticou

- **[MESA/FÓRUM]** A talk page da classe registra reclamação direta sobre o sure-hit ser incontestável: *"20°th Lv The Malevolent Shrine, when the Cleave and Dismantle are garanteed hits, i was thinking on a saving throw like the others domain to avoid the garanteed hits."* — é exatamente o seu problema, levantado por um usuário na mesa dele.
- **[FÓRUM]** Dúvida de aplicação que mostra onde o texto falha: *"i have 2 questions for the Falling Blossom Emotion feat. 1 does it still shield the user from the special sure-hit attack of a domain like Self-Embodiment of Perfection constitution save. 2 in the feat it says it does not work for melee weapon attacks so would it not work against the fish shikigami sure-hit melee attacks from Horizon of the Captivating Skandha?"* — **as duas perguntas são sobre a fronteira do que a defesa cobre.** Nenhuma é sobre o preço. Guarde isso: em mesa real, a dor da anti-domínio é **de escopo**, não de custo.
- **[FÓRUM]** Briga de edição pública sobre poder (Black Flash): *"You're increasing your damage by upwards of 130, can trigger this several times per round (…) What you have to consider is there is no balanced game at that point. A party of like, two of these guys will shatter games very easily."* Resposta do mantenedor: *"at this point all of them have insane potential."* → o projeto assumiu publicamente que o teto é alto e balanceia por paridade de absurdo, não por freio.
- **[FÓRUM]** E o mantenedor admite viés autoral: *"the Gojo and Sukuna subclasses will be a bit stronger than the others since the author is REALLY enjoying putting more and more buffs on those two."*
- **[NÃO ACHEI]** Post-mortem estruturado, changelog com números antes/depois, ou errata formal. O projeto vive em histórico de wiki e num Discord fechado; a talk page da classe diz explicitamente *"This talk page will be rarely looked at anymore, if you want answers or have suggestions about the class please use the newly made discord server."* Não entrei no Discord.

---

## 1.2 — *Jujutsu Kaisen 5e* (eidorii.com) — o segundo sistema completo

- Fonte: `https://eidorii.com/sorcery/domain-expansion/` e `https://eidorii.com/feats/barrier-technique-feats`
- Base: D&D 5e, site próprio, organizado por capítulos. Independente do D&D Wiki, mas claramente da mesma família de ideias (refino de domínio 1-1000, tabela de clash). Diverge em pontos importantes, e as divergências é que interessam.

**[REGRA]** Domínio: *"All domains require a specific hand sign for their expansion to be activated, taking a Full Turn Action (Action + Bonus Action + Movement) to activate. All domains cost 20 Cursed Energy unless specified, and trap all creatures of your choice in a 175-foot circle centered on you, creating a barrier for 1 minute."*

**[REGRA]** Sure-hit: *"While inside your domain radius, all of your innate techniques will be affected by a sure hit effect. No matter what your cursed energy attack roll is, it will be considered a hit. Creatures will automatically fail saving throws for your innate technique. This and any other effects of your domain only apply to targets that you choose inside it."*

### As anti-domínio dele — e a divergência que importa

**[REGRA] SIMPLE DOMAIN** — pré-requisito: 16+ de Cursed Energy score.
*"As an action or reaction against an attack roll or saving throw effect, spell or domain expansion opening for 4 Cursed Energy, you surround yourself with a 10 ft barrier for 1 minute. The circle has an amount of hit points equal to your proficiency bonus times twice your Cursed Energy modifier. Any damaging cursed techniques, spells, or attacks that target you or targets an area that overlaps with your simple domain, will now damage the barrier instead, reducing its hit points by the damage it would cause. **Your Simple Domain ends if you move.**"*

> **Repare: aqui o Simple Domain NÃO anula o acerto garantido.** Ele é um **para-choque de HP** — o golpe acerta, mas bate na barreira em vez de em você. É outra solução para o mesmo problema: em vez de tirar o "não erra", ele deixa o "não erra" acontecer e troca o alvo. E o preço é **você para de andar**.

**[REGRA] HOLLOW WICKER BASKET** — sem pré-requisito.
*"As an action, bonus action, or reaction against being affected by a sure hit effect of a Domain, or seeing a Domain Expansion open, for 4 Cursed Energy you surround yourself with a 15 ft barrier for 1 minute. Within that radius, the sure hit effect of a domain is negated and deals no damage. Anyone of your choice inside the barrier is unaffected. The barrier has no effect on normal cursed techniques or others entering the barrier. **It only negates sure hit effects.**"*

> Aqui **o Hollow Wicker é a anulação de verdade**, e é a única das quatro sem nenhum pré-requisito — literalmente *"Prerequisites: N/A"*. A anti-domínio mais acessível do sistema é a que o próprio texto restringe ao escopo mais estreito: **ela só faz uma coisa, e não faz mais nada.** Preço baixo comprado com escopo cirúrgico.

**[REGRA] FALLING BLOSSOM EMOTION** — pré-requisito: background Clan Sorcerer.
*"As an action or reaction for 5 Cursed Energy, you surround yourself in cursed energy to make any attack or effect with a guaranteed hit nullified and deal no damage. This technique lasts for 1 minute, but **does not affect attacks without a guaranteed hit**."*
E o modo ofensivo, separado e mais barato: *"As an action for 4 Cursed Energy, you can surround yourself in cursed energy to prepare for an attack for 1 minute. As a reaction to an attack, you can make a melee weapon attack at advantage against the attacker before the attack happens. On a hit, the attack counts as a critical hit (…). Once you make this attack, you must reactivate the technique to use it again."*

> **"does not affect attacks without a guaranteed hit"** é uma frase de seis palavras que faz o trabalho de uma página de balanceamento. A defesa perfeita **só funciona contra o perfeito**. Ela é inútil contra ataque normal. Isso é o freio mais elegante que achei em todo o levantamento — e tem eco direto na Frente 2 (é exatamente o que o *Shield* do 5e faz com Magic Missile, e o que a PF2e faz com o trait Incapacitation).

**[REGRA] DOMAIN AMPLIFICATION** — aqui **não é feat**, é um degrau de refino, o de **600 pontos**:
*"As an action for half as much Cursed Energy your domain requires, you can cover your body to 'wear' your domain in order to neutralize cursed techniques for 1 minute. (…) You will also negate a domain's sure hit effect if you're inside one. In addition, you can not use your Innate Technique unless you dismiss Domain Amplification (…). This technique does not work against techniques on Maximum Output if the user has 51 or more higher refinement than you. If they are within 50 refinement of you, you have resistance to their technique, and if they have 51 or less refinement than you, you are immune to their techniques even if they use Maximum Output."*

> Esse último bloco é um **desempate por refino em três faixas** (imune / resistente / não funciona) em vez de binário. É a resposta explícita ao problema "defesa que escala contra ofensiva que escala": **o resultado da defesa depende da diferença de investimento entre os dois lados**, e a faixa é de 50 pontos. Vale copiar a forma.

**[NÚMERO]** Razões contra o domínio de 20 CE: Simple Domain **5:1**, Hollow Wicker **5:1**, Falling Blossom **4:1**, Domain Amplification **2:1** (escrito no texto como "metade").

- **[NÃO ACHEI]** Nenhum registro de playtest, changelog, errata ou crítica de comunidade sobre este sistema. Site fechado, sem seção de comentários indexada, sem thread de fórum que eu tenha achado.

---

## 1.3 — GMBinder, *Jujutsu Class* por TrevorAco

- Fonte: `https://www.gmbinder.com/share/-NmCj8Ct6kRouiuITSGh`
- **[REGRA]** Tem Domínio (custo 0 a 20+ CE dependendo da técnica, ação, concentração, raio 100-200 ft, com save por turno para os presos) e tem os domínios canônicos escritos (Malevolent Shrine, Unlimited Void, Chimera Shadow Garden, Coffin of the Iron Mountain).
- **[REGRA]** E **não tem nenhuma das quatro anti-domínio.** Nem Simple Domain, nem Hollow Wicker, nem Falling Blossom, nem Domain Amplification.

> **Isto é um achado, não um vazio.** Uma versão inteira de JJK em 5e escolheu resolver o sure-hit **com save por turno** em vez de com contra-jogo dedicado. A saída dele é: o domínio não dá acerto garantido no sentido forte — ele impõe uma rolagem repetida de CD alta. Se o sure-hit é um save difícil e não uma certeza, o "contra-jogo" é a ficha do jogador (bônus de save) e não uma aptidão comprada. **É a alternativa estrutural ao seu desenho: ou você tem acerto garantido + anti-domínio nomeada, ou você tem save duro + nenhuma anti-domínio.** Misturar os dois seria cobrar duas vezes.

---

## 1.4 — Mod de Minecraft *Jujutsu Kaisen* (RadonCoding) — implementação digital, números duros

- Fonte: `https://github.com/RadonCoding/jujutsu-kaisen` — arquivos `ability/misc/SimpleDomain.java`, `FallingBlossomEmotion.java`, `DomainAmplification.java`, `config/ServerConfig.java`, `entity/SimpleDomainEntity.java`.
- Não é RPG de mesa, mas é **um sistema que teve que precificar exatamente o seu problema e roda com milhares de jogadores em servidor**, o que é playtest involuntário em volume. Vale como terceiro voto independente.

**[REGRA]** Reservatório base: `cursedEnergyAmount = 300.0F`, regeneração `0.25` por tick.

**[REGRA]** Custos de **desbloqueio** (pontos de progressão), em `ServerConfig.java`:

| Habilidade | Pontos |
|---|---|
| `domainExpansionCost` | **200** |
| `domainAmplificationCost` | **100** |
| `zeroPointTwoSecondDomainExpansionCost` | **100** |
| `simpleDomainCost` | **50** |
| `fallingBlossomEmotionCost` | **50** |

**[NÚMERO]** Razão de desbloqueio: **4:1** para Simple Domain e Falling Blossom; **2:1** para Domain Amplification.

**[REGRA]** Custos de **ativação** (`getCost`): Simple Domain `0.1F`; Domain Amplification `0.2F`; Falling Blossom Emotion `1.0F`.
**[REGRA]** Recarga (`getCooldown`): Simple Domain e Falling Blossom = `10 * 20` ticks = **10 segundos**.
**[REGRA]** Simple Domain é uma **entidade com raio e vida próprios**: `RADIUS = 2.0F`, `MAX_RADIUS = 4.0F`, raio real = `min(4, 2 × (1 + perícia_de_Barreira × 0.1))`; ela **absorve o dano até a própria vida acabar**:
```java
float blocked = Math.min(simple.getHealth(), event.getAmount());
event.setAmount(amount - blocked);
simple.hurt(event.getSource(), blocked);
```
**[REGRA]** E a árvore de pré-requisitos é explícita no código: o **pai do Falling Blossom Emotion é o Simple Domain** (`getParent` → `JJKAbilities.SIMPLE_DOMAIN`), e o pai do Simple Domain é o Cursed Energy Flow.

> Ou seja: três sistemas independentes (D&D Wiki, eidorii, mod) e **os três põem as anti-domínio numa faixa de 1/4 a 1/6 do domínio**, e **dois dos três fazem o Simple Domain absorver dano na barreira em vez de anular pura e simplesmente**. A convergência é forte o bastante para tratar como régua do hobby.

---

## 1.5 — Os outros que eu abri e o que tinha em cada um

- **`custom-tabletop-rpg.github.io/jujutsu-kaisen`** (alemão, em construção). **[REGRA]** *"Jede Sphären-Entfaltung ist ab einer Erfahrung von 5000 für die Fluchtechnik möglich"* — domínio destravado a 5000 de experiência na técnica. **[NÃO ACHEI]** nenhuma anti-domínio, nenhum sure-hit escrito. Sistema incompleto.
- **`The Eternal Battle of Curses`** (Leonardo Azevedo, itch.io, One-Page RPG Jam 2023). É um **RPG de uma página**. Não baixei o PDF (o download é "name your own price", ou seja, passa por formulário). **[NÃO ACHEI]** o texto de regra. Pelo formato, é praticamente certo que não tenha as quatro anti-domínio — não cabe. Comentário público do próprio público pedindo mais: *"eu gostaria de uma expansão ensinando como fazer os feitiços"*.
- **"Jujutsu Kaisen TTRPG"** (conversão do *My Hero Class 1-C*, circulando em scribd). **[FÓRUM/indireto]** o resumo que consegui diz: *domínios custam 8 seções de energia amaldiçoada e só podem ser opostos por domínios de nível igual ou maior.* → **sistema sem anti-domínio: o único contra-jogo é outro domínio.** Não consegui abrir o documento para citar literal. **[NÃO ACHEI]** o texto.
- **Wikis de RP** (`jjkroleplaying.fandom.com`, `jujutsu-kaisen-minus-one.fandom.com`): abri via API. São **enciclopédias de lore do mangá**, não sistemas com números. Não servem.
- **Busca em GitHub por TTRPG de JJK**: 1023 repositórios com "jujutsu kaisen", **nenhum** é RPG de mesa. São mods de Minecraft, APIs, landing pages, um jogo web. **[NÃO ACHEI]**.
- **[NÃO ACHEI]** conversão de JJK para **Pathfinder 2e, FATE, Savage Worlds, PbtA, Anime 5e ou BESM** com regra publicada de anti-domínio. Procurei nas três frentes e não existe material indexado. Se existe, está em Discord fechado ou Google Doc não indexado.

---

# PARTE 2 — Como os sistemas grandes tratam efeito que não erra

## 2.1 — D&D 5e: o par *Magic Missile* / *Shield*

É o único efeito verdadeiramente sem rolagem do 5e básico, e o desenho dele é uma aula de contenção.

**[REGRA]** *Magic Missile*, 1º círculo, 1 ação, 120 pés: *"You create three glowing darts of magical force. Each dart hits a creature of your choice that you can see within range. A dart deals 1d4 + 1 force damage to its target."*
**[REGRA]** *Shield*, 1º círculo, **1 reação**, alcance Pessoal: *"An invisible barrier of magical force appears and protects you. Until the start of your next turn, you have a +5 bonus to AC, including against the triggering attack, **and you take no damage from magic missile**."*

**O que funcionou, e por quê:**
1. **[NÚMERO]** O acerto garantido é **deliberadamente minúsculo**: 3d4+3 = média **10,5** de dano no 1º círculo. Uma bola de fogo do 3º círculo faz 8d6 = 28. O 5e permitiu "não erra" só num efeito cujo dano não decide nada. **Preço do "não erra" pago em potência, não em recurso.**
2. **[REGRA]** O contra-jogo é do **mesmo círculo** (1º contra 1º) e é uma **reação**, não uma ação. Custa o mesmo recurso nominal, mas ocupa uma casa mais barata da economia de ação.
3. **[REGRA]** O contra-jogo **não é dedicado**. O *Shield* é uma boa magia de qualquer jeito (+5 de CA por uma rodada). A anulação total do Magic Missile é um **bônus embutido**, não a razão de existir da magia. → **é por isso que ele nunca vira imposto**: você já ia comprar mesmo.
4. **[REGRA]** E é **assimétrico de propósito**: o *Shield* anula 100% do Magic Missile mas apenas 25% (+5 de CA) de um ataque comum. A defesa perfeita **só é perfeita contra a coisa que não erra**.

> **Padrão nº 1 do hobby, e ele repete em quatro sistemas:** *a defesa que anula o inanulável não pode ser boa contra o resto.* Amarre a anulação total ao gatilho "isto era um acerto garantido"; contra qualquer outra coisa ela dá um bônus modesto ou nada.

## 2.2 — D&D 5e: *Counterspell*, e o redesenho de 2024

**[REGRA] 2014**, 3º círculo, reação: *"If the creature is casting a spell of 3rd level or lower, its spell fails and has no effect. If it is casting a spell of 4th level or higher, make an ability check using your spellcasting ability. The DC equals 10 + the spell's level."*
**[REGRA] 2024**: *"You attempt to interrupt a creature in the process of casting a spell. The creature makes a Constitution saving throw. On a failed save, the spell dissipates with no effect, and the action, Bonus Action, or Reaction used to cast it is wasted."* — e, decisivo: **"If that spell was cast with a spell slot, the slot isn't expended."**

**O que quebrou na versão 2014** — o modo de falha é exatamente o seu:
- Abaixo de um patamar (3º círculo), a anulação era **automática e sem rolagem**: um "não erra" combatendo outro "não erra".
- O alvo **perdia o recurso mesmo assim**. Duas magias gastas, zero acontecendo. **[FÓRUM]** o vocabulário da comunidade para isso é *"counterspell war"* — os dois lados param de jogar e só trocam anulações até um ficar sem espaço.

**O que a versão 2024 fez, e é a parte aproveitável:**
1. Trocou o automático por **rolagem opostaable** (save de Constituição). Deixou de ser binário.
2. **Devolveu o recurso do lado que foi anulado.** *"the slot isn't expended"* — você perde o **turno**, não o **tanque**.
3. **[FÓRUM]** Crítica que ficou: *"this is way more frustrating because it's harder to pull off and just delays the spell instead of stopping it, while DMs can bypass the players with Legendary Resistance."* → **[MESA]** o conserto mudou quem reclama: antes reclamava quem era anulado; agora reclama quem anula.

> **Padrão nº 2:** quando a defesa anula, decida **se ela come o recurso ou só o turno**. Comer os dois é o que gera a sensação de jogada morta dos dois lados.

## 2.3 — D&D 5e: *Legendary Resistance*, e a crítica pesada

**[REGRA]** *"Legendary Resistance (3/Day): If the dragon fails a saving throw, it can choose to succeed instead."*

Uma anulação **total, automática, sem rolagem, sem custo de ação, sem custo de recurso**, limitada só por **3 usos por dia**. É o desenho oposto ao seu: em vez de barato e repetível, é gratuito e contado.

**[FÓRUM/MESA]** O que a comunidade documentou de errado:
- *"Legendary Resistances are one of 5e's most unsatisfying mechanics. They are an incredibly blunt solution that the designers had to include to counter the many annoying spells they let in the door."*
- *"The spellcaster has 3 spell slots? Well Legendary Resistance has 3 uses. Looks like you're not getting your spell off."*
- **[NÚMERO]** A conta que um analista fez do tempo de queima: *"unless another primary caster is chipping away at the BBEG's Legendary Resistances too, this strategy is going to take 6-7 rounds minimum if we assume that the boss fails half their saves… an optimistic estimate."* — ou seja, **o recurso "3 usos" leva 6-7 rodadas para ser drenado**, e a luta média não dura isso. Na prática o teto de 3 é um teto que nunca é atingido.
- Diagnóstico de fundo: *"Instead of deciding a combat in round 1, the combat is likely to be over by the time the wizard casts a spell that the BBEG doesn't save against."*

**Os quatro consertos propostos** (todos convergem numa ideia: **fazer a anulação custar alguma coisa**):
1. Virar **re-rolagem** em vez de sucesso automático: *"If the dragon fails a saving throw, it can choose to re-roll the result."*
2. Cobrar **dano**: *"the dragon takes 1d6 damage per level of the spell slot used."*
3. Cobrar **condição**: *"gives the dragon one level of exhaustion that lasts until the end of the creature's next turn"* (com exaustão 2024: −2 em tudo).
4. Cobrar **ação**: gastar uma Ação Lendária para passar no save, ou seja, **pagar em economia de ação**.

> **Padrão nº 3, e é o mais transferível para você:** uma anulação que não custa nada além de um contador de usos **não gera jogo**. Dos quatro consertos que a comunidade convergiu, **três cobram um recurso que a ficha já tem** (vida, condição, ação) em vez de um contador novo. Se as suas quatro anti-domínio hoje custam "pouco de propósito", a pergunta certa não é *quanto elas deveriam custar*, é **em que moeda**.

## 2.4 — D&D 5e: *Silvery Barbs*, o caso de defesa barata demais

Magia de 1º círculo, reação, que força uma re-rolagem (fica o pior resultado) de um ataque, teste ou salvaguarda, e ainda dá vantagem para um aliado.

**[FÓRUM]** Análise do ThinkDM: *"This spell is a new trap choice for spellcasters. You can't live without it."* E: tem *"95% chance to negate a critical hit"*.
**[FÓRUM]** Comparação registrada: é *"dramatically better than Fortune's Favor and slightly better than Shield"*; a primeira metade dela é *"basically a better version of the wild magic sorcerer's bend luck ability that they get at 6th level"* — que é uma feature de nível 6 custando 2 pontos de feitiçaria.
**[MESA]** É a magia mais banida do 5e moderno em mesa doméstica.

**Por que ela quebra e o *Shield* não:**
| | Shield | Silvery Barbs |
|---|---|---|
| Escopo | Só CA e só Magic Missile | **Qualquer** d20: ataque, teste, save |
| Só contra "não erra"? | A anulação total, sim | Não — funciona contra tudo |
| Dá vantagem extra? | Não | Sim, dá bônus a um aliado |

> **Padrão nº 4:** a defesa por reação barata vira imposto quando o **escopo é largo**. *Shield* é barato e não é imposto porque é estreito. **Preço baixo é aceitável; preço baixo com escopo largo é o que mata.** Se as suas quatro anti-domínio são baratas de propósito, a trava tem que estar no **escopo**, e escopo é escrito em uma frase — a do eidorii é o modelo: *"does not affect attacks without a guaranteed hit."*

## 2.5 — Pathfinder 2e: graus de sucesso, trait Incapacitation, e uma reação por rodada

**[REGRA] Quatro graus de sucesso**: *"You critically succeed when the check's result meets or exceeds the DC by 10 or more. (…) if you fail a check by 10 or more, that's a critical failure."* E: *"If you rolled a 20 on the die (a 'natural 20'), your result is one degree of success better than it would be."*

> Isso **elimina o binário na origem**. Não existe "acertou/errou" — existe uma escada de quatro degraus. Um efeito que "não erra" na PF2e ainda pode cair num degrau mais fraco.

**[REGRA] Trait Incapacitation** (o texto inteiro, é curto e é o mais importante do bloco): *"An ability with this trait can take a character completely out of the fight or even kill them, and it's harder to use on a more powerful character. If a spell has the incapacitation trait, any creature of more than twice the spell's rank treats the result of their check to prevent being incapacitated by the spell as one degree of success better, or the result of any check the spellcaster made to incapacitate them as one degree of success worse. If any other effect has the incapacitation trait, a creature of higher level than the item, creature, or hazard generating the effect gains the same benefits."*

> **Esta é a resposta da PF2e ao "save-or-suck" — e é estruturalmente diferente da Legendary Resistance.** Não existe um contador de usos, não existe um botão. **A resistência é automática, universal e proporcional à diferença de nível.** Todo mundo que está acima do patamar recebe um degrau grátis, sempre, e ninguém precisa comprar nada. **É uma anti-domínio que não é uma aptidão — é uma regra de escala.**
>
> Isso resolve de graça o "tax feat": se ninguém precisa **comprar** a defesa, ela não pode virar imposto. O preço é que o autor perde a possibilidade de o jogador **escolher** ser bom nisso.

**[REGRA] Uma reação por rodada**: *"You gain 1 reaction per round, and you can use a reaction on anyone's turn (including your own), but only when its trigger occurs."*
**[REGRA]** *Shield Block* (reação): *"Your shield prevents you from taking an amount of damage up to the shield's Hardness, and you and the shield each take any remaining damage, possibly breaking or destroying the shield."*
**[REGRA]** *Nimble Dodge* (reação): *"+2 circumstance bonus to AC against the triggering attack."*

**[FÓRUM]** A crítica registrada no fórum da Paizo, e é exatamente o problema de "tax feat": *"Having Shield Block be the only defensive reaction option among General feats makes every character that wants one orbit towards it, even if it doesn't fit the class fantasy."* E o porquê: *"Reaction is a MASSIVE upgrade in action economy."* A proposta: *"classes like Champion or Fighter gained a Defensive Reaction of their flavor of choice"* — ou seja, **resolver o imposto dando variedade temática da mesma função**, não removendo a função.
**[FÓRUM]** A contra-argumentação, também registrada: Shield Block *já* é caro se você contar mão ocupada + ação de erguer o escudo + reação + peso.

> **Padrão nº 5, estrutural e talvez o mais aplicável ao seu caso:** o freio da PF2e para defesa por reação **não é o preço, é o teto de uma reação por rodada.** Defesa barata é inofensiva se ela **compete com todas as outras defesas do personagem pela mesma casa**. Note o contraste com o D&D Wiki de JJK, que foi na direção oposta e **deu reações extras** — e por isso teve que equilibrar pela barra de vida da barreira.

## 2.6 — Mutants & Masterminds 3e: a única tabela de preço publicada para "anular completamente"

Este é o achado que responde direto à sua Frente 3, e é **regra publicada, não opinião**.

**[REGRA]** Efeito **Immunity**, custo **1 ponto por grau**, e a tabela do que cada faixa compra:

| Graus | O que compra |
|---:|---|
| 1 | envelhecimento, doença, veneno, uma condição ambiental, fome/sede, descritor raro |
| 2 | **acertos críticos**, todos os efeitos de sufocamento, descritor incomum |
| 5 | alteração, Aflição sensorial, emoção, aprisionamento, fadiga, perícias de interação, **um descritor de Dano específico** |
| 10 | descritor comum (frio / eletricidade / fogo / radiação / clima), suporte vital |
| 20 | descritor muito comum (contundente ou energia) |
| 30 | **todos os efeitos resistidos por Fortitude**; **todos os efeitos resistidos por Vontade** |
| 80 | **todos os efeitos resistidos por Resistência (Toughness)** — ou seja, *todo o dano* |

**[REGRA]** E a modificação que interessa: **"Limited to Half Effect"** é uma falha de **−1 ponto por grau** — *"character suffers halved effect rather than complete immunity"*. Ou seja, no M&M, **meia imunidade custa metade do preço da imunidade total.** Linear.

**[NÚMERO]** A escala em perspectiva: um herói padrão de campanha M&M começa com **150 pontos de poder** no total. Imunidade a todo o dano custa **80** — mais de **metade da ficha inteira**. Imunidade a uma categoria inteira de salvaguarda (tudo de Fortitude) custa **30**, ou **20% da ficha**. Imunidade a um tipo de dano específico custa **5**, ou **3,3%**.

> **Esta é a régua publicada que você pediu.** Traduzindo para linguagem de sistema: no único jogo mainstream que tem uma tabela explícita de preço de negação,
> - anular **um efeito nomeado e específico** custa ~3% do orçamento do personagem;
> - anular **uma categoria inteira de resolução** custa ~20%;
> - anular **tudo** custa ~53%.
>
> As suas quatro anti-domínio são "anular um efeito nomeado e específico" — a faixa de 3% a 5% do orçamento total do personagem é defensável pela régua do M&M. **Isso é um argumento independente a favor de elas serem baratas.** O que a mesma régua diz é que elas **não podem** também anular coisas fora do domínio, porque aí sobem de faixa e o preço teria que multiplicar por 4 ou por 6.

## 2.7 — Lancer

**[REGRA]** Lancer tem uma lista fechada de efeitos que não podem ser parados: certos efeitos *"doesn't count as an attack, hits automatically, ignores cover, bypasses IMMUNITY"*. A saída de contra-jogo do sistema é **mudar o eixo**: ataques de área forçam salvaguarda em vez de rolagem de ataque, então "errar" deixa de ser o conceito.
**[REGRA/FÓRUM]** E há uma crítica de balanceamento registrada que espelha o seu medo de esteira: *"one of the reasons the playerbase prioritizes Hull over Agility and Systems is that increasing these does not meaningfully decrease your odds of taking damage."* Um patch posterior *"had levels of excessive accuracy/to-hit numbers pared down, making Evasion, cover, the Impaired condition, and Lock On all more important."*

> **Padrão nº 6:** quando a ofensiva é alta demais, a estatística defensiva **deixa de ser comprada**, e o jogador migra tudo para vida. Se o seu acerto garantido é grande o bastante, ninguém investe em esquiva — investe em anti-domínio e em vida, e o resto da ficha morre. O conserto do Lancer foi **abaixar a precisão geral**, não encarecer a defesa.

## 2.8 — [NÃO ACHEI] Gloomhaven, 13th Age, Fabula Ultima

Procurei e não encontrei nada com número **e** modo de falha documentado que valesse a pena nestes três para o seu problema específico.
- **13th Age**: o *escalation die* (*"starts at 0 on round one (…) increases by 1 at the start of each subsequent round, with player characters getting to add the current value to their attack rolls"*) é relevante como mecânica de "o combate aperta com o tempo", mas **não é contra-jogo contra efeito que não erra**.
- **Fabula Ultima**: não achei nenhuma discussão de auto-acerto com contra-jogo documentado.
- **Gloomhaven**: não achei post-mortem publicado sobre o Shield contra efeitos que não erram. Não perdi mais tempo ali.

---

# PARTE 3 — Exalted e a corrida das Perfect Defenses

**Este é o seu caso, com vinte anos de vantagem.** Exalted 2e (White Wolf, 2006) tinha exatamente o desenho que você está avaliando: uma defesa barata, repetível, que anula completamente um ataque, comprada porque sem ela o jogo é letal demais. Ela quebrou o jogo de uma forma documentada com nome próprio, e recebeu um conserto oficial com números que dá para copiar.

## 3.1 — O que era a Perfect Defense

**[REGRA]** Três Charms de Solar, cada uma anulando 100% de um ataque, **reflexivas** (não gastam ação), com custos originais de 2e:
| Charm | Tipo | Custo original |
|---|---|---|
| Seven Shadow Evasion | esquiva perfeita | **3 motes** |
| Heavenly Guardian Defense | aparo perfeito | **4 motes** |
| Adamant Skin Technique | absorção perfeita | **4 motes** |

**[FÓRUM]** *"Seven Shadow Evasion costs 3 motes and allows a character to dodge an attack without any roll. It is considered arguably the best perfect defense, costing fewer motes and having only one prerequisite charm."* E: *"The Solar automatically dodges an attack, even if it is undodgeable."*

**[REGRA]** O preço de desenho não era em motes — era o **Flaw of Invulnerability**: toda Perfect Defense fica presa a uma Virtude escolhida na compra, e só pode ser ativada se a condição daquela Virtude estiver satisfeita. As quatro condições, do texto:
- **Valor**: *"must move toward the opponent he considers most dangerous, on every tick"*
- **Compaixão**: *"can only use this Charm when in the presence of someone or something he cares about"*
- **Temperança**: *"cannot take movement actions such as move, dash, flight, teleportation"*
- **Convicção**: *"does not function when a Solar's actions are contrary to his Motivation"*

**[REGRA]** E a válvula de escape: *"If the Exalt does not fulfill that requirement, the Charm may still be invoked through the expenditure of a point of Willpower."*

## 3.2 — Como quebrou, com os números

**Falha 1 — o Flaw não era um preço, era um pedágio de 5 XP.**
**[MESA/FÓRUM]** *"A Solar with Seven Shadow Evasion tied to Conviction may also purchase the Valor version by spending 5 XP (or 4 XP if Dodge is favored)."*
E a leitura crítica: *"A player can purchase the same Perfect Defense twice with different virtue flaws, effectively neutralizing the limitation unless facing highly specific circumstances."*
> **Restrição narrativa comprável não é restrição.** Se o jogador pode comprar a mesma defesa de novo com a restrição oposta, você vendeu a restrição, não a defesa. **Se você usa condição de ativação como preço, ela tem que ser única por personagem e não-duplicável.**

**Falha 2 — o custo era menor que a devolução.**
**[REGRA]** Em Exalted 2e, uma manobra descrita bem (stunt) devolve motes: *"In 2E stunts award 2-6 motes"*, à razão de 1 mote por dado de stunt concedido.
**[FÓRUM/MESA]** E o efeito prático: *"if you were attacked, you could do a stunt (regenerating 2-4 motes, occasionally 6) and spend 3 motes on Seven Shadow Evasion to avoid being hit, and if you were good at stunting, you were impossible to hit but didn't actually go down motes."*

**[NÚMERO]** A conta, com um Solar inicial padrão (Essência 3, Força de Vontade 7; Pessoal = Essência×3 + FdV = **16**; Periférico = Essência×7 + FdV + soma das Virtudes ≈ **36**; total ≈ **52**):

| | Custo | % do reservatório | Negações brutas | Com stunt de 2 motes devolvidos |
|---|---:|---:|---:|---|
| Seven Shadow Evasion (2e original) | 3m | **5,8%** | 17 | custo líquido **1m** → ~52 negações |
| Heavenly Guardian Defense (2e original) | 4m | **7,7%** | 13 | custo líquido 2m → ~26 negações |
| Perfect pós-errata 2.5 | 8m | **15,4%** | **6** | custo líquido 6m → **~8 negações** |

> **Essa tabela é a coisa mais importante do arquivo para o seu caso.** A defesa perfeita não estava "um pouco barata". Ela estava num regime em que **a devolução de recurso por narrar bem cobria dois terços do custo**, e o resultado é que ela era **efetivamente gratuita**. Um combate de 5 rodadas não chega perto de drenar 52 negações.
>
> **Teste que vale para o seu sistema: some tudo que devolve energia por rodada e compare com o custo da anti-domínio. Se a devolução passar de metade do custo, a defesa é grátis, independente do número que está escrito nela.**

**Falha 3 — motes viraram a barra de vida, e os pontos de vida viraram enfeite.**
**[MESA]** *"motes are your actual HP bar. Your health levels are a formality."*
**[MESA]** O nome que a comunidade deu ao regime: **paranoia combat**. *"The paranoia combo is a Combo that you invoke every single action in combat, using a 2-die stunt to restore the expended Willpower. This Combo costs a total of 10 XP to purchase and allows the character to perfectly defend against any attack."* E: *"Paranoia combat ends when motes run out."*
**[MESA]** A descrição do que isso vira na mesa, do lado do 3e olhando para trás: *"In 2e, every single attack was targeting health levels, making combat a long series of ineffectual swats depleting an invisible mote counter until one side ran out of motes and abruptly died from the next attack."*

> **Este é o modo de falha exato que a sua regra corre o risco de produzir, e ele tem nome.** Se a anti-domínio é boa e barata, o combate deixa de ser sobre o domínio e passa a ser sobre **quem fica sem energia primeiro**. E como ninguém toma dano até acabar a energia, a luta inteira fica **invisível** — nada muda na mesa até o momento em que tudo muda de uma vez.

**Falha 4 — a corrida armamentista, e a segunda camada de impostos.**
**[MESA]** *"2E demands you have a perfect defense array."* — não *uma* defesa perfeita, um **array**, porque cada tipo de ataque precisa de um tipo de perfeita.
**[MESA]** *"Soaking 100% of the damage of an attack doesn't stop it from applying (at least some kinds of) negative status effect, so you can't just rely on popping a Perfect Soak when you get hit; you need a Perfect Dodge/Parry so that you don't get hit in the first place."*
**[MESA/NÚMERO]** E a resposta ofensiva: o *flurry*, um ataque múltiplo, porque cada ataque do flurry tem que ser defendido separadamente — *"each activation of a flurry charm costs less motes than enough PD activations to negate it"*. Então nasceu o **flurry-breaker**, um contra-contra-jogo: *"Perfect defenses cost 8 motes, generally; and flurry-breakers are… usually 3. So, a PD+Flurry-breaker combo is 11 motes, compared to the 40 motes you would need to perfectly defend against the entire flurry."*

> **A corrida armamentista é literal e tem três andares:** defesa perfeita → ataque múltiplo para furar a defesa perfeita → quebra-múltiplo para reabilitar a defesa perfeita. **Cada andar é um imposto novo que todo mundo tem que comprar.** É isso que "rock-paper-scissors defensivo" vira quando a defesa é boa demais: não vira pedra-papel-tesoura, vira **escada de compras obrigatórias**.

**Falha 5 — a resistência a não-perfeitas.**
**[FÓRUM]** *"Non-perfect defenses are either inefficient, or unreliable."*
**[REGRA]** E o sistema **tinha** um incentivo escrito para não usar a perfeita: *"Whenever successfully evading an attack by applying Dodge DV, he gains (attacker's Essence/2, round up) motes in step 10, so long as he does not use a charm with a Flaw of Invulnerability to defend."* → ganhar 1 a 3 motes por **não** usar a perfeita.
> **O incentivo existia e não funcionou**, porque 1 a 3 motes não pagam o risco de morrer num sistema em que um golpe que passa mata. **Bônus por não usar a defesa só funciona se falhar não for letal.**

## 3.3 — O conserto oficial: errata 2.5 (2012)

**[REGRA]** *Scroll of Errata* — Exalted 2.5, que a comunidade tratou como uma meia-edição. As mudanças que interessam:
- **Heavenly Guardian Defense: `Cost: 8m`** (era 4m) → **dobrou**.
- **Seven Shadow Evasion: `Cost: 8m`** (era 3m) → **multiplicou por 2,67**.
- **Teto de usos por cena**, introduzido em Charms de duração longa: *"With Melee 5+, Essence 5+, the Solar may invoke this defense up to (Essence ÷ 2) times in one scene before this Charm ends."* (Protection of Celestial Bliss)
- Errata paralela em **regeneração de motes, Combos e stunts** — ou seja, mexeram **na fonte da devolução** junto com o preço.
- **[REGRA]** E abolição dos custos de XP e de Força de Vontade do sistema de Combos.

**[FÓRUM/MESA]** A avaliação da comunidade sobre se funcionou: *"The revised perfect costs were a significant change (…) the perfects being increased rendered combat more tactical because you have to decide what to spend your motes on."* E: *"the errata breaks down the pre-existing combat paradigm, wherein 'paranoia combat' ran rampant."* Resenha contemporânea considera a 2.5 uma melhoria clara.

> **Os dois movimentos do conserto oficial, isolados:**
> 1. **Dobrar o preço** — de ~6% para ~15% do reservatório por negação.
> 2. **Pôr teto de usos por cena** — para que "eu tenho energia sobrando" pare de significar "eu sou invulnerável".
> 3. E, junto, **cortar a devolução** (errata em stunts e regeneração), porque preço sem cortar devolução não é preço.

**[NÚMERO]** O efeito líquido em uma frase: a errata moveu a defesa perfeita de **~52 negações por combate** para **~8**. Uma luta de Exalted dura umas 5 rodadas. Passou de "infinito" para "dá para o combate inteiro, mas só se você não gastar em mais nada" — que é onde a decisão nasce.

## 3.4 — O conserto radical: Exalted 3e removeu as Perfect Defenses

**[REGRA/FÓRUM]** *"Perfect defenses no longer exist in 3rd edition, which was a deliberate design choice."*
**[FÓRUM]** A justificativa registrada: *"3e's split between initiative and health level attacks, withering and decisive damage, allows for far better combats that feel like you're making ground, like you can actually tell the swing of the battle beyond your own mote count."*
**[FÓRUM]** E o diagnóstico da raiz: *"in the 2e paradigm, those attack-Ability-Charms don't matter for most of the fight because it's trivial to negate attacks with perfect defenses for much cheaper, making it pointless to use attack Charms if you know you can't use a defense Charm if you're targeted."*

> **A 3e não consertou o preço da defesa perfeita. Ela apagou a defesa perfeita e criou uma camada intermediária de recurso (Iniciativa) para o combate ter progresso visível.** Ataques *withering* não causam dano: eles roubam Iniciativa. Só o ataque *decisive* converte Iniciativa em ferimento. O resultado é que **todo turno muda alguma coisa**, mesmo quando ninguém morre.
>
> Se o seu problema de fundo é "com anti-domínio ligada, o domínio não faz nada e a mesa fica parada", **a resposta da 3e é: dê ao acerto garantido um efeito que a anti-domínio NÃO anula, mas que também não é dano.** O domínio sempre entrega alguma coisa (pressão, posição, um recurso do alvo), mesmo contra quem se defendeu. É a mesma ideia do *Counterspell* 2024 devolvendo o espaço de magia: **nunca deixe o resultado ser zero-a-zero.**

**[FÓRUM]** E o contra-argumento, que também tem base de comunidade e é honesto registrar — existe uma tese oposta, com título de tópico: *"An Exalted without Perfect Defense is not Exalted."* Ou seja, parte do público entende a defesa perfeita como **identidade de gênero**, não como bug. No seu caso isso importa: as quatro anti-domínio são canônicas do mangá. Tirar não é opção; o que está em jogo é preço e forma.

---

# PARTE 4 — O princípio de design, com fonte

## 4.1 — Quanto deve custar uma defesa que anula completamente um ataque?

**Existe régua publicada? Sim, uma, e é do Mutants & Masterminds.** (Detalhe na seção 2.6.) Resumo operacional:

**[REGRA]** M&M 3e, efeito *Immunity*, **1 ponto por grau**, e a escada é: **2** para críticos, **5** para um descritor de dano específico, **10** para um descritor comum, **20** para um muito comum, **30** para uma categoria inteira de salvaguarda, **80** para todo o dano.
**[REGRA]** E **"Limited to Half Effect" custa −1 por grau**, ou seja, **metade do efeito por metade do preço — linear**.

**[NÚMERO]** Contra uma ficha padrão de 150 pontos:

| O que se anula | Preço | % da ficha |
|---|---:|---:|
| Um efeito nomeado e específico | 5 | **3,3%** |
| Uma categoria de resolução inteira | 30 | **20%** |
| Tudo | 80 | **53%** |

**[REGRA]** A filosofia declarada pelo próprio manual, que é a defesa do preço baixo: *"it's simpler at some point to say a character is immune to something than it is to bother rolling dice"* e *"Immunity also encourages creativity: if you can't overcome a foe just by hitting him, what then?"*

> **Conclusão da régua publicada:** anular um efeito **nomeado, específico e de escopo estreito** é barato por desenho, em torno de 3% a 5% do orçamento do personagem, **e isso é considerado correto**, não uma concessão. O que custa caro é a **largura**. A sua intuição de que as quatro anti-domínio devem ser baratas tem respaldo publicado. O que a régua diz que você precisa garantir é que elas sejam **estreitas** — que não façam nada além de resolver o acerto garantido.

**[NÃO ACHEI]** Nenhuma palestra de GDC, artigo de designer ou thread de r/RPGdesign com uma **fórmula geral fechada** para preço de negação total em RPG de mesa. O que existe de fórmula é o point-buy do M&M e o do Hero System; o resto do hobby precifica por comparação e por playtest. Buraco declarado.

## 4.2 — Quando defesa binária é boa, e quando vira imposto

**A síntese que sai do cruzamento das fontes — quatro condições, e o *Shield* do 5e satisfaz as quatro, o *Silvery Barbs* falha em três:**

| Condição | Por quê | Fonte |
|---|---|---|
| **1. Escopo estreito e nomeado** | Se ela anula só uma coisa nomeada, ela não domina o resto do jogo. | M&M *Immunity* (preço por largura); eidorii (*"does not affect attacks without a guaranteed hit"*); D&D Wiki JJK (*"do not work against a feature affected by this unless it specifically states otherwise"*) |
| **2. Assimétrica** | Perfeita contra o perfeito, fraca contra o comum. | *Shield*: 100% contra Magic Missile, +5 de CA contra o resto |
| **3. Compete com outra coisa na mesma casa** | Se ela não disputa nada, ela é sempre ligada. | PF2e: *"You gain 1 reaction per round"*; Simple Domain de JJK: gasta a concentração e proíbe a técnica inata |
| **4. Não devolve mais do que custa** | Se a economia repõe o custo, o preço escrito é ficção. | Exalted 2e: stunt de 2-4 motes contra perfeita de 3 motes |

**Quando ela vira imposto — os três sintomas documentados:**
1. **[FÓRUM]** É a única opção da sua função: *"Having Shield Block be the only defensive reaction option among General feats makes every character that wants one orbit towards it, even if it doesn't fit the class fantasy."*
2. **[FÓRUM]** É estritamente melhor que as alternativas: *"This spell is a new trap choice for spellcasters. You can't live without it."* (Silvery Barbs)
3. **[MESA]** Não tê-la é morrer: *"2E demands you have a perfect defense array."* (Exalted)

> **O teste de uma pergunta, que sai dos três sintomas:** *um personagem competente que NÃO comprou esta aptidão ainda tem uma resposta ao acerto garantido?* Se a resposta é não, ela é imposto — e aí a decisão certa **não é abaixar o preço, é dar a resposta de graça a todo mundo** (o que é literalmente o que a PF2e faz com o trait Incapacitation) **e vender a aptidão como um grau a mais**.

**O conserto padrão do hobby para tax feat** — *Elephant in the Room*, de Pathfinder 1e, que virou a house rule mais adotada do sistema:
**[REGRA/FÓRUM]** O diagnóstico: *"Many rungs on the feat ladder are considered either undesirable or overtly mundane. These are feat taxes."* E: *"Weapon Finesse is the ultimate feat tax. It's begrudgingly mandatory for most rogues… but weapon finesse still doesn't grant a damage bonus."*
As duas manobras de conserto, e ambas cabem no seu caso:
1. **Transformar o imposto em regra base de graça.** *Power Attack* e *Deadly Aim* deixaram de ser feats e viraram opções de combate de qualquer personagem com +1 de BAB.
2. **Fundir a escada em um item só.** *Deft Maneuvers* substituiu **seis** feats "Improved X"; a linha de Two-Weapon Fighting foi de três feats para um.

**[FÓRUM]** E a formulação canônica do problema, do D&D 4e wiki: *"Feats should be optional upgrades, not mandatory patches."*

## 4.3 — Defesa que escala contra ofensiva que escala (o modo de falha da esteira)

Este é o item da sua lista que menos gente escreveu diretamente, mas os sintomas estão documentados nos três lugares:

1. **Exalted 2e** — **[MESA]** os dois lados escalavam e nada mudava: *"combat was a long series of ineffectual swats depleting an invisible mote counter until one side ran out of motes and abruptly died."* A ofensiva cresceu (flurry), a defesa cresceu (flurry-breaker), e o resultado observável na mesa ficou **idêntico**: ninguém toma dano até alguém zerar.
2. **Lancer** — **[FÓRUM]** quando a precisão sobe demais, a defesa **para de ser comprada**: *"increasing these does not meaningfully decrease your odds of taking damage."* O conserto foi **cortar a precisão**, não subir a defesa.
3. **Legendary Resistance** — **[NÚMERO]** o teto de 3 usos nunca é atingido: 6-7 rodadas para drenar, e a luta média não dura isso. **Um teto que nunca é alcançado é um teto que não existe.**

**As três soluções estruturais que o hobby achou, em ordem de radicalidade:**

**(a) Escala em degraus com faixa de folga** — eidorii JJK: Domain Amplification dá **imunidade / resistência / nada** conforme a diferença de refino, em faixas de 50 pontos. Os dois lados escalam, mas **o que é lido é a diferença**, não o valor absoluto. → *A porcentagem fica constante e a decisão continua viva.*

**(b) Relógio em vez de interruptor** — D&D Wiki JJK: a anti-domínio é uma barreira com HP, o domínio come **3d12 por 100 de refino** por rodada, e a conta diz que ela aguenta 1 a 3 rodadas contra um domínio grande. → *A defesa não anula o domínio; ela compra tempo, e quanto tempo é função de quem investiu mais.*

**(c) Camada intermediária de recurso** — Exalted 3e: ataques *withering* não tiram vida, tiram Iniciativa; só o *decisive* fere. → *Nenhum turno é zero-a-zero, mesmo quando a defesa funciona.*

**[REGRA]** E a formulação de princípio mais citada do hobby sobre por que binário é ruim, de Justin Alexander (The Alexandrian), sobre save-or-die:
*"On the basis of a single die roll, the player is no longer allowed to participate in the game."*
E o que ele aponta como a coisa que funciona, que é o oposto disso: *"the ablative nature of hit points — the back-and-forth dynamic of dealing damage."*
E o modo de falha em nível alto, que é a esteira: *"With astronomical HP totals and massive saving throw bonuses, gameplay becomes: who's going to roll a 1 on their saving throw first?"*
A solução dele: converter o efeito binário em **dano a atributo** (ex.: morte vira 4d6 de dano em Constituição), reintegrando o efeito ao sistema desgastável.

> **Padrão nº 7, e fecha o arquivo:** a saída de quase todo mundo que enfrentou esse problema foi **converter o binário em desgaste**. Acerto garantido que anula ou não anula é binário dos dois lados. Acerto garantido que **sempre entrega alguma coisa desgastável** (e a anti-domínio reduz quanto, ou por quantas rodadas) nunca produz turno morto.

---

# PARTE 5 — O que eu não achei

Buracos declarados. Cada um foi procurado de propósito.

1. **Post-mortem escrito de autor de homebrew de JJK.** Nenhum dos sistemas que achei publicou changelog com números antes/depois, errata formal ou retrospectiva. O D&D Wiki tem histórico de wiki e briga de edição pública, mas a manutenção migrou para Discord fechado (*"This talk page will be rarely looked at anymore"*). **Não entrei em Discord.** Se você quiser esse material, é ali que ele está.
2. **Relato de mesa real de JJK homebrew onde a anti-domínio quebrou a sessão.** O mais perto que cheguei foram duas perguntas de regra na talk page do D&D Wiki, ambas sobre **escopo** do Falling Blossom Emotion, e uma reclamação de um usuário pedindo salvaguarda contra o sure-hit do Malevolent Shrine. Nada de "isso destruiu minha campanha".
3. **Conversão de JJK para PF2e, FATE, Savage Worlds, PbtA, Anime 5e ou BESM** com anti-domínio escrita. Procurei nas três rodadas e não existe material indexado.
4. **Fórmula geral publicada de preço para negação total.** Só achei point-buy (M&M). Nenhuma palestra de GDC, nenhum artigo de designer, nenhuma thread de r/RPGdesign com conclusão fechada.
5. **Texto integral das Perfect Defenses de Exalted 2e direto do livro.** Os custos vieram cruzados de errata e de discussão de comunidade, não do PDF. Os números batem em três fontes independentes (3m/4m originais, 8m pós-errata), mas a redação completa do Charm eu não tenho.
6. **Declaração de designer da Exalted 3e** explicando em primeira pessoa por que removeram as Perfect Defenses. Tenho a racionalização da comunidade e a estrutura do sistema novo, não a fala de Holden Shearer ou John Mørke.
7. **Alguns fóruns ficaram fechados atrás de verificação de bot** e eu não tentei contornar: Onyx Path Forums, RPGnet, Giant in the Playground, reddit, D&D Beyond, rpg.stackexchange, EN World. O que eu tenho desses veio de trechos de busca, não de leitura da página. **Trate essas citações como confiança média** — a frase é fiel, o contexto ao redor eu não li.
8. **Gloomhaven, 13th Age e Fabula Ultima** — procurei e não achei nada com número **e** modo de falha que valesse para o seu problema. Não é que não exista; é que não achei e não vou fingir.

---

# Aplicação direta ao seu caso — as decisões que este material sustenta

Nada aqui é regra sua; é a régua do hobby com o número na mão, para você decidir.

### O que o material sustenta bem

**1. O preço baixo está certo. A faixa é 1/4 a 1/6.**
Três sistemas de JJK independentes chegaram lá sem se falar (6:1, 5:1, 4:1), e a régua publicada do M&M diz que anular **um efeito nomeado e estreito** custa ~3% do orçamento do personagem. Se as suas quatro custam nessa faixa, elas estão no lugar certo do mapa.

**2. O preço não é energia — é ação, posição e a sua própria técnica.**
Os três sistemas de JJK cobram a mesma moeda: **concentração, imobilidade, ou proibição de usar a técnica inata.** O D&D Wiki chega a escrever isso como voto de compromisso: *"you cannot move from where the simple domain was cast and you cannot use any innate technique features."* O eidorii: *"Your Simple Domain ends if you move."* O Hollow Wicker: duas mãos ocupadas e cantando.
→ **Se você quiser encarecer sem mexer no número, encareça aqui.** É a moeda em que o hobby inteiro já paga.

**3. A trava tem que ser de escopo, e escopo se escreve em uma frase.**
O *Silvery Barbs* não é banido por ser barato; é banido por ser barato **e largo**. A frase do eidorii — *"does not affect attacks without a guaranteed hit"* — faz sozinha o trabalho de uma página de balanceamento. A do D&D Wiki faz o mesmo pelo outro lado: nenhuma outra defesa do livro funciona contra o sure-hit **a menos que diga explicitamente que funciona**. Lista fechada e nomeada.

**4. Some tudo que devolve energia por rodada antes de julgar o preço.**
A defesa perfeita de Exalted custava 3 motes e o stunt devolvia 2-4. O preço escrito era ficção. **Se a sua devolução de energia por rodada cobre mais de metade do custo da anti-domínio, ela é de graça, e o número que está no livro não importa.**

### O que o material sugere testar

**5. Trocar o interruptor por relógio.**
O melhor desenho que achei em toda a Frente 1 é o do D&D Wiki: a anti-domínio tem **barra de vida**, o domínio a come a **3d12 por 100 de refino** por rodada, e a conta dá **1 a 3 rodadas** contra domínio grande. A defesa não anula o domínio — ela **compra rodadas**, e quantas é função de quem treinou mais. Isso resolve de uma vez: o binário some, a esteira some (é diferença de investimento, não valor absoluto), e o domínio caro continua valendo o preço.

**6. Nunca deixar o resultado ser zero-a-zero.**
Três sistemas grandes chegaram nisso separadamente: *Counterspell* 2024 devolve o espaço de magia; Exalted 3e dá ao ataque um efeito (Iniciativa) que não é dano e não é anulável; Alexander propõe converter o binário em desgaste. **Se o domínio, contra uma anti-domínio ligada, entrega exatamente zero, você criou um turno morto para os dois lados.** Dê a ele algo que atravesse — pressão, posição, um recurso do alvo, uma rodada do relógio.

**7. Se você abrir defesa por reação, olhe a economia de reação antes do preço.**
A PF2e freia tudo com **uma reação por rodada** e não precisa encarecer nada. O D&D Wiki de JJK foi na direção oposta — **duas reações a partir do nível 5**, mais reações dedicadas — e por isso **teve** que equilibrar pela barra de vida da barreira. As duas funcionam; o que não funciona é escolher a segunda sem perceber que escolheu.

**8. E o teste de imposto, em uma pergunta.**
*Um personagem competente que não comprou nenhuma das quatro ainda tem resposta ao acerto garantido?*
Se a resposta é não, elas são imposto, e o conserto documentado **não é baratear** — é dar a resposta mínima de graça a todo mundo (é o que a PF2e faz com o trait Incapacitation: resistência automática por diferença de nível, sem compra) e **vender as quatro como o grau acima**. Foi assim que o *Elephant in the Room* consertou o Pathfinder: *"Feats should be optional upgrades, not mandatory patches."*

---

## Fontes

**Homebrews de JJK**
- D&D Wiki, *Jujutsu Kaisen Supplement*: `Domain_Expansion_(Jujutsu_Kaisen_Supplement)`, `Feats_(Jujutsu_Kaisen_Supplement)`, `Jujutsu_Sorcerer_(Jujutsu_Kaisen_Supplement)`, `Talk:Feats_(...)`, `Talk:Jujutsu_Sorcerer_(...)` — dandwiki.com
- *Jujutsu Kaisen 5e* — eidorii.com (`/sorcery/domain-expansion/`, `/feats/barrier-technique-feats`, `/sorcery/cursed-energy/`)
- *Jujutsu Class* por TrevorAco — gmbinder.com/share/-NmCj8Ct6kRouiuITSGh
- Mod *Jujutsu Kaisen* (RadonCoding) — github.com/RadonCoding/jujutsu-kaisen
- *Jujutsu Kaisen P&P* (alemão) — custom-tabletop-rpg.github.io/jujutsu-kaisen
- *The Eternal Battle of Curses* — leonardo-azevedo.itch.io

**Sistemas grandes**
- 5e SRD via open5e (Magic Missile, Shield, Counterspell, Legendary Resistance)
- Counterspell 2024 — texto via roll20/D&D Beyond
- Archives of Nethys — trait Incapacitation (`Traits.aspx?ID=631`), graus de sucesso (`Rules.aspx?ID=2286`), Shield Block, Nimble Dodge
- d20HeroSRD — Immunity (Defense), M&M 3e
- LANCER Wiki / Lancer FAQ
- ThinkDM — *Why DMs Are Banning Silvery Barbs*
- Hipsters & Dragons — *Fixing Legendary Resistance in 5e D&D (4 Ideas)*
- versamus.blogspot.com — *Problems with D&D 5E: Legendary Resistance*
- paizo.com/threads/rzs43t4z — *rethink Shield Block (and defensive reactions)*

**Exalted**
- Scroll of Errata — Exalted 2.5 (custos pós-errata)
- theonyxpath.com — anúncio da errata 2.5
- tentacledvitriol.wordpress.com — *Review – Exalted 2.5 (Errata)*
- writeups.letsyouandhimfight.com/purplexvi/exalted-second-edition — leitura crítica longa
- forums.sufficientvelocity.com — *Exalted Questions Thread* (flurry-breaker, custos de 8 motes)
- tgdmb.com — *Need help: how to break Exalted 2nd Combat* (paranoia combo, motes como HP)
- oakthorne.net — Four Flaws of Invulnerability
- exalted275e.wikidot.com — revisão de fãs 2.75e
- forum.theonyxpath.com — *An Exalted without Perfect Defense is not Exalted*, *2e: Biggest problems fix?* (lidos por trecho de busca, página bloqueada)

**Princípio de design**
- michaeliantorno.com/feat-taxes-in-pathfinder — *The Elephant in the Room*
- thealexandrian.net — *Save-or-Die Effects*
- enworld.org — threads de feat tax e de Silvery Barbs (lidas por trecho de busca)
- dnd4.fandom.com — verbete *Feat tax*
