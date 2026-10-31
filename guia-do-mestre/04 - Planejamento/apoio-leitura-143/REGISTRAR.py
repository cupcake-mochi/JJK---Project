"""Registrar a leitura de Jogar em guilda e deixar a próxima etapa explícita."""
from pathlib import Path
import json,hashlib,os,re
A=Path(__file__).resolve().parent;R=A.parents[1];T=R/'06 - Redacao do Guia/edicao-integrada-136';E=R/'07 - Edicao de Leitura/edicao-integrada-136'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
assert not json.loads((A/'conferencia.json').read_text())['falhas']
names=['10-jogar-em-guilda.md','casos/79-o-po-na-sala-de-conservacao.md','casos/81-passar-a-missao-entre-mestres.md','consultas/12-registro-de-descobertas.md','consultas/16-linha-de-continuidade.md','consultas/24-registro-de-estado-e-socorro.md','consultas/32-ficha-de-avaliacao-de-capacidade.md','consultas/38-ficha-de-projeto-e-entrega.md','consultas/40-registro-de-dedicacao-por-ficha.md','consultas/42-registro-de-pactos-e-promessas.md','consultas/44-registro-de-aquisicao-e-estado-de-entidade.md','consultas/A4-retomar-a-missao.md','consultas/A4-exemplo-sala-de-conservacao.md','consultas/LEIA-ME.md']
changed={row['fonte'] for row in json.loads((A/'destinos-alterados.json').read_text())};rows=[]
for name in names:
 p=T/name;rel=p.relative_to(R).as_posix();rows.append({'fonte':rel,'sha256':sha(p),'palavras_da_fonte':len(p.read_text().split()),'alcance':'Leitura completa e segunda leitura completa depois dos ajustes.' if rel in changed else 'Leitura completa e comparação com o capítulo, sem mudança neste lote.'})
