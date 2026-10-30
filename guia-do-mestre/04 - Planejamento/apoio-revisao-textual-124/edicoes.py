"""Edições da primeira passagem do lote B2-06 (registro 124). Lidas por REVISAR.py."""
COPIA = 'Criar cópia e apontar as remissões para as cópias revistas vizinhas.'
CLARO = 'Clareza: frase direta, termo do Livro de Regras 1.0 ou ordem de leitura.'
PENTE = 'Pente fino da segunda leitura, na prova completa.'


def sib(*names):
    return [(f']({n})', f'](<{n}>)') for n in names]


LINKS = {
    's103': sib('78-preparar-perigos-ambientais.md', '79-o-po-na-sala-de-conservacao.md'),
    's077': [('](58-ficha-de-inimigo-e-encontro.md)', '](<../../58-ficha-de-inimigo-e-encontro.md>)'),
             ('](<../04 - Planejamento/76-dupla-de-nivel-6-e-composicao.md>)', '](<../../../04 - Planejamento/76-dupla-de-nivel-6-e-composicao.md>)')]
            + [('](73-ensaio-guiado-do-sineiro.md)', '](<73-ensaio-guiado-do-sineiro.md#personagens-usados>)')],
    's068': [('](58-ficha-de-inimigo-e-encontro.md)', '](<../../58-ficha-de-inimigo-e-encontro.md>)')]
            + sib('67-preparar-chefes-e-confrontos-maiores.md', '63-carregador-consulta-e-doma.md', '62-o-carregador-e-o-corredor-de-entulho.md',
                  '65-comparar-confronto-e-pressao-ambiental.md', '71-sineiro-do-recolhimento.md', '72-sineiro-consulta-e-doma.md',
                  '73-ensaio-guiado-do-sineiro.md', '75-ren-e-sora-atacante-e-apoio.md', '76-confronto-de-ren-e-sora.md'),
}
# Links que aparecem mais de uma vez são trocados por um laço próprio em REVISAR.py.
MULTI = {
    's077': [('](75-ren-e-sora-atacante-e-apoio.md)', '](<75-ren-e-sora-atacante-e-apoio.md>)'),
             ('](76-confronto-de-ren-e-sora.md)', '](<76-confronto-de-ren-e-sora.md>)')],
    's068': [('](66-o-carregador-e-a-saida-que-fecha.md)', '](<66-o-carregador-e-a-saida-que-fecha.md>)')],
}

E = []
def e(caso, antes, depois, motivo=CLARO, passagem=1, tipo='clareza'):
    E.append((caso, passagem, tipo, motivo, antes, depois))

# ---------------------------------------------------------------- s103
e('s103', 'Use com [Preparar perigos ambientais](<78-preparar-perigos-ambientais.md>).', 'Use com [Perigos do ambiente](<78-preparar-perigos-ambientais.md>).', 'Clareza: nome atual da consulta revista.')
e('s103', 'Não cobre testes a cada segundo real ou enquanto o chat está fechado.', 'Não cobre testes a cada segundo real nem enquanto ninguém está jogando.')
e('s103', 'A próxima crise seis horas depois não substitui essa urgência de rodadas.', 'A janela de socorro conta em rodadas; a próxima crise, horas depois, não muda esse prazo.')
e('s103', 'a espera e o cuidado recebidos não são descontados automaticamente como fabricação na dedicação do paciente.',
  'o tempo de espera e de cuidado não consome, por si, horas de dedicação do paciente.',
  'Clareza: "fabricação" não é o que está em jogo; a frase diz o que não acontece com a dedicação por ficha.')
e('s103', 'Interrupções pausam o trabalho já realizado, sem apagar as horas;', 'Uma interrupção pausa o atendimento, e as horas já feitas continuam valendo;')
e('s103', 'Na guilda, o calendário aproximadamente acompanha os dias reais,', 'Na guilda, o calendário acompanha aproximadamente os dias reais,')

# ---------------------------------------------------------------- s077
e('s077', 'Não são maldições adquiríveis por Doma.', 'Como não são maldições, não podem ser domados.')
e('s077', 'Conservar recursos e efeitos ao mudar de conduta.', 'Ao mudar de conduta, conservam recursos e efeitos.')
e('s077', 'também compara a hipótese de concentrar duas declarações em Ren.', 'também compara a hipótese de concentrar os dois ataques seguintes em Ren.',
  'Clareza: "duas declarações" não dizia o que era concentrado.')
e('s077', 'Registrar o estado dos efeitos ainda em curso', 'Registre o estado dos efeitos ainda em curso')

# ---------------------------------------------------------------- s068
e('s068', 'Use o [método de chefes](<67-preparar-chefes-e-confrontos-maiores.md>)', 'Use [Preparar chefes e confrontos maiores](<67-preparar-chefes-e-confrontos-maiores.md>)', 'Clareza: nome da consulta.')
e('s068', 'O [Carregador de Sinos](<63-carregador-consulta-e-doma.md>) serve aqui',
  'O [Carregador](<63-carregador-consulta-e-doma.md>) serve aqui',
  'Coerência, documentada: a criatura se chama Carregador em todas as outras fontes; "de Sinos" mistura o nome com o Sineiro.',
  tipo='coerencia_do_nome')
e('s068', 'sua [conversão conhecida antes da Doma](<72-sineiro-consulta-e-doma.md>)', 'a [ficha após a Doma](<72-sineiro-consulta-e-doma.md>)', 'Clareza: nome atual da consulta revista.')
e('s068', 'Use três personagens apenas para contar turnos; suas fichas completas não foram simuladas.',
  'Os três personagens servem só para contar turnos; suas fichas completas não foram simuladas.')
e('s068', 'Ele observa o comando e usa **Padrão para Preparar deslocamento**: depois de perceber o clique da parada, aproximar-se de quem a operou pelo corredor.',
  'Ele observa o comando e usa **Padrão para Preparar deslocamento**, com este gatilho: quando perceber o clique da parada, aproximar-se pelo corredor de quem a operou.')
e('s068', 'Agora deve conferir a posição do inimigo.', 'Antes de usá-los, ela confere a nova posição do inimigo.')
