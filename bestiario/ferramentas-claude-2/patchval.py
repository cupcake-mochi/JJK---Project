import sys
P = sys.argv[1]
T = open(P, encoding='utf-8').read()
def troca(old, new):
    global T
    n = T.count(old)
    if n != 1: sys.exit(f'!! aparece {n}x: {old[:100]!r}')
    T = T.replace(old, new)
def entre(ini, fim, novo):
    global T
    if T.count(ini) != 1: sys.exit(f'!! inicio {T.count(ini)}x: {ini[:90]!r}')
    a = T.find(ini); b = T.find(fim, a + len(ini))
    if b < 0: sys.exit(f'!! fim ausente: {fim[:90]!r}')
    T = T[:a] + novo + T[b:]
SEP = "# --------------------------------------------------------------------------\n"

troca("    'categoria': (PECA, r'\\*\\*`Ronda`\\*\\*'),", "    'categoria': (PECA, r'\\*\\*`Desastre`\\*\\*'),")

# ---------------------------------------------------------------- 3a: a tabela do §4
entre("_CAT = []\nfor _c in tabela(TXT, '| categoria | personagens | fator sobre a linha do manual | ações |'):",
      "_FICHAS = tabela(TXT, '| categoria | nv 10 | nv 20 | nv 30 |')", '''_CAT = []
_INT = {}
for _c in tabela(TXT, '| categoria | personagens | fator sobre a linha do manual | ações |'):
    if len(_c) < 5:
        continue
    _m = re.match(r'([\\d,]+)', _c[2].replace('×', '').strip())
    if _m and _c[3].isdigit():
        # v0.221: o `Capanga` e' a unica categoria sem numero de personagens — a vida
        # dele sai do dano do grupo, e nao do fator. O travessao vira None.
        _pes = int(_c[1]) if _c[1].isdigit() else None
        _CAT.append((_c[0], _pes, float(_m.group(1).replace(',', '.')), int(_c[3])))
        _INT[_c[0]] = _c[4].strip().lower() == 'sim'
if len(_CAT) != 5:
    erro(f'3: achei {len(_CAT)} categoria(s) na tabela do §4 e a peca promete cinco — '
         'ela mudou de forma e esta checagem parou de conferir')
_CAPS = [c for c in _CAT if c[1] is None]
_CAPA = _CAPS[0] if len(_CAPS) == 1 else None
if _CAT and _CAPA is None:
    erro(f'3: esperava UMA categoria sem numero de personagens, o Capanga, e achei {len(_CAPS)}')
if 'Vida do capanga = o dano do grupo por rodada dividido por quatro, arredondado para baixo' not in TXT:
    erro('3: a peca parou de publicar de onde sai a vida do capanga — sem isso a linha dele '
         'no §4.1 e numero solto')

''')

