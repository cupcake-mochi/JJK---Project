"""Ensaio delimitado §§41–45; não é simulador nem prova de equilíbrio.
Trajeto em segmentos abstratos. Requisitos, opções disponíveis, efeitos escritos
sobre movimento e validade de Aberturas são dados explícitos do caso, não inferidos.
Não simula concessão/expiração de Abertura pelo relógio do Guia ou todas as fichas.
"""
from dataclasses import dataclass, field
from pathlib import Path
import json
import bancada_r4 as r4
base = r4.base

@dataclass
class Corpo(r4.Corpo):
    opcoes_bonus: dict = field(default_factory=dict)
    bonus_impedida: bool = False
    abertura_avancar: bool = False
    trechos_avancar: int = 0

@dataclass
class Cena(r4.Cena):
    trajeto: dict = field(default_factory=dict)
    observacoes: list = field(default_factory=list)

    def bonus_por_basica(self, nome, opcao, requisitos=True, coerente=True):
        c = self.corpos[nome]
        ficha = c.opcoes_bonus.get(opcao)
        if ficha is None:
            return 'recusado:opcao-indisponivel'
        if c.bonus_impedida or 'Lento' in c.condicoes:
            return 'recusado:bonus-impedida'
        if ficha.get('especial_comandada'):
            return 'fora-do-recorte:exige-procedimento-especial'
        if not requisitos or not coerente or not ficha.get('custo_disponivel', True):
            return 'recusado:requisitos-opcao'
        if ficha.get('limitada') and opcao in c.usos:
            return 'recusado:uso-esgotado'
        resultado = self.basica_normal(nome)
        if resultado != 'basica':
            return resultado
        if ficha.get('limitada'):
            c.usos.append(opcao)
        if ficha.get('custo_proprio'):
            self.eventos.append(f'custo-proprio:bonus:{nome}:{opcao}')
        self.eventos.append(f'opcao-bonus:executada:{nome}:{opcao}')
        return 'opcao-executada'

    def avancar(self, nome, requisitos=True, janela=True, dispensa_expressa=False):
        c = self.corpos[nome]
        if not (c.em_campo and c.abertura_avancar and requisitos and janela
                and self.momento in ('turno', 'fora')):
            return 'recusado:avancar'
        if self.momento == 'fora' and not dispensa_expressa:
            resultado = self.reagir(nome, 'Avancar')
            if resultado != 'respondeu':
                return resultado
        c.abertura_avancar = False
        c.trechos_avancar += 1
        self.eventos.append(f'avancar:trecho-concedido:{nome}')
        return 'avancou'

    def cruzar_porta(self, nome='A', recusar=False, impede_movimento=False,
                     continuar=True, sucesso=True):
        # Um deslocamento legal e uma passagem efetiva são premissas deste roteiro.
        if self.trajeto.get('posicao') != 'antes' or self.trajeto.get('saldo', 0) < 1:
            return 'recusado:trajeto'
        self.trajeto['saldo'] -= 1
        self.trajeto['posicao'] = 'porta'
        self.eventos.append('alvo:cruzou-porta')
        self.acontecimento('cruzar:X')
        r = self.resolver_gatilho(nome, recusar=recusar, sucesso=sucesso)
        self.observacoes.append(dict(janela='porta', resultado=r,
            posicao=self.trajeto['posicao'], saldo=self.trajeto['saldo']))
        if r == 'executada' and impede_movimento:
            self.trajeto['impedido'] = True
        self.evento_atual = None
        if continuar and not self.trajeto.get('impedido') and self.trajeto['saldo']:
            self.trajeto['saldo'] -= 1
            self.trajeto['posicao'] = 'cobertura'
            self.eventos.append('alvo:alcancou-cobertura')
        return r

base.Corpo = Corpo
base.Cena = Cena
V = base.verificar
cena = base.cena

def opcoes(nomes=('A',), reservas=()):
    s = cena(nomes, reservas)
    # Conhecimento e aptidão da criatura são premissas; nenhum valor é concedido.
    s.corpos['A'].opcoes_bonus = {'Provocar': {}, 'Ler o Ambiente': {},
        'opcao limitada de fixture': {'limitada': True, 'custo_proprio': True},
        'especial de fixture': {'especial_comandada': True}}
    return s

def porta():
    s = r4.pronta(); s.fechar_turno()
    s.trajeto = dict(posicao='antes', saldo=2, impedido=False)
    return s

def abertura(nomes=('A',)):
    s = cena(nomes); s.corpos['A'].abertura_avancar = True
    return s

