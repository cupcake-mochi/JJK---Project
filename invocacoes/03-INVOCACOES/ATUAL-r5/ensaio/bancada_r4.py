"""Ensaio delimitado §§33–40, com regressão r1+r2 sobre as classes ampliadas.

Não interpreta frases (§§31–32), calcula geometria/preços nem simula combate.
Eventos, requisitos e legalidade de emissão são entradas da cena. Transições
espaciais booleanas exercitam apenas 'entrar', não um alcance numérico. Uma
básica por corpo é fixture herdada. Resoluções são atômicas; não há escalonador
universal de gatilhos nem regra nova de interrupção/prioridade.
"""
from dataclasses import dataclass, field
from pathlib import Path
import hashlib
import json
import bancada_r2 as r2

base = r2.base


@dataclass
class Corpo(r2.Corpo):
    especial_preparada: dict | None = None
    pagamentos_antecipados: list = field(default_factory=list)


@dataclass
class Cena(r2.Cena):
    numero_evento: int = 0
    evento_atual: dict | None = None
    estados_observados: dict = field(default_factory=dict)

    def invariantes(self):
        super().invariantes()
        for c in self.corpos.values():
            if c.especial_preparada:
                assert c.em_campo and c.gastou and c.basica is None
                assert c.ordem is None and c.preparado is None
                assert c.especial_preparada['ciclo_emissao'] == self.ciclo

    def abrir_turno(self):
        for c in self.corpos.values():
            c.especial_preparada = None
        self.evento_atual = None
        super().abrir_turno()

    def perder_preparacoes(self):
        super().perder_preparacoes()
        for c in self.corpos.values():
            c.especial_preparada = None

    def recolher_apos_evento_legal(self, nome):
        resultado = super().recolher_apos_evento_legal(nome)
        if resultado == 'recolhida':
            self.corpos[nome].especial_preparada = None
        return resultado

    def substituir_apos_evento_legal(self, saidas, entradas, direta, tarefa):
        resultado = super().substituir_apos_evento_legal(saidas, entradas, direta, tarefa)
        if resultado == 'substituida':
            for nome in saidas:
                self.corpos[nome].especial_preparada = None
        return resultado

    def antecipar(self, nome, capacidade='especial A', alvo='X', nova_intencao=None):
        if self.corpos[nome].especial_preparada:
            return 'recusado:ja-tem-especial'
        return super().antecipar(nome, capacidade, alvo, nova_intencao)

    def preparar_especial(self, nome, capacidade='especial A', alvo='X',
                         gatilho='cruzar:X', emissao_legal=True):
        c = self.corpos[nome]
        if c.ordem or c.especial_preparada:
            return 'recusado:ja-tem-especial'
        if not (self.momento == 'turno' and self.consciente and self.comunica
                and self.padrao and emissao_legal):
            return 'recusado:comando'
        if not (c.em_campo and not c.atordoado and c.basica):
            return 'recusado:preparar-especial'
        self.padrao = False
        self.eventos.append(f'P:preparar-especial:{nome}')
        if not self.recebe(nome):
            return 'falha:recepcao'
        token = c.basica
        c.basica = None
        c.gastou = True
        c.especial_preparada = dict(capacidade=capacidade, alvo=alvo,
            gatilho=gatilho, ciclo_emissao=self.ciclo,
            depois_de=self.numero_evento, ultima_ocorrencia=self.numero_evento)
        self.eventos.append(f'basica:preparar-especial:{nome}:{token}')
        return 'especial-preparada'

    def ajustar_preparada(self, nome, capacidade, alvo, gatilho, emissao_legal=True):
        c = self.corpos[nome]
        p = c.especial_preparada
        if not (p and self.momento == 'turno' and self.ciclo == p['ciclo_emissao']
                and self.consciente and self.comunica and emissao_legal):
            return 'recusado:ajuste-preparada'
        if not self.recebe(nome):
            return 'falha:recepcao'
        p.update(capacidade=capacidade, alvo=alvo, gatilho=gatilho,
                 depois_de=self.numero_evento)
        self.eventos.append(f'ajuste-livre:preparada:{nome}')
        return 'ajustada'

    def desistir_preparada(self, nome):
        c = self.corpos[nome]
        if not (c.especial_preparada and self.consciente and self.recebe(nome)):
            return 'recusado:desistencia-preparada'
        c.especial_preparada = None
        self.eventos.append(f'preparada:desistiu:{nome}')
        return 'desistiu'

    def converter_sem_novo_comando(self, nome):
        # Sonda da interface: nenhuma mutação ou aproveitamento é permitido.
        return 'recusado:exige-encerramento-e-novo-comando'

    def acontecimento(self, gatilho, criatura_percebe=True, invocador_percebe=True):
        # O roteiro atesta que aconteceu uma ocorrência nova na janela legal.
        self.numero_evento += 1
        self.evento_atual = dict(numero=self.numero_evento, gatilho=gatilho,
            criatura_percebe=criatura_percebe, invocador_percebe=invocador_percebe)
        return 'ocorrencia'

    def observar_estado(self, chave, presente):
        # Estado espacial conhecido da cena, sem inferir sentidos compartilhados.
        antes = self.estados_observados.get(chave, False)
        self.estados_observados[chave] = presente
        if presente and not antes:
            return self.acontecimento('entrada:' + chave)
        self.evento_atual = None
        return 'sem-nova-ocorrencia'

    def resolver_gatilho(self, nome, recusar=False, nova_intencao=None, sucesso=True):
        c = self.corpos[nome]
        p, e = c.especial_preparada, self.evento_atual
        if not p:
            return 'recusado:sem-preparacao-especial'
        if not (e and e['gatilho'] == p['gatilho'] and e['criatura_percebe']
                and e['numero'] > max(p['depois_de'], p['ultima_ocorrencia'])):
            return 'recusado:sem-nova-ocorrencia'
        if not (c.em_campo and not c.atordoado and c.alvo_valido
                and c.custos_disponiveis and self.coletiva):
            p['ultima_ocorrencia'] = e['numero']
            self.eventos.append(f'gatilho:inviavel:{nome}')
            return 'inviavel:ocorrencia-descartada'
        if recusar:
            if not (self.consciente and self.recebe(nome) and e['invocador_percebe']):
                return 'recusado:sem-comunicacao-para-recusar'
            p['ultima_ocorrencia'] = e['numero']
            self.eventos.append(f'gatilho:recusado:{nome}')
            return 'recusada:preparacao-conservada'
        # Sem segunda básica/Padrão. Reagir descarta todas as preparações.
        assert self.reagir(nome, 'especial preparada') == 'respondeu'
        self.eventos.append(f"especial-preparada:executou:{nome}:{p['capacidade']}:{p['alvo']}")
        self.eventos.append(f'custo-proprio:ativacao:{nome}')
        self.eventos.append(f'resultado:{nome}:{"sucesso" if sucesso else "falha"}')
        if nova_intencao and self.consciente and self.recebe(nome):
            c.intencao = nova_intencao
            self.eventos.append(f'intencao:apos-resultado:{nome}')
        return 'executada'