# ---------------------------------------------------------------- 3b e 4
entre("    _mau3 = 0\n    for _c in _FICHAS:", SEP + "bloco('5. O CAMBIO", '''    _mau3 = 0
    for _c in _FICHAS:
        if len(_c) < 4:
            continue
        _achou = [x for x in _CAT if x[0] == _c[0]]
        if not _achou:
            erro(f'3: o §4.1 publica a categoria "{_c[0]}", que nao esta na tabela do §4')
            _mau3 += 1
            continue
        _pes, _fator = _achou[0][1], _achou[0][2]
        if _pes is not None and abs(_fator - _pes / 4) > 1e-9:
            erro(f'3: a categoria {_c[0]} exige {_pes} personagem(ns) e publica fator '
                 f'{_fator}, e {_pes}/4 da {_pes / 4}')
            _mau3 += 1
        for _nv, _cel in zip((10, 20, 30), _c[1:4]):
            _nums = re.findall(r'(\\d+)', _cel)
            if len(_nums) < 2:
                erro(f'3: nao consegui ler a celula "{_cel}" do §4.1')
                _mau3 += 1
                continue
            # ⚠ meio para BAIXO, pela regra declarada no §4.1 da peca. E a vida do
            # Capanga e' outra regra: o dano do grupo dividido por quatro, para baixo
            # por inteiro — um quarto de ponto poe o esquadrao vivo numa rodada a mais.
            if _pes is None:
                _ve = math.floor(_MANUAL[_nv][0] / 4)
            else:
                _ve = math.ceil(_MANUAL[_nv][1] * _fator - 0.5)
            _de = math.ceil(_MANUAL[_nv][2] * _fator - 0.5)
            if int(_nums[0]) != _ve or int(_nums[1]) != _de:
                erro(f'3: {_c[0]} no nv{_nv}: a peca publica {_nums[0]} vida e '
                     f'{_nums[1]} dano, e a linha do manual da {_ve} e {_de}')
                _mau3 += 1
    if not _mau3:
        print(f'  [x] as {len(_FICHAS)} categorias do §4.1 reconstroem da tabela do '
              'manual vezes o fator, e o Capanga do dano do grupo')
        print('  [x] os fatores reconstroem de personagens/4, onde ha personagens')


''' + SEP + '''bloco('4. AS ACOES — declaradas, e a categoria de fator 1,00 bate com o piso da peca 19')
''' + SEP + '''# Ate a v0.220 as acoes saiam de "personagens menos um, piso 1", e foi isso que
# quebrou a Dupla: a razao pessoas/(pessoas-1) explode embaixo. Desde a v0.221 elas
# sao DECLARADAS na tabela do §4. O que continua amarrado e' a categoria de fator
# 1,00, que e' a linha do manual sem tocar em nada: ela age o que a frase do manual
# diz, e a peca 19 §2.2 preca quatro condicoes dividindo por esse numero. Se aquele
# piso mudar, ESTA acende.
if not _CAT:
    erro('4: sem a tabela do §4 lida nao da para conferir as acoes')
else:
    _mau4 = [c[0] for c in _CAT if c[3] < 1]
    if _mau4:
        erro('4: categoria(s) que publicam menos de uma acao: ' + ', '.join(_mau4))
    _m19 = re.search(r'O chefe age `(\\d+)` vezes por rodada', ler(P19))
    _um = [c for c in _CAT if c[1] is not None and abs(c[2] - 1.0) < 1e-9]
    if not _m19:
        erro('4: nao achei o piso das acoes do chefe na peca 19 §2.2 — ele e a metade '
             'de fora desta checagem, e sem ele ela so se compara com ela mesma')
    elif not _um:
        erro('4: nenhuma categoria desta peca tem fator 1,00 — a linha do manual ficou sem '
             'categoria, e a peca 19 e calibrada contra ela')
    elif _um[0][1] != 4:
        erro(f'4: a categoria de fator 1,00 exige {_um[0][1]} personagens, e a tabela do '
             'manual e a peca 19 sao calibradas para quatro')
    elif _um[0][3] != int(_m19.group(1)):
        erro(f'4: a categoria de fator 1,00 publica {_um[0][3]} acoes e a peca 19 §2.2 '
             f'publica {_m19.group(1)} — a regua de condicao daquela peca divide por esse '
             'numero, entao os dois nao podem discordar')
    elif not _mau4:
        print(f'  [x] as cinco categorias declaram ao menos uma acao, e a de fator 1,00 '
              f'({_um[0][0]}) age {_m19.group(1)} vezes, igual ao piso da peca 19 §2.2')


''')

