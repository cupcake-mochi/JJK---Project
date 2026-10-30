"""Edições da primeira passagem do lote B5-01 (registro 128). Lidas por REVISAR.py."""
COPIA = 'Criar cópia e apontar as remissões para as cópias revistas vizinhas ou para as fontes ainda não revistas.'
CLARO = 'Clareza: frase direta, termo do Livro de Regras 1.0 ou ordem de leitura.'
PENTE = 'Pente fino da segunda leitura, na prova completa.'


def orig(*names):
    return [(f']({n})', f'](<../../{n}>)') for n in names]


def sib(*names):
    return [(f']({n})', f'](<{n}>)') for n in names]


LINKS = {
    's047': orig('41-pactos-e-promessas.md', '42-registro-de-pactos-e-promessas.md') + sib('48-pacifismo-impraticavel-minuta.md', '49-liberacao-irregular-minuta.md'),
    's048': [('](<../04 - Planejamento/46-pacifismo-conducao-pela-materia.md>)', '](<../../../04 - Planejamento/46-pacifismo-conducao-pela-materia.md>)')],
    's049': [],
    's050': orig('41-pactos-e-promessas.md'),
}
MULTI = {}

E = []
def e(caso, antes, depois, motivo=CLARO, passagem=1, tipo='clareza'):
    E.append((caso, passagem, tipo, motivo, antes, depois))

# ---------------------------------------------------------------- s047
e('s047', 'Comece com uma cena. Peça ao jogador que mostre uma situação em que a proposta ajuda e outra em que seu preço atrapalha.',
  'Comece por uma cena. Peça ao jogador que descreva uma situação em que a proposta ajuda e outra em que o preço atrapalha.')
e('s047', 'Um pacto de energia que envolva quantidade usa porcentagem do máximo combinada com o mestre.',
  'Um pacto de energia que envolva quantidade usa uma porcentagem do máximo de PE, combinada com o mestre, nunca um número fixo.',
  'Clareza: mesma regra do Livro de Regras 1.0, com a parte "nunca um número fixo".')

# ---------------------------------------------------------------- s048
e('s048', 'Na guilda, use o calendário vivido pela personagem. A ausência de postagens não comprova cumprimento nem autoriza inventar mortes fora de cena.',
  'Na guilda, use o calendário vivido pela personagem. Ficar sem jogar não comprova cumprimento nem autoriza inventar mortes fora de cena.',
  'Clareza: vale para mesa presencial e on-line, como no lote B4-01.')
e('s048', 'Não cobrar custos de uma execução subordinada que não chegou a começar.', 'Não cobre custos de uma execução subordinada que não chegou a começar.')

# ---------------------------------------------------------------- s049
e('s049', 'Mesmo tendo energia, não pode pagar Amortecer por 2 PE antes da próxima renovação.',
  'Mesmo tendo energia, não pode pagar os 2 PE de Cobrir-se de Energia para amortecer um golpe antes da próxima renovação.',
  'Clareza: nome completo da aptidão do Livro de Regras 1.0.')
e('s049', 'anunciar um pagamento conhecido como impossível não consome a ação nem cobra uma parcela.',
  'anunciar um pagamento que já se sabe impossível não consome a ação nem cobra uma parcela.')

# ---------------------------------------------------------------- s050
e('s050', 'A consequência deste acordo é a perda de PE com bloqueio até uma reparação definida.',
  'A consequência de quebra escolhida é a perda de PE, com bloqueio da recuperação até uma reparação definida.')
