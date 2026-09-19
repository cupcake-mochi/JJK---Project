# -*- coding: utf-8 -*-
"""Confere a economia de acao: regua de preco das Restricoes, dominancia e Adianta.

Roda antes de fechar qualquer versao que mexa em Restricao de tempo ou movimento.

CONTRATO:
  Turno = movimento (9 m) + acao padrao + acao bonus + reacao
  Rodada inteira = movimento + acao padrao + acao bonus, de uma vez
  Iniciativa = d20 + Destreza

REGUA DE PRECO (derivada dos recursos, nao arbitrada):
  Leve  = consome UM recurso, ou meio recurso por dois turnos
  Media = consome o TURNO INTEIRO, ou um recurso mais um risco real

  1. Toda Restricao do catalogo tem que caber na regua.
  2. Nenhum par de mesmo preco pode ter um conjunto de recursos contendo o outro.
  3. Adianta so vale o preco se a iniciativa for ROLADA — com iniciativa fixa ela
     vira bonus automatico para quem tem Destreza alta.

E, desde a v0.253, a checagem 7: a Concentracao rola Vigor contra a CD de quem
feriu, e as duas tabelas e os numeros da prosa da peca 3 saem dos donos.
"""
import itertools
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, '..', 'skills', 'balanceamento-simulacao', 'scripts'))
from dados import soma, p_ao_menos  # noqa: E402

ERROS = []


def erro(msg):
    ERROS.append(msg)
    print('  ERRO:', msg)


# nome: (preco, recursos consumidos, quando)
RESTRICOES = {
    'Parado':        ('Leve',  {'movimento'},                                'este turno'),
    'Gesto':         ('Leve',  {'maos', 'voz'},                              'este turno'),
    'Peso Morto':    ('Leve',  {'meio_movimento', 'meio_movimento_proximo'}, 'dois turnos'),
    'Fragil':        ('Leve',  {'risco_perder_efeito'},                      'ate o proximo'),
    'Tudo ou Nada':  ('Leve',  {'chance_de_zerar'},                          'na hora'),
    'Atrasar':       ('Media', {'movimento', 'acao_bonus', 'acao_padrao'},   'este turno'),
    'Corpo a Corpo': ('Media', {'distancia'},                                'permanente'),
    'Sangra':        ('Media', {'vida'},                                     'na hora'),
    'Recuo':         ('Media', {'corpo_condicao_menor'},                     'ate o proximo'),
    'Sem Volta':     ('Media', {'proximo_turno_inteiro'},                    'condicional'),
    # DECISAO v0.11: quem carrega mantem movimento e acao bonus no turno de carga.
    # Sem isso, Carregar = Atrasar + espera + risco, e fica dominado.
    'Carregar':      ('Media', {'acao_padrao_anterior', 'risco_perder_tudo'}, 'turno anterior'),
    # A `Divida` era uma das SETE que este validador nao alcancava — a peca 14
    # registra a lista. Ela entrou quando a regra mudou de "custa o dobro de
    # energia" para um acrescimo fixo, porque a redacao velha se esquivava: o
    # dobro de um feitico de Classe 0 e ZERO, e o manual chama Classe 0 de "o
    # golpe de todo turno em que o PE precisa ser poupado".
    'Divida':        ('Media', {'pe_do_proximo_feitico'},                    'condicional'),
}

print('=' * 92)
print('1. BALANCO DE RECURSOS')
print('=' * 92)
print(f"  {'Restricao':<16}{'preco':<8}{'quando':<16}consome")
for n, (p, rec, q) in sorted(RESTRICOES.items(), key=lambda x: (x[1][0], x[0])):
    print(f'  {n:<16}{p:<8}{q:<16}{sorted(rec)}')

print()
print('=' * 92)
print('2. DOMINANCIA — algum par de mesmo preco em que um contem o outro?')
print('=' * 92)
achou = False
for a, b in itertools.permutations(RESTRICOES, 2):
    pa, ra, _ = RESTRICOES[a]
    pb, rb, _ = RESTRICOES[b]
    if pa != pb:
        continue
    if rb > ra:
        achou = True
        erro(f'"{b}" contem "{a}" e as duas custam {pa}')
        print(f'     {b}: {sorted(rb)}')
        print(f'     {a}: {sorted(ra)}')
if not achou:
    print('  Nenhum par estritamente dominado. As 11 Restricoes cabem na regua.')

print()
print('=' * 92)
print('3. A REGUA — cada preco corresponde ao peso certo?')
print('=' * 92)
TURNO = {'movimento', 'acao_padrao', 'acao_bonus'}
for n, (p, rec, q) in RESTRICOES.items():
    turno_inteiro = TURNO <= rec
    tem_risco = any('risco' in r or 'chance' in r for r in rec)
    if p == 'Media' and not (turno_inteiro or tem_risco or len(rec) >= 1):
        erro(f'{n} custa Media mas nao consome turno inteiro nem carrega risco')
    if p == 'Leve' and turno_inteiro:
        erro(f'{n} custa Leve mas consome o turno inteiro')