# ---------------------------------------------------------------- 5 e 5.1
entre("_m5 = re.search(r'vale (\\w+) capangas', TXT)", "    # -- 5.2: a linha do manual obedece", '''_m5 = re.search(r'vale (\\w+) capangas', TXT)
if not _m5:
    erro('5: a peca nao publica o cambio como "vale N capangas" — a frase mudou de '
         'forma e esta checagem ficou sem o outro lado')
elif not _MANUAL:
    pulou('5. o cambio contra a simulacao — a tabela do manual nao foi lida')
elif _CAPA is None:
    erro('5: sem a linha do Capanga no §4 nao da para derivar o capanga')
else:
    _pub5 = _NUM_PT.get(_m5.group(1).lower())

    # v0.221: o capanga e' o da ESCADA — a vida e' o dano do grupo dividido por quatro,
    # para baixo, e o dano e' o do chefe vezes o fator da categoria dele. Ate a v0.220
    # ele era o da Alcateia (vida do chefe ÷ 4, dano ÷ 3), e esta checagem conferia
    # justamente aquilo. Nada aqui e' escrito: a saida do grupo e o chefe saem do
    # manual, e o fator sai da linha do Capanga no §4.
    def _capanga(nv):
        return (math.floor(_MANUAL[nv][0] / 4), _meio_baixo(_MANUAL[nv][2] * _CAPA[2]))

    _medidos = []
    for _nv, (_saida, _cv, _cd, _kv, _kd) in sorted(_MANUAL.items()):
        _r0, _t0 = _simula(_saida, [(_cv, _cd)])
        _k = _capanga(_nv)
        _melhor = min(range(1, 13),
                      key=lambda n: abs(_simula(_saida, [_k] * n)[1] - _t0))
        _medidos.append((_nv, _melhor))
    print('  cambio medido por nivel: ' + ' · '.join(f'nv{n}:{m}' for n, m in _medidos))
    _valores = sorted({m for _, m in _medidos})
    if _pub5 is None:
        erro(f'5: nao entendi "{_m5.group(1)}" como numero por extenso')
    elif _valores != [_pub5]:
        erro(f'5: a peca publica {_pub5} capangas por chefe, e a simulacao devolve '
             f'{_valores} nos {len(_medidos)} niveis da tabela do manual')
    else:
        print(f'  [x] a simulacao devolve {_pub5} em todos os niveis, e e o que a peca '
              'publica')

    # a declaracao que sobreviveu a decisao — a guarda da v0.206 continua: prosa que
    # diz que uma faixa nao tem capanga le-se como regra viva.
    if any(('não tem capanga' in _l or 'sem capanga' in _l) and not _l.lstrip().startswith('|')
           for _l in TXT.split('\\n')):
        erro('5: a peca declara em prosa que uma faixa nao tem capanga — e o capanga da '
             'escada existe em todas, porque sai do dano do grupo')

    if not ('Vida do capanga = o dano do grupo por rodada dividido por quatro' in TXT
            and 'Dano do capanga = o dano do chefe vezes o fator da categoria' in TXT):
        erro('5: a peca nao publica as duas linhas da derivacao do capanga — sem elas '
             'a coluna volta a ser numero solto que ninguem reconstroi')

    # o capanga que a tabela `Inimigos` do MANUAL publica tem de ser este. E' a coluna
    # que o gerador do bloco copia, entao um capanga morto ali chega na mao do mestre.
    _fora, _sem = [], []
    for _nv, (_saida, _cv, _cd, _kv, _kd) in sorted(_MANUAL.items()):
        if _kv is None or _kd is None:
            _sem.append(_nv)
            continue
        _ev, _ed = _capanga(_nv)
        if (_kv, _kd) != (_ev, _ed):
            _fora.append(f'nv{_nv}: o manual da ({_kv:.0f}, {_kd:.0f}) e o capanga da '
                         f'escada e ({_ev}, {_ed})')
    if _sem:
        erro(f'5: a tabela do manual tem {len(_sem)} faixa(s) sem capanga, e o capanga da '
             'escada existe em todas')
    if _fora:
        erro('5: o capanga da tabela `Inimigos` do manual nao e o da escada — '
             + ' · '.join(_fora[:3]))
    elif not _sem:
        print(f'  [x] o capanga do manual e o da escada nas {len(_MANUAL)} faixas — o dano '
              'do grupo ÷ 4, para baixo, e o dano do chefe vezes o fator')

    # -- 5.1: a coluna da sub-categoria, recontada -----------------------------
    # Desde a v0.221 com uma casa decimal: meio ponto percentual na fracao do chefe
    # atravessa a borda de uma rodada. A ordem de abate continua declarada.
    _ordem_declarada = 'os capangas primeiro' in TXT
    _m51 = re.findall(r'\\|\\s*\\*\\*`(sozinho|com um apoio|com dois|bando)`\\*\\*\\s*\\|\\s*'
                      r'`([\\d,]+)%`\\s*\\|\\s*`?([\\d—]+)`?\\s*\\|\\s*`([\\d,]+)%`\\s*\\|', TXT)
    if not _ordem_declarada:
        erro('5.1: a peca publica a coluna da sub-categoria e nao declara em que ordem o '
             'grupo abate — a coluna muda com a ordem')
    elif len(_m51) != 4:
        erro(f'5.1: achei {len(_m51)} das 4 linhas da tabela de sub-categoria do §4.5 — '
             'ela mudou de forma e esta checagem parou de conferir')
    elif 30 not in _MANUAL:
        pulou('5.1. a sub-categoria — a linha do nivel 30 do manual nao foi lida')
    else:
        _saida, _cv, _cd, _kv, _kd = _MANUAL[30]
        _vg = 4 * _VIDA_PC(30)
        _k = _capanga(30)
        _mau51 = 0
        for _rot, _frac, _ncap, _pct in _m51:
            _f = float(_frac.replace(',', '.')) / 100.0
            _n = 0 if _ncap == '—' else int(_ncap)
            _r, _c = _simula(_saida, [_k] * _n + [(_cv * _f, _cd * _f)])
            _esp = _c / _vg * 100
            if abs(_esp - float(_pct.replace(',', '.'))) > 0.051:
                erro(f'5.1: a sub-categoria `{_rot}` publica {_pct}% da vida do grupo e a '
                     f'simulacao devolve {_esp:.1f}%')
                _mau51 += 1
        if not _mau51:
            print('  [x] as quatro formas da sub-categoria reconstroem da simulacao, com '
                  'os capangas abatidos primeiro e o Capanga da escada')

''')

