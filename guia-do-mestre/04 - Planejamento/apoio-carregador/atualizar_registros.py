from pathlib import Path
import hashlib, json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent.parent
initial=json.loads((HERE/'estado-inicial.json').read_text(encoding='utf-8'))
def edit(rel, transform):
    p=ROOT/rel
    assert hashlib.sha256(p.read_bytes()).hexdigest()==initial['snapshot'][rel], f'Alteração concorrente: {rel}'
    old=p.read_text(encoding='utf-8')
    new=transform(old)
    assert new!=old,rel
    p.write_text(new,encoding='utf-8',newline='\n')
def replace_once(s,a,b):
    assert s.count(a)==1, (a[:80],s.count(a))
    return s.replace(a,b,1)
status='Encontro do Carregador desenvolvido no registro 66 e nas seções 62/63, com ficha experimental, terreno, contenção, transporte, respostas, encerramento e conversão opcional por Doma. Nenhuma economia universal, curva de dificuldade ou número novo foi aprovado.'
next_task='**Próxima tarefa recomendada:** preparar um perigo ambiental completo com escalada perceptível, intervenção e encerramento, distinguindo regras da R53 de eventuais propostas. Ampliar D12 além do terreno difícil antes de combiná-lo com um chefe. **GPT-6 Astra, esforço extra alto** para interações de tempo, dano, socorro e retirada; **GPT-6.1 Sol, esforço alto** para a prosa. Bestiário integral e treinamentos continuam adiados.'
record='[66 — Encontro do Carregador](66-encontro-do-carregador-de-sinos.md)'
for rel,version in [('04 - Planejamento/01-plano-completo-do-guia.md',56),('04 - Planejamento/02-decisoes-para-conversar.md',50)]:
    def transform(s,version=version):
        lines=s.splitlines()
        assert lines[2].startswith('Versão ')
        lines[2]=f'Versão {version}, de 23 de outubro de 2026. {status}'
        s='\n'.join(lines)+'\n'
        if version==56:
            old='Próximo: encontro curto com o Carregador de sinos e um elemento ambiental, com corpo experimental identificado, percurso, informação, respostas, retirada e encerramento. GPT-6 Astra, esforço extra alto; prosa GPT-6.1 Sol alto. Não altera o piloto, não atualiza o catálogo integral e não retoma treinamentos.'
            s=replace_once(s,old,'A continuação foi entregue no '+record+'. O recorte de habilidade acima permanece histórico; o caso completo está nas seções 62/63.')
            s+='\n## C04 — encontro completo do Carregador\n\n'+record+': recuperação do estado salvo, fonte R53 com hash idêntico ao anterior, corpo experimental 32 PV/16 Integridade, rotas, entulho, carga, conversões de ação e Doma com talento de transporte proposto. Conferência documental e aritmética; sem teste humano ou simulação integral de combate. Piloto e decisões preservados.\n\n'+next_task+'\n'
        else:
            s=replace_once(s,'**O que desenvolver e decidir depois:** aplicar os critérios em um encontro curto com o Carregador de sinos e um elemento ambiental, fechando corpo, percurso, respostas e continuidade. Desenvolver depois as referências numéricas de construção por nível, função e composição, com energia conforme as capacidades escolhidas.','**O que desenvolver e decidir depois:** o encontro do Carregador foi entregue no '+record+', com corpo, percurso, respostas, continuidade e Doma experimental. Desenvolver um perigo ambiental completo e, depois, referências numéricas de construção por nível, função e composição, com energia conforme as capacidades escolhidas.')
            a='**Próximo desenvolvimento:** definir critérios para feitiço conservado, adaptação de inimigo e habilidade própria.'
            start=s.index(a); end=s.index('\n\n## D12',start)
            s=s[:start]+'**Critérios entregues e aplicados:** registro 65 e seções 60/61 distinguem conservar, adaptar e criar; registro 66 e seções 62/63 aplicam o método num encontro completo. Informação de energia não obriga gasto em toda habilidade. As variantes N conservam custo-base 3 da Classe 1 e dispensam apenas o pagamento normal; base zero é formulação superada. Nenhuma economia universal foi escolhida. Não repetir a pergunta binária anterior como pendência obrigatória.'+s[end:]
            s=replace_once(s,'**Desenvolvimento atual:** a seção 58 oferece campos de sinais, área, gatilho, ritmo, resolução e intervenção. O registro 60 identifica os casos ambientais completos como pendentes; a ferramenta não conclui M017/M129 nem aprova dano, doença ou subsistema novo.','**Desenvolvimento atual:** a seção 58 oferece campos de sinais, área, gatilho, ritmo, resolução e intervenção. O registro 66 e as seções 62/63 acrescentam entulho com rotas medidas e custos publicados de terreno/arrasto. É um caso de terreno; perigos com escalada, dano ou doença continuam exigindo desenvolvimento próprio. Não conclui M017/M129 nem aprova subsistema novo.')
        return s
    edit(rel,transform)

