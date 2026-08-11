# -*- coding: utf-8 -*-
"""Monta eval_metadata.json, timing.json, grading.json e benchmark.json da iteracao 1.

RESSALVAS DE METODO — leia antes de confiar nos numeros:
  1. As assercoes foram escritas DEPOIS de ver as saidas (post-hoc). Isso enfraquece
     a nota: uma assercao escrita apos o fato tende a favorecer o que ja aconteceu.
  2. Uma execucao por condicao. Sem repeticao nao da para separar efeito da skill de
     variacao entre execucoes.
  3. Quem escreveu as skills tambem escreveu os prompts de teste.
  4. Executores rodaram em Sonnet; a sessao principal do usuario e Opus.
  5. A correcao e automatica (padrao de texto + presenca de arquivo), nao julgamento
     humano. Ela mede se o conceito APARECE, nao se esta certo.

CONDICOES (nao sao repeticoes umas das outras):
  with_skill          — leu o SKILL.md e os arquivos de apoio
  without_skill MORNA — sem skill, mas COM acesso a pasta do projeto (leu o dossie)
  without_skill FRIA  — sem skill e SEM acesso a pasta do projeto. Ambiente isolado.
                        Verificado por varredura de vazamento: nenhum termo exclusivo
                        do projeto aparece na saida.
"""
import json
import os
import re
import statistics
from datetime import datetime, timezone

RAIZ = os.path.dirname(os.path.abspath(__file__))
IT = os.path.join(RAIZ, 'iteration-1')

# -----------------------------------------------------------------------------
# Timing recuperado do historico da conversa. NAO re-executado.
# -----------------------------------------------------------------------------
TIMING = {
    ('eval-0-dominancia-restricao', 'with_skill'):          (83426, 659788),
    ('eval-0-dominancia-restricao', 'without_skill'):       (81658, 470571),
    ('eval-1-curva-teste-resistencia', 'with_skill'):       (78882, 488176),
    ('eval-1-curva-teste-resistencia', 'without_skill'):    (66530, 503540),
    ('eval-2-revisar-texto-de-regra', 'with_skill'):        (65752, 428123),
    ('eval-2-revisar-texto-de-regra', 'without_skill'):     (44940, 286130),
    ('eval-3-montar-leva-de-playtest', 'with_skill'):       (118730, 768940),
    ('eval-3-montar-leva-de-playtest', 'without_skill_morna'): (98859, 712430),
    ('eval-3-montar-leva-de-playtest', 'without_skill_fria'):  (34251, 195700),
}

PROMPTS = {
    'eval-0-dominancia-restricao':
        "No meu RPG, feiticos sao montados com pontos e voce pode aceitar desvantagens pra "
        "recuperar pontos. Duas delas: 'Parado' e 'Gesto'. As duas devolvem o mesmo tanto: "
        "metade do Grau. Quero adicionar uma terceira, 'Vulneravel', tambem devolvendo metade "
        "do Grau. Ta certo esse preco?",
    'eval-1-curva-teste-resistencia':
        "Meu sistema usa d20. Um feitico de area faz o alvo rolar Teste de Resistencia. A CD e "
        "8 + metade do nivel + 2 se comprou Precisao. Inimigos tem +2 no nivel 1 subindo pra +8 "
        "no nivel 20. Isso fica bom ou os inimigos vao passar sempre? E se eu trocar pra 3d6?",
    'eval-2-revisar-texto-de-regra':
        "Revisa esse trecho do meu manual pra ficar acessivel pra quem nunca jogou RPG: "
        "[trecho CONDICOES em linguagem de contrato]",
    'eval-3-montar-leva-de-playtest':
        "Meu server de RPG tem entre 5 e 7 mestres ativos, e toda semana 2 ou 3 deles rodam mesa "
        "em dias diferentes. Os personagens sao persistentes. Quero testar a primeira versao do "
        "sistema de combate. Como eu organizo isso?",
}