# ---------------------------------------------------------------- 7.1
entre("    # a regra publicada e \"dobra quantos personagens ele exige\".", SEP + "bloco('8. RESISTENCIA", '''    # v0.221: a regra deixou de arredondar o multiplicador para "dobra". A moeda e' o
    # FATOR, que e' continuo, e a peca publica a regra e a tabela de pessoas. A tabela
    # tem de ser a coluna de personagens do §4 vezes o multiplicador, com uma casa.
    _mreg = re.search(r'Uma Expansão de Domínio completa multiplica o fator do inimigo por '
                      r'`([\\d,]+)`', TXT)
    if not _mreg:
        erro('7.1: a peca parou de publicar a regra da Expansao como "multiplica o fator '
             'do inimigo por N" — sem ela a tabela vira numero solto')
    elif abs(float(_mreg.group(1).replace(',', '.')) - _mult_pub) > 1e-9:
        erro(f'7.1: a regra publica {_mreg.group(1)} e a conta do §6.4 da {_mult_pub:.2f}')
    else:
        _pes = {c[0]: c[1] for c in _CAT if c[1] is not None}
        _dob = {}
        for _l in TXT.split('\\n'):
            _m = re.match(r'\\|\\s*\\*\\*`(\\w+)`\\*\\*\\s*\\|\\s*`(\\d+)`\\s*\\|\\s*`([\\d,]+)`\\s*\\|\\s*$', _l)
            if _m and _m.group(1) in _pes:
                _dob[_m.group(1)] = (int(_m.group(2)), float(_m.group(3).replace(',', '.')))
        if not _pes or len(_dob) != len(_pes):
            erro(f'7.1: li {len(_pes)} categorias com personagens no §4 e {len(_dob)} na '
                 'tabela do §6.4 — alguma mudou de forma')
        else:
            _mau = 0
            for _n, (_p, _c) in _dob.items():
                if _p != _pes[_n]:
                    erro(f'7.1: o §6.4 diz que a `{_n}` exige {_p} personagens e o §4 diz '
                         f'{_pes[_n]}')
                    _mau += 1
                elif abs(_c - round(_p * _mult_pub, 1)) > 1e-9:
                    erro(f'7.1: a `{_n}` exige {_p} e com Expansao o §6.4 publica {_c}, e '
                         f'{_p} × {_mult_pub:.2f} da {round(_p * _mult_pub, 1)}')
                    _mau += 1
            if not _mau:
                print(f'  [x] a tabela do §6.4 e a coluna de personagens do §4 vezes '
                      f'{_mult_pub:.2f}, nas {len(_dob)} categorias que tem personagens')


''')

# ---------------------------------------------------------------- 8
troca("bloco('8. RESISTENCIA E VIDA ESCONDIDA — e o degrau de categoria e a moeda dela')",
      "bloco('8. RESISTENCIA E VIDA ESCONDIDA — e o fator da categoria e a moeda dela')")