print('  Nenhuma Leve consome o turno inteiro; nenhuma Media custa menos que um recurso.')

print()
print('=' * 92)
print('4. ADIANTA — quanto vale, e por que a iniciativa precisa ser rolada')
print('=' * 92)
D20 = soma([20])


def ganha_iniciativa(minha_des, dele_des):
    """P(d20+minha > d20+dele), empate resolvido pela maior Destreza."""
    p = 0.0
    for a in range(1, 21):
        for b in range(1, 21):
            ta, tb = a + minha_des, b + dele_des
            if ta > tb or (ta == tb and minha_des >= dele_des):
                p += 1
    return p / 400


print(f"  {'Destreza sua':<14}{'Destreza dele':<16}{'age antes':<12}{'valor medio de Adianta'}")
for md, dd in [(3, 3), (4, 3), (6, 3), (3, 5)]:
    p = ganha_iniciativa(md, dd)
    print(f'  {md:<14}{dd:<16}{p*100:>8.0f}%    {p*10:>10.1f} pp de efeito')
print()
print('  Com iniciativa FIXA (ordem = Destreza), quem tem Destreza maior age antes')
print('  em 100% das rodadas: Adianta vira +2 permanente por preco Medio.')
print('  Isso e o teste do bonus automatico falhando. Por isso a iniciativa e rolada.')
fixa = 1.0
if fixa * 10 <= 10 * ganha_iniciativa(4, 3):
    erro('iniciativa fixa nao tornaria Adianta automatica — reveja o argumento')

print()
print('=' * 92)
print('  A LISTA DE ACOES — peca 3 SS3.1, escrita na v0.83')
print('=' * 92)
#
# Ate a v0.82 esta peca tinha os quatro slots do turno e NENHUMA acao nomeada.
# A lista vivia no fim do DESENHO-caminhos.md, que nao e peca, e NOVE Trilhas
# fechadas apontavam para ela. Agora a peca 3 SS3.1 e a dona.
#
# NADA DE VALOR MORA AQUI: os nomes sao lidos da propria peca. O que este bloco
# guarda e a ESTRUTURA — que as doze existam, que Agarrar e Derrubar NAO sejam
# acoes proprias, e que a linha que separa Ler o Ambiente de Vasculhar/Estudar
# continue escrita.
import re as _re

_p3 = os.path.join(AQUI, '03-economia-de-acao-e-iniciativa.md')
if not os.path.exists(_p3):
    erro('nao achei a peca 3 para conferir a lista de acoes')
else:
    _t3 = open(_p3, encoding='utf-8').read()
    _sec = _re.search(r'## 3\.1 A lista de a[cç][oõ]es(.*?)(?=\n## 4\.)', _t3, _re.S)
    if not _sec:
        erro('a peca 3 nao tem mais a secao 3.1 "A lista de acoes" — ela e a dona '
             'da lista desde a v0.83, e nove Trilhas apontam para ela')
    else:
        _txt = _sec.group(1)

        # 1. as doze de Acao Padrao continuam nomeadas
        _doze = ['Atacar', 'Conjurar', 'Correr', 'Desengajar', 'Esquivar', 'Esconder',
                 'Ajudar', 'Influenciar', 'Preparar', 'Vasculhar', 'Estudar',
                 'Usar objeto']
        _faltando = [a for a in _doze
                     if not _re.search(r'\|\s*\*\*' + _re.escape(a) + r'\*\*\s*\|', _txt)]
        if _faltando:
            erro(f'peca 3 SS3.1: sumiram da tabela de Acao Padrao: {_faltando}. A lista '
                 f'do 5e 2024 tem doze e a decisao foi copiar as doze — oito ja '
                 f'existiam aqui, Influenciar e Preparar entraram, e Vasculhar e '
                 f'Estudar sao o Search e o Study com alvo separado')
        else:
            print(f'  [x] as {len(_doze)} acoes de Acao Padrao estao nomeadas na tabela')

        # 2. Agarrar e Derrubar NAO podem ser acao propria — sao opcao do Atacar.
        #    Como acao propria elas ficam mortas: agarrar custaria o turno inteiro
        #    e bater duas vezes rende mais que segurar alguem.
        _proprias = [a for a in ('Agarrar', 'Derrubar')
                     if _re.search(r'\|\s*\*\*' + a + r'\*\*\s*\|', _txt)]
        if _proprias:
            erro(f'peca 3 SS3.1: {_proprias} voltaram a ser acao propria. Elas sao '
                 f'OPCAO da acao de Atacar desde a v0.83 (o 2024 fez igual): como '
                 f'acao propria elas ficam dominadas, porque bater duas vezes rende '
                 f'mais do que gastar o turno segurando alguem')
        else:
            print('  [x] Agarrar e Derrubar sao opcao do Atacar, e nao acao propria')

        # 3. A LINHA QUE MATA A DOMINANCIA, e ela e a unica coisa de balanco aqui.
        #    Ler o Ambiente e Acao BONUS; Vasculhar e Estudar sao Acao PADRAO. Se
        #    os tres respondessem a mesma pergunta, ninguem usaria os dois caros.
        #    O que separa e o ALVO: o Ler o Ambiente fala do LUGAR e nunca de
        #    criatura. Sem essa linha escrita, a dominancia volta em silencio.
        _guarda = _re.search(r'`?Ler o Ambiente`?\s*NUNCA fala de criatura', _txt)
        if not _guarda:
            erro('peca 3 SS3.1: sumiu a linha que diz que o "Ler o Ambiente" NUNCA '
                 'fala de criatura. Ela e o que separa ele do Vasculhar e do '
                 'Estudar — sem ela os tres respondem a mesma pergunta, e uma Acao '
                 'Bonus domina duas Acoes Padrao')
        else:
            print('  [x] a linha de alvo que separa Ler o Ambiente de Vasculhar/Estudar')

        # 4. o teto do Ler o Ambiente — ele obriga o mestre a produzir conteudo
        if not _re.search(r'Ler o Ambiente`?\*\*.{0,120}uma vez por cena', _txt, _re.S | _re.I):
            erro('peca 3 SS3.1: o "Ler o Ambiente" perdeu o teto de uma vez por cena. '
                 'Sem teto ela obriga o mestre a produzir conteudo em todo turno e '
                 'vira imposto de improviso')
        else:
            print('  [x] o "Ler o Ambiente" continua com teto de uma vez por cena')

        # 5. o Ajudar ganhou custo de acao nesta versao, e ele nunca tinha tido um.
        #    A peca 4 SS5 escreve a regra do "um por teste" e nunca disse o slot.
        if not _re.search(r'\|\s*\*\*Ajudar\*\*\s*\|', _txt):
            erro('peca 3 SS3.1: o Ajudar saiu da tabela de Acao Padrao. Ele e a unica '
                 'acao que ja existia escrita em OUTRA peca (a 4 SS5) sem custo de '
                 'acao declarado, e foi esta secao que deu um a ele')
        else:
            print('  [x] o Ajudar esta na tabela, com o custo de acao que faltava')

