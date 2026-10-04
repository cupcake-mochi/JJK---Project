# Adendo de verificação final — piloto editorial r2

**Resultado: os seis ajustes solicitados estão presentes e não introduzem regressão mecânica identificada neste recorte.** Os esclarecimentos mantêm custos, recursos e momentos de uso já conferidos.

Conferência somente leitura em 02/10/2026 (America/Sao_Paulo). Registro UTC: 2026-10-03T00:20:17+00:00. Nenhum artefato do projeto foi alterado; não foi executado git.

Pasta examinada: `/media/mizuki/HD Externo II/Claude/Claude 2/sistema/05-material/livro/piloto-editorial-r2/`.

## Identificação das versões conferidas

| Arquivo | Bytes | SHA-256 |
|---|---:|---|
| `PILOTO.md` | 24665 | `5c274c0aff8c8d8fde7935a44a004f3ea8f594ffea9e48a2cd97fcc52bd7b003` |
| `LOTE-TECNICO.md` | 26308 | `d5bca16496bbe281a0826043159a267010acefb435a24a3cab7aeb7db9edcd66` |

Os hashes foram recalculados após a leitura e conferidos contra os da versão examinada. Uma edição posterior exige considerar novamente o trecho alterado, sem atribuir este parecer a outro conteúdo.

## Ajustes conferidos

| Ajuste | Localização | Resultado |
|---|---|---|
| Renovação da básica em campo | `LOTE-TECNICO.md:189` | A linha diz que cada entidade **em campo** renova uma básica no começo do turno do invocador. Concorda com o fluxo e preserva a entrada sem básica explicada na linha 204. |
| Limite de entidades que causam dano | `LOTE-TECNICO.md:183` | Mantém “no seu turno, no máximo duas entidades suas atuam causando dano, fora as especiais comandadas”. É o mesmo limite da fonte integrada. Não foi convertido em dois ataques totais nem em uma permissão para usar básica e especial no mesmo corpo. |
| Lidar com Animais | `LOTE-TECNICO.md:261` | A descrição ficou restrita a acalmar, montar, conduzir e orientar animais. Não sugere teste adicional para uma invocação cumprir Intenção. Inteligência foi mantida. |
| Escopo do exercício de Kaito | `LOTE-TECNICO.md:213` | Explicita a comparação de ações e energia, sem simular rolagens ou dano contra uma ficha inimiga completa. Assim não promete resolver um ataque sem fornecer a Defesa inimiga. As alternativas conservam 6 PE ou gastam 3, chegando a 3. |
| Momento do saldo de Kaori | `PILOTO.md:162` | “Neste ponto do turno” indica que os 6 m restantes, a Bônus e a Reação ainda podem estar disponíveis naquele turno. Corrige a impressão de que movimento sobraria depois do seu encerramento. |
| Origem do bônus de Bloquear | `PILOTO.md:288` | Exibe `2d10 + (Defesa − 11)`; com Defesa 13, o bônus é 2. `7 + 6 + 2 = 15` supera o ataque 14. Não cobra outra Reação além da já gasta para assumir o golpe. |

## Fontes confrontadas

- `invocacoes/05-Edicao-Integrada/60-invocacoes.md`: Entrada rápida; Recursos e ciclo; Entrada e recolhimento; Intenção; Básica e limite de ataques; Especial e Energia. O limite das duas entidades está na linha 673.
- `sistema/05-material/livro/manual/10-como-jogar.md`: Bloquear, linha 155; a ausência de custo de Reação está na linha 157.
- `sistema/05-material/livro/manual/11-o-turno.md`: Recursos do turno e Deslocamento.
- `sistema/05-material/livro/manual/12-pericias-e-oficios.md`: atributo e usos de Lidar com Animais. O recorte evita transportar a formulação antiga sobre invocações, sem reescrever a regra integral no livro.

Os exemplos e o catálogo já conferidos não foram submetidos novamente à bateria completa. Esta etapa verificou os ajustes finais e os trechos imediatamente relacionados. Não examinou novas exportações PDF nem substitui inspeção visual ou teste humano de compreensão.
