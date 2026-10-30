"""Registrar leitura, mudanças e continuidade do lote 138."""
from pathlib import Path
import json,hashlib,os,re,math
A=Path(__file__).resolve().parent;R=A.parents[1];T=R/'06 - Redacao do Guia/edicao-integrada-136';E=R/'07 - Edicao de Leitura/edicao-integrada-136'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
files=['04-na-mesa-de-jogo.md','05-criar-uma-campanha.md','casos/82-testes-trabalho-em-grupo-e-iniciativa.md','casos/83-perceber-procurar-e-interpretar-sinais.md','casos/85-trajetorias-ferramentas-e-improvisacao.md','casos/22-quedas-e-socorro.md','casos/23-retirada-e-recuperacao.md','consultas/08-ficha-de-acordos-do-grupo.md','consultas/16-linha-de-continuidade.md','consultas/20-ficha-de-faccao.md','consultas/A2-conduzir-a-sessao.md','consultas/A4-retomar-a-missao.md']
rows=[]
for name in files:
 p=T/name;rows.append({'fonte':p.relative_to(R).as_posix(),'sha256':sha(p),'palavras_da_fonte':len(p.read_text().split()),'alcance':'Leitura completa; capítulos 4–5 em sequência, com segunda passagem de clareza; casos e folhas comparados às orientações que os citam.'})
