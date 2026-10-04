#!/usr/bin/env python3
"""Enumeração exata de Esconder e buscas contra a Furtividade guardada.

Executar com Python 3; somente biblioteca padrão. Escreve deteccao-contas.json
e deteccao-contas.md ao lado deste script. Não lê nem altera a minuta.
"""

from fractions import Fraction
from itertools import product
import json
from pathlib import Path


FACES = tuple(range(1, 21))
CASOS = ((4, 4, 4), (4, 4, 12), (12, 4, 4), (12, 4, 12))


def prob_busca(cd, bonus):
    """Empatar basta; sem sucesso/falha automática em 1 ou 20."""
    return Fraction(sum(dado + bonus >= cd for dado in FACES), 20)


def prob_duas_buscas(cd, bonus_a, bonus_b):
    """Pelo menos um sucesso; os dados são independentes dada a mesma CD."""
    enumerada = Fraction(
        sum(a + bonus_a >= cd or b + bonus_b >= cd
            for a, b in product(FACES, repeat=2)),
        400,
    )
    formula = 1 - (1 - prob_busca(cd, bonus_a)) * (1 - prob_busca(cd, bonus_b))
    assert enumerada == formula
    return enumerada


def media(valores):
    return sum(valores, Fraction(0)) / len(valores)


def serializar(prob):
    return {
        "fracao": str(prob),
        "numerador": prob.numerator,
        "denominador": prob.denominator,
        "percentual_aproximado": round(float(prob * 100), 8),
    }


def mostrar(prob):
    percentual = f"{float(prob * 100):.4f}".rstrip("0").rstrip(".")
    return f"{percentual.replace('.', ',')}% ({prob})"


def analisar(furtividade, percepcao, sentir):
    cd_passiva = 10 + percepcao
    faces_ocultas = tuple(d for d in FACES if d + furtividade >= cd_passiva)
    assert faces_ocultas
    cds = tuple(d + furtividade for d in faces_ocultas)
    simples = tuple(prob_busca(cd, sentir) for cd in cds)
    duas_iguais = tuple(prob_duas_buscas(cd, sentir, sentir) for cd in cds)
    duas_mistas = tuple(prob_duas_buscas(cd, percepcao, sentir) for cd in cds)
    p_esconder = Fraction(len(faces_ocultas), 20)
    p_simples = media(simples)
    p_duas = media(duas_iguais)
    p_mistas = media(duas_mistas)
    p_passiva_errada = Fraction(
        sum(d + furtividade >= max(cd_passiva, 10 + sentir) for d in FACES), 20
    )
    media_antes_de_quadrado = 1 - (1 - p_simples) ** 2
    assert media_antes_de_quadrado >= p_duas
    # Verificação independente: enumera simultaneamente o dado de Esconder
    # condicionado ao sucesso e os dois dados de busca, sem simulação aleatória.
    total = len(faces_ocultas) * 400
    exaustiva = Fraction(
        sum(a + sentir >= f + furtividade or b + sentir >= f + furtividade
            for f, a, b in product(faces_ocultas, FACES, FACES)),
        total,
    )
    assert exaustiva == p_duas
    resultados = {
        "esconder": p_esconder,
        "busca_sentir_condicionada": p_simples,
        "antena_condicionada": p_duas,
        "dois_buscadores_sentir_condicionada": p_duas,
        "dois_buscadores_percepcao_sentir_condicionada": p_mistas,
        "esconder_com_segunda_cd_passiva_indevida": p_passiva_errada,
        "queda_absoluta_esconder_com_cd_indevida": p_esconder - p_passiva_errada,
        "formula_incorreta_aplicada_a_media": media_antes_de_quadrado,
        "superestimacao_da_formula_incorreta": media_antes_de_quadrado - p_duas,
    }
    return {
        "bonus": {"furtividade": furtividade, "percepcao": percepcao, "sentir": sentir},
        "cd_passiva_percepcao": cd_passiva,
        "faces_esconder_condicionadas": list(faces_ocultas),
        "cds_guardadas_condicionadas": list(cds),
        "resultados": resultados,
        "por_cd": [{
            "dado_esconder": d,
            "cd_guardada": cd,
            "peso_condicionado": serializar(Fraction(1, len(cds))),
            "uma_busca_sentir": serializar(prob_busca(cd, sentir)),
            "antena_ou_duas_sentir": serializar(prob_duas_buscas(cd, sentir, sentir)),
            "duas_percepcao_sentir": serializar(prob_duas_buscas(cd, percepcao, sentir)),
        } for d, cd in zip(faces_ocultas, cds)],
    }