entre("    # e o degrau de categoria tem de ser a moeda: o maior multiplicador de", SEP + "bloco('9. O CATALOGO", '''    # v0.221: a moeda deixou de ser o degrau de categoria — na escada viva ele vai de
    # 1,000x a 4,000x — e passou a ser o FATOR. A peca tem de declarar a moeda, e o
    # multiplicador que ela declara tem de ser o que a conta de cima devolve.
    if 'Físicos' in _PESOS:
        _res_fis = round(_efetiva(_PESOS['Físicos'], 'resistência'), 2)
        _imu_fis = round(_efetiva(_PESOS['Físicos'], 'imunidade'), 2)
        _mr = re.search(r'Resistência ao grupo `Físicos` multiplica o fator da categoria por '
                        r'`([\\d,]+)`', TXT)
        _mi = re.search(r'Imunidade a `Físicos` multiplica o fator por `([\\d,]+)`', TXT)
        if not _mr or not _mi:
            erro('8: a peca nao declara em que moeda a resistencia se paga — sem isso '
                 'ela e vida de graca, e a categoria passa a mentir sobre o encontro')
        elif (abs(float(_mr.group(1).replace(',', '.')) - _res_fis) > 0.011
              or abs(float(_mi.group(1).replace(',', '.')) - _imu_fis) > 0.011):
            erro(f'8: a peca declara que resistir aos Físicos multiplica o fator por '
                 f'{_mr.group(1)} e ser imune por {_mi.group(1)}, e a conta da '
                 f'{_res_fis:.2f} e {_imu_fis:.2f}')
        else:
            print(f'  [x] a peca declara a moeda, o fator, e os multiplicadores declarados '
                  f'sao os da conta: resistir {_res_fis:.2f}x, ser imune {_imu_fis:.2f}x')


''')

