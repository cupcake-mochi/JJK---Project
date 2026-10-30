"""Edições da primeira passagem do lote C-04 das consultas complementares (registro 134). Lidas por REVISAR.py.

As cópias ficam em revisao-98/consultas/. Cada remissão a um capítulo antigo vai para o capítulo novo que recebeu
o conteúdo, conforme o mapa de destinos do registro 99 (estrutura-e-fontes.json). Quando o texto do link era o
título antigo, passa a ser o título da seção nova; textos descritivos ("Entrada essencial", "Modos de vida") ficam."""
from pathlib import Path
import re
A = Path(__file__).resolve().parent
G = A.parents[1] / '06 - Redacao do Guia'
COPIA = 'Criar cópia e apontar as remissões para os capítulos novos e cópias revistas, conforme o mapa de destinos do registro 99; links com título antigo recebem o título da seção nova.'
CLARO = 'Clareza: frase direta, termo do Livro de Regras 1.0 ou ordem de leitura.'
PENTE = 'Pente fino da segunda leitura, na prova completa.'

CAP = {  # fonte antiga -> capítulo novo (registro 99)
    '01-preparar-uma-missao.md': '../03-preparar-aventuras.md',            # 3.1 O que preparar
    '13-preparar-uma-investigacao.md': '../03-preparar-aventuras.md',      # 3.4 Pistas e investigações
    '06-mundo-e-cotidiano.md': '../02-o-mundo-dos-feiticeiros.md',
    '86-sociedade-apoio-e-modos-de-vida.md': '../02-o-mundo-dos-feiticeiros.md',  # 2.3 e 2.4
    '07-preparar-o-grupo.md': '../05-criar-uma-campanha.md',               # 5.1
    '17-faccoes-e-reacoes.md': '../05-criar-uma-campanha.md',              # 5.4
    '26-vinculos-e-mudancas.md': '../05-criar-uma-campanha.md',            # 5.2
    '21-acompanhar-recursos.md': '../04-na-mesa-de-jogo.md',               # 4.7
    '25-conferir-personagens.md': '../07-personagens-e-tecnicas.md',       # 7.1
    '27-convivencia-do-receptaculo.md': '../07-personagens-e-tecnicas.md', # 7.2
    '29-avaliar-tecnicas-e-criacoes.md': '../07-personagens-e-tecnicas.md',# 7.4
    '35-equipamento-acesso-e-servicos.md': '../08-entre-missoes.md',       # 8.4
    '37-recompensas-e-fechamento.md': '../08-entre-missoes.md',            # 8.6
    '41-pactos-e-promessas.md': '../09-pactos-e-entidades.md',
}
CASOS = {'23-retirada-e-recuperacao.md', '30-pareceres-de-criacoes.md', '31-avaliar-poderes-avancados.md', '43-aquisicao-e-projetos-de-entidades.md',
         '52-domar-o-amontoado.md', '81-passar-a-missao-entre-mestres.md', '83-perceber-procurar-e-interpretar-sinais.md'}
IRMAS = {'08-ficha-de-acordos-do-grupo.md', '12-registro-de-descobertas.md', '87-casos-da-obra-para-preparar-situacoes.md', '88-indice-de-termos-do-mundo.md'}
TITULO = {  # (texto antigo, fonte) -> texto novo
    ('O mundo de Ciclo Maldito', '06-mundo-e-cotidiano.md'): 'O mundo dos feiticeiros',
    ('A sociedade jujutsu', '86-sociedade-apoio-e-modos-de-vida.md'): 'Escolas, famílias e contatos',
    ('Vínculos e mudanças', '26-vinculos-e-mudancas.md'): 'Vínculos e interesses dos personagens',
    ('Avaliar técnicas e criações', '29-avaliar-tecnicas-e-criacoes.md'): 'Avaliar uma capacidade',
    ('Avaliar técnicas', '29-avaliar-tecnicas-e-criacoes.md'): 'Avaliar uma capacidade',
    ('Avaliar criações', '29-avaliar-tecnicas-e-criacoes.md'): 'Avaliar uma capacidade',
    ('Conferir personagens', '25-conferir-personagens.md'): 'Conferir a ficha',
    ('Convivência do Receptáculo', '27-convivencia-do-receptaculo.md'): 'Personagens e seus cuidados',
    ('Preparar uma missão', '01-preparar-uma-missao.md'): 'O que preparar',
    ('Preparar uma investigação', '13-preparar-uma-investigacao.md'): 'Pistas e investigações',
    ('Acompanhar recursos', '21-acompanhar-recursos.md'): 'Combate, socorro e retirada',
    ('Recursos', '21-acompanhar-recursos.md'): 'Combate, socorro e retirada',
    ('Pactos e Promessas', '41-pactos-e-promessas.md'): 'Pactos e entidades',
    ('Encerrar a missão e entregar recompensas', '37-recompensas-e-fechamento.md'): 'Recompensas e progressão',
    ('Equipamento e acesso', '35-equipamento-acesso-e-servicos.md'): 'Comprar, emprestar e contratar',
    ('Sociedade e apoio', '86-sociedade-apoio-e-modos-de-vida.md'): 'Escolas, famílias e contatos',
}


def destino(n):
    if n in CAP: return CAP[n]
    if n in CASOS: return '../casos/' + n
    if n in IRMAS: return n
    raise KeyError(n)


LINKS, MULTI = {}, {}
for cid, nome in [('s088', '88-indice-de-termos-do-mundo.md'), ('s087', '87-casos-da-obra-para-preparar-situacoes.md')]:
    src = (G / nome).read_text()
    pares = sorted(set(re.findall(r'\[([^\]]+)\]\(([0-9][^)#]*\.md)\)', src)))
    one, many = [], []
    for texto, alvo in pares:
        a = f'[{texto}]({alvo})'
        b = f'[{TITULO.get((texto, alvo), texto)}](<{destino(alvo)}>)'
        (one if src.count(a) == 1 else many).append((a, b))
    LINKS[cid], MULTI[cid] = one, many

E = []
def e(caso_, antes, depois, motivo=CLARO, passagem=1, tipo='clareza'):
    E.append((caso_, passagem, tipo, motivo, antes, depois))

# ---------------------------------------------------------------- s088
e('s088', 'As definições resumem o uso no Guia e no Livro de Regras 1.0; custos, exceções e aquisição continuam na regra correspondente.',
  'As definições resumem o uso no Guia e no Livro de Regras 1.0; custos, exceções e aquisição ficam na regra de cada termo.')
e('s088', 'São escolhas originais desta campanha.', 'As duas foram criadas para esta campanha; não vêm da obra.',
  'Clareza: "originais" podia ser lido como "da obra".')

# ---------------------------------------------------------------- s087
e('s087', 'Os exemplos abaixo se baseiam nas sinopses oficiais indicadas em cada caso.',
  'Cada caso abaixo se baseia na sinopse oficial ou apresentação editorial indicada nele.',
  'Clareza: o caso dos aliados usa a apresentação editorial do volume 18, não uma sinopse de episódio.')