def roadmap(s):
    start=s.index('**Próxima tarefa recomendada:** preparar um encontro curto')
    end=s.index('\n\n## Base das recomendações',start)
    return s[:start]+'**Entrega atual:** '+record+' e seções 62/63 completam o encontro autorizado. Conferências de regras, contas e preservação registradas; números e talento de Doma continuam experimentais.\n\n'+next_task+s[end:]
edit('04 - Planejamento/19-roteiro-pre-1-e-modelos.md',roadmap)

ret='''\n## Retomada — 23/10/2026: encontro do Carregador entregue no Windows

P66/G62/G63: encontro completo de recuperação de caixa, um Carregador e entulho, com duas rotas, informação, respostas, retirada, contenção posterior, socorro e Doma opcional. Produção em E:\\Claude\\Pesquisa de Campo - Mestragem; não é checkout. Os 699 arquivos de produção coincidiram com o commit f13e0814d5011b834c2f5a0059196c712c1a7742; README/SALVAMENTO pertencem à cópia de salvamento. Manifesto inicial209/209 íntegro.

R53 recuperada do GitHub no caminho histórico sistema/05-material/livro/ciclo-maldito-r41/LIVRO-COMPLETO.md. Conteúdo tem SHA256 7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d; cópia exata em apoio-carregador/fontes. Não presumir revisão pela pasta r41. Acervo original do conceito não recuperado; intenção retomada via P61/P65, cenário é elaboração nova. Índice e camada curada do Claude relidos, sem edição ou auditoria integral.

Inimigo experimental nível2, atributos3/1/3/1/1, 32PV/16I, 0PE, sem técnica, Defesa11/Bloquear2d10, +4/Pancada1d4+3, AgarrarTR12, um ataque. CorpoMédio72kg, duas mãos, carga8/tetoarrasto16. Terreno direto18m (6reg+6dif+6reg): andar24, arrastar42. Lateral24reg: andar24, arrastar48. Bônus pode virar Movimento: turno de Agarrar já ao alcance oferece18m, anda7,5m arrastando por custo16,5; próximo com Correr+Movimento+Bônus convertida27 paga25,5 restantes. Não prometer rodada gratuita de resgate. Entulho sem dano/teste automático; recuo aberto não encerra participação.

Doma preparada antes da tentativa: nível2 ou maior, derrota sem destruição, TREspírito+1 com penalidades atuais vs CD da rota; falha doma/sucesso exorciza. Limites inimigo32/excedente>16. Convertida14PV/7I, básica1d6, vagaespecial vazia, sem técnica/reserva; talento próprioCE1 Conduzir pelo chão ocupa escolha, um transportadoMédiooumenor/teto8/custos3ou4,5por1,5m. Não duplica8para16. Sem Bônus independente, sem recolhimento gratuito, retorno2PE/Bônus7PV sem curarI. Números/talento permanecem experimentais, sem escolha autoral nova.

Plano56/pauta50, roteiro, índice, referências e remissões atualizados. P06, piloto e protótipos preservados. QA apoio-carregador/verificacao.json; histórico antes-do-encontro. Somente salvamento local, sem commit/push. Conferência documental/aritmética, não sessão humana ou simulação integral de combate.
'''
edit('04 - Planejamento/apoio-piloto/RETOMADA.md',lambda s:s+ret+'\n'+next_task+'\n')