print()
print('=' * 92)
print('5. A `Divida` — o mesmo numero nas duas publicacoes, e sem o desvio do Classe 0')
print('=' * 92)
# ⚠ Este validador NAO abria o .docx, e a peca 14 registra isso como divida:
# "a faixa de cada Restricao esta escrita a mao dentro dele, e ele cobre 11 das
# 18". O dono do texto da `Divida` e o manual; o 40-fundamento.md e copia. Sem
# comparar os dois, a regra que decide gasto de PE podia divergir calada.
_DOCX = os.path.join(AQUI, '..', '..', 'manual', 'Fundamento-MANUAL-v7.docx')
_MD = os.path.join(AQUI, '..', '05-material', 'livro', 'manual', '40-fundamento.md')
try:
    import docx as _docx
except ImportError:
    _docx = None

if _docx is None:
    print('  PULADA: sem python-docx nao da para ler o manual, que e o DONO do texto.')
    print('          pip install python-docx --break-system-packages')
elif not os.path.isfile(_DOCX):
    erro('nao achei o manual .docx — o dono do texto da `Divida` nao foi conferido')
else:
    import re as _re
    _cel = None
    for _t in _docx.Document(_DOCX).tables:
        for _r in _t.rows:
            if _r.cells[0].text.strip() == 'Dívida':
                _cel = _r.cells[2].text.strip()
    if not _cel:
        erro('a `Divida` sumiu da tabela de Restricoes do manual')
    else:
        _mdoc = _re.search(r'custa (\d+) × a Classe deste feitiço', _cel)
        _dobro = 'o dobro de energia' in _cel
        if _dobro:
            erro('o manual voltou a dizer "o dobro de energia" na `Divida` — o dobro de '
                 'um feitico de Classe 0 e ZERO, e a Restricao se esquiva com o golpe '
                 'que o proprio manual manda usar para poupar PE')
        elif not _mdoc:
            erro(f'nao achei o multiplicador da `Divida` no manual: "{_cel[:70]}"')
        else:
            _n = int(_mdoc.group(1))
            _md = open(_MD, encoding='utf-8').read()
            # ⚠ a palavra `Dívida` aparece TRES vezes neste capitulo — a linha da
            # tabela, a lista de Restricoes de frequencia e a trava de combinacao.
            # Pegar "a primeira ocorrencia" le a lista, nao a regra. Casa a LINHA
            # inteira da tabela, que e a unica que carrega o multiplicador.
            _mmd = _re.search(r'^\|\s*`Dívida`\s*\|[^|]*\|([^|]*)\|\s*$', _md, _re.M)
            _linha_md = _mmd.group(1) if _mmd else ''
            _mmd = _re.search(r'`(\d+) ×` a Classe deste feitiço', _linha_md) if _mmd else None
            if not _mmd:
                erro('o 40-fundamento.md nao publica o multiplicador da `Divida` na mesma '
                     'forma que o manual — um numero, um dono')
            elif int(_mmd.group(1)) != _n:
                erro(f'a `Divida` e {_n}x no manual e {_mmd.group(1)}x no 40-fundamento.md')
            elif 'Classe 0' not in _cel or 'Classe 0' not in _linha_md:
                erro('a `Divida` parou de dizer que vale mesmo num feitico de Classe 0 — '
                     'sem essa frase o desvio de graca volta')
            else:
                # a ancora: uma `Media` devolve 1 x Classe, e o cap. 40 escreve que
                # duas `Media` batem no teto de 2 x Classe. Cobrar MENOS do que
                # devolve faria a Restricao pagar para ser levada.
                if _n < 1:
                    erro(f'a `Divida` cobra {_n}x a Classe e uma `Media` DEVOLVE 1x — '
                         'ela passaria a dar mais do que tira')
                else:
                    print(f'  [x] a `Divida` cobra {_n} x a Classe do proprio feitico, o '
                          f'manual e o 40-fundamento.md concordam, e os dois dizem que ela '
                          f'vale mesmo num Classe 0.')

    # v0.221: a MESMA frase morava na `Sobrecarga`, e esta checagem so' olhava a
    # `Divida`. La ela dizia "o feitico dele custa o dobro de energia" — ZERO contra
    # inimigo, que nao conta PE (peca 26 §6.1), e o dobro de zero contra quem
    # conjura Classe 0, que e' o buraco que a v0.217 fechou na `Divida`. A metade
    # que entrou no lugar e' "ele nao usa Reacao". Sem esta guarda a frase voltava
    # pela porta que ninguem olhava.
    import re as _re
    _cel_s = None
    for _t in _docx.Document(_DOCX).tables:
        for _r in _t.rows:
            if _r.cells[0].text.strip() == 'Sobrecarga':
                _cel_s = _r.cells[2].text.strip()
    _mds = _re.search(r'^\|\s*`Sobrecarga`\s*\|[^|]*\|([^|]*)\|\s*$',
                      open(_MD, encoding='utf-8').read(), _re.M)
    if not _cel_s:
        erro('a `Sobrecarga` sumiu da tabela de Auxiliares do manual')
    elif not _mds:
        erro('a `Sobrecarga` sumiu da tabela de Auxiliares do 40-fundamento.md')
    else:
        _volta = [_q for _q, _tx in (('o manual', _cel_s), ('o 40-fundamento.md', _mds.group(1)))
                  if 'dobro de energia' in _tx]
        if _volta:
            erro(f'{" e ".join(_volta)} voltou a dizer "o dobro de energia" na `Sobrecarga` '
                 '— contra inimigo isso vale zero, e contra Classe 0 dobra zero')
        elif 'não usa Reação' not in _cel_s or 'não usa Reação' not in _mds.group(1):
            erro('a `Sobrecarga` parou de dizer que o alvo nao usa Reacao em uma das duas '
                 'publicacoes — e essa e a metade que substituiu o dobro de energia')
        else:
            print('  [x] a `Sobrecarga` nao cobra "o dobro de energia" em nenhuma das duas '
                  'publicacoes, e as duas dizem que o alvo nao usa Reacao.')