# A regressão inteira usa as classes novas, inclusive cenas de r2.novos().
base.Corpo = Corpo
base.Cena = Cena
V = base.verificar
cena = base.cena


def pronta(nomes=('A',), reservas=(), gatilho='cruzar:X'):
    s = cena(nomes, reservas)
    assert s.preparar_especial('A', gatilho=gatilho) == 'especial-preparada'
    return s


def novos():
    s = cena()
    V('R4-01 preparar especial paga P e basica sem coletiva ou ativacao', s,
      lambda: s.preparar_especial('A'), 'especial-preparada',
      lambda x: not x.padrao and x.bonus and x.coletiva and x.corpos['A'].gastou
      and not any(e.startswith('custo-proprio:') for e in x.eventos))
    s.acontecimento('cruzar:X')
    V('R4-02 gatilho no proprio turno usa coletiva sem outra P ou basica', s,
      lambda: s.resolver_gatilho('A', nova_intencao='proteger Y'), 'executada',
      lambda x: not x.coletiva and not x.padrao and x.bonus
      and x.corpos['A'].intencao == 'proteger Y' and x.corpos['A'].movimento
      and len([e for e in x.eventos if e.startswith('basica:')]) == 1
      and x.eventos.index('resultado:A:sucesso') < x.eventos.index('intencao:apos-resultado:A'))
    V('R4-03 especial preparada resolvida nao deixa basica extra', s,
      lambda: s.basica_normal('A'), 'recusado:basica', imutavel=True)
    V('R4-04 mesma ocorrencia nao repete especial resolvida', s,
      lambda: s.resolver_gatilho('A'), 'recusado:sem-preparacao-especial', imutavel=True)
    s = pronta(); s.fechar_turno(); s.acontecimento('cruzar:X')
    V('R4-05 preparada fora do turno paga coletiva sem segunda basica', s,
      lambda: s.resolver_gatilho('A'), 'executada',
      lambda x: not x.coletiva and x.corpos['A'].basica is None and not x.padrao)
    s = cena(); s.basica_normal('A')
    V('R4-06 sem basica nao cria preparacao especial', s,
      lambda: s.preparar_especial('A'), 'recusado:preparar-especial', imutavel=True)
    s = cena(); s.padrao = False
    V('R4-07 sem Padrao nao prepara especial', s,
      lambda: s.preparar_especial('A'), 'recusado:comando', imutavel=True)
    s = cena(); s.recepcao['A'] = False
    V('R4-08 emissao falha paga P sem gastar basica ou criar preparacao', s,
      lambda: s.preparar_especial('A'), 'falha:recepcao',
      lambda x: not x.padrao and x.corpos['A'].basica is not None
      and x.corpos['A'].especial_preparada is None and x.coletiva)
    s = cena(); s.comunica = False
    V('R4-09 canal conhecido indisponivel bloqueia antes do gasto', s,
      lambda: s.preparar_especial('A'), 'recusado:comando', imutavel=True)
    s = cena(); s.fechar_turno()
    V('R4-10 nao cria comando de preparacao fora do turno', s,
      lambda: s.preparar_especial('A'), 'recusado:comando', imutavel=True)
    s = pronta(('A', 'B')); s.preparar('B'); s.acontecimento('cruzar:X')
    V('R4-11 especial preparada executa e encerra preparacao basica alheia', s,
      lambda: s.resolver_gatilho('A'), 'executada',
      lambda x: x.corpos['B'].preparado is None and x.corpos['B'].gastou)
    s = pronta(('A', 'B')); s.fechar_turno()
    V('R4-12 resposta Guia encerra preparada sem devolver basica', s,
      lambda: s.resposta_guia30('B'), 'golpe-comum',
      lambda x: x.corpos['A'].especial_preparada is None and x.corpos['A'].gastou
      and x.corpos['B'].basica is not None)
    s.abrir_turno(); s.acontecimento('cruzar:X')
    V('R4-13 renovar coletiva nao restaura preparada perdida', s,
      lambda: s.resolver_gatilho('A'), 'recusado:sem-preparacao-especial', imutavel=True)
    s = pronta(reservas=('B',))
    V('R4-14 substituta nao recebe basica investida na preparacao', s,
      lambda: s.substituir_apos_evento_legal(['A'], ['B'], 'B', 'proteger Y'), 'substituida',
      lambda x: x.corpos['A'].especial_preparada is None and x.corpos['A'].gastou
      and x.corpos['B'].basica is None and x.corpos['B'].intencao == 'proteger Y'
      and x.corpos['B'].movimento and x.coletiva)
    V('R4-15 retorno no ciclo nao restaura preparacao ou basica', s,
      lambda: s.substituir_apos_evento_legal(['B'], ['A'], 'A', 'guardar'), 'substituida',
      lambda x: x.corpos['A'].especial_preparada is None and x.corpos['A'].basica is None)
    s = pronta(); s.rodada_global()
    V('R4-16 rodada global nao expira nem renova preparacao', s,
      lambda: 'conferido', 'conferido',
      lambda x: x.corpos['A'].especial_preparada is not None and not x.padrao
      and x.corpos['A'].basica is None, imutavel=True)
    s.abrir_turno()
    V('R4-17 fronteira expira preparacao antes de nova tentativa de gatilho', s,
      lambda: s.resolver_gatilho('A'), 'recusado:sem-preparacao-especial',
      lambda x: x.padrao and x.corpos['A'].basica is not None, imutavel=True)
    s = pronta(); s.corpos['A'].custos_disponiveis = False; s.acontecimento('cruzar:X')
    V('R4-18 gatilho sem custo descarta ocorrencia sem gastar coletiva', s,
      lambda: s.resolver_gatilho('A'), 'inviavel:ocorrencia-descartada',
      lambda x: x.coletiva and x.corpos['A'].especial_preparada is not None
      and not any(e.startswith('custo-proprio:') for e in x.eventos))
    s.corpos['A'].custos_disponiveis = True
    V('R4-19 recuperar custo nao reaproveita ocorrencia perdida', s,
      lambda: s.resolver_gatilho('A'), 'recusado:sem-nova-ocorrencia', imutavel=True)
    s.acontecimento('cruzar:X')
    V('R4-20 nova ocorrencia valida executa sem outra basica', s,
      lambda: s.resolver_gatilho('A'), 'executada', lambda x: not x.coletiva)
    s = pronta(); s.acontecimento('cruzar:X')
    V('R4-21 recusa conserva preparacao sem pagar ativacao ou coletiva', s,
      lambda: s.resolver_gatilho('A', recusar=True), 'recusada:preparacao-conservada',
      lambda x: x.coletiva and not x.padrao and x.corpos['A'].gastou
      and x.corpos['A'].especial_preparada['ciclo_emissao'] == 1)
    V('R4-22 recusa nao guarda disparo para a mesma ocorrencia', s,
      lambda: s.resolver_gatilho('A'), 'recusado:sem-nova-ocorrencia', imutavel=True)
    s.acontecimento('cruzar:X')
    V('R4-23 nova ocorrencia apos recusa pode executar', s,
      lambda: s.resolver_gatilho('A'), 'executada', lambda x: not x.coletiva)
    s = pronta(); s.fechar_turno(); s.acontecimento('cruzar:X')
    V('R4-24 recusa comunicada fora do turno nao e ajuste de conteudo', s,
      lambda: s.resolver_gatilho('A', recusar=True), 'recusada:preparacao-conservada',
      lambda x: x.corpos['A'].especial_preparada['gatilho'] == 'cruzar:X' and x.bonus)
    s = pronta(); s.consciente = False; s.acontecimento('cruzar:X')
    V('R4-25 inconsciente nao emite recusa nova', s,
      lambda: s.resolver_gatilho('A', recusar=True), 'recusado:sem-comunicacao-para-recusar', imutavel=True)
    V('R4-26 ordem previa executa inconsciente sem nova intencao', s,
      lambda: s.resolver_gatilho('A', nova_intencao='atacar Y'), 'executada',
      lambda x: x.corpos['A'].intencao == 'guardar entrada' and not x.coletiva)
    s = pronta(); s.recepcao['A'] = False; s.acontecimento('cruzar:X')
    V('R4-27 recusa nao recebida nao interrompe ordem recebida', s,
      lambda: s.resolver_gatilho('A', recusar=True), 'recusado:sem-comunicacao-para-recusar', imutavel=True)
    V('R4-28 execucao permanece possivel sem comunicacao atual', s,
      lambda: s.resolver_gatilho('A', nova_intencao='atacar Y'), 'executada',
      lambda x: x.corpos['A'].intencao == 'guardar entrada')
    s = pronta(); s.acontecimento('cruzar:X', invocador_percebe=False)
    V('R4-29 recusa nao usa conhecimento exclusivo do jogador', s,
      lambda: s.resolver_gatilho('A', recusar=True), 'recusado:sem-comunicacao-para-recusar', imutavel=True)
    s = pronta(); s.bonus = False
    V('R4-30 ajuste no turno emitido nao exige B disponivel', s,
      lambda: s.ajustar_preparada('A', 'especial B', 'Y', 'cruzar:Y'), 'ajustada',
      lambda x: not x.bonus and not x.padrao and x.corpos['A'].gastou and x.coletiva
      and x.corpos['A'].especial_preparada['capacidade'] == 'especial B')
    s.acontecimento('cruzar:X')
    V('R4-31 gatilho anterior nao aciona conteudo ajustado', s,
      lambda: s.resolver_gatilho('A'), 'recusado:sem-nova-ocorrencia', imutavel=True)
    s.fechar_turno()
    V('R4-32 fora do turno de emissao nao ha ajuste gratuito', s,
      lambda: s.ajustar_preparada('A', 'especial C', 'Z', 'cruzar:Z'), 'recusado:ajuste-preparada', imutavel=True)
    s.acontecimento('cruzar:Y')
    V('R4-33 gatilho ajustado recebido executa normalmente', s,
      lambda: s.resolver_gatilho('A'), 'executada',
      lambda x: not x.coletiva and 'especial-preparada:executou:A:especial B:Y' in x.eventos)
    s = pronta(); s.recepcao['A'] = False
    V('R4-34 ajuste gratuito falho nao cobra B nem muda a preparacao', s,
      lambda: s.ajustar_preparada('A', 'especial B', 'Y', 'cruzar:Y'), 'falha:recepcao', imutavel=True)
    s = pronta(); s.acontecimento('cruzar:Y'); s.ajustar_preparada('A', 'especial B', 'Y', 'cruzar:Y')
    V('R4-35 ajuste nao aproveita acontecimento anterior a alteracao', s,
      lambda: s.resolver_gatilho('A'), 'recusado:sem-nova-ocorrencia', imutavel=True)
    s = cena(); s.corpos['A'].alvo_valido = False; s.antecipar('A'); s.abrir_turno()
    V('R4-36 antecipada impede segunda especial preparada no mesmo corpo', s,
      lambda: s.preparar_especial('A'), 'recusado:ja-tem-especial', imutavel=True)
    V('R4-37 antecipada inviavel pode coexistir com Preparar basica', s,
      lambda: s.preparar('A'), 'preparada',
      lambda x: x.corpos['A'].ordem is not None and x.corpos['A'].preparado is not None)
    s = pronta()
    V('R4-38 preparada impede segunda especial antecipada no mesmo corpo', s,
      lambda: s.antecipar('A'), 'recusado:ja-tem-especial', imutavel=True)
    V('R4-39 preparada impede outra preparacao especial', s,
      lambda: s.preparar_especial('A', 'especial B'), 'recusado:ja-tem-especial', imutavel=True)
    # A ordem de B foi paga em ciclo anterior; A prepara neste ciclo.
    s = cena(('A', 'B')); s.corpos['B'].alvo_valido = False; s.antecipar('B'); s.abrir_turno(); s.preparar_especial('A')
    V('R4-40 corpos diferentes podem manter modalidades diferentes', s,
      lambda: 'conferido', 'conferido',
      lambda x: x.corpos['A'].especial_preparada is not None and x.corpos['B'].ordem is not None, imutavel=True)
    s.fechar_turno(); s.corpos['B'].alvo_valido = True; s.acontecimento('cruzar:X')
    V('R4-41 preparada escolhida deixa antecipada sem coletiva esperando', s,
      lambda: s.resolver_gatilho('A'), 'executada',
      lambda x: x.corpos['B'].ordem is not None and x.corpos['B'].basica is not None)
    V('R4-42 concorrente nao executa sem coletiva', s,
      lambda: s.janela(['B'], 'B'), 'espera:sem-elegivel', imutavel=True)
    s = cena(('A', 'B')); s.corpos['B'].alvo_valido = False; s.antecipar('B'); s.abrir_turno(); s.preparar_especial('A')
    s.fechar_turno(); s.corpos['B'].alvo_valido = True
    V('R4-43 antecipada concorrente encerra preparacao especial', s,
      lambda: s.janela(['B'], 'B'), 'executada', lambda x: x.corpos['A'].especial_preparada is None)
    s = cena(); s.corpos['A'].alvo_valido = False; s.antecipar('A')
    V('R4-44 conversao direta nao aproveita investimento', s,
      lambda: s.converter_sem_novo_comando('A'), 'recusado:exige-encerramento-e-novo-comando', imutavel=True)
    V('R4-45 encerrar antecipada nao recupera P', s,
      lambda: s.desistir('A'), 'desistiu', lambda x: not x.padrao and x.corpos['A'].basica is not None)
    V('R4-46 nao prepara depois de encerrar sem nova P', s,
      lambda: s.preparar_especial('A'), 'recusado:comando', imutavel=True)
    s = cena(); s.corpos['A'].alvo_valido = False; s.antecipar('A'); s.abrir_turno(); s.desistir('A')
    V('R4-47 nova P e basica legal permitem novo comando preparado', s,
      lambda: s.preparar_especial('A'), 'especial-preparada',
      lambda x: not x.padrao and x.corpos['A'].gastou and x.corpos['A'].ordem is None
      and len([e for e in x.eventos if e.startswith('P:')]) == 2)
    s = cena(); s.corpos['A'].alvo_valido = False; s.antecipar('A'); s.abrir_turno(); s.basica_normal('A'); s.desistir('A')
    V('R4-48 nova P nao substitui basica ja gasta para preparar', s,
      lambda: s.preparar_especial('A'), 'recusado:preparar-especial', imutavel=True)
    s = pronta(); s.corpos['A'].pagamentos_antecipados = ['pagamento especifico ja ocorrido na cena']
    V('R4-49 encerrar preparada conserva P basica e pagamento proprio gastos', s,
      lambda: s.desistir_preparada('A'), 'desistiu',
      lambda x: not x.padrao and x.corpos['A'].gastou and x.corpos['A'].basica is None
      and len(x.corpos['A'].pagamentos_antecipados) == 1 and x.coletiva)
    V('R4-50 preparada encerrada nao compra antecipada sem nova P', s,
      lambda: s.antecipar('A'), 'recusado:comando', imutavel=True)
    # Recurso extra explícito da cena para exercitar §39; não é concedido pelo subsistema.
    s.padrao = True; s.eventos.append('premissa:outra-P-legal-fornecida-pela-cena')
    V('R4-51 outra P legal cria antecipada mas nao devolve basica investida', s,
      lambda: s.antecipar('A'), 'ordenado',
      lambda x: not x.padrao and x.corpos['A'].gastou and x.corpos['A'].basica is None
      and x.corpos['A'].especial_preparada is None and x.corpos['A'].ordem is not None)
    V('R4-52 antecipada nova aguarda basica elegivel', s,
      lambda: s.janela(['A'], 'A'), 'espera:sem-elegivel', imutavel=True)
    s.abrir_turno()
    V('R4-53 nova antecipada executa na oportunidade valida seguinte', s,
      lambda: s.janela(['A'], 'A'), 'executada',
      lambda x: x.corpos['A'].ordem is None and x.padrao and x.coletiva
      and len(x.corpos['A'].pagamentos_antecipados) == 1)
    s = cena(); s.corpos['A'].alvo_valido = False; s.antecipar('A'); s.corpos['A'].alvo_valido = True
    V('R4-54 oportunidade valida nao permite conversao como adiamento', s,
      lambda: s.converter_sem_novo_comando('A'), 'recusado:exige-encerramento-e-novo-comando', imutavel=True)
    V('R4-55 compromisso da antecipada continua valido', s,
      lambda: s.janela(['A'], 'A', adiar=True), 'recusado:adiar-ordem-valida', imutavel=True)
    V('R4-56 desistir na oportunidade e permitido sem estornar P', s,
      lambda: s.janela(['A'], 'A', desistir=True), 'desistiu',
      lambda x: not x.padrao and x.corpos['A'].basica is not None and x.corpos['A'].ordem is None)
    s = pronta(); s.recepcao['A'] = False
    V('R4-57 cancelamento de preparada nao recebido preserva ordem', s,
      lambda: s.desistir_preparada('A'), 'recusado:desistencia-preparada', imutavel=True)
    s = pronta(); s.fechar_turno(); s.desistir_preparada('A')
    V('R4-58 desistir fora do turno nao concede janela para comando novo', s,
      lambda: s.antecipar('A'), 'recusado:comando', imutavel=True)
    s = cena(); s.observar_estado('alcance:X', True); s.preparar_especial('A', gatilho='entrada:alcance:X')
    V('R4-59 entrada anterior a preparacao nao dispara retroativamente', s,
      lambda: s.resolver_gatilho('A'), 'recusado:sem-nova-ocorrencia', imutavel=True)
    s.observar_estado('alcance:X', True)
    V('R4-60 permanecer em alcance nao produz entrada nova', s,
      lambda: s.resolver_gatilho('A'), 'recusado:sem-nova-ocorrencia', imutavel=True)
    s.observar_estado('alcance:X', False); s.observar_estado('alcance:X', True)
    V('R4-61 sair e entrar pode criar ocorrencia recusavel', s,
      lambda: s.resolver_gatilho('A', recusar=True), 'recusada:preparacao-conservada',
      lambda x: x.corpos['A'].especial_preparada is not None and x.coletiva)
    s.observar_estado('alcance:X', True)
    V('R4-62 permanencia apos recusa nao cria disparo livre', s,
      lambda: s.resolver_gatilho('A'), 'recusado:sem-nova-ocorrencia', imutavel=True)
    s.observar_estado('alcance:X', False); s.observar_estado('alcance:X', True)
    V('R4-63 outra entrada valida executa dentro do prazo', s,
      lambda: s.resolver_gatilho('A'), 'executada', lambda x: not x.coletiva)
    s = pronta(gatilho='entrada:alcance:X'); s.corpos['A'].alvo_valido = False
    s.observar_estado('alcance:X', True); s.resolver_gatilho('A'); s.corpos['A'].alvo_valido = True
    s.observar_estado('alcance:X', True)
    V('R4-64 recuperar requisito em estado continuo nao cria nova ocorrencia', s,
      lambda: s.resolver_gatilho('A'), 'recusado:sem-nova-ocorrencia', imutavel=True)
    s = pronta(); s.acontecimento('cruzar:X'); s.resolver_gatilho('A', recusar=True); s.abrir_turno(); s.acontecimento('cruzar:X')
    V('R4-65 recusa anterior nao estende preparacao alem do prazo', s,
      lambda: s.resolver_gatilho('A'), 'recusado:sem-preparacao-especial', imutavel=True)
    s = pronta(); s.acontecimento('cruzar:X', criatura_percebe=False)
    V('R4-66 evento nao percebido pela criatura nao dispara', s,
      lambda: s.resolver_gatilho('A'), 'recusado:sem-nova-ocorrencia', imutavel=True)
    s = pronta(); s.acontecimento('cruzar:X')
    V('R4-67 especial executada que falha termina sem credito de repeticao', s,
      lambda: s.resolver_gatilho('A', sucesso=False, nova_intencao='proteger Y'), 'executada',
      lambda x: x.corpos['A'].especial_preparada is None and not x.coletiva
      and x.corpos['A'].intencao == 'proteger Y' and 'resultado:A:falha' in x.eventos)
    # Cruzamento ainda não coberto pela primeira execução: duas preparadas especiais.
    s = pronta(('A', 'B')); s.padrao = True
    s.eventos.append('premissa:outra-P-legal-fornecida-pela-cena')
    s.preparar_especial('B'); s.acontecimento('cruzar:X')
    V('R4-68 duas preparadas especiais compartilham perda pela coletiva', s,
      lambda: s.resolver_gatilho('A', nova_intencao='proteger Y'), 'executada',
      lambda x: all(c.especial_preparada is None and c.gastou for c in x.corpos.values())
      and x.corpos['B'].intencao == 'guardar entrada' and not x.coletiva)
    s = cena(('A', 'B')); s.corpos['A'].intencao = None
    s.preparar_especial('A'); s.acontecimento('cruzar:X')
    V('R4-69 sem intencao anterior especial concede orientacao posterior so a destinataria', s,
      lambda: s.resolver_gatilho('A', nova_intencao='proteger Y'), 'executada',
      lambda x: x.corpos['A'].intencao == 'proteger Y' and x.corpos['B'].intencao == 'guardar entrada'
      and x.bonus and x.corpos['B'].basica is not None)
    s = pronta(); s.recepcao['A'] = False; s.acontecimento('cruzar:X')
    s.resolver_gatilho('A', nova_intencao='proteger Y'); s.recepcao['A'] = True
    V('R4-70 recuperar canal depois da preparada nao concede orientacao gratuita atrasada', s,
      lambda: s.orientar(['A'], 'proteger Y'), 'orientado', lambda x: not x.bonus)
    s = cena(); s.corpos['A'].alvo_valido = False; s.antecipar('A'); s.abrir_turno()
    s.desistir('A'); s.recepcao['A'] = False
    V('R4-71 novo comando falho nao restaura ordem ja encerrada', s,
      lambda: s.preparar_especial('A'), 'falha:recepcao',
      lambda x: not x.padrao and x.corpos['A'].ordem is None
      and x.corpos['A'].especial_preparada is None and x.corpos['A'].basica is not None)


if __name__ == '__main__':
    base.executar()
    r2.novos()
    regressao = len(base.resultados)
    novos()
    folder = Path(__file__).resolve().parent
    report = dict(tipo='Ensaio simbolico; nao demonstra equilibrio',
        regressao_r1_r2_no_modelo_r4=regressao,
        novos=len(base.resultados)-regressao, verificacoes=len(base.resultados),
        passaram=sum(r['aprovado'] for r in base.resultados),
        falharam=sum(not r['aprovado'] for r in base.resultados),
        rejeicoes_ou_consultas_sem_mutacao=sum(r['imutavel_exigido'] for r in base.resultados),
        arquivos_modelo={n: hashlib.sha256((folder/n).read_bytes()).hexdigest()
            for n in ('base_r1.py', 'bancada_r2.py', 'bancada_r4.py')},
        resultados=base.resultados)
    (folder/'resultados.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    summary = {k:v for k,v in report.items() if k != 'resultados'}
    (folder/'execucao.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(summary, ensure_ascii=False, indent=2))