def novos():
    s = porta()
    V('R5-01 passagem resolve antes da cobertura e continua sem impedimento', s,
      lambda: s.cruzar_porta(), 'executada',
      lambda x: x.eventos.index('alvo:cruzou-porta') < x.eventos.index('resultado:A:sucesso') < x.eventos.index('alvo:alcancou-cobertura')
      and x.observacoes[-1]['posicao']=='porta' and x.observacoes[-1]['saldo']==1
      and x.trajeto['saldo']==0 and not x.coletiva and x.corpos['A'].basica is None)
    s = porta()
    V('R5-02 efeito escrito impede restante sem renovar saldo', s,
      lambda: s.cruzar_porta(impede_movimento=True), 'executada',
      lambda x: x.trajeto['posicao']=='porta' and x.trajeto['saldo']==1 and x.trajeto['impedido']
      and 'alvo:alcancou-cobertura' not in x.eventos)
    s = porta()
    V('R5-03 falha da especial nao impede movimento nem devolve coletiva', s,
      lambda: s.cruzar_porta(sucesso=False), 'executada',
      lambda x: x.trajeto['posicao']=='cobertura' and not x.coletiva and x.corpos['A'].especial_preparada is None)
    s = porta()
    V('R5-04 recusa conserva preparacao e alvo continua', s,
      lambda: s.cruzar_porta(recusar=True), 'recusada:preparacao-conservada',
      lambda x: x.trajeto['posicao']=='cobertura' and x.coletiva and x.corpos['A'].especial_preparada is not None)
    V('R5-05 nao disparar cruzamento recusado na cobertura', s,
      lambda: s.resolver_gatilho('A'), 'recusado:sem-nova-ocorrencia', imutavel=True)
    s = porta(); s.corpos['A'].custos_disponiveis=False
    V('R5-06 inviabilidade na porta preserva coletiva e alvo continua', s,
      lambda: s.cruzar_porta(), 'inviavel:ocorrencia-descartada',
      lambda x: x.coletiva and x.trajeto['posicao']=='cobertura')
    s.corpos['A'].custos_disponiveis=True
    V('R5-07 custo recuperado depois nao armazena passagem', s,
      lambda: s.resolver_gatilho('A'), 'recusado:sem-nova-ocorrencia', imutavel=True)
    s = porta()
    V('R5-08 continuar e opcional sem parada imposta pelo dano', s,
      lambda: s.cruzar_porta(continuar=False), 'executada',
      lambda x: x.trajeto['saldo']==1 and not x.trajeto['impedido'])
    s = opcoes()
    V('R5-09 Provocar paga basica e preserva recursos do invocador', s,
      lambda: s.bonus_por_basica('A','Provocar'), 'opcao-executada',
      lambda x: x.corpos['A'].gastou and x.corpos['A'].basica is None and x.padrao and x.bonus and x.coletiva and x.corpos['A'].movimento)
    V('R5-10 conhecer outra opcao nao fornece segunda basica', s,
      lambda: s.bonus_por_basica('A','Ler o Ambiente'), 'recusado:basica', imutavel=True)
    s = opcoes(); s.corpos['A'].condicoes=['Lento']
    V('R5-11 Lento impede Provocar sem gastar basica', s,
      lambda: s.bonus_por_basica('A','Provocar'), 'recusado:bonus-impedida', imutavel=True)
    V('R5-12 Lento nao elimina outra basica permitida', s,
      lambda: s.basica_normal('A'), 'basica', lambda x: x.corpos['A'].gastou)
    s = opcoes(); s.corpos['A'].bonus_impedida=True
    V('R5-13 outro efeito que proibe Bonus tambem impede conversao', s,
      lambda: s.bonus_por_basica('A','Ler o Ambiente'), 'recusado:bonus-impedida', imutavel=True)
    s = opcoes()
    V('R5-14 nao concede habilidade ausente', s,
      lambda: s.bonus_por_basica('A','poder do invocador'), 'recusado:opcao-indisponivel', imutavel=True)
    V('R5-15 nao dispensa requisitos da opcao', s,
      lambda: s.bonus_por_basica('A','Provocar',requisitos=False), 'recusado:requisitos-opcao', imutavel=True)
    V('R5-16 nao dispensa coerencia com intencao', s,
      lambda: s.bonus_por_basica('A','Provocar',coerente=False), 'recusado:requisitos-opcao', imutavel=True)
    V('R5-17 especial comandada nao vira autonoma por custo Bonus', s,
      lambda: s.bonus_por_basica('A','especial de fixture'), 'fora-do-recorte:exige-procedimento-especial', imutavel=True)
    s.fechar_turno()
    V('R5-18 conversao nao cria janela fora do turno', s,
      lambda: s.bonus_por_basica('A','Provocar'), 'recusado:basica-fora-turno', imutavel=True)
    s = opcoes(reservas=('B',))
    V('R5-19 opcao limitada paga basica uso e custo proprio', s,
      lambda: s.bonus_por_basica('A','opcao limitada de fixture'), 'opcao-executada',
      lambda x: 'opcao limitada de fixture' in x.corpos['A'].usos and 'custo-proprio:bonus:A:opcao limitada de fixture' in x.eventos)
    s.substituir_apos_evento_legal(['A'],['B'],'B','guardar entrada')
    s.substituir_apos_evento_legal(['B'],['A'],'A','guardar entrada'); s.abrir_turno()
    V('R5-20 retorno e ciclo novo nao renovam uso limitado proprio', s,
      lambda: s.bonus_por_basica('A','opcao limitada de fixture'), 'recusado:uso-esgotado', imutavel=True)
    s = opcoes(); s.corpos['A'].opcoes_bonus['Provocar']['custo_disponivel']=False
    V('R5-21 sem custo proprio disponivel nao gasta basica', s,
      lambda: s.bonus_por_basica('A','Provocar'), 'recusado:requisitos-opcao', imutavel=True)
    s = opcoes(); s.corpos['A'].alvo_valido=False; s.antecipar('A'); s.corpos['A'].alvo_valido=True
    V('R5-22 conversao nao evita compromisso de antecipada valida', s,
      lambda: s.bonus_por_basica('A','Provocar'), 'recusado:preterir-especial', imutavel=True)
    s = abertura(); s.corpos['A'].movimento=0
    V('R5-23 Avancar proprio turno preserva basica coletiva e Movimento gasto', s,
      lambda: s.avancar('A'), 'avancou',
      lambda x: x.corpos['A'].basica is not None and x.coletiva and x.corpos['A'].movimento==0 and not x.corpos['A'].abertura_avancar)
    V('R5-24 Abertura consumida nao repete movimento', s,
      lambda: s.avancar('A'), 'recusado:avancar', imutavel=True)
    s = abertura(('A','B')); s.preparar_especial('A'); s.preparar('B')
    V('R5-25 Avancar no turno nao destroi preparacoes', s,
      lambda: s.avancar('A'), 'avancou',
      lambda x: x.coletiva and x.corpos['A'].especial_preparada is not None and x.corpos['B'].preparado is not None)
    s.acontecimento('cruzar:X')
    V('R5-26 preparada depois de Avancar gratuito ainda exige coletiva', s,
      lambda: s.resolver_gatilho('A'), 'executada',
      lambda x: not x.coletiva and x.corpos['B'].preparado is None)
    s = abertura(('A','B')); s.preparar_especial('A'); s.preparar('B'); s.fechar_turno()
    V('R5-27 Avancar fora gasta coletiva e perde ambas preparacoes', s,
      lambda: s.avancar('A'), 'avancou',
      lambda x: not x.coletiva and x.corpos['A'].especial_preparada is None and x.corpos['B'].preparado is None and x.pessoal)
    V('R5-28 outro corpo nao paga resposta Guia apos Avancar', s,
      lambda: s.resposta_guia30('B'), 'recusado:reacao', imutavel=True)
    s = abertura(); s.fechar_turno(); s.coletiva=False
    V('R5-29 falta de coletiva nao consome Abertura fora do turno', s,
      lambda: s.avancar('A'), 'recusado:reacao', imutavel=True)
    V('R5-30 dispensa expressa permite Avancar sem renovar coletiva', s,
      lambda: s.avancar('A',dispensa_expressa=True), 'avancou',
      lambda x: not x.coletiva and x.corpos['A'].trechos_avancar==1)
    s = abertura(); s.preparar_especial('A'); s.fechar_turno()
    V('R5-31 dispensa expressa preserva preparacao sem gasto de coletiva', s,
      lambda: s.avancar('A',dispensa_expressa=True), 'avancou',
      lambda x: x.coletiva and x.corpos['A'].especial_preparada is not None)
    s = abertura(); s.fechar_turno()
    V('R5-32 fora da janela escrita nao usa Avancar', s,
      lambda: s.avancar('A',janela=False), 'recusado:avancar', imutavel=True)
    V('R5-33 trajeto impedido nao consome Abertura ou coletiva', s,
      lambda: s.avancar('A',requisitos=False), 'recusado:avancar', imutavel=True)
    s = abertura(); s.coletiva=False
    V('R5-34 coletiva gasta nao impede Avancar no proprio turno', s,
      lambda: s.avancar('A'), 'avancou', lambda x: not x.coletiva)

if __name__ == '__main__':
    base.executar(); r4.r2.novos(); r4.novos()
    regressao = len(base.resultados)
    novos()
    report=dict(tipo='Ensaio simbolico delimitado; nao e prova de equilibrio',
        regressao_no_modelo_r5=regressao, novos=len(base.resultados)-regressao,
        verificacoes=len(base.resultados), passaram=sum(r['aprovado'] for r in base.resultados),
        falharam=sum(not r['aprovado'] for r in base.resultados),
        sem_mutacao=sum(r['imutavel_exigido'] for r in base.resultados), resultados=base.resultados)
    pasta=Path(__file__).resolve().parent
    (pasta/'resultados.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    resumo={k:v for k,v in report.items() if k!='resultados'}
    (pasta/'execucao.json').write_text(json.dumps(resumo,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(resumo,ensure_ascii=False,indent=2))