def index(s):
    old='Não há PE ou recarga obrigatórios para todos os especiais. Próximo: encontro curto com Carregador de sinos e elemento ambiental, **GPT-6 Astra, esforço extra alto**. A produção completa do Bestiário continua adiada.'
    new='Não há PE ou recarga obrigatórios para todos os especiais. O [encontro do Carregador](62-o-carregador-e-o-corredor-de-entulho.md) e sua [consulta com Doma](63-carregador-consulta-e-doma.md) aplicam o método com terreno, carga e ações da R53; novos valores e talento continuam experimentais. Próximo: perigo ambiental completo com escalada, intervenção e encerramento, **GPT-6 Astra, esforço extra alto**; prosa **GPT-6.1 Sol alto**. A produção completa do Bestiário continua adiada.'
    s=replace_once(s,old,new)
    return s+'\n## Encontro completo de C04\n\n[O Carregador e o corredor de entulho](62-o-carregador-e-o-corredor-de-entulho.md) ensina a preparar e conduzir uma disputa de objetivo, com respostas à contenção e duas rotas medidas. [Consulta e Doma](63-carregador-consulta-e-doma.md) reúne ficha experimental e conversão conhecida antes da aquisição. O [registro 66](<../04 - Planejamento/66-encontro-do-carregador-de-sinos.md>) identifica fontes, recuperação do estado salvo, conferências e limites.\n'
edit('06 - Redacao do Guia/LEIA-ME.md',index)

refs='''\n## Seções 62–63 — Encontro do Carregador e Doma

Fonte primária: [R53 recuperada do commit f13e081](<../04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md>), SHA-256 `7311979bdfc61bda1d2fd5113106f072edc7dd5b8a801a02779ada53fd13a81d`. O arquivo do GitHub estava em `sistema/05-material/livro/ciclo-maldito-r41/LIVRO-COMPLETO.md`; o nome histórico da pasta não corresponde à revisão do conteúdo. O [registro 66](<../04 - Planejamento/66-encontro-do-carregador-de-sinos.md>) relaciona regras consultadas e âncoras: ações/conversões, manobras/contenções, espaço, terreno, carga/arrasto, informação, amarras, Integridade, socorro, Doma, construção e campo de entidades.

Conceito retomado pelos registros61/65 e seções60/61. A base editorial original de Conceitos de Ideias para o sistema não foi recuperada nesta etapa; não houve alegação de releitura. Galpão, caixa, geografia, ficha32PV e comportamento específico são criação local. Talento de transporteCE1 da domada é proposta expressa, com limite8, sem duplicação pelo arrasto. Não se importaram números do Bestiário antigo ou de outro sistema.

Índice e camada curada da Pesquisa de Campo — Inimigos, Itens e Técnicas relidos, para localizar sinal, decisão e resposta. A pesquisa paralela não foi editada nem auditada integralmente. Conferências desta entrega são documentais, aritméticas e de preservação de arquivos; não equivalem a teste humano, simulação integral de combate ou validação de equilíbrio.
'''
edit('06 - Redacao do Guia/REFERENCIAS.md',lambda s:s+refs)
edit('06 - Redacao do Guia/60-montar-habilidades-de-inimigos.md',lambda s:replace_once(s,'Antes de colocar a criatura num encontro, complete sua ficha e o percurso; este recorte ensina uma capacidade, não entrega um novo inimigo pronto.','Este recorte ensina uma capacidade. Para a aplicação com ficha completa e percurso, consulte [O Carregador e o corredor de entulho](62-o-carregador-e-o-corredor-de-entulho.md) e sua [consulta com Doma](63-carregador-consulta-e-doma.md); os valores novos permanecem experimentais.'))
edit('06 - Redacao do Guia/61-ficha-de-habilidade-de-inimigo.md',lambda s:replace_once(s,'**Limite do exemplo:** ficha de uma capacidade. A criatura e o encontro completos ainda precisam de preparação; estes valores não formam uma tabela geral de construção.','**Limite deste formulário:** ficha de uma capacidade. A criatura e o encontro foram completados em [O Carregador e o corredor de entulho](62-o-carregador-e-o-corredor-de-entulho.md), com [consulta e Doma](63-carregador-consulta-e-doma.md). Os valores experimentais não formam uma tabela geral de construção.'))
print('8 registros atualizados; snapshot e controle de concorrência preservados.')