SKILL_DO_EVAL = {
    'eval-0-dominancia-restricao': 'design-mecanicas-rpg',
    'eval-1-curva-teste-resistencia': 'balanceamento-simulacao',
    'eval-2-revisar-texto-de-regra': 'redacao-acessivel-rpg',
    'eval-3-montar-leva-de-playtest': 'playtesting-rpg',
}


def tem(txt, padrao):
    return bool(re.search(padrao, txt, re.I | re.M))


# -----------------------------------------------------------------------------
# Assercoes. Cada uma e (texto, funcao(texto, arquivos) -> bool).
# Escolhidas para DISCRIMINAR: coisas que a skill ensina e que nao sao obvias.
# -----------------------------------------------------------------------------
ASSERCOES = {
 'eval-0-dominancia-restricao': [
  ("Nomeia o conceito de dominancia explicitamente",
   lambda t, f: tem(t, r'domin')),
  ("Compara as tres desvantagens entre si, nao so avalia a nova isolada",
   lambda t, f: tem(t, r'(Parado.{0,80}Gesto|Gesto.{0,80}Parado)')),
  ("Identifica que o custo de Vulneravel escala com o numero de inimigos",
   lambda t, f: tem(t, r'(quantos inimigos|n[uú]mero de inimigos|mais inimigos|escala com)')),
  ("Propoe um conserto concreto com preco, nao so aponta o problema",
   lambda t, f: tem(t, r'(pr[oó]ximo ataque|ataque [uú]nico|1 ponto|metade do Grau)')),
  ("Separa o que e conta do que e opiniao",
   lambda t, f: tem(t, r'opini[aã]o')),
  ("Levanta risco de arbitragem entre mestres diferentes",
   lambda t, f: tem(t, r'(dois mestres|outro mestre|mesas diferentes|mestres decid)')),
 ],
 'eval-1-curva-teste-resistencia': [
  ("Escreve e executa codigo em vez de estimar",
   lambda t, f: any(x.endswith('.py') for x in f)),
  ("Usa distribuicao exata e diz isso (nao Monte Carlo)",
   lambda t, f: tem(t, r'(exat[ao]|enumera[cç]|sem Monte Carlo|n[aã]o.{0,20}Monte Carlo)')),
  ("Da a taxa de sucesso nivel a nivel, nao so nas pontas",
   lambda t, f: tem(t, r'n[ií]vel 10') and tem(t, r'n[ií]vel 20')),
  ("Compara d20 e 3d6 com numeros dos dois lados",
   lambda t, f: tem(t, r'3d6') and len(re.findall(r'\d+[,.]\d+\s*%', t)) >= 6),
  ("Quantifica quanto a melhoria Precisao vale em cada mecanica",
   lambda t, f: tem(t, r'(pp|pontos percentuais)')),
  ("Declara contrato de invariantes ou faz regressao contra os numeros dados",
   lambda t, f: tem(t, r'(invariante|regress[aã]o|contrato)')),
 ],
 'eval-2-revisar-texto-de-regra': [
  ("Entrega o texto reescrito, nao so conselhos sobre ele",
   lambda t, f: tem(t, r'^>|^##')),
  ("Define 'condicao' antes de usar o termo",
   lambda t, f: tem(t, r'(condi[cç][aã]o [eé]|uma condi[cç][aã]o [eé]|chamamos de condi)')),
  ("Poe o caso padrao antes da excecao",
   lambda t, f: tem(t, r'(salvo|exce[cç][aã]o|caso padr[aã]o|regra r[aá]pida)')),
  ("Converte a lista de condicoes em tabela",
   lambda t, f: tem(t, r'^\s*\|.*\|.*\|')),
  ("Inclui exemplo jogavel concreto",
   lambda t, f: tem(t, r'(exemplo|por exemplo)')),
  ("Lista o que mudou e por que cada mudanca conserta algo",
   lambda t, f: tem(t, r'(o que mudou|troquei|inverti|converti|mudei)')),
  ("Sinaliza problema do original que NAO e de redacao (lacuna de regra)",
   lambda t, f: tem(t, r'(pend[eê]ncia|n[aã]o diz o que|falta definir|n[aã]o resolvi|continua faltando)')),
 ],
 'eval-3-montar-leva-de-playtest': [
  ("Propoe medir DIVERGENCIA entre mestres — a metrica propria do caso multi-mestre",
   lambda t, f: tem(t, r'(sonda|mesmo caso.{0,60}mestres|decidiram igual|diverg[eê]nc|dois mestres.{0,40}mesma)')),
  ("Estrutura a leva em bloco tematico com prazo definido",
   lambda t, f: tem(t, r'(duas semanas|bloco|onda|rodada de teste)')),
  ("Define o ciclo em numero de pessoas e rodadas",
   lambda t, f: tem(t, r'(tr[eê]s rodadas|3 rodadas|cinco pessoas|5 pessoas|5\s*[x×]\s*3)')),
  ("Distingue o que perguntar ao mestre do que perguntar ao jogador",
   lambda t, f: tem(t, r'(mestre.{0,80}jogador|formul[aá]rio do mestre|vers[aã]o do mestre|pergunt.{0,40}mestre)')),
  ("Trata o risco especifico ao personagem persistente",
   lambda t, f: tem(t, r'(persistente|morte|backup|ficha de teste|congel)')),
  ("Entrega artefato pronto para usar como arquivo separado",
   lambda t, f: len([x for x in f if x != 'resposta.md']) > 0),
  # Regex corrigida em 06/08. A versao anterior exigia "parar de testar" ou "quando
  # parar" literais e nao pegava "o sinal de parar", que e como a skill mesma escreve.
  # Isso produziu um falso negativo na execucao com skill do eval-3.
  ("Diz quando PARAR de testar",
   lambda t, f: tem(t, r'(sinal de parar|parar de testar|quando parar|s[oó] repete o da anterior|encerrar o teste|crit[eé]rio de sa[ií]da|fechar a vers[aã]o)')),
 ],
}