def main():
    casos = [analisar(*caso) for caso in CASOS]
    fixos = [{
        "cd": 16,
        "bonus": bonus,
        "uma_busca": prob_busca(16, bonus),
        "antena_ou_duas_buscas_iguais": prob_duas_buscas(16, bonus, bonus),
    } for bonus in (4, 6)]
    assert fixos[0]["uma_busca"] == Fraction(9, 20)
    assert fixos[1]["uma_busca"] == Fraction(11, 20)
    assert fixos[0]["antena_ou_duas_buscas_iguais"] == Fraction(279, 400)
    assert fixos[1]["antena_ou_duas_buscas_iguais"] == Fraction(319, 400)
    assert prob_busca(30, 4) == 0  # 20 não supera uma CD inalcançável.
    assert prob_busca(5, 4) == 1   # 1 pode empatar e obter sucesso.

    dados = {
        "schema": 1,
        "metodo": "Enumeração exata de d20 equiprováveis com fractions.Fraction; não é Monte Carlo.",
        "hipoteses": {
            "esconder": "d20 + Furtividade >= 10 + Percepção; o total obtido fica guardado.",
            "busca": "d20 + bônus >= Furtividade guardada; empate basta; nenhum 1/20 automático.",
            "condicionamento": "Buscas avaliadas somente nas faces em que Esconder já teve sucesso.",
            "antena": "Uma busca mais uma única rerrolagem se falhar; mesma CD guardada e mesmo bônus; 1 Ação Padrão + uso de Antena.",
            "duas_iguais": "Dois buscadores com o mesmo bônus Sentir Energia do caso; dois dados independentes diante da mesma CD; custo 2 Ações Padrão.",
            "duas_mistas": "Um buscador com o bônus Percepção e outro com Sentir Energia do caso, se ambos puderem examinar sinais acessíveis; custo 2 Ações Padrão.",
            "segunda_passiva": "Contrafactual indevido: o mesmo dado de Esconder deve atingir max(10 + Percepção, 10 + Sentir Energia).",
            "geometria": "Todos os casos supõem uma fonte oculta de energia alcançada pela busca candidata de 18 m, sem bloqueio/interferência extra. O alcance não é variável deste cálculo.",
            "limites": "Não modela economia completa de combate, múltiplos alvos, efeitos de classe adicionais, informação de resultado parcial, nem equilíbrio global.",
        },
        "casos": [dict(caso, resultados={nome: serializar(prob) for nome, prob in caso["resultados"].items()})
                  for caso in casos],
        "cd_fixa": [dict(caso,
                         uma_busca=serializar(caso["uma_busca"]),
                         antena_ou_duas_buscas_iguais=serializar(caso["antena_ou_duas_buscas_iguais"]))
                    for caso in fixos],
    }
    linhas = [
        "# Detecção — comparação matemática exata",
        "",
        "Gerado por `deteccao-contas.py`, usando somente Python 3 e `fractions.Fraction`. Enumeração completa; nenhuma amostragem aleatória. Frações são exatas; percentuais são arredondados a até quatro casas. O JSON conserva numeradores, denominadores e a distribuição por CD.",
        "",
        "## Premissas",
        "",
        "O personagem primeiro usa Esconder: `d20 + Furtividade ≥ 10 + Percepção`. Só as faces que conseguiram esse sucesso entram na comparação de buscas. O total histórico de Furtividade obtido é a CD guardada; **não é uma CD passiva calculada pelo bônus de Furtividade**. Todas as faces restantes têm o mesmo peso condicionado. A busca tem sucesso com `d20 + Sentir Energia ≥ total guardado`, incluindo empates. Não há falha automática em 1 nem sucesso automático em 20.",
        "",
        "Todos os casos supõem uma fonte de energia já alcançada pela busca candidata de 18 m, sem bloqueio ou interferência adicional. O cálculo compara testes; **não demonstra que 18 m seja o alcance adequado**. A regra calculada não acrescenta CD passiva de energia ao ato de Esconder.",
        "",
        "Antena significa uma única rerrolagem após falhar, contra a **mesma CD**, consumindo o uso do Legado e mantendo o custo de uma Ação Padrão. Dois buscadores rolam separadamente contra essa mesma CD, com o mesmo bônus Sentir Energia indicado; a comparação principal considera duas Ações Padrão e pelo menos um sucesso. Não inclui dois usos de Antena nem mudanças de posição/alvo entre as tentativas.",
        "",
        "## Depois que Esconder funcionou",
        "",
        "| Furtividade / Percepção / Sentir | Chance inicial de Esconder | CDs guardadas possíveis, após sucesso | Uma busca | Busca + Antena | Dois buscadores iguais, 2 Padrões |",
        "|---|---|---|---|---|---|",
    ]
    for caso in casos:
        b, r = caso["bonus"], caso["resultados"]
        cds = caso["cds_guardadas_condicionadas"]
        linhas.append(
            f"| +{b['furtividade']} / +{b['percepcao']} / +{b['sentir']} "
            f"| {mostrar(r['esconder'])} | {cds[0]} a {cds[-1]} "
            f"| {mostrar(r['busca_sentir_condicionada'])} "
            f"| {mostrar(r['antena_condicionada'])} "
            f"| {mostrar(r['dois_buscadores_sentir_condicionada'])} |"
        )
    linhas += [
        "",
        "A chance nas três últimas colunas é **condicionada ao sucesso inicial de Esconder**. Não é a chance de localizar alguém antes de saber se conseguiu se ocultar. Antena e duas buscas iguais têm a mesma probabilidade de ao menos um sucesso neste recorte; os custos e a disponibilidade são diferentes. Se o segundo buscador só agir depois de o primeiro falhar, o grupo pode economizar a segunda ação nos sucessos iniciais; esta tabela contabiliza a capacidade de investir até duas, sem avaliar esse valor tático.",
        "",
        "As rolagens de busca são independentes **dada a CD guardada**, mas compartilham a mesma dificuldade histórica. Por isso calculamos `média[1 − (1 − p(CD))²]`, e não `1 − (1 − média[p(CD)])²`. Por exemplo, no caso +4/+4/+4, a chance média de uma busca é 30%, mas Antena dá **48,5%**, não 51%. Tirar a média antes de elevar ao quadrado superestimaria o benefício.",
        "",
        "## Variante: um buscador de Percepção e outro de Sentir Energia",
        "",
        "Esta comparação adicional só vale quando ambos têm sinais acessíveis para usar sua perícia. O custo considerado é de duas Ações Padrão. A tabela principal usa dois buscadores com o mesmo Sentir; não se deve confundir os dois cenários.",
        "",
        "| Furtividade / Percepção / Sentir | Pelo menos um sucesso, condicionado a Esconder |",
        "|---|---|",
    ]
    for caso in casos:
        b, r = caso["bonus"], caso["resultados"]
        linhas.append(f"| +{b['furtividade']} / +{b['percepcao']} / +{b['sentir']} | {mostrar(r['dois_buscadores_percepcao_sentir_condicionada'])} |")
    linhas += [
        "",
        "## Contrafactual: acrescentar uma segunda CD passiva",
        "",
        "Este cenário é **uma alteração indevida da regra candidata**, incluída somente para medir seu efeito. O mesmo resultado de Esconder teria de alcançar as duas CDs, equivalendo a `max(10 + Percepção, 10 + Sentir Energia)`. Não se multiplicam duas probabilidades: existe um só dado de Esconder. A comparação abaixo é anterior a qualquer busca ativa; não mistura a distribuição nova com os resultados condicionados da primeira tabela.",
        "",
        "| Furtividade / Percepção / Sentir | Só CD 10 + Percepção | Com segunda CD 10 + Sentir | Queda absoluta em pontos percentuais |",
        "|---|---|---|---|",
    ]
    for caso in casos:
        b, r = caso["bonus"], caso["resultados"]
        queda = f"{float(r['queda_absoluta_esconder_com_cd_indevida'] * 100):.4f}".rstrip("0").rstrip(".").replace(".", ",")
        linhas.append(
            f"| +{b['furtividade']} / +{b['percepcao']} / +{b['sentir']} "
            f"| {mostrar(r['esconder'])} | {mostrar(r['esconder_com_segunda_cd_passiva_indevida'])} | {queda} p.p. |"
        )
    linhas += [
        "",
        "Nos dois exemplos com Sentir +12 e Percepção +4, a segunda passiva reduziria a chance inicial de Esconder em 40 pontos percentuais. Isso concederia influência sem gastar a Ação Padrão da busca. O número descreve estes casos, não prova que toda defesa passiva energética seria inviável em qualquer design.",
        "",
        "## Referência simples: CD fixa 16",
        "",
        "Aqui a CD já está fixada, portanto não existe a média sobre resultados históricos diferentes. A fórmula `1 − (1 − p)²` pode ser aplicada diretamente.",
        "",
        "| Bônus da busca | Uma tentativa | Com uma rerrolagem de Antena | Dois buscadores iguais, 2 Padrões |",
        "|---|---|---|---|",
    ]
    for caso in fixos:
        linhas.append(f"| +{caso['bonus']} | {mostrar(caso['uma_busca'])} | {mostrar(caso['antena_ou_duas_buscas_iguais'])} | {mostrar(caso['antena_ou_duas_buscas_iguais'])} |")
    linhas += [
        "",
        "## Leitura limitada dos resultados",
        "",
        "O bônus de Sentir aumenta a chance de uma busca ativa superar a Furtividade já conseguida. Antena amplia essa chance ao custo de seu uso; outro buscador exige outra ação. Os dados mostram esses efeitos exatos nos casos escolhidos, **sem concluir equilíbrio global**, validar alcance, valorar PE, simular múltiplos alvos ou medir o valor de atacar um inimigo localizado que ainda não pode ser visto.",
        "",
        "A distribuição por CD está no JSON. O script confere a fórmula de duas tentativas contra enumeração dos 400 pares possíveis de d20 e também enumera conjuntamente o dado original de Esconder e os dois dados de busca. As verificações de CD fixa e de ausência de 1/20 automáticos estão no próprio script.",
        "",
        "Reprodução: execute `python3 deteccao-contas.py` na pasta deste arquivo, ou passe o caminho completo do script. Os dois arquivos gerados são gravados ao lado dele; a minuta não é modificada.",
        "",
    ]
    pasta = Path(__file__).resolve().parent
    (pasta / "deteccao-contas.json").write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (pasta / "deteccao-contas.md").write_text("\n".join(linhas), encoding="utf-8")
    print("Gerados deteccao-contas.json e deteccao-contas.md; enumerações exatas verificadas.")


if __name__ == "__main__":
    main()
