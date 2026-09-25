"""Ensaio simbólico delimitado; não é motor completo nem teste de equilíbrio.

Acompanha uma oportunidade identificada por corpo/ciclo como fixture, sem
definir quantidade final de básicas. Pagamentos próprios são registrados por
evento e por disponibilidade fornecida à cena, sem escolher fonte/preço numérico.
Trocas/entradas são eventos legais fornecidos à bancada; seu custo não é zero:
ele permanece fora do modelo. Saída atravessando a fronteira, Preparar e regras
sem decisão suficiente não são implementadas.
"""

from dataclasses import dataclass, field, asdict
from pathlib import Path
import copy
import hashlib
import json


@dataclass
class Corpo:
    em_campo: bool = True
    ja_entrou: bool = True
    basica: str | None = None
    gastou: bool = False
    perdeu: bool = False
    movimento: bool = True
    intencao: str | None = "guardar entrada"
    ordem: dict | None = None
    alvo_valido: bool = True
    custos_disponiveis: bool = True
    atordoado: bool = False
    pv: str = "estado de PV fornecido à cena"
    condicoes: list = field(default_factory=list)
    usos: list = field(default_factory=list)


@dataclass
class Cena:
    corpos: dict = field(default_factory=dict)
    ciclo: int = 1
    padrao: bool = True
    bonus: bool = True
    pessoal: bool = True
    coletiva: bool = True
    consciente: bool = True
    comunica: bool = True
    momento: str = "turno"
    eventos: list = field(default_factory=list)
    guia_respondentes: list = field(default_factory=list)
    guia_reacao: bool = True

    def foto(self):
        return copy.deepcopy(asdict(self))

    def invariantes(self):
        fichas = [c.basica for c in self.corpos.values() if c.basica]
        assert len(fichas) == len(set(fichas)), "Básica duplicada entre corpos"
        for c in self.corpos.values():
            assert not (c.basica and (c.gastou or c.perdeu))
            assert c.em_campo or c.ordem is None, "Ordem guardada fora de campo"

    def abrir_turno(self):
        self.ciclo += 1
        self.momento = "turno"
        self.padrao = self.bonus = self.pessoal = self.coletiva = True
        for nome, c in self.corpos.items():
            if c.em_campo:
                c.gastou = c.perdeu = False
                c.basica = f"c{self.ciclo}:{nome}"
                c.movimento = True
                if c.atordoado:
                    c.basica = None
                    c.perdeu = True
        self.eventos.append("fronteira:inicio-comum")

    def fechar_turno(self, saem_de_atordoado=()):
        # Sucesso do TR é fornecido à cena, sem CD, rolagem ou regra de cura nova.
        for nome in saem_de_atordoado:
            self.corpos[nome].atordoado = False
        self.eventos.append("fronteira:fim-comum")
        self.momento = "fora"

    def rodada_global(self):
        self.eventos.append("rodada-global:sem-renovacao")

    def orientar(self, nomes, tarefa):
        # Destinatários já declarados dentro de X; não se escolhe X aqui.
        if not (self.momento == "turno" and self.consciente and self.comunica and self.bonus):
            return "recusado:orientacao"
        if not all(self.corpos[n].em_campo for n in nomes):
            return "recusado:fora-de-campo"
        self.bonus = False
        for n in nomes:
            self.corpos[n].intencao = tarefa
        self.eventos.append("B:orientacao")
        return "orientado"

    def converter_padrao(self):
        if self.momento != "turno":
            return "recusado:conversao-fora-turno"
        if not self.padrao:
            return "recusado:sem-padrao"
        if self.bonus:
            return "fora-do-recorte:conversao-com-bonus-ja-disponivel"
        self.padrao = False
        self.bonus = True
        self.eventos.append("P:convertida-em-B")
        return "convertido"

    def basica_normal(self, nome):
        c = self.corpos[nome]
        if self.momento != "turno":
            return "recusado:basica-fora-turno"
        if not c.em_campo or c.atordoado or not c.basica:
            return "recusado:basica"
        if not c.intencao:
            return "fora-do-recorte:sem-intencao"
        if c.ordem and c.alvo_valido and c.custos_disponiveis:
            return "fora-do-recorte:preterir-especial-ja-viavel"
        token = c.basica
        c.basica = None
        c.gastou = True
        self.eventos.append(f"basica:{nome}:{token}")
        return "basica"

    def antecipar(self, nome, capacidade="especial A", alvo="X"):
        c = self.corpos[nome]
        if not (self.momento == "turno" and self.consciente and self.comunica and self.padrao):
            return "recusado:comando"
        if not c.em_campo:
            return "recusado:fora-de-campo"
        if c.ordem:
            return "recusado:ja-tem-ordem"
        if not c.gastou:
            return "fora-do-recorte:antecipar-sem-basica-ja-usada"
        self.padrao = False
        c.ordem = {"capacidade": capacidade, "alvo": alvo}
        self.eventos.append(f"P:ordem:{nome}")
        return "ordenado"

    def ajustar(self, nome, capacidade, alvo):
        c = self.corpos[nome]
        if not (self.momento == "turno" and self.consciente and self.comunica and self.bonus and c.ordem):
            return "recusado:ajuste"
        self.bonus = False
        c.ordem = {"capacidade": capacidade, "alvo": alvo}
        self.eventos.append(f"B:ajuste:{nome}")
        return "ajustado"

    def desistir(self, nome):
        c = self.corpos[nome]
        if not (self.consciente and self.comunica and c.ordem):
            return "recusado:desistencia"
        c.ordem = None
        self.eventos.append(f"ordem:desistiu:{nome}")
        return "desistiu"

    def especial(self, nome, nova_intencao=None, sucesso=True, imediata=False):
        c = self.corpos[nome]
        if self.momento == "resolvendo":
            return "recusado:resolucao-em-andamento"
        if imediata:
            if not (self.momento == "turno" and self.consciente and self.comunica and self.padrao):
                return "recusado:comando-imediato"
        elif not c.ordem:
            return "recusado:sem-ordem"
        if not c.em_campo or c.atordoado or not c.basica:
            return "espera:atuacao"
        if not c.alvo_valido or not c.custos_disponiveis:
            return "espera:requisitos"
        if self.momento == "fora" and not self.coletiva:
            return "espera:coletiva"
        # As pré-condições foram verificadas antes de consumir os recursos.
        if imediata:
            self.padrao = False
            self.eventos.append(f"P:imediata:{nome}")
        if self.momento == "fora":
            self.coletiva = False
            self.eventos.append(f"R:coletiva:especial:{nome}")
        self.eventos.append(f"basica:especial:{nome}:{c.basica}")
        self.eventos.append(f"custo-proprio:ativacao:{nome}")
        c.basica = None
        c.gastou = True
        c.ordem = None
        self.eventos.append(f"resultado:{nome}:{'sucesso' if sucesso else 'falha'}")
        if nova_intencao and self.consciente and self.comunica:
            c.intencao = nova_intencao
            self.eventos.append(f"intencao:apos-resultado:{nome}")
        return "executada"

    def reagir(self, nome, fonte="capacidade escrita elegivel"):
        c = self.corpos[nome]
        if not c.em_campo or c.atordoado or not self.coletiva:
            return "recusado:reacao"
        self.coletiva = False
        self.eventos.append(f"R:coletiva:{fonte}:{nome}")
        return "respondeu"

    def resposta_guia30(self, nome):
        # Abertura, alvo, consentimento, alcance, capacidade e cadeia válidos
        # são premissas do caso; não se simula a ficha completa do Guia.
        if nome in self.guia_respondentes or len(self.guia_respondentes) >= 2:
            return "recusado:limite-guia"
        if not self.guia_respondentes and not self.guia_reacao:
            return "recusado:reacao-guia"
        r = self.reagir(nome, "Golpe comum do Guia")
        if r != "respondeu":
            return r
        if not self.guia_respondentes:
            self.guia_reacao = False
        self.guia_respondentes.append(nome)
        return "golpe-comum"

    def substituir_apos_evento_legal(self, saidas, entradas, direta, tarefa):
        # Sem preço de troca: o evento e sua legalidade são dados de entrada.
        if not all(self.corpos[n].em_campo for n in saidas):
            return "recusado:saida-invalida"
        if direta not in entradas or any(self.corpos[n].em_campo for n in entradas):
            return "recusado:entrada-invalida"
        destino = self.corpos[direta]
        fonte = next((self.corpos[n] for n in saidas if self.corpos[n].basica), None)
        if fonte and not (destino.gastou or destino.perdeu or destino.basica):
            destino.basica = fonte.basica
            fonte.basica = None
        for n in saidas:
            self.corpos[n].em_campo = False
            self.corpos[n].ordem = None
        for n in entradas:
            c = self.corpos[n]
            c.em_campo = True
            if not c.ja_entrou:
                c.movimento = True
                c.ja_entrou = True
        destino.intencao = tarefa
        self.eventos.append("evento-legal:substituicao-sem-custo-modelado")
        return "substituida"

    def entrar_apos_evento_legal(self, nome):
        c = self.corpos[nome]
        if c.em_campo:
            return "recusado:ja-em-campo"
        c.em_campo = True
        if not c.ja_entrou:
            c.ja_entrou = True
            c.movimento = True
        self.eventos.append("evento-legal:entrada-sem-custo-modelado")
        return "entrou"