CONDICOES = {
    'with_skill':          ('with_skill', 1, 'COM SKILL — leu o SKILL.md e os arquivos de apoio'),
    'without_skill':       ('without_skill', 1, 'BASELINE MORNA — sem skill, mas com acesso a pasta do projeto (leu o dossie da Fase 1)'),
    'without_skill_morna': ('without_skill', 1, 'BASELINE MORNA — sem skill, mas com acesso a pasta do projeto (leu o dossie da Fase 1)'),
    'without_skill_fria':  ('without_skill', 2, 'BASELINE FRIA — sem skill e SEM acesso a pasta do projeto. Ambiente isolado, sem vazamento verificado.'),
}


def main():
    runs = []
    agora = datetime.now(timezone.utc).isoformat()

    for eval_dir in sorted(os.listdir(IT)):
        cam_eval = os.path.join(IT, eval_dir)
        if not os.path.isdir(cam_eval):
            continue
        eval_id = int(re.match(r'eval-(\d+)', eval_dir).group(1))

        for cond_dir in sorted(os.listdir(cam_eval)):
            cam_run = os.path.join(cam_eval, cond_dir)
            cam_out = os.path.join(cam_run, 'outputs')
            if not os.path.isdir(cam_out):
                continue

            config, run_number, rotulo = CONDICOES[cond_dir]
            arquivos = sorted(os.listdir(cam_out))
            texto = ''
            for a in arquivos:
                if a.endswith(('.md', '.py')):
                    with open(os.path.join(cam_out, a), encoding='utf-8') as fh:
                        texto += fh.read() + '\n'

            # --- eval_metadata.json
            meta = {
                'eval_id': eval_id,
                'eval_name': eval_dir,
                'skill_avaliada': SKILL_DO_EVAL[eval_dir],
                'prompt': PROMPTS[eval_dir],
                'condicao': cond_dir,
                'condicao_rotulo': rotulo,
                'configuration': config,
                'run_number': run_number,
                'assertions': [a[0] for a in ASSERCOES[eval_dir]],
                'assertions_post_hoc': True,
                'correcao': 'automatica (padrao de texto e presenca de arquivo)',
            }
            with open(os.path.join(cam_run, 'eval_metadata.json'), 'w', encoding='utf-8') as fh:
                json.dump(meta, fh, ensure_ascii=False, indent=2)

            # --- timing.json (recuperado do historico, nao re-executado)
            chave = (eval_dir, cond_dir)
            tok, dur = TIMING.get(chave, (None, None))
            tj = {
                'total_tokens': tok,
                'duration_ms': dur,
                'total_duration_seconds': round(dur / 1000, 1) if dur else None,
                'origem': 'recuperado do historico da conversa; a execucao nao foi repetida',
            }
            with open(os.path.join(cam_run, 'timing.json'), 'w', encoding='utf-8') as fh:
                json.dump(tj, fh, ensure_ascii=False, indent=2)

            # --- grading.json
            exps = []
            for txt_a, fn in ASSERCOES[eval_dir]:
                ok = bool(fn(texto, arquivos))
                exps.append({
                    'text': txt_a,
                    'passed': ok,
                    'evidence': ('padrao encontrado nas saidas' if ok
                                 else 'padrao ausente em todas as saidas desta execucao'),
                })
            passou = sum(1 for e in exps if e['passed'])
            grading = {
                'expectations': exps,
                'summary': {
                    'passed': passou,
                    'failed': len(exps) - passou,
                    'total': len(exps),
                    'pass_rate': round(passou / len(exps), 3),
                },
                'timing': {'total_duration_seconds': tj['total_duration_seconds']},
                'condicao_rotulo': rotulo,
                'ressalva': 'assercoes post-hoc, correcao automatica por padrao de texto',
            }
            with open(os.path.join(cam_run, 'grading.json'), 'w', encoding='utf-8') as fh:
                json.dump(grading, fh, ensure_ascii=False, indent=2)

            runs.append({
                'eval_id': eval_id,
                'eval_name': f'{eval_dir}  [{ "FRIA" if cond_dir.endswith("fria") else ("MORNA" if config=="without_skill" else "SKILL") }]',
                'configuration': config,
                'run_number': run_number,
                'result': {
                    'pass_rate': grading['summary']['pass_rate'],
                    'passed': passou,
                    'failed': len(exps) - passou,
                    'total': len(exps),
                    'time_seconds': tj['total_duration_seconds'],
                    'tokens': tok,
                    'tool_calls': None,
                    'errors': 0,
                },
                'expectations': exps,
                'notes': [rotulo,
                          f'arquivos produzidos: {", ".join(arquivos)}'],
            })

    # ------------------------------------------------------------------ resumo
    def agrega(sel):
        pr = [r['result']['pass_rate'] for r in sel]
        ts = [r['result']['time_seconds'] for r in sel]
        tk = [r['result']['tokens'] for r in sel]
        def st(v):
            return {'mean': round(statistics.mean(v), 3),
                    'stddev': round(statistics.pstdev(v), 3) if len(v) > 1 else 0.0,
                    'min': min(v), 'max': max(v)}
        return {'pass_rate': st(pr), 'time_seconds': st(ts), 'tokens': st(tk), 'n': len(sel)}

    com = [r for r in runs if r['configuration'] == 'with_skill']
    # A FRIA e uma condicao diferente, nao repeticao: fica FORA da media de baseline.
    morna = [r for r in runs if r['configuration'] == 'without_skill' and r['run_number'] == 1]
    fria = [r for r in runs if r['configuration'] == 'without_skill' and r['run_number'] == 2]

    resumo = {'with_skill': agrega(com), 'without_skill': agrega(morna)}
    if fria:
        resumo['without_skill_FRIA_isolada'] = agrega(fria)
    resumo['delta'] = {
        'pass_rate': f"{resumo['with_skill']['pass_rate']['mean'] - resumo['without_skill']['pass_rate']['mean']:+.3f}",
        'time_seconds': f"{resumo['with_skill']['time_seconds']['mean'] - resumo['without_skill']['time_seconds']['mean']:+.1f}",
        'tokens': f"{resumo['with_skill']['tokens']['mean'] - resumo['without_skill']['tokens']['mean']:+.0f}",
    }

    bench = {
        'metadata': {
            'skill_name': 'rpg-guilda (4 skills)',
            'skill_path': 'RPG-JJK/skills/',
            'executor_model': 'claude-sonnet (subagentes)',
            'sessao_principal': 'claude-opus — NAO e o modelo dos executores',
            'timestamp': agora,
            'evals_run': sorted({r['eval_id'] for r in runs}),
            'runs_per_configuration': 1,
            'condicoes': {
                'with_skill': 'leu o SKILL.md e arquivos de apoio',
                'without_skill run 1 (MORNA)': 'sem skill, COM acesso a pasta do projeto',
                'without_skill run 2 (FRIA)': 'sem skill, SEM acesso a pasta do projeto (so eval-3)',
            },
        },
        'runs': runs,
        'run_summary': resumo,
        'notes': [
            'CONDICOES NAO SAO REPETICOES. O eval-3 tem tres condicoes: com skill, baseline MORNA '
            '(com acesso ao projeto) e baseline FRIA (isolada). A FRIA fica FORA da media de '
            'without_skill de proposito — misturar as duas produziria um numero sem significado.',
            'A baseline FRIA e o unico par "skill vs nada" real da matriz inteira. Os demais evals '
            'comparam a skill contra Claude que ja tinha lido o dossie da Fase 1.',
            'Assercoes escritas DEPOIS de ver as saidas (post-hoc). Isso favorece o que ja aconteceu '
            'e enfraquece a nota como evidencia.',
            'Uma execucao por condicao: sem estimativa de variancia. Diferenca pequena de pass_rate '
            'nao deve ser lida como efeito real.',
            'Quem escreveu as skills tambem escreveu os prompts de teste — vies a favor das skills. '
            'O eval-0 e o caso mais grave: o enunciado ja apresenta duas desvantagens de mesmo preco '
            'lado a lado, que e exatamente a montagem que o teste de dominancia pede.',
            'Executores em Sonnet, sessao do usuario em Opus: o benchmark mede o efeito no modelo errado.',
            'Correcao automatica por padrao de texto mede se o conceito APARECE, nao se esta correto.',
        ],
    }

    with open(os.path.join(IT, 'benchmark.json'), 'w', encoding='utf-8') as fh:
        json.dump(bench, fh, ensure_ascii=False, indent=2)

    # relatorio no terminal
    print('=' * 92)
    print('BENCHMARK — iteracao 1')
    print('=' * 92)
    for r in runs:
        print(f"  {r['eval_name']:<48} {r['result']['passed']}/{r['result']['total']}  "
              f"({r['result']['pass_rate']*100:5.1f}%)  {r['result']['time_seconds']:6.1f}s  "
              f"{r['result']['tokens']:>7} tok")
    print()
    for k, v in resumo.items():
        if k == 'delta':
            continue
        print(f"  {k:<32} pass {v['pass_rate']['mean']*100:5.1f}%  "
              f"tempo {v['time_seconds']['mean']:6.1f}s  tokens {v['tokens']['mean']:>8.0f}  (n={v['n']})")
    print(f"  {'delta (skill - morna)':<32} pass {resumo['delta']['pass_rate']}  "
          f"tempo {resumo['delta']['time_seconds']}s  tokens {resumo['delta']['tokens']}")
    print()
    print(f'benchmark.json escrito em {IT}')


if __name__ == '__main__':
    main()