# ---------------------------------------------------------------- 9.1
entre("    _T91 = tabela(TXT, '| pontos por ação | `Ronda` | `Dupla` | `Alcateia` | `Calamidade` |')",
      "    # -- 9.2: a aptidao come a cota", '''    # v0.221: o golpe entra como a ficha imprime ele — a MEDIA do dado do §4.4 — e
    # quem carrega `Intervencao` entra com o fator dela. Nada mora aqui: a lista de
    # dados, o teto de dados na mao e o piso do numero seco saem do §4.4; o fator e
    # quem o carrega saem do §6.5 e da coluna `Intervencao` da tabela do §4.
    _T91 = tabela(TXT, '| pontos por ação | `Capanga` | `Ameaça` | `Desastre` | `Catástrofe` | `Calamidade` |')
    _mdl = re.search(r'O tamanho do dado se escolhe entre ([^*]+?)\\s*—', TXT)
    _DL = [int(x) for x in re.findall(r'`d(\\d+)`', _mdl.group(1))] if _mdl else []
    _mteto = re.search(r'no máximo \\*\\*(\\w+)\\*\\* dados', TXT)
    _TETO_D = _NUM_PT.get(_mteto.group(1).lower()) if _mteto else None
    _mseco = re.search(r'Abaixo de `(\\d+)` o golpe fica em número seco', TXT)
    _mfi = re.search(r'o fator de dano de quem carrega `Intervenção` é multiplicado por `([\\d,]+)`', TXT)
    _FI = float(_mfi.group(1).replace(',', '.')) if _mfi else None

    def _jr(x):
        return math.floor(x + 0.5)            # o Math.round do gerador

    def _arr(x):
        return math.ceil(x - 0.5)             # o meio para baixo do §4.1

    def _media_do_dado(alvo):
        """a regra do §4.4, na mesma ordem de desempate do gerador do bloco"""
        if alvo < int(_mseco.group(1)):
            return float(_arr(alvo))
        meta, bom = alvo / 2, None
        for _d in _DL:
            med = (_d + 1) / 2
            n = max(1, _jr(meta / med))
            if n > _TETO_D:
                continue
            fixo = alvo - n * med
            if fixo < 0:
                continue
            inte = 0 if abs(fixo - _jr(fixo)) < 1e-9 else 1
            er = abs(n * med - meta)
            if (bom is None or inte < bom[0] or (inte == bom[0] and er < bom[1] - 1e-9)
                    or (inte == bom[0] and abs(er - bom[1]) < 1e-9 and n < bom[2])):
                bom = (inte, er, n, med, _jr(fixo))
        if bom is None:
            n = max(1, _jr(alvo / 9))
            return n * (8 + 1) / 2 + max(_arr(alvo - n * (8 + 1) / 2), 0)
        return bom[2] * bom[3] + max(bom[4], 0)

    if not (_DL and _TETO_D and _mseco and _FI):
        erro('9.1: nao achei na peca a regra do dado do §4.4 ou o fator da Intervencao do '
             '§6.5 — o orcamento de uma acao se mede contra os dois')
    elif not _CAT or not _MANUAL:
        pulou('9.1. o orcamento de feitico — sem a tabela do manual ou a do §4')
    elif len(_T91) != len(_MANUAL):
        erro(f'9.1: a tabela de orcamento do §6.5 tem {len(_T91)} linha(s) e a tabela de '
             f'inimigo do manual tem {len(_MANUAL)} — ela parou de cobrir as faixas')
    else:
        _mau91 = 0
        for _l91 in _T91:
            _mn = re.search(r'(\\d+)', _l91[0])
            if not _mn or int(_mn.group(1)) not in _MANUAL:
                erro(f'9.1: nao reconheci o nivel na linha "{_l91[0]}" do §6.5')
                _mau91 += 1
                continue
            _nv91 = int(_mn.group(1))
            _cd91 = _MANUAL[_nv91][2]
            for _cel91, _c91 in zip(_l91[1:], _CAT):
                _g91 = (_media_do_dado(_arr(_cd91 * _c91[2]) / _c91[3])
                        * (_FI if _INT.get(_c91[0]) else 1.0))
                _pts = _g91 / _PONTO
                if _pts < _PISO19 - 1e-9:
                    if _cel91.strip().lower() != 'seco':
                        erro(f'9.1: nv {_nv91}, {_c91[0]}: o orcamento e {_pts:.2f} pontos, '
                             f'abaixo do piso de {_PISO19} que a Classe 1 do manual custa, '
                             f'e a peca publica "{_cel91}" em vez de seco')
                        _mau91 += 1
                    continue
                _mv = re.match(r'([\\d,]+)$', _cel91.strip())
                if not _mv or abs(float(_mv.group(1).replace(',', '.')) - _pts) > 0.051:
                    erro(f'9.1: nv {_nv91}, {_c91[0]}: a peca publica "{_cel91}" e o golpe de '
                         f'{_g91:.2f} da {_pts:.2f} pontos')
                    _mau91 += 1
        if not _mau91:
            print(f'  [x] as {len(_T91) * len(_CAT)} celulas do orcamento de feitico saem '
                  f'da media do dado ÷ {_PONTO}, com o fator {_FI} de quem carrega '
                  'Intervencao, e o `seco` e o piso da Classe 1 do manual')

''')

# ---------------------------------------------------------------- 9.2 e 9.4
troca("    _T92 = tabela(TXT, '| ligada a luta inteira, no nível 30 | da cota de uma `Ronda` | de uma `Alcateia` |')",
      "    _T92 = tabela(TXT, '| ligada a luta inteira, no nível 30 | da cota de uma `Ameaça` | de um `Desastre` |')")
troca("                       for _r in ('Ronda', 'Alcateia')]", "                       for _r in ('Ameaça', 'Desastre')]")
troca("                _esp92 = round(_custo / _meio_baixo(_cd92 * _c92[2]) * 100)",
      "                # v0.221: a cota de quem carrega `Intervencao` leva o fator dela\n"
      "                _cota92 = _meio_baixo(_cd92 * _c92[2]) * ((_FI or 1.0) if _INT.get(_c92[0]) else 1.0)\n"
      "                _esp92 = round(_custo / _cota92 * 100)")
troca("    _MOEDAS = ('orçamento de feitiço', 'cota de dano por rodada', 'degrau de categoria')",
      "    _MOEDAS = ('orçamento de feitiço', 'cota de dano por rodada', 'multiplica o fator')")

open(P, 'w', encoding='utf-8').write(T)
print('ok — validador reescrito')
