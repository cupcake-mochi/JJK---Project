"""Registrar a comparação 146 uma vez; não modifica fontes do livro ou PDFs."""
from pathlib import Path
import hashlib, json, os, re

A = Path(__file__).resolve().parent
R = A.parents[1]
M = R / '04 - Planejamento/apoio-piloto/manifesto-entrega.json'
REPORT = R / '04 - Planejamento/146-comparacao-final-e-proximos-ajustes.md'
load = lambda p: json.loads(p.read_text())
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
def save(p, data):
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')

def main():
    assert load(M) == load(A / 'antes/manifesto-entrega.json')
    assert len(load(M)) == 6363
    controls = [
        'LEIA-ME.md', 'RETOMADA-CODEX-2026-10-23.md',
        '04 - Planejamento/01-plano-completo-do-guia.md',
        '04 - Planejamento/04-competencias-que-o-livro-deve-ensinar.md',
        '04 - Planejamento/19-roteiro-pre-1-e-modelos.md',
        '04 - Planejamento/98-plano-de-melhoria-e-validacao-do-guia.md',
        '04 - Planejamento/99-sumario-comentado-e-caminhos-de-leitura.md',
        '06 - Redacao do Guia/LEIA-ME.md',
        '06 - Redacao do Guia/revisao-98/LEIA-ME.md',
        '04 - Planejamento/apoio-piloto/RETOMADA.md',
        '07 - Edicao de Leitura/LEIA-ME.md',
        '08 - Diagramacao do Guia/LEIA-ME.md',
    ]
    for rel in controls:
        p = R / rel
        old = p.read_text()
        assert 'Fila vigente - registro 146' not in old, rel
        backup = A / 'antes' / rel
        backup.parent.mkdir(parents=True, exist_ok=True)
        assert not backup.exists()
        backup.write_bytes(p.read_bytes())
        old = re.sub(r'> \*\*Fila vigente', '> **Fila histórica', old, count=1)
        target = os.path.relpath(REPORT, p.parent)
        block = (
            '> **Fila vigente - registro 146, 30/10/2026:** comparação editorial da etapa 8 concluída, '
            f'com [parecer, matriz das 20 competências e notas da edição](<{target}>). '
            'Primeira missão reunida, preparo mínimo e variedade demonstrados; equivalência geral ainda parcial. '
            '**Próximo: três ajustes editoriais — folhas curtas primeiro, distinção de falas e comentários, '
            'redução de avisos genéricos repetidos nas ideias; GPT-6.1 Sol, esforço alto.** '
            'Depois, conferir texto e PDF afetados e incorporar retorno da pré-1.0. '
            'Dificuldade geral dos encontros permanece em frente mecânica separada. '
            'PDF atual de 383 páginas, HTML e regras inalterados neste lote. '
            'Geradores: PDF 145; HTML 144. Salvamento local; último GitHub: registro 141.\n\n'
        )
        first, rest = old.split('\n', 1)
        new = first + '\n\n' + block + rest.lstrip('\n')
        if rel.endswith('98-plano-de-melhoria-e-validacao-do-guia.md'):
            start = new.index('## 7. Próxima tarefa e configuração')
            new = new[:start] + '''## 7. Próxima tarefa e configuração

**Situação no registro 146:** as três perguntas receberam novo parecer sobre o PDF de 383 páginas. A comparação editorial da etapa 8 está concluída, com limites identificados. O resultado não certifica equivalência de aprendizagem ou equilíbrio com livros publicados.

**Próximo lote:** aplicar os três ajustes delimitados no [parecer final](146-comparacao-final-e-proximos-ajustes.md): colocar as folhas curtas antes dos formulários completos; distinguir conversa, comentário e consulta técnica na primeira missão; reunir avisos genéricos repetidos nas ideias de aventuras. Preservar regras, números e condições no ponto de escolha.

Fazer duas leituras dos trechos alterados, recompor e conferir referências. Revisar visualmente todas as páginas afetadas; se o conjunto for repaginado, percorrer todo o fluxo. Não ampliar este lote com outra coleção de aventuras ou rebalanceamento de inimigos.

**Recomendação já prevista para ajustes e consolidação:** GPT-6.1 Sol, esforço alto. A frente mecânica mantém GPT-6 Astra, esforço extra alto. Estas configurações são recomendações do projeto, sem mudança automática de modelo ou alegação de desempenho medido entre modelos.

Depois dos ajustes, incorporar retorno da pré-1.0 pelas tarefas e perfis da seção 5. Leitores não foram recrutados; sua disponibilidade não bloqueia a conclusão editorial. O fechamento da 1.0 terá uma decisão própria sobre as limitações restantes.
'''
        p.write_text(new)

    meta = load(A / 'fontes-consultadas.json')
    consulted = {
        'dmg2024': [12, 13, 14, 15, 35, 51, 123],
        'dmg2014': [4, 90, 91], 'pf2': [489, 490, 491],
        'cairn': [8, 9, 32, 33, 56, 57, 154, 155],
        'fate': [195, 196, 197, 248, 249, 250],
        'lazy': [1, 2, 3, 4, 5, 6], 'wwn': [146, 150, 151],
    }
    for row in meta:
        row['paginas_usadas_na_avaliacao'] = consulted[row['id']]
    current = '08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0-Revisado.pdf'
    previous = '08 - Diagramacao do Guia/output/pdf/Ciclo-Maldito-Guia-do-Mestre-Pre-1.0.pdf'
    save(A / 'fontes-consultadas.json', {
        'registro': 146, 'data': '2026-10-30', 'livros': meta,
        'guia_atual': {'arquivo': current, 'paginas': 383, 'sha256': sha(R/current)},
        'guia_anterior': {'arquivo': previous, 'paginas': 357, 'sha256': sha(R/previous)},
        'resenhas_reabertas': [
            {'titulo': "DnD 2024 Dungeon Master's Guide review", 'autor': 'Mollie Russell',
             'url': 'https://www.wargamer.com/dnd/2024-dungeon-masters-guide-review',
             'atualizacao_indicada': '2024-10-15'},
            {'titulo': 'Prep Techniques / Review – Return of the Lazy Dungeon Master',
             'autor_exibido': 'guyeatsfood',
             'url': 'https://burnafterrunningrpg.com/2021/07/12/prep-techniques-review-return-of-the-lazy-dungeon-master/',
             'data_da_entrada': '2021-07'},
        ],
        'limites': ['Consulta dirigida, não nova leitura integral das referências.',
                    'Pathfinder Livro Básico anterior ao Remaster; não GM Core.',
                    'Lazy GM é o documento de recursos; não o livro integral.',
                    'Resenhas são opiniões individuais; não consenso.',
                    'Sem novos participantes externos ou sessões observadas.'],
    })
    tasks = [
        ('Primeira missão', [3,4,5,6,7,8,9,10,11,12,13], 'Caminho e materiais localizados; fichas de jogadores e Livro de Regras são prévios.'),
        ('Outra situação', [19,23,24,25,26,116], 'Aplicação interna registrada na matriz; sem jogo real.'),
        ('Recusa e grupo sem rumo', [30,31,32,117], 'Respostas concretas e alternativas encontradas.'),
        ('Retomada', [75,76,77,95,96,118,119,120], 'Próximo turno e dados de socorro recuperáveis; sem mestre externo.'),
        ('Limite de ataque especial', [43,166,167,168,169,170,171,172], 'Método distingue PE, usos, recarga, intervalo e preparo.'),
        ('Dificuldade para outro grupo', [44,45,46,173,174,175,176,177,178,179,180], 'Parcial: existem premissas; falta ferramenta geral validada.'),
    ]
    save(A / 'conferencia-de-aplicacao.json', {
        'registro': 146, 'tipo': 'Conferência editorial pelo assistente',
        'tarefas': [dict(tarefa=t,paginas_de_consulta=pages,resultado=result) for t,pages,result in tasks],
        'leitores_externos': 0, 'mesas_realizadas': 0, 'tempo_de_uso_medido': False,
        'simulacao_nova_de_equilibrio': False,
        'nota': 'Destinos conferidos no texto, no mapa de composição e em extrações dirigidas. Não é uma nova leitura integral de todos os casos citados.'
    })
    save(A / 'arquivos-do-lote.json', {
        'registro':146, 'controles':controls, 'relatorio':REPORT.relative_to(R).as_posix(),
        'fontes_alteradas':[], 'html_alterados':[], 'pdfs_alterados':[],
        'proximo':'Três ajustes editoriais do parecer; GPT-6.1 Sol, esforço alto.',
    })
    print(json.dumps({'controles':len(controls),'fontes_modificadas':0,'pdfs_modificados':0}))

if __name__ == '__main__':
    main()