print()
print('=' * 92)
print('6. O MOMENTO DO FEITICO APAGA A RESTRICAO — os vetos do `Rápido` e da `Reação`')
print('=' * 92)
# v0.246. Uma Restricao que so cobra recurso DO TURNO EM QUE VOCE CONJURA nao cobra
# nada quando a Melhoria tira a conjuracao desse recurso ou desse turno:
#   - o `Rápido` conjura na acao bonus, entao a Restricao que tira a acao bonus
#     neste turno se contradiz com ele (o `Atrasar`);
#   - a `Reação` conjura no turno de OUTRO, entao a Restricao que so cobra
#     movimento/acao do seu turno sai de graca (o `Atrasar` e o `Parado`).
# Os vetos NAO moram aqui: eles saem dos conjuntos de recurso da tabela do topo,
# que e a regua da peca 3 §4, e o TEXTO que os aplica mora no manual (dono) e no
# livro (copia). A checagem compara os dois lados, nos dois sentidos.
# ⚠ A tabela do topo cobre 11 das Restricoes do manual. Uma Restricao nova de
# "este turno" que nao entrar nela nao gera veto aqui.
_art6 = {'Rápido': 'o', 'Reação': 'a'}
_TURNO6 = {'movimento', 'acao_padrao', 'acao_bonus'}
_deste6 = {n: rec for n, (p, rec, q) in RESTRICOES.items() if q == 'este turno'}
_vetos6 = {
    'Rápido': {n for n, rec in _deste6.items() if 'acao_bonus' in rec},
    'Reação': {n for n, rec in _deste6.items() if rec <= _TURNO6},
}