old=json.loads((R/'04 - Planejamento/apoio-leitura-137/leitura-realizada.json').read_text())
p84=T/'casos/84-percursos-apoios-e-quedas.md';previous84=next(e for e in old['nucleo'] if e['fonte']==p84.relative_to(R).as_posix());assert sha(p84)==previous84['sha256']
save(A/'leitura-realizada.json',{'registro':138,'data':'2026-10-30','fontes_lidas':rows,'retomadas':[{'fonte':p84.relative_to(R).as_posix(),'sha256':sha(p84),'alcance':'Leitura integral realizada no registro 137, fonte inalterada; retomados os trechos de correnteza e saltos na conferência atual.'},{'fonte':(T/'07-personagens-e-tecnicas.md').relative_to(R).as_posix(),'sha256':sha(T/'07-personagens-e-tecnicas.md'),'alcance':'Trecho de revisão de escolha da Origem consultado; adicionada somente uma âncora. Não é leitura integral do capítulo 7.'},{'fonte':(T/'01-sua-primeira-missao.md').relative_to(R).as_posix(),'alcance':'Demonstração do anexo comparada aos casos 22–23; conserva duas rodadas e uma primeira queda.'}],'regras_consultadas':['Nível e patente iniciais','Testes: dificuldade e sucesso com custo','Testes de grupo e Ajudar','Influenciar','Cena e usos de habilidades','Socorro, Cicatrizes e Derrota e morte','Rever a Origem'],'fonte_tecnica':'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md','limite':'Leitura editorial das fontes e inspeção estrutural do HTML; não teste com pessoas, sessão de mesa ou revisão visual do futuro PDF completo.'})
save(A/'contas-conferidas.json',{'registro':138,'dificuldade_do_criador':{'base':8+4+2,'muito_dificil':8+4+2+2,'fixa_muito_dificil':18},'socorro_maximo_93_classe_3':{'aguentar':math.ceil(93/4),'primeiro_insistir':math.ceil(93/3),'segundo_insistir_com_teto':min(math.ceil(93/2),15*3)},'duas_quedas_maximo_23':{'primeiro_insistir':math.ceil(23/3),'segundo_insistir':math.ceil(23/2),'janela_apos_uma_sequela':3-1,'tratamento_segunda_queda':7+5},'recuperacao_pe_maximo_8_fora_de_ambiente_propicio':[max(1,math.floor(8*p)) for p in [.25,.15,.05]]+[0],'limite':'Contas dos exemplos existentes; não simulação de mesa nem alteração de parâmetros.'})
report=R/'04 - Planejamento/138-leitura-de-conducao-e-campanha.md'
report.write_text('''# Leitura de condução e campanha

Registro 138, 30 de outubro de 2026. Concluída a leitura contínua dos capítulos 4 e 5, com os casos e as folhas usados por eles. A segunda passagem conferiu clareza, títulos e ligação entre as explicações. Os ajustes estão na edição vigente, mantendo as regras e os parâmetros das fichas.

[Abrir a edição atual](<../07 - Edicao de Leitura/edicao-integrada-136/index.html>) · [Na mesa de jogo](<../07 - Edicao de Leitura/edicao-integrada-136/capitulo-04.html>) · [Criar uma campanha](<../07 - Edicao de Leitura/edicao-integrada-136/capitulo-05.html>) · [Histórico das alterações](apoio-leitura-138/alteracoes.json) · [Conferência](apoio-leitura-138/conferencia.json).

## Alcance da leitura

Na mesa de jogo foi lido da descrição inicial ao encerramento da sessão: testes, ajuda, negociação, investigação, improvisação, atenção ao grupo, combate, socorro e retirada. Criar uma campanha foi lido da sessão zero aos epílogos, incluindo vínculos, continuidade, facções e antagonistas.

Também foram lidos integralmente os casos de testes e iniciativa, percepção e pistas, ferramentas e improvisação, quedas e socorro e retirada e recuperação. Foram conferidas a folha de condução, a folha de retomada, a ficha de acordos, a linha de continuidade e a ficha de facção. Movimento, saltos e quedas, lido integralmente no registro 137, permanece inalterado; seus trechos de correnteza e salto foram retomados nesta comparação.

O trecho de revisão da Origem no capítulo 7 foi consultado para corrigir uma remissão. Esse capítulo recebeu somente uma âncora, sem alteração do texto visível; sua leitura integral continua pendente. O inventário `leitura-realizada.json` distingue fontes completas e trechos retomados.

## Correções que mudam a compreensão

### O exemplo do anexo

A consulta Quedas e socorro ainda dizia que a demonstração do anexo tinha três rodadas. A missão atual termina na segunda rodada. A descrição foi corrigida para duas; nenhuma ação, cura ou custo da missão foi modificado.

A mesma consulta apresentava a tabela de duas quedas como se fosse o roteiro do confronto principal. Agora ela identifica o caso como um exemplo separado, que reaproveita máximo 23 e Classe 1 para comparar socorro e derrota. A demonstração do anexo acompanha uma primeira queda. A remissão de Retirada e recuperação passou a apontar diretamente à versão com derrota do exemplo de duas quedas.

As diferenças são de identificação dos exemplos. A janela geral continua com três rodadas menos as Sequelas anteriores; a exigência de tratamento e os dois possíveis resultados da tabela permanecem iguais. A correção de “três” para “duas” não reduz a janela de socorro.

### Vínculos e cuidados

O capítulo de campanha prometia desenvolver os limites de revisão da Origem, mas o link retornava ao próprio parágrafo. A remissão agora abre o trecho correspondente em Personagens e técnicas. Esse parágrafo já explicava perda duradoura, revisão entre missões e preservação do pacote; recebeu uma âncora para ser acessado sem procurar dentro de outro assunto.

Retirada e recuperação também encaminhava o cuidado de corpos para uma seção genérica sobre vínculos. Agora aponta para Personagens e seus cuidados, onde estão as orientações pertinentes. As exceções de descanso e atendimento continuam nas fichas e no Livro de Regras 1.0.

### Dois personagens chamados Nilo

O intermediário que negocia um relatório, no capítulo 5, passa a se chamar **César**. Ele é um antagonista de um exemplo separado. Nilo continua sendo o personagem da Restrição corporal, com Rede Remota, no capítulo 7 e nos casos correspondentes. A troca evita sugerir que o mesmo personagem assumiu dois papéis sem explicação. O relatório, as alternativas da negociação e seu resultado possível são preservados. A âncora anterior do subtítulo continua funcionando.

## Clareza e consulta durante o jogo

No capítulo 4, Estabilizar e Derrota passaram a ter subtítulos próprios. O resultado da estabilização, o efeito de um dano posterior e a recuperação segura foram separados em parágrafos, sem retirar condições. Isso ajuda a encontrar a regra pertinente no momento do atendimento.

A explicação da dificuldade ligada ao criador agora diz o que fazer com a base calculada: aplicar o ajuste da dificuldade usando os valores do criador. O caso longo continua oferecendo a comparação numérica com a escala fixa. O exemplo de sucesso com custo apresenta primeiro a pesquisa de uma remessa; o leitor não precisa abrir o caso para saber qual tarefa está sendo tentada.

A abertura do capítulo oferece acesso ao anexo, à despedida e à folha curta de condução. A parte de encerramento aponta para Retomar a missão. Diferenças de expectativa levam à sessão zero; acordos de interpretação levam aos cuidados das Origens. Os atalhos usam folhas e explicações existentes, sem criar formulários repetidos.

## O que foi mantido

A condução continua partindo da intenção dos jogadores e dos fatos preparados. Uma falha conserva suas consequências, informação evidente pode ser fornecida sem rolagem e uma solução válida muda o obstáculo. Ajudar, teste coletivo e resultados individuais continuam distintos.

As orientações de ritmo preservam o espaço para conversas, a participação de quem ainda não falou e a alternância quando o grupo se separa. Cena, sessão e missão mantêm suas diferenças e os prazos das fichas. A pressão citada no conceito de cena acompanha o uso do Livro de Regras; mudar de cômodo não renova recursos.

A festa da ponte continua sendo um esboço de campanha, identificado assim na abertura. O capítulo ensina a ligar missões e desenvolver as propostas com o método de preparo, sem apresentar o esboço como aventura pronta com todas as fichas. A autonomia das facções depende de informação, meios e oportunidade. A oposição de César pode terminar por negociação ou por encontrar outra cópia do relatório.

A presença do Receptáculo continua interpretada pelo mestre mediante acordo com o jogador, com alternativas já explicadas. Guilda e campanha fechada continuam atendidas, preservando o foco do sistema em guilda. Não foi introduzida regra de treinamento, recurso de inimigo ou variante de recuperação.

## Conferência e preservação

São **18 registros de alteração em cinco fontes**: capítulos 4 e 5, dois casos de socorro e retirada e a âncora do capítulo 7. O histórico é reproduzido a partir das cópias anteriores. As 99 fontes da edição são comparadas; tabelas e números escritos em algarismos devem permanecer iguais. A correção da quantidade de rodadas descrita por extenso é declarada acima e conferida contra a demonstração.

As verificações estruturais percorrem os arquivos HTML, as âncoras, as imagens e os destinos das fontes Markdown. As âncoras anteriores dos cinco documentos modificados são preservadas, inclusive os dois subtítulos alterados. Há ainda conferências específicas para a descrição das duas rodadas, a independência do exemplo de duas quedas, o destino da revisão de Origem e a preservação do texto visível do capítulo 7. A contagem e o resultado final ficam em `conferencia.json`.

As contas retomadas estão em `contas-conferidas.json`: base 14 e dificuldade 16 na avaliação Muito difícil do criador; CD fixa 18 para a tarefa comum correspondente; tratamento 24, 31 e 45 nos três casos de máximo 93 e Classe 3; tratamento 8 e 12 nas duas quedas de máximo 23. Os totais continuam os das fontes. Não são uma avaliação nova de equilíbrio nem um teste de mesa.

O estado anterior das 99 fontes e dos cinco arquivos HTML modificados está em `apoio-leitura-138/antes/`. O manifesto é atualizado por união a partir de 4.531 entradas, admitindo somente cinco fontes, cinco documentos HTML e nove controles antigos alterados. As 104 fontes originais, as fontes históricas da revisão 135, os mapas, as fontes tipográficas e os PDFs anteriores ficam preservados. O salvamento desta entrega é local.

## Próxima tarefa

A abertura e os capítulos 1–5 já passaram pela leitura contínua desta fase. **Próximo: capítulo 6, Inimigos e perigos, junto de seus exemplos. Modelo: GPT-6.1 Sol; esforço alto.** Conferir o caminho entre escolher uma ameaça, interpretar sua ficha, usar energia ou recarga e preparar terreno e objetivos, mantendo as propostas experimentais como tais.

Depois seguem os capítulos 7–10 e as consultas ainda necessárias. O novo PDF completo será composto após essa passagem, com revisão visual de cada página e nova inspeção após as correções. Esta entrega é textual: não cria outro PDF parcial e não declara revisão visual do HTML no navegador. O bloqueio de abertura de arquivos locais continua respeitado. A revisão visual global e a comparação final com o livro base e os demais guias permanecem pendentes.
''')
config=json.loads((R/'04 - Planejamento/apoio-leitura-137/arquivos-do-lote.json').read_text());routes=json.loads((A/'destinos-alterados.json').read_text())
config.update(registro=138,base_manifesto=4531,relatorio=report.relative_to(R).as_posix(),fontes_alteradas=[row['fonte'] for row in routes],html_alterados=[(E/row['pagina']).relative_to(R).as_posix() for row in routes])
save(A/'arquivos-do-lote.json',config)
for rel in config['controles']:
 p=R/rel;b=A/'antes'/rel
 if not b.exists():b.parent.mkdir(parents=True,exist_ok=True);b.write_bytes(p.read_bytes())
 s=p.read_text()
 if '**Fila vigente - registro 138,' in s:continue
 s=s.replace('**Fila vigente - registro 137,','**Fila histórica - registro 137,',1)
 url=os.path.relpath(report,p.parent)
 banner=f'> **Fila vigente - registro 138, 30/10/2026:** leitura dos capítulos 4–5 e das consultas citadas concluída. [Registro e edição atual](<{url}>). Corrigidas a descrição do anexo em duas rodadas, a identificação do caso de duas quedas e referências de Origem e cuidados; socorro com subtítulos próprios. Tabelas e parâmetros preservados. **Próximo: capítulo 6 e exemplos de inimigos e perigos; GPT-6.1 Sol, esforço alto.** Depois, capítulos 7–10, consultas e PDF completo com revisão visual global. Use o gerador deste registro; não reaplique preparadores antigos sobre a edição atual.\n\n'
 first=s.index('\n\n');s=s[:first+2]+banner+s[first+2:]
 if rel.endswith('revisao-98/LEIA-ME.md'):
  s=re.sub(r'(?m)^\*\*Próxima tarefa:\*\* leitura contínua dos capítulos 4–5.*?\*\*GPT-6\.1 Sol, esforço alto\.\*\*', '**Próxima tarefa:** leitura contínua do capítulo 6 e de seus exemplos de inimigos e perigos. Depois, capítulos 7–10, demais consultas e revisão visual do PDF completo. **GPT-6.1 Sol, esforço alto.**',s)
 p.write_text(s)
print('Registro 138, inventário de leitura e continuidade atualizados.')
