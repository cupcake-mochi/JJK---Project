"""Ensaio simbólico r2. Não é simulador de combate nem prova de equilíbrio.
A regressão r1 usa este modelo ampliado. Uma oportunidade por corpo é fixture;
Movimento parcial usa fração abstrata, sem metros. Eventos legais de troca,
recepção, percepção, custos disponíveis, gatilhos e sucesso de TR são premissas.
Não implementa preços, todas as condições, queda definitiva ou vínculo completo.
"""
from dataclasses import dataclass, field
from pathlib import Path
import hashlib,json
import base_r1 as base

@dataclass
class Corpo(base.Corpo):
    preparado: str | None = None
    impedimento_temporario: bool = False
    efeitos: list = field(default_factory=list)
    ocorrencias: list = field(default_factory=list)

@dataclass
class Cena(base.Cena):
    recepcao: dict = field(default_factory=dict)  # fato da cena, não confirmação ao personagem

    def recebe(self,n):
        return self.comunica and self.recepcao.get(n,True)

    def invariantes(self):
        super().invariantes()
        for c in self.corpos.values():
            assert not c.preparado or (c.em_campo and c.gastou and c.basica is None)

    def abrir_turno(self):
        for c in self.corpos.values():
            c.preparado=None
            if not c.em_campo:
                c.basica=None
                c.gastou=c.perdeu=False
        super().abrir_turno()
        # Efeitos com início/fim são resolvidos explicitamente pelo roteiro:
        # não escolher aqui precedência geral ainda não aprovada.

    def recolher_apos_evento_legal(self,n):
        c=self.corpos[n]
        if not c.em_campo: return 'recusado:fora-de-campo'
        c.em_campo=False; c.ordem=None; c.preparado=None
        self.eventos.append('evento-legal:recolhimento-sem-custo-modelado')
        return 'recolhida'

    def substituir_apos_evento_legal(self,saidas,entradas,direta,tarefa):
        anterior=self.corpos[direta].intencao
        r=super().substituir_apos_evento_legal(saidas,entradas,direta,tarefa)
        if r=='substituida':
            for n in saidas: self.corpos[n].preparado=None
            if not (self.consciente and self.recebe(direta)):
                self.corpos[direta].intencao=anterior
        return r

    def orientar(self,nomes,tarefa):
        if not (self.momento=='turno' and self.consciente and self.comunica and self.bonus):
            return 'recusado:orientacao'
        if not all(self.corpos[n].em_campo for n in nomes): return 'recusado:fora-de-campo'
        self.bonus=False
        recebidas=[n for n in nomes if self.recebe(n)]
        for n in recebidas: self.corpos[n].intencao=tarefa
        self.eventos.append('B:orientacao')
        if len(recebidas)==len(nomes): return 'orientado'
        return 'recepcao-parcial' if recebidas else 'falha:recepcao'

    def antecipar(self,nome,capacidade='especial A',alvo='X',nova_intencao=None):
        c=self.corpos[nome]
        if not (self.momento=='turno' and self.consciente and self.comunica and self.padrao):
            return 'recusado:comando'
        if not c.em_campo: return 'recusado:fora-de-campo'
        if c.ordem: return 'recusado:ja-tem-ordem'
        self.padrao=False; self.eventos.append(f'P:ordem:{nome}')
        if not self.recebe(nome): return 'falha:recepcao'
        c.ordem={'capacidade':capacidade,'alvo':alvo}
        if self.viavel(nome): return self.especial(nome,nova_intencao)
        return 'ordenado'

    def ajustar(self,nome,capacidade,alvo):
        c=self.corpos[nome]
        if not (self.momento=='turno' and self.consciente and self.comunica and self.bonus and c.ordem):
            return 'recusado:ajuste'
        if not self.recebe(nome):
            self.bonus=False; self.eventos.append(f'B:ajuste-falhou:{nome}')
            return 'falha:recepcao'
        return super().ajustar(nome,capacidade,alvo)

    def desistir(self,nome):
        if not self.recebe(nome): return 'recusado:desistencia'
        return super().desistir(nome)

    def perder_preparacoes(self):
        for c in self.corpos.values(): c.preparado=None

    def especial(self,nome,nova_intencao=None,sucesso=True,imediata=False):
        if imediata:
            return self.antecipar(nome,nova_intencao=nova_intencao)
        # A falha da orientação posterior não desfaz a resolução.
        if not self.recebe(nome): nova_intencao=None
        antes=self.coletiva
        r=super().especial(nome,nova_intencao,sucesso,imediata)
        if antes and not self.coletiva: self.perder_preparacoes()
        return r

    def reagir(self,nome,fonte='capacidade escrita elegivel'):
        r=super().reagir(nome,fonte)
        if r=='respondeu': self.perder_preparacoes()
        return r

    def viavel(self,n):
        c=self.corpos[n]
        return bool(c.em_campo and not c.atordoado and c.basica and c.ordem
            and c.alvo_valido and c.custos_disponiveis and self.momento!='resolvendo'
            and (self.momento=='turno' or self.coletiva))

    def janela(self,nomes,escolhida=None,desistir=False,adiar=False):
        # nomes contém ordens com a mesma janela, fornecida pela cena.
        aptas=[n for n in nomes if self.viavel(n)]
        if not aptas: return 'espera:sem-elegivel'
        if adiar: return 'recusado:adiar-ordem-valida'
        if escolhida not in aptas: return 'recusado:escolha'
        if desistir: return self.desistir(escolhida)
        return self.especial(escolhida)

    def basica_normal(self,nome):
        if self.viavel(nome): return 'recusado:preterir-especial'
        return super().basica_normal(nome)

    def preparar(self,nome):
        c=self.corpos[nome]
        # Básica e gatilho escritos/compatíveis com a intenção são premissas.
        if not (self.momento=='turno' and c.em_campo and not c.atordoado and c.basica):
            return 'recusado:preparar'
        if self.viavel(nome): return 'recusado:preterir-especial'
        c.preparado='acao basica com gatilho legal'
        token=c.basica; c.basica=None; c.gastou=True
        self.eventos.append(f'basica:preparar:{nome}:{token}')
        return 'preparada'

    def executar_preparada(self,nome):
        c=self.corpos[nome]
        # Momento do gatilho e requisitos próprios são dados do roteiro.
        if not (c.preparado and c.em_campo and not c.atordoado and self.coletiva):
            return 'recusado:preparacao'
        self.reagir(nome,'preparacao')
        self.eventos.append(f'preparada:executada:{nome}')
        return 'executada'

    def estado_tarefa(self,nome,estado):
        c=self.corpos[nome]
        if estado=='impedida': c.impedimento_temporario=True
        elif estado=='retomada': c.impedimento_temporario=False
        elif estado=='cumprida': c.intencao=None; c.impedimento_temporario=False
        else: raise ValueError(estado)
        return estado

    def autopreservar(self,nome,opcao):
        c=self.corpos[nome]
        if self.momento!='turno' or not c.em_campo or (c.intencao and not c.impedimento_temporario):
            return 'recusado:autopreservacao'
        if opcao=='perseguir': return 'recusado:novo-objetivo'
        if self.viavel(nome): return 'recusado:preterir-especial'
        if opcao=='esquivar' and c.basica and not c.atordoado:
            c.basica=None; c.gastou=True
            self.eventos.append(f'basica:autopreservacao:{nome}')
            return 'esquivou'
        if opcao=='sair-de-perigo' and c.movimento:
            c.movimento=False
            return 'moveu'
        return 'recusado:recurso'

    def aplicar_momento(self,momento,tr_sucesso=()):
        # Efeitos previamente aplicados; nenhuma nova capacidade é concedida.
        for nome,c in self.corpos.items():
            for e in list(c.efeitos):
                if e.get('expira')==momento:
                    c.efeitos.remove(e)
                    continue
                if e.get('momento')!=momento: continue
                if e.get('exige_presenca') and not c.em_campo: continue
                c.ocorrencias.append(e['nome'])
                if e.get('leva_zero'): c.pv='zero'
            if momento=='fim' and c.atordoado and nome in tr_sucesso:
                c.atordoado=False
        return 'efeitos-resolvidos'

    def efeito_espacial(self,nome,fonte=None,aura=False,independente=False):
        # Posição e relação espacial em campo são premissas verdadeiras do caso.
        if independente: return True
        if not self.corpos[nome].em_campo: return False
        if aura and not self.corpos[fonte].em_campo: return False
        return True

    def queda(self,nome,regra_valida=None):
        if self.corpos[nome].pv!='zero': return 'nao-caiu'
        return regra_valida if regra_valida is not None else 'indeterminado:regra-de-queda'