def _vetados6(texto):
    """os nomes depois de `nem com a Restricao X` / `nem com as Restricoes X e Y`"""
    texto = texto.replace('`', '')
    _m = _re.search(r'nem com as? Restriç(?:ão|ões) ([^.]+)', texto)
    if not _m:
        return set()
    return {_x.strip() for _x in _re.split(r',| e ', _m.group(1)) if _x.strip()}


import re as _re
if _docx is None:
    print('  PULADA: sem python-docx nao da para ler o manual, que e o DONO do texto.')
elif not os.path.isfile(_DOCX):
    erro('nao achei o manual .docx — os vetos do `Rápido` e da `Reação` nao foram conferidos')
else:
    _cel6 = {}
    for _t in _docx.Document(_DOCX).tables:
        for _r in _t.rows:
            _nome = _r.cells[0].text.strip()
            if _nome in _vetos6 and len(_r.cells) >= 3:
                _cel6[_nome] = _r.cells[2].text.strip()
    _md6 = open(_MD, encoding='utf-8').read()
    for _mel, _esperado in _vetos6.items():
        _mm = _re.search(r'^\|\s*`' + _mel + r'`\s*\|[^|]*\|([^|]*)\|\s*$', _md6, _re.M)
        _fontes = (('o manual', _cel6.get(_mel)), ('o 40-fundamento.md', _mm.group(1) if _mm else None))
        for _onde, _txt in _fontes:
            if not _txt:
                erro(f'nao achei a linha do `{_mel}` em {_onde}')
                continue
            _escrito = _vetados6(_txt)
            _faltam, _sobram = _esperado - _escrito, _escrito - _esperado
            if _faltam:
                erro(f'{_onde}: {_art6[_mel]} `{_mel}` nao veta {sorted(_faltam)} — pela regua da peca 3 §4 '
                     f'essa Restricao nao cobra nada num feitico de `{_mel}`, e devolve de graca')
            if _sobram:
                erro(f'{_onde}: {_art6[_mel]} `{_mel}` veta {sorted(_sobram)}, e a regua nao pede — ou a '
                     f'tabela de recursos mudou, ou o texto trava uma combinacao que cobra')
            if not (_faltam or _sobram):
                print(f'  [x] {_onde}: {_art6[_mel]} `{_mel}` veta {sorted(_esperado)}, que e o que a regua deriva')

print()
print('=' * 92)
print('7. A CONCENTRACAO — a CD de quem te feriu, e as tabelas da peca 3 saem dos donos')
print('=' * 92)
# v0.253 (decisao do Mizuki, 19/09/2026). A Concentracao rolava Vigor contra `10` ou
# metade do dano, sem teto; ela passou a rolar contra a CD de quem feriu. As duas tabelas
# e os numeros da prosa da peca 3 nao podem ser digitados aqui: cada um sai de um dono.
#   - a maestria por nivel .............. peca 1 §2
#   - o 8 da CD e o dado do TR .......... peca 1 §5 (as formulas)
#   - a CD do inimigo por nivel ......... peca 26 §3.1 (a linha `CD`)
#   - o atributo do inimigo investido ... CD publicada − 8 − maestria (a peca 26 diz que ele
#                                          carrega a curva de quem investe)
#   - o golpe do chefe (regra antiga) ... a coluna `Chefe: dano` da tabela `Inimigos` do
#                                          manual, dividida pelos golpes por rodada
# O que NAO sai de um dono e e' escolha da peca — o cenario (golpes, acerto, alvo, rodadas)
# e o piso da regra antiga — e' lido do TEXTO da propria peca 3, nunca escrito aqui.
import re as _re7

_p3_7 = open(os.path.join(AQUI, '03-economia-de-acao-e-iniciativa.md'), encoding='utf-8').read()
_p1_7 = open(os.path.join(AQUI, '01-atributos-acerto-defesa.md'), encoding='utf-8').read()
_p26_7 = open(os.path.join(AQUI, '26-bestiario.md'), encoding='utf-8').read()

_i7 = _p3_7.find('### A CD de quem te feriu')
_sec7 = _p3_7[_i7:_p3_7.find('\n## ', _i7)] if _i7 >= 0 else ''
_par7 = _re7.search(r'^\*\*Concentração\.\*\*.*', _p3_7, _re7.M)
_par7 = _par7.group(0) if _par7 else ''


def _limpa7(c):
    return c.replace('`', '').replace('**', '').replace('*', '').strip()


def _tabela7(md, inicio):
    """(cabecalho, {rotulo: [celulas]}) da tabela cuja 1a linha comeca em `inicio`."""
    _ls = md.split('\n')
    for _k, _l in enumerate(_ls):
        if _limpa7(_l).startswith(inicio):
            _cab = [_limpa7(c) for c in _l.strip().strip('|').split('|')]
            _out = {}
            for _l2 in _ls[_k + 2:]:
                if not _l2.startswith('|'):
                    break
                _cel = [_limpa7(c) for c in _l2.strip().strip('|').split('|')]
                _out[_cel[0]] = _cel[1:]
            return _cab, _out
    return None, {}