primary=R/'04 - Planejamento/apoio-carregador/fontes/LIVRO-COMPLETO-R53.md'
save(A/'leitura-realizada.json',{'registro':143,'data':'2026-10-30','fontes_lidas':rows,'trechos_comparados':[{'fonte':(T/'08-entre-missoes.md').relative_to(R).as_posix(),'sha256':sha(T/'08-entre-missoes.md'),'alcance':'Seção 8.2: ciclo, entrada, saldo e trabalho ainda em conferência; o capítulo já foi lido no registro 141.'}],'fonte_tecnica_preservada':primary.relative_to(R).as_posix(),'sha256_fonte_tecnica':sha(primary),'limite':'Leitura editorial, comparação com capítulos e registros anteriores e contas selecionadas. Não é teste com jogadores nem revisão visual do PDF final.'})
report=R/'04 - Planejamento/143-leitura-de-jogo-em-guilda.md'
report.write_text('''# Leitura de Jogar em guilda

Registro 143, 30 de outubro de 2026. Concluída a leitura contínua do capítulo 10 com os exemplos de passagem entre mestres e as folhas que ele indica. O texto mantém o foco na guilda e explica a aplicação dos mesmos cuidados em campanhas fechadas.

[Abrir a edição atual](<../07 - Edicao de Leitura/edicao-integrada-136/index.html>) · [Jogar em guilda](<../07 - Edicao de Leitura/edicao-integrada-136/capitulo-10.html>) · [Alterações](apoio-leitura-143/alteracoes.json) · [Conferência](apoio-leitura-143/conferencia.json) · [Contas selecionadas](apoio-leitura-143/contas-conferidas.json).

## Alcance da leitura

Foram lidos por inteiro **14 arquivos**: o capítulo, O pó na sala de conservação, Passar a missão entre mestres e onze consultas. As consultas abrangem descobertas, continuidade, estado e socorro, avaliação de capacidade, projeto e entrega, dedicação por ficha, Pactos e Promessas, aquisição e estado de entidade, folha de retomada, seu exemplo preenchido e orientação para escolher uma folha.

As duas fontes alteradas passaram por outra leitura completa depois dos ajustes. A seção de tempo do capítulo Entre missões foi consultada para comparar o resumo com as definições já revistas no registro 141. Essa consulta não é contada como nova leitura integral daquele capítulo. O inventário de leitura identifica arquivos, hashes e alcance.

## Ajustes aplicados

| Dificuldade | Ajuste |
|---|---|
| O resumo do capítulo dizia que o saldo valia no ciclo seguinte, sem repetir quais horas podiam passar | Explicita que somente as horas novas e livres são transferidas. Abertura da folha de dedicação passa a usar a mesma distinção. |
| Horas confirmadas, reservadas e livres eram citadas sem acesso direto à definição | A menção leva à seção Trabalho ainda em conferência, em Entre missões. |
| A orientação sobre aceitar uma tarefa era indireta | Agora diz para registrar alguém como responsável somente após a pessoa aceitar. |

São **quatro registros de alteração em duas fontes**, com duas páginas HTML atualizadas. Todos os números e todas as linhas das tabelas foram preservados. Não foi criada uma regra nova.

## Calendário e registros

A concessão continua sendo por ficha, com 28 horas novas em sete dias; XP semanal continua por jogador e na conclusão da missão. Ciclo administrativo, calendário vivido, jornada de Overtime, prazos de Pactos e rodadas de socorro permanecem separados. Campanhas fechadas não precisam adotar o ciclo da guilda para usar os cuidados de continuidade.

Horas reservadas continuam vinculadas ao trabalho pendente e não entram também no saldo livre. O progresso confirmado não expira com as horas restantes. Foram reconferidos os seis registros de Rina e Mei em três ciclos, a entrada proporcional e a abertura com saldo e conferência pendente. O ajuste da abertura do formulário concorda com seu fechamento, sem mudar elegibilidade, prazos ou quantidade.

As folhas mantêm a mesma orientação sobre quem recebe a informação, onde está o estado atual, o que aconteceu e o que ainda é intenção. Uma decisão local não se torna regra comum, e uma pessoa que mantém os arquivos não recebe autoridade adicional por isso. Nenhuma tarefa foi atribuída a alguém neste lote.

## Passagem na sala de conservação

O capítulo, o caso completo, a ficha do perigo e a retomada preenchida concordam no ponto da interrupção: toda a fase ambiental 1 terminou; Mei 2 é o próximo turno. Ela está em A12, com vida zero, consciente por Insistir, ainda sem a nova Sequela e com três rodadas de janela. Akira está em B0. Não houve uma volta completa ao ponto de contagem.

Foram reconferidos o tratamento de 15, seu teto de 30, o percurso de 18 m, as rolagens de saída, os quatro dados de Sutura e o saldo de 24 PE de Akira. O tratamento também recupera vida, e a Sequela entra no momento da recuperação. O fim da nuvem não encerra Envenenado. A nota de retomada preserva a urgência e deixa a decisão com a jogadora.

A transferência de mestre não concede ação, descanso, recuperação, recompensa ou passagem automática do tempo da cena. Não se acrescentou a causa técnica que o grupo não descobriu. O encerramento das recompensas continua pendente dos dados que o exemplo não fornece. A conferência aritmética não mede equilíbrio de perigo ou experiência de jogo.

## Conferência e salvamento

Os ajustes foram reproduzidos contra as 99 fontes anteriores. A conferência compara números e tabelas, verifica destinos e âncoras Markdown, percorre as 99 páginas HTML e suas imagens e preserva as âncoras anteriores. Também conserva a posição do complemento de ideias no capítulo 3. Os resultados estão em `conferencia.json`.

A edição continua nas pastas `edicao-integrada-136`. Use o gerador de `apoio-leitura-143`; não reaplique preparadores antigos sobre as fontes vigentes. As cópias anteriores foram guardadas. O manifesto é atualizado por união a partir de **5.193 entradas**, admitindo alterações apenas nas duas fontes, duas páginas HTML e nove controles anteriores. Originais, demais textos, imagens e PDF anterior permanecem preservados. Este lote tem salvamento local; o último envio ao GitHub continua sendo o registro 141.

## Próxima tarefa

**Conferência final do texto integrado, apêndices e caminhos de consulta antes da composição do PDF. Modelo recomendado: GPT-6.1 Sol; esforço alto.** Fechar a cobertura de leitura, conferir termos, referências e avisos de exemplos experimentais e registrar correções restantes. A leitura dos capítulos principais foi concluída; isso não declara encerrada a revisão de todo o livro.

Depois, compor o PDF completo a partir das fontes atuais, inspecionar visualmente cada página e repetir a inspeção após as correções. Conferir colunas, títulos, tabelas, mapas, imagens e espaços evitáveis, com comparação final ao livro base e aos guias já pesquisados. O PDF anterior continua sendo uma versão mais antiga. Este lote não gera outro PDF nem declara inspeção visual em navegador ou equivalência final aos livros de referência.
''')
config=json.loads((R/'04 - Planejamento/apoio-leitura-142/arquivos-do-lote.json').read_text());routes=json.loads((A/'destinos-alterados.json').read_text())
config.update(registro=143,base_manifesto=5193,relatorio=report.relative_to(R).as_posix(),fontes_alteradas=[row['fonte'] for row in routes],html_alterados=[(E/row['pagina']).relative_to(R).as_posix() for row in routes]);save(A/'arquivos-do-lote.json',config)
for rel in config['controles']:
 p=R/rel;b=A/'antes'/rel
 if not b.exists():b.parent.mkdir(parents=True,exist_ok=True);b.write_bytes(p.read_bytes())
 s=p.read_text()
 if '**Fila vigente - registro 143,' in s:continue
 s=s.replace('**Fila vigente - registro 142,','**Fila histórica - registro 142,',1)
 url=os.path.relpath(report,p.parent)
 banner=f'> **Fila vigente - registro 143, 30/10/2026:** capítulo 10, dois casos e onze consultas lidos; duas fontes relidas após quatro ajustes. [Registro e edição atual](<{url}>). Saldo livre, acesso às definições e aceitação de tarefas esclarecidos; passagem entre mestres e contas selecionadas conferidas. Números e tabelas preservados. **Próximo: conferência final do texto, apêndices e caminhos de consulta; GPT-6.1 Sol, esforço alto.** Depois, PDF completo e revisão visual de todas as páginas. Use o gerador deste registro; não reaplique preparadores antigos sobre a edição atual. Último GitHub: registro 141.\n\n'
 first=s.index('\n\n');s=s[:first+2]+banner+s[first+2:]
 if rel.endswith('revisao-98/LEIA-ME.md'):
  s=re.sub(r'(?m)^\*\*Próxima tarefa:\*\* leitura contínua do capítulo 10.*?\*\*GPT-6\.1 Sol, esforço alto\.\*\*','**Próxima tarefa:** conferência final do texto integrado, apêndices e caminhos de consulta. Depois, composição e revisão visual do PDF completo. **GPT-6.1 Sol, esforço alto.**',s)
 p.write_text(s)
print('Registro 143 e continuidade atualizados; 14 arquivos lidos e dois relidos após os ajustes.')