# Rodar a mesma regressão com o modelo ampliado, não com uma cópia antiga do modelo.
base.Corpo=Corpo
base.Cena=Cena
V=base.verificar
cena=base.cena

def novos():
    s=cena(('A','B')); s.basica_normal('A'); s.corpos['A'].movimento=False
    s.recolher_apos_evento_legal('A'); s.abrir_turno()
    V('R2-01 ausente libera trava sem gerar basica ou Movimento',s,lambda:'conferido','conferido',
      lambda x:not x.corpos['A'].gastou and x.corpos['A'].basica is None and not x.corpos['A'].movimento)
    token=s.corpos['B'].basica
    V('R2-02 retorno posterior recebe saldo doador sem renovar Movimento',s,
      lambda:s.substituir_apos_evento_legal(['B'],['A'],'A','guardar'),'substituida',
      lambda x:x.corpos['A'].basica==token and not x.corpos['A'].movimento)
    s.abrir_turno()
    V('R2-03 fronteira em campo renova Movimento',s,lambda:'conferido','conferido',lambda x:bool(x.corpos['A'].movimento))
    s=cena(('A','B')); s.corpos['A'].movimento=.4; s.recolher_apos_evento_legal('A'); s.abrir_turno(); s.abrir_turno()
    V('R2-04 ausencia longa apaga basica velha e conserva so fracao restante',s,lambda:'conferido','conferido',
      lambda x:x.corpos['A'].basica is None and x.corpos['A'].movimento==.4)
    s.basica_normal('B')
    V('R2-05 retorno sem doador nao cria basica',s,
      lambda:s.substituir_apos_evento_legal(['B'],['A'],'A','guardar'),'substituida',
      lambda x:x.corpos['A'].basica is None and x.corpos['A'].movimento==.4)
    s=cena(); s.recolher_apos_evento_legal('A'); s.abrir_turno()
    V('R2-06 Movimento intacto e conservado sem duplicacao',s,lambda:'conferido','conferido',lambda x:x.corpos['A'].movimento is True)
    s=cena(); c=s.corpos['A']; c.efeitos=[{'nome':'beneficio','expira':'fim'},{'nome':'penalidade','expira':'fim'},{'nome':'sem prazo'}]
    s.recolher_apos_evento_legal('A')
    V('R2-07 beneficio e penalidade expiram fora sem limpar condicao sem prazo',s,
      lambda:s.aplicar_momento('fim'),'efeitos-resolvidos',lambda x:x.corpos['A'].efeitos==[{'nome':'sem prazo'}])
    s=cena(); c=s.corpos['A']; c.efeitos=[{'nome':'dano persistente','momento':'fim'}, {'nome':'beneficio recorrente','momento':'fim'}]
    c.atordoado=True; s.abrir_turno(); s.recolher_apos_evento_legal('A')
    V('R2-08 ausente resolve dano beneficio e TR sem restaurar basica',s,
      lambda:s.aplicar_momento('fim',('A',)),'efeitos-resolvidos',
      lambda x:x.corpos['A'].ocorrencias==['dano persistente','beneficio recorrente'] and not x.corpos['A'].atordoado and x.corpos['A'].basica is None)
    V('R2-09 reentrada nao repete ocorrencias',s,lambda:s.entrar_apos_evento_legal('A'),'entrou',
      lambda x:len(x.corpos['A'].ocorrencias)==2)
    s=cena(('A','B')); s.recolher_apos_evento_legal('A')
    V('R2-10 recolhida nao recebe area na posicao do invocador',s,lambda:s.efeito_espacial('A'),False,imutavel=True)
    V('R2-11 aura da recolhida nao alcanca campo',s,lambda:s.efeito_espacial('B','A',aura=True),False,imutavel=True)
    V('R2-12 efeito independente sobrevive retirada da fonte',s,lambda:s.efeito_espacial('B','A',independente=True),True,imutavel=True)
    s.corpos['A'].efeitos=[{'nome':'area dependente','momento':'fim','exige_presenca':True},{'nome':'persistente','momento':'fim'}]
    V('R2-13 ausencia distingue efeito de area de consequencia persistente',s,
      lambda:s.aplicar_momento('fim'),'efeitos-resolvidos',lambda x:x.corpos['A'].ocorrencias==['persistente'])
    s=cena(('A','B')); s.corpos['A'].efeitos=[{'nome':'dano','momento':'fim','leva_zero':True}]
    s.corpos['B'].efeitos=[{'nome':'dano','momento':'fim','leva_zero':True}]
    s.recolher_apos_evento_legal('B'); s.aplicar_momento('fim')
    V('R2-14 mesma queda em campo e fora quando regra fornecida',s,
      lambda:(s.queda('A','consequencia fornecida'),s.queda('B','consequencia fornecida')),
      ('consequencia fornecida','consequencia fornecida'),imutavel=True)
    V('R2-15 falta de regra de queda e explicitamente indeterminada',s,
      lambda:s.queda('B'),'indeterminado:regra-de-queda',imutavel=True)
    # A entrada seguinte é só um evento legal fornecido; não autoriza invocar a zero.
    V('R2-16 evento de entrada nao cura PV',s,lambda:s.entrar_apos_evento_legal('B'),'entrou',lambda x:x.corpos['B'].pv=='zero')
    s=cena(reservas=('B',))
    V('R2-17 Preparar gasta basica antes do gatilho',s,lambda:s.preparar('A'),'preparada',lambda x:x.corpos['A'].basica is None and x.corpos['A'].gastou and x.coletiva)
    V('R2-18 recolher preparada nao transfere basica gasta',s,
      lambda:s.substituir_apos_evento_legal(['A'],['B'],'B','guardar'),'substituida',
      lambda x:x.corpos['B'].basica is None and x.corpos['A'].preparado is None)
    s=cena(); s.preparar('A'); s.fechar_turno()
    V('R2-19 preparada executa com coletiva sem segunda basica',s,lambda:s.executar_preparada('A'),'executada',
      lambda x:not x.coletiva and x.corpos['A'].gastou and x.corpos['A'].preparado is None)
    s=cena(('A','B')); s.preparar('A'); s.preparar('B')
    V('R2-20 executar uma preparacao encerra as outras da mesma reserva',s,
      lambda:s.executar_preparada('A'),'executada',lambda x:all(c.preparado is None for c in x.corpos.values()))
    s=cena(('A','B')); s.preparar('A'); s.reagir('B')
    V('R2-21 resposta distinta perde preparacao',s,lambda:s.executar_preparada('A'),'recusado:preparacao',imutavel=True)
    s=cena(); s.preparar('A'); s.abrir_turno()
    V('R2-22 fronteira expira preparacao sem transportar credito',s,lambda:s.executar_preparada('A'),'recusado:preparacao',
      lambda x:x.corpos['A'].basica is not None,imutavel=True)
    s=cena(('A','B')); s.corpos['A'].alvo_valido=False; s.antecipar('A'); s.abrir_turno()
    s.corpos['B'].alvo_valido=False; s.antecipar('B'); s.fechar_turno(); s.consciente=False
    for c in s.corpos.values(): c.alvo_valido=True
    V('R2-23 jogador escolhe B entre ordens validas mesmo inconsciente',s,
      lambda:s.janela(['A','B'],'B'),'executada',lambda x:x.corpos['A'].ordem is not None and x.corpos['B'].ordem is None and not x.coletiva)
    V('R2-24 concorrente aguarda reserva sem perder ordem',s,
      lambda:s.janela(['A'],'A'),'espera:sem-elegivel',lambda x:x.corpos['A'].ordem is not None,imutavel=True)
    s=cena(); s.corpos['A'].alvo_valido=False; s.antecipar('A'); s.corpos['A'].alvo_valido=True
    V('R2-25 negar adiamento nao gasta nem cancela silenciosamente',s,
      lambda:s.janela(['A'],'A',adiar=True),'recusado:adiar-ordem-valida',imutavel=True)
    V('R2-26 oportunidade valida executa sem nova Padrao',s,lambda:s.janela(['A'],'A'),'executada',lambda x:not x.padrao and x.coletiva)
    s=cena(); s.corpos['A'].alvo_valido=False
    V('R2-27 emitir com basica disponivel e alvo fora do alcance',s,
      lambda:s.antecipar('A'),'ordenado',lambda x:not x.padrao and x.corpos['A'].basica is not None and x.corpos['A'].ordem is not None)
    V('R2-28 inviavel permite outra basica sem apagar ordem',s,lambda:s.basica_normal('A'),'basica',lambda x:x.corpos['A'].ordem is not None)
    s.corpos['A'].alvo_valido=True
    V('R2-29 basica gasta bloqueia especial mesmo com alvo agora valido',s,lambda:s.janela(['A'],'A'),'espera:sem-elegivel',imutavel=True)
    s=cena()
    V('R2-30 emissao totalmente viavel executa imediatamente',s,lambda:s.antecipar('A'),'executada',
      lambda x:x.corpos['A'].ordem is None and x.corpos['A'].gastou and not x.padrao)
    s=cena(); anterior=s.corpos['A'].intencao; s.estado_tarefa('A','impedida')
    V('R2-31 retomar tarefa nao gasta Bonus',s,lambda:s.estado_tarefa('A','retomada'),'retomada',
      lambda x:x.bonus and x.corpos['A'].intencao==anterior)
    V('R2-32 tarefa cumprida nao escolhe missao nova',s,lambda:s.estado_tarefa('A','cumprida'),'cumprida',lambda x:x.corpos['A'].intencao is None)
    V('R2-33 autopreservar gasta basica sem atribuir tarefa',s,lambda:s.autopreservar('A','esquivar'),'esquivou',
      lambda x:x.corpos['A'].basica is None and x.corpos['A'].intencao is None)
    V('R2-34 autopreservacao nao autoriza perseguir novo alvo',s,lambda:s.autopreservar('A','perseguir'),'recusado:novo-objetivo',imutavel=True)
    s=cena(reservas=('B',)); s.entrar_apos_evento_legal('B')
    V('R2-35 nova sem tarefa pode usar Movimento para perigo percebido',s,lambda:s.autopreservar('B','sair-de-perigo'),'moveu',
      lambda x:x.corpos['B'].basica is None and not x.corpos['B'].movimento)
    V('R2-36 sem basica na entrada nao recebe Esquivar gratis',s,lambda:s.autopreservar('B','esquivar'),'recusado:recurso',imutavel=True)
    s=cena(); s.comunica=False
    V('R2-37 canal conhecido indisponivel nao consome Padrao',s,lambda:s.antecipar('A'),'recusado:comando',imutavel=True)
    s=cena(); s.recepcao['A']=False
    V('R2-38 falha oculta gasta P sem criar ordem ou gastar basica',s,lambda:s.antecipar('A'),'falha:recepcao',
      lambda x:not x.padrao and x.corpos['A'].basica is not None and x.corpos['A'].ordem is None and x.coletiva)
    s.recepcao['A']=True
    V('R2-39 recuperar comunicacao nao entrega mensagem ou devolve P',s,lambda:s.antecipar('A'),'recusado:comando',imutavel=True)
    s=cena(('A','B')); s.recepcao['B']=False
    V('R2-40 recepcao parcial consome uma B e altera so destinataria apta',s,
      lambda:s.orientar(['A','B'],'proteger Y'),'recepcao-parcial',
      lambda x:not x.bonus and x.corpos['A'].intencao=='proteger Y' and x.corpos['B'].intencao=='guardar entrada')
    s.recepcao['B']=True
    V('R2-41 reenvio nao aproveita Bonus ja gasta',s,lambda:s.orientar(['B'],'proteger Y'),'recusado:orientacao',imutavel=True)
    s=cena(); s.corpos['A'].alvo_valido=False; s.antecipar('A'); s.recepcao['A']=False
    V('R2-42 ajuste nao recebido gasta B e preserva ordem',s,lambda:s.ajustar('A','especial B','Y'),'falha:recepcao',
      lambda x:not x.bonus and x.corpos['A'].ordem=={'capacidade':'especial A','alvo':'X'})
    V('R2-43 cancelamento nao recebido preserva ordem sem taxa',s,lambda:s.desistir('A'),'recusado:desistencia',imutavel=True)
    s.comunica=False; s.corpos['A'].alvo_valido=True
    V('R2-44 ordem previa executa sem comunicacao atual',s,lambda:s.janela(['A'],'A'),'executada',lambda x:x.corpos['A'].ordem is None)
    s=cena(reservas=('B',)); token=s.corpos['A'].basica; s.recepcao['B']=False
    V('R2-45 falha da intencao incluida nao desfaz troca ou transferencia',s,
      lambda:s.substituir_apos_evento_legal(['A'],['B'],'B','atacar X'),'substituida',
      lambda x:x.corpos['B'].em_campo and x.corpos['B'].basica==token and x.corpos['B'].intencao is None and x.bonus)
    s.recepcao['B']=True
    V('R2-46 orientacao posterior ao evento usa B normal',s,lambda:s.orientar(['B'],'atacar X'),'orientado',lambda x:not x.bonus)
    s=cena(); s.corpos['A'].alvo_valido=False; s.antecipar('A'); s.corpos['A'].alvo_valido=True; s.recepcao['A']=False
    V('R2-47 especial resolvida conserva intencao se nova orientacao falhar',s,
      lambda:s.especial('A','proteger Y'),'executada',lambda x:x.corpos['A'].intencao=='guardar entrada' and x.corpos['A'].gastou)
    s.recepcao['A']=True
    V('R2-48 apos evento nao ha credito de intencao gratuita',s,lambda:s.orientar(['A'],'proteger Y'),'orientado',lambda x:not x.bonus)
    s=cena(('A','B')); s.corpos['A'].alvo_valido=False; s.antecipar('A'); s.preparar('B'); s.fechar_turno(); s.corpos['A'].alvo_valido=True
    V('R2-49 especial concorrente usa coletiva e perde preparacao alheia',s,
      lambda:s.janela(['A'],'A'),'executada',lambda x:x.corpos['B'].preparado is None and x.corpos['B'].gastou)
    s=cena(('A','B')); s.corpos['A'].alvo_valido=False; s.antecipar('A'); s.preparar('B'); s.fechar_turno(); s.corpos['A'].alvo_valido=True
    V('R2-50 preparada escolhida conserva especial sem coletiva',s,
      lambda:s.executar_preparada('B'),'executada',lambda x:x.corpos['A'].ordem is not None and x.corpos['A'].basica is not None and not x.coletiva)


    s=cena(); s.recepcao['A']=False
    V('R2-51 comando imediato tambem exige recepcao e conserva gasto da tentativa',s,
      lambda:s.especial('A',imediata=True),'falha:recepcao',
      lambda x:not x.padrao and x.corpos['A'].basica is not None and x.corpos['A'].ordem is None)
    s=cena(); s.comunica=False
    V('R2-52 impossibilidade conhecida bloqueia tambem emissao imediata',s,
      lambda:s.especial('A',imediata=True),'recusado:comando',imutavel=True)
    s=cena(('A','B')); s.preparar('A'); s.fechar_turno()
    V('R2-53 Golpe do Guia usa coletiva e encerra preparacao',s,
      lambda:s.resposta_guia30('B'),'golpe-comum',lambda x:x.corpos['A'].preparado is None and x.corpos['B'].basica is not None)
    s.abrir_turno()
    V('R2-54 renovar coletiva nao recupera preparacao perdida',s,
      lambda:s.executar_preparada('A'),'recusado:preparacao',imutavel=True)
    s=cena(('A','B')); s.corpos['B'].intencao='proteger ponte'; s.recolher_apos_evento_legal('B'); s.recepcao['B']=False
    V('R2-55 corpo retornando conserva intencao propria se orientacao falhar',s,
      lambda:s.substituir_apos_evento_legal(['A'],['B'],'B','atacar X'),'substituida',
      lambda x:x.corpos['B'].intencao=='proteger ponte')
    s=cena(); s.corpos['A'].alvo_valido=False; s.antecipar('A'); s.corpos['A'].alvo_valido=True
    V('R2-56 nao gastar basica comum para preterir especial ja valida',s,
      lambda:s.basica_normal('A'),'recusado:preterir-especial',imutavel=True)
    s.corpos['A'].intencao=None
    V('R2-57 autopreservacao nao pretere especial valida',s,
      lambda:s.autopreservar('A','esquivar'),'recusado:preterir-especial',imutavel=True)
    s.consciente=False
    V('R2-58 escolha de resolucao inconsciente nao permite cancelar',s,
      lambda:s.janela(['A'],'A',desistir=True),'recusado:desistencia',imutavel=True)

if __name__=='__main__':
    base.executar()
    novos()
    p=Path(__file__).resolve()
    report={'tipo':'Ensaio simbolico de estados; nao demonstra equilibrio',
        'script_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
        'base_sha256':hashlib.sha256((p.parent/'base_r1.py').read_bytes()).hexdigest(),
        'regressao_r1_no_modelo_r2':49,'casos_novos':len(base.resultados)-49,
        'verificacoes':len(base.resultados),'passaram':sum(r['aprovado'] for r in base.resultados),
        'falharam':sum(not r['aprovado'] for r in base.resultados),
        'rejeicoes_ou_consultas_sem_mutacao':sum(r['imutavel_exigido'] for r in base.resultados),
        'resultados':base.resultados}
    (p.parent/'resultados.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    summary={k:v for k,v in report.items() if k!='resultados'}
    (p.parent/'execucao.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(summary,ensure_ascii=False,indent=2))