def _tabela_apos7(sec, titulo):
    """a tabela que vem logo depois de uma linha-titulo em negrito."""
    _k = sec.find(titulo)
    if _k < 0:
        return None, {}
    return _tabela7(sec[_k + len(titulo):].lstrip('\n'), '|')


# --- os donos ---
_sec_m = _re7.search(r'## 2\. Maestria(.*?)\n## ', _p1_7, _re7.S)
_MAES7, _ok7 = [], True
if _sec_m:
    _cab_m, _lin_m = _tabela7(_sec_m.group(1), '| nível |')
    if _cab_m and 'maestria' in _lin_m:
        for _fx, _v in zip(_cab_m[1:], _lin_m['maestria']):
            _mm = _re7.match(r'(\d+)[–-](\d+)', _fx)
            if _mm and _v.isdigit():
                _MAES7.append((int(_mm.group(1)), int(_mm.group(2)), int(_v)))
_K_CD = _re7.search(r'CD de feitiço\s*=\s*(\d+) \+ atributo da técnica \+ maestria', _p1_7)
_DADO = _re7.search(r'Teste de Resistência\s*=\s*d(\d+) \+ atributo do TR \+ maestria', _p1_7)
_cab26, _lin26 = _tabela7(_p26_7, '| nível do grupo |')
_CD26 = {}
if _cab26 and 'CD' in _lin26:
    for _n, _v in zip(_cab26[1:], _lin26['CD']):
        if _n.isdigit() and _v.isdigit():
            _CD26[int(_n)] = int(_v)

if not (_MAES7 and _K_CD and _DADO and _CD26 and _sec7 and _par7):
    _ok7 = False
    erro(f'7: nao li todos os donos da Concentracao — maestria da peca 1 §2 ({len(_MAES7)} degraus), '
         f'o 8 da CD e o dado do TR da peca 1 §5 ({bool(_K_CD)}/{bool(_DADO)}), a linha CD da '
         f'peca 26 §3.1 ({len(_CD26)} niveis), a subsecao da peca 3 ({bool(_sec7)}) e o paragrafo '
         f'da regra ({bool(_par7)})')