def cena(nomes=("A",), reservas=()):
    s = Cena()
    for n in nomes:
        s.corpos[n] = Corpo(basica=f"c1:{n}")
    for n in reservas:
        s.corpos[n] = Corpo(em_campo=False, ja_entrou=False, movimento=False, intencao=None)
    return s


resultados = []


def verificar(nome, s, operacao, esperado, predicado=lambda _: True, imutavel=False):
    antes = s.foto()
    obtido = operacao()
    s.invariantes()
    depois = s.foto()
    ok = obtido == esperado and bool(predicado(s)) and (not imutavel or antes == depois)
    resultados.append(dict(caso=nome, esperado=esperado, obtido=obtido,
                           aprovado=ok, imutavel_exigido=imutavel,
                           antes=antes, depois=depois))
    assert ok, nome


def pronta(nomes=("A",), reservas=()):
    s = cena(nomes, reservas)
    assert s.basica_normal("A") == "basica"
    assert s.antecipar("A") == "ordenado"
    return s


def executar():
    s = cena()
    verificar("01 especial imediata muda intencao depois do resultado", s,
        lambda: s.especial("A", "focar Y", imediata=True), "executada",
        lambda x: not x.padrao and x.bonus and x.coletiva and x.corpos['A'].intencao == 'focar Y'
        and x.eventos.index('resultado:A:sucesso') < x.eventos.index('intencao:apos-resultado:A'))
    verificar("02 especial nao deixa basica extra", s, lambda: s.basica_normal('A'),
        'recusado:basica', imutavel=True)
    s = pronta()
    verificar("03 ordem paga P mas nao paga capacidade ao emitir", s, lambda: 'conferido', 'conferido',
        lambda x: not x.padrao and x.corpos['A'].ordem and not any(e.startswith('custo-proprio') for e in x.eventos))
    t = pronta(); t.corpos['A'].alvo_valido = False; t.abrir_turno()
    verificar("04 segunda ordem na mesma criatura nao forma fila", t,
        lambda: t.antecipar('A'), 'recusado:ja-tem-ordem', imutavel=True)
    s.fechar_turno()
    verificar("05 coletiva nao substitui basica ja gasta", s, lambda: s.especial('A'),
        'espera:atuacao', imutavel=True)
    s.rodada_global()
    verificar("06 rodada global nao renova basica", s, lambda: s.especial('A'),
        'espera:atuacao', imutavel=True)
    s.corpos['A'].alvo_valido = False
    s.abrir_turno()
    s.fechar_turno()
    s.momento = 'resolvendo'
    verificar("07 especial nao interrompe resolucao", s, lambda: s.especial('A'),
        'recusado:resolucao-em-andamento', imutavel=True)
    s.momento = 'fora'; s.corpos['A'].alvo_valido = True
    verificar("08 fora do turno paga basica e coletiva sem nova P", s,
        lambda: s.especial('A'), 'executada',
        lambda x: x.padrao and x.pessoal and not x.coletiva and x.corpos['A'].gastou
        and x.corpos['A'].ordem is None and sum(e.startswith('P:ordem') for e in x.eventos) == 1)
    s = pronta(); s.corpos['A'].alvo_valido = False; s.abrir_turno()
    verificar("09 alvo invalido conserva ordem e recursos", s, lambda: s.especial('A'),
        'espera:requisitos', imutavel=True)
    verificar("10 outra basica enquanto especial inviavel mantem ordem", s,
        lambda: s.basica_normal('A'), 'basica', lambda x: x.corpos['A'].ordem is not None)
    s.corpos['A'].alvo_valido = True; s.fechar_turno()
    verificar("11 alvo surge depois de basica gasta e ordem aguarda", s,
        lambda: s.especial('A'), 'espera:atuacao', imutavel=True)
    s.abrir_turno()
    verificar("12 ordem sobrevive a mais de uma fronteira", s, lambda: s.especial('A'),
        'executada', lambda x: x.padrao and x.coletiva)
    s = pronta(); s.corpos['A'].custos_disponiveis = False; s.abrir_turno()
    verificar("13 recursos proprios insuficientes nao consomem atuacao", s,
        lambda: s.especial('A'), 'espera:requisitos', imutavel=True)
    verificar("14 Bonus ajusta capacidade e alvo preservando P", s,
        lambda: s.ajustar('A', 'especial B', 'Y'), 'ajustado',
        lambda x: x.padrao and not x.bonus and x.corpos['A'].ordem == {'capacidade':'especial B','alvo':'Y'})
    s.corpos['A'].custos_disponiveis = True
    verificar("15 falhar na execucao encerra ordem e mantem gastos", s,
        lambda: s.especial('A', sucesso=False), 'executada',
        lambda x: x.corpos['A'].ordem is None and x.corpos['A'].gastou
        and 'custo-proprio:ativacao:A' in x.eventos and 'resultado:A:falha' in x.eventos)
    s = pronta()
    verificar("16 desistir nao devolve P anterior", s, lambda: s.desistir('A'), 'desistiu',
        lambda x: not x.padrao and x.corpos['A'].ordem is None and x.coletiva and x.bonus)
    s = pronta(); s.corpos['A'].alvo_valido = False; s.abrir_turno(); s.fechar_turno(); s.corpos['A'].alvo_valido = True
    token = s.corpos['A'].basica
    verificar("17 desistir na janela valida preserva recursos da execucao", s,
        lambda: s.desistir('A'), 'desistiu',
        lambda x: x.corpos['A'].basica == token and x.coletiva and x.padrao and x.bonus
        and not any(e.startswith('custo-proprio') for e in x.eventos))
    s = pronta(); s.consciente = False; s.abrir_turno()
    verificar("18 inconsciente nao ajusta ordem", s, lambda: s.ajustar('A','especial B','Y'),
        'recusado:ajuste', imutavel=True)
    verificar("19 inconsciente nao emite cancelamento", s, lambda: s.desistir('A'),
        'recusado:desistencia', imutavel=True)
    verificar("20 ordem previa executa com usuario inconsciente e conserva intencao", s,
        lambda: s.especial('A', 'nova tarefa'), 'executada',
        lambda x: x.corpos['A'].intencao == 'guardar entrada' and 'custo-proprio:ativacao:A' in x.eventos)
    s = pronta(reservas=('B',)); s.corpos['A'].alvo_valido = False; s.abrir_turno()
    token = s.corpos['A'].basica; s.corpos['A'].movimento = False
    verificar("21 troca encerra ordem e transmite saldo sem copiar", s,
        lambda: s.substituir_apos_evento_legal(['A'],['B'],'B','atacar Y'), 'substituida',
        lambda x: x.corpos['A'].ordem is None and x.corpos['A'].basica is None
        and x.corpos['B'].basica == token and x.corpos['B'].movimento and x.bonus)
    verificar("22 substituta executa basica recebida", s, lambda: s.basica_normal('B'), 'basica')
    verificar("23 retorno nao recupera ficha transmitida nem Movimento gasto", s,
        lambda: s.substituir_apos_evento_legal(['B'],['A'],'A','atacar Z'), 'substituida',
        lambda x: x.corpos['A'].basica is None and not x.corpos['A'].movimento and x.corpos['A'].ordem is None)
    s = pronta(reservas=('B',))
    verificar("24 cancelar ordem por troca nao devolve basica anterior executada", s,
        lambda: s.substituir_apos_evento_legal(['A'],['B'],'B','atacar Y'), 'substituida',
        lambda x: x.corpos['B'].basica is None and not x.padrao)
    s = cena(reservas=('B','C')); token=s.corpos['A'].basica
    verificar("25 uma saida varias entradas so uma recebe saldo e intencao", s,
        lambda: s.substituir_apos_evento_legal(['A'],['B','C'],'B','atacar Y'), 'substituida',
        lambda x: x.corpos['B'].basica == token and x.corpos['C'].basica is None
        and x.corpos['C'].intencao is None and x.corpos['B'].movimento and x.corpos['C'].movimento)
    s = cena(('A','B'),('C',)); tokens={c.basica for c in s.corpos.values() if c.basica}
    verificar("26 varias saidas nao fundem basicas na substituta", s,
        lambda: s.substituir_apos_evento_legal(['A','B'],['C'],'C','atacar Y'), 'substituida',
        lambda x: x.corpos['C'].basica in tokens and sum(bool(c.basica) for c in x.corpos.values()) == 2)
    s = cena(('A','B')); s.basica_normal('B'); s.corpos['B'].em_campo=False
    verificar("27 corpo que ja agiu nao recebe basica por rotacao", s,
        lambda: s.substituir_apos_evento_legal(['A'],['B'],'B','atacar Y'), 'substituida',
        lambda x: x.corpos['B'].basica is None and x.corpos['B'].gastou)
    s = cena(reservas=('B',)); s.corpos['A'].pv='ferido'; s.corpos['A'].condicoes=['Lento']; s.corpos['A'].usos=['uso por cena gasto']
    s.substituir_apos_evento_legal(['A'],['B'],'B','guardar')
    verificar("28 retorno conserva PV condicoes usos", s,
        lambda: s.substituir_apos_evento_legal(['B'],['A'],'A','guardar'), 'substituida',
        lambda x: x.corpos['A'].pv=='ferido' and x.corpos['A'].condicoes==['Lento'] and x.corpos['A'].usos==['uso por cena gasto'])
    s = cena(reservas=('B',)); s.coletiva=False
    verificar("29 entrada adicional fornece Movimento mas nao basica coletiva ou intencao", s,
        lambda: s.entrar_apos_evento_legal('B'), 'entrou',
        lambda x: x.corpos['B'].movimento and x.corpos['B'].basica is None
        and x.corpos['B'].intencao is None and not x.coletiva)
    verificar("30 primeira intencao adicional usa Bonus sem renovar basica", s,
        lambda: s.orientar(['B'],'guardar entrada'), 'orientado',
        lambda x: not x.bonus and x.padrao and x.corpos['B'].basica is None and not x.coletiva)
    verificar("31 conversao P para B nao cria P", s, lambda: s.converter_padrao(), 'convertido',
        lambda x: not x.padrao and x.bonus)
    verificar("32 orientacao comum pode incluir entrante e outra entidade", s,
        lambda: s.orientar(['A','B'],'recuar'), 'orientado',
        lambda x: all(c.intencao=='recuar' for c in x.corpos.values()) and not x.bonus)
    s = pronta(('A','B')); s.corpos['A'].atordoado=True; s.abrir_turno()
    verificar("33 Atordoado retira basica e preserva ordem", s, lambda: s.especial('A'),
        'espera:atuacao', lambda x: x.corpos['A'].perdeu and x.corpos['A'].ordem is not None, imutavel=True)
    verificar("34 criatura Atordoada nao gasta coletiva ao tentar reagir", s,
        lambda: s.reagir('A'), 'recusado:reacao', imutavel=True)
    verificar("35 outra criatura apta usa coletiva", s, lambda: s.reagir('B'), 'respondeu')
    s.fechar_turno(('A',))
    verificar("36 fim de Atordoado nao devolve basica nem reacao ja gasta", s,
        lambda: s.especial('A'), 'espera:atuacao',
        lambda x: not x.corpos['A'].atordoado and x.corpos['A'].basica is None and not x.coletiva, imutavel=True)
    s = cena(); s.corpos['A'].atordoado=True; s.abrir_turno(); s.fechar_turno(('A',))
    verificar("37 TR ao fim permite reagir sem devolver basica", s,
        lambda: s.reagir('A'), 'respondeu', lambda x: x.corpos['A'].basica is None)
    s = pronta(('A','B'))
    for c in s.corpos.values(): c.alvo_valido = False
    s.abrir_turno(); s.basica_normal('B'); s.antecipar('B'); s.abrir_turno(); s.fechar_turno()
    for c in s.corpos.values(): c.alvo_valido = True
    verificar("38 primeira de duas ordens usa coletiva", s, lambda: s.especial('A'), 'executada')
    verificar("39 segunda ordem aguarda sem gastar sua basica", s, lambda: s.especial('B'),
        'espera:coletiva', lambda x: x.corpos['B'].ordem is not None and x.corpos['B'].basica is not None, imutavel=True)
    s.abrir_turno()
    verificar("40 segunda ordem executa apos renovacao sem nova P", s, lambda: s.especial('B'),
        'executada', lambda x: x.padrao and x.coletiva)
    s = cena(('A','B')); s.basica_normal('A'); s.fechar_turno()
    verificar("41 Golpe do Guia depois de basica nao a recupera", s,
        lambda: s.resposta_guia30('A'), 'golpe-comum', lambda x: x.corpos['A'].basica is None and x.corpos['A'].gastou)
    verificar("42 Guia30 sem renovacao nao paga segunda resposta", s,
        lambda: s.resposta_guia30('B'), 'recusado:reacao', imutavel=True)
    s.abrir_turno(); token=s.corpos['B'].basica
    verificar("43 Guia30 com renovacao permite outra criatura responder", s,
        lambda: s.resposta_guia30('B'), 'golpe-comum',
        lambda x: x.corpos['B'].basica==token and not x.guia_reacao and x.guia_respondentes==['A','B'])
    verificar("44 Guia30 nao concede terceira resposta", s,
        lambda: s.resposta_guia30('A'), 'recusado:limite-guia', imutavel=True)
    s = pronta(); s.corpos['A'].alvo_valido=False; s.abrir_turno(); s.fechar_turno()
    verificar("45 intencao persistente nao autoriza basica comum fora do turno", s,
        lambda: s.basica_normal('A'), 'recusado:basica-fora-turno', imutavel=True)
    verificar("46 Bonus de ajuste nao recebe janela fora do turno", s,
        lambda: s.ajustar('A','especial B','Y'), 'recusado:ajuste', imutavel=True)
    verificar("47 redirecionamento comum respeita turno", s,
        lambda: s.orientar(['A'],'atacar Y'), 'recusado:orientacao', imutavel=True)
    verificar("48 conversao comum respeita turno", s,
        lambda: s.converter_padrao(), 'recusado:conversao-fora-turno', imutavel=True)
    verificar("49 emissao do comando respeita turno", s,
        lambda: s.antecipar('A'), 'recusado:comando', imutavel=True)


if __name__ == '__main__':
    executar()
    p=Path(__file__).resolve()
    report={
        'tipo':'Ensaio simbolico de procedimentos; nao prova de equilibrio',
        'script_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
        'cenarios_verificados':len(resultados),
        'aprovados':sum(r['aprovado'] for r in resultados),
        'falhas':sum(not r['aprovado'] for r in resultados),
        'tentativas_sem_mutacao_verificadas':sum(r['imutavel_exigido'] for r in resultados),
        'resultados':resultados,
    }
    (p.parent/'resultados.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    summary={k:v for k,v in report.items() if k!='resultados'}
    (p.parent/'execucao.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(summary,ensure_ascii=False,indent=2))