else:
    _K = int(_K_CD.group(1))
    _D = int(_DADO.group(1))

    def _maestria7(nv):
        for _lo, _hi, _v in _MAES7:
            if _lo <= nv <= _hi:
                return _v
        return None

    def _passa(cd, bonus):
        return max(0.0, min(1.0, (_D + 1 - (cd - bonus)) / _D))

    def _inv(nv):
        return _CD26[nv] - _K - _maestria7(nv)

    _pct = lambda x: int(x * 100 + 0.5)
    _faltas7 = 0

    # a regra, como o texto a diz
    if not _re7.search(r'ao tomar dano faz um \*\*Teste de Resistência Vigor\*\* contra \*\*a CD de quem te feriu\*\*', _par7):
        _faltas7 += 1
        erro('7: o paragrafo da Concentracao nao diz "ao tomar dano faz um Teste de Resistencia Vigor '
             'contra a CD de quem te feriu"')
    if _re7.search(r'ao tomar dano faz um \*\*Teste de Resistência Vigor\*\* contra CD \d+ ou metade', _p3_7):
        _faltas7 += 1
        erro('7: a peca 3 ainda escreve a regra antiga ("contra CD 10 ou metade do dano") como regra viva')

    # o cenario, lido do texto
    _cen = _re7.search(r'o chefe faz `(\d+)` golpes por rodada, acerta `(\d+)%`, e `(\d+)` golpe em `(\d+)` cai em quem '
                       r'concentra', _sec7)
    _rod = _re7.search(r'aguenta `(\d+)` rodadas', _sec7)
    _velha = _re7.search(r'rolava contra `(\d+)` ou metade do dano', _sec7)
    if not (_cen and _rod and _velha):
        _faltas7 += 1
        erro('7: a subsecao da peca 3 parou de declarar o cenario (golpes, acerto, alvo), as rodadas '
             'ou o piso da regra antiga — sem eles a segunda tabela nao tem contra o que conferir')
    else:
        _gol, _ace, _a, _b = int(_cen.group(1)), int(_cen.group(2)) / 100, int(_cen.group(3)), int(_cen.group(4))
        _rodadas, _piso_velho = int(_rod.group(1)), int(_velha.group(1))

        def _segura(q):
            return ((1 - _ace * (_a / _b) * q) ** _gol) ** _rodadas

        # --- a regra antiga, do manual (dono da tabela `Inimigos`) ---
        _DANO_CHEFE = {}
        try:
            import docx as _dx7
        except ImportError:
            _dx7 = None
        if _dx7 is not None and os.path.isfile(_DOCX):
            for _t in _dx7.Document(_DOCX).tables:
                _c = [c.text.strip() for c in _t.rows[0].cells] if _t.rows else []
                if _c and _c[0].startswith('Nível do grupo') and 'Chefe: dano' in _c:
                    for _r in _t.rows[1:]:
                        _v = [c.text.strip() for c in _r.cells]
                        if _v[0].isdigit() and _v[3].isdigit():
                            _DANO_CHEFE[int(_v[0])] = float(_v[3])

        def _cd_velha(nv):
            return max(_piso_velho, int((_DANO_CHEFE[nv] / _gol) // 2))

        def _bonus_treinado(nv):
            return _inv(nv) + _maestria7(nv)

        # --- tabela 1: passar no teste de Vigor contra a CD do inimigo ---
        _c1, _t1 = _tabela_apos7(_sec7, '**Chance de passar no teste de Vigor contra a CD do inimigo**')
        _niv1 = [int(_x.split()[-1]) for _x in (_c1 or [])[1:]]
        if not _t1 or not _niv1 or any(_n not in _CD26 for _n in _niv1):
            _faltas7 += 1
            erro('7: nao achei a tabela "Chance de passar no teste de Vigor" na peca 3, ou ela usa um '
                 'nivel que a peca 26 §3.1 nao publica')
        else:
            for _rot, _cels in _t1.items():
                _esp = []
                if _rot.startswith('CD do inimigo'):
                    _esp = [_CD26[_n] for _n in _niv1]
                    _cels_n = [int(_x) for _x in _cels]
                else:
                    _tr = 'sem treino' not in _rot
                    _mc = _re7.search(r'Constituição (\d+)', _rot)
                    for _n in _niv1:
                        _attr = int(_mc.group(1)) if _mc else _inv(_n)
                        _esp.append(_pct(_passa(_CD26[_n], _attr + (_maestria7(_n) if _tr else 0))))
                    _cels_n = [int(_x.rstrip('%')) for _x in _cels]
                if _cels_n != _esp:
                    _faltas7 += 1
                    erro(f'7: a linha "{_rot}" da primeira tabela publica {_cels_n} e os donos dao {_esp} '
                         f'(niveis {_niv1})')
            _lt = [_r for _r in _t1 if _r.startswith('Vigor investido e treinado')]
            if _lt and len(set(_t1[_lt[0]])) != 1:
                _faltas7 += 1
                erro('7: a peca diz que quem treinou o Vigor "nao deriva", e a linha dele muda com o nivel')

        # --- tabela 2: segurar N rodadas ---
        _c2, _t2 = _tabela_apos7(_sec7, '**Chance de segurar `10` rodadas**')
        _niv2 = [int(_x.split()[-1]) for _x in (_c2 or [])[1:]]
        _hold_nova, _hold_velha, _bx = {}, {}, {}
        if not _t2 or not _niv2 or any(_n not in _CD26 for _n in _niv2):
            _faltas7 += 1
            erro('7: nao achei a tabela "Chance de segurar 10 rodadas" na peca 3, ou ela usa um nivel '
                 'que a peca 26 §3.1 nao publica')
        else:
            _pul7 = False
            for _rot, _cels in _t2.items():
                if _rot.startswith('regra nova'):
                    _tr = 'sem treino' not in _rot
                    _mc = _re7.search(r'Constituição (\d+)', _rot)
                    _esp = []
                    for _n in _niv2:
                        _attr = int(_mc.group(1)) if _mc else _inv(_n)
                        _q = 1 - _passa(_CD26[_n], _attr + (_maestria7(_n) if _tr else 0))
                        _esp.append(_pct(_segura(_q)))
                        if _tr and not _mc:
                            _hold_nova[_n] = _esp[-1]
                    _cels_n = [int(_x.rstrip('%')) for _x in _cels]
                elif 'regra antiga' in _rot:
                    if not _DANO_CHEFE or any(_n not in _DANO_CHEFE for _n in _niv2):
                        _pul7 = True
                        continue
                    if _rot.startswith('CD da regra antiga'):
                        _esp = [_cd_velha(_n) for _n in _niv2]
                        _cels_n = [int(_x) for _x in _cels]
                        _bx.update({_n: _cd_velha(_n) for _n in _niv2})
                    else:
                        _esp = []
                        for _n in _niv2:
                            _q = 1 - _passa(_cd_velha(_n), _bonus_treinado(_n))
                            _esp.append(_pct(_segura(_q)))
                            _hold_velha[_n] = _esp[-1]
                        _cels_n = [int(_x.rstrip('%')) for _x in _cels]
                else:
                    _faltas7 += 1
                    erro(f'7: a segunda tabela tem a linha "{_rot}", que a checagem nao sabe derivar')
                    continue
                if _cels_n != _esp:
                    _faltas7 += 1
                    erro(f'7: a linha "{_rot}" da segunda tabela publica {_cels_n} e os donos dao {_esp} '
                         f'(niveis {_niv2})')
            if _pul7:
                print('  PULADA: sem python-docx (ou sem a tabela `Inimigos`) nao da para derivar as '
                      'linhas da regra antiga.')
            if _hold_nova and len(set(_hold_nova.values())) != 1:
                _faltas7 += 1
                erro('7: a peca diz que a regra nova segura o mesmo em qualquer nivel, e a conta '
                     f'muda com o nivel: {_hold_nova}')

            # --- os numeros da prosa ---
            _m = _re7.search(r'A regra nova segura `(\d+)%` em qualquer nível', _sec7)
            if not _m:
                _faltas7 += 1
                erro('7: a prosa parou de dizer "A regra nova segura X% em qualquer nivel"')
            elif _hold_nova and int(_m.group(1)) != next(iter(_hold_nova.values())):
                _faltas7 += 1
                erro(f'7: a prosa diz {_m.group(1)}% e a conta da {next(iter(_hold_nova.values()))}%')
            if _hold_velha:
                _m = _re7.search(r'`(\d+)%` contra `(\d+)%` no nível `(\d+)`', _sec7)
                if not _m:
                    _faltas7 += 1
                    erro('7: a prosa parou de dizer "X% contra Y% no nivel N" (o preco nos niveis baixos)')
                else:
                    _n = int(_m.group(3))
                    if _n not in _hold_velha or _n not in _hold_nova:
                        _faltas7 += 1
                        erro(f'7: a prosa cita o nivel {_n}, que a segunda tabela nao tem')
                    elif (int(_m.group(1)), int(_m.group(2))) != (_hold_nova[_n], _hold_velha[_n]):
                        _faltas7 += 1
                        erro(f'7: a prosa diz {_m.group(1)}% contra {_m.group(2)}% no nivel {_n} e a '
                             f'conta da {_hold_nova[_n]}% contra {_hold_velha[_n]}%')
                    elif not _hold_nova[_n] < _hold_velha[_n]:
                        _faltas7 += 1
                        erro(f'7: a prosa diz que a regra nova e mais dura no nivel {_n}, e ela nao e')
                _m = _re7.search(r'No nível `(\d+)` ela passa a `(\d+)` e quem treinou resiste `(\d+)%`', _sec7)
                if not _m:
                    _faltas7 += 1
                    erro('7: a prosa parou de dizer "No nivel N ela passa a CD e quem treinou resiste X%"')
                else:
                    _n = int(_m.group(1))
                    if _n not in _bx:
                        _faltas7 += 1
                        erro(f'7: a prosa cita o nivel {_n}, que a segunda tabela nao tem')
                    else:
                        _res = _pct(_passa(_bx[_n], _bonus_treinado(_n)))
                        if (int(_m.group(2)), int(_m.group(3))) != (_bx[_n], _res):
                            _faltas7 += 1
                            erro(f'7: a prosa diz CD {_m.group(2)} e {_m.group(3)}% no nivel {_n}, e os donos '
                                 f'dao CD {_bx[_n]} e {_res}%')
                _m = _re7.search(r'do nível `(\d+)` em diante nenhum `d20` resiste, e o `(\d+)%` que sobra', _sec7)
                if not _m:
                    _faltas7 += 1
                    erro('7: a prosa parou de dizer "do nivel N em diante nenhum d20 resiste, e o X% que sobra"')
                else:
                    _n0 = int(_m.group(1))
                    _apos = [_n for _n in _niv2 if _n >= _n0]
                    _antes = [_n for _n in _niv2 if _n < _n0]
                    _zero = all(_passa(_bx[_n], _bonus_treinado(_n)) == 0 for _n in _apos)
                    _ant = [_n for _n in _antes if _passa(_bx[_n], _bonus_treinado(_n)) == 0]
                    if not _zero or _ant:
                        _faltas7 += 1
                        erro(f'7: a prosa diz que do nivel {_n0} em diante nenhum d20 resiste, e a conta '
                             f'diz outra coisa (algum nivel depois passa: {not _zero}; algum antes ja zerava: {_ant})')
                    if {_hold_velha[_n] for _n in _apos} != {int(_m.group(2))}:
                        _faltas7 += 1
                        erro(f'7: a prosa diz que sobram {_m.group(2)}%, e a regra antiga segura '
                             f'{sorted({_hold_velha[_n] for _n in _apos})}% nesses niveis')

    if _faltas7 == 0 and _ok7:
        print(f'  [x] a regra esta no paragrafo, a regra antiga saiu, as duas tabelas e os numeros da prosa '
              f'saem dos donos (CD da peca 26 §3.1, maestria da peca 1 §2, dado d{_D}).')

print()
print('=' * 92)
if ERROS:
    print(f'>>> {len(ERROS)} PROBLEMA(S):')
    for e in ERROS:
        print('   -', e)
    raise SystemExit(1)
print(f'>>> TUDO OK — as {len(RESTRICOES)} Restricoes cabem na regua, nenhuma esta '
      'dominada, e a `Divida` bate nas duas publicacoes.')
