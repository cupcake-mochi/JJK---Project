"""Registrar o lote de leitura e atualizar as indicações de continuidade."""
from pathlib import Path
import json,os,hashlib,re
A=Path(__file__).resolve().parent;R=A.parents[1];T=R/'06 - Redacao do Guia/edicao-integrada-136';E=R/'07 - Edicao de Leitura/edicao-integrada-136'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def save(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
core=['00-como-usar-este-livro.md','01-sua-primeira-missao.md','02-o-mundo-dos-feiticeiros.md','03-preparar-aventuras.md','03a-ideias-para-aventuras.md']
read=[{'fonte':str((T/n).relative_to(R)),'sha256':sha(T/n),'palavras_da_fonte':len((T/n).read_text().split()),'leitura':'Completa; núcleo da leitura contínua e segunda passagem de clareza, ordem e remissões.'} for n in core]
for n in ['casos/14-o-aviso-de-reabertura.md','casos/84-percursos-apoios-e-quedas.md','consultas/A1-preparar-a-missao.md','consultas/24-registro-de-estado-e-socorro.md']:
 p=T/n;read.append({'fonte':str(p.relative_to(R)),'sha256':sha(p),'leitura':'Completa para conferir o exemplo ou a folha usados pelo núcleo; sem alteração neste lote.'})
save(A/'leitura-realizada.json',{'registro':137,'data':'2026-10-30','nucleo':read,'transicao_seguinte':'Abertura e início de Na mesa de jogo consultados; não constitui leitura integral do capítulo 4.','regras_consultadas':'Trechos de Latente, Sem Técnica, movimento, saltos, Estudar, Vida a zero, janela de socorro, Aguentar, Insistir, Socorro e Sequelas do Livro de Regras 1.0, arquivo técnico R53.','limite':'Leitura editorial pela ferramenta, não teste com leitor humano nem sessão de mesa. O restante do livro e a inspeção visual global permanecem pendentes.'})
report=R/'04 - Planejamento/137-leitura-da-abertura-e-capitulos-iniciais.md'
report.write_text('''# Leitura da abertura e dos capítulos iniciais

Registro 137, 30 de outubro de 2026. A leitura contínua da abertura e dos capítulos 1–3 foi concluída, incluindo o catálogo de ideias incorporado à seção 3.6. Os ajustes já estão na edição reunida. A prioridade foi aproximar instrução, exemplo e consulta, preservando as regras e os acontecimentos preparados.

[Abrir a edição atual](<../07 - Edicao de Leitura/edicao-integrada-136/index.html>) · [Primeira missão](<../07 - Edicao de Leitura/edicao-integrada-136/capitulo-01.html>) · [Preparar aventuras](<../07 - Edicao de Leitura/edicao-integrada-136/capitulo-03.html>) · [Histórico exato das alterações](apoio-leitura-137/alteracoes.json) · [Conferência](apoio-leitura-137/conferencia.json).

## O que foi lido

Foram lidos por inteiro Como usar este livro, Sua primeira missão, O mundo dos feiticeiros, Preparar aventuras e o complemento Ideias para aventuras. A passagem seguinte conferiu novamente a clareza dos textos, os termos, as ligações entre assuntos e a nova ordem do capítulo 3. O catálogo foi conferido dentro da sequência do capítulo, onde aparece na edição de leitura.

Também foram lidos O aviso de reabertura, Movimento, saltos e quedas, a folha curta de preparo e o Registro de estado e socorro. Os dois casos foram comparados com o uso feito pelos capítulos: o aviso continua um desfecho possível da missão anterior, sem restaurar uma criatura já derrotada; a correnteza do catálogo conserva a distância, o custo e o resultado de falha do caso detalhado.

A abertura do capítulo 4 foi consultada para conferir a passagem ao assunto seguinte. Sua leitura integral será a próxima tarefa. O inventário `leitura-realizada.json` identifica o alcance da conferência; os demais capítulos não são dados como lidos nesta etapa.

## O que mudou

| Problema de leitura | Ajuste aplicado |
|---|---|
| A primeira missão anuncia mapa, ficha e resumo, mas o leitor precisava procurá-los no texto longo | Os três itens agora abrem diretamente as partes correspondentes do capítulo. |
| A montagem da técnica aparece dentro da primeira ficha de inimigo, com vocabulário que o iniciante ainda não aprendeu | Uma orientação curta distingue os ataques, defesas e comportamento usados em jogo da nota sobre como o feitiço foi criado. A ficha completa continua disponível. |
| O capítulo ensina a anotar a queda sem levar à folha já existente | O momento de registro agora oferece acesso direto aos campos de queda da folha de estado e socorro. |
| Algumas menções aos capítulos técnicos exigiam outra busca | Os assuntos de Doma, avaliação de capacidade, interpretação da outra presença e preparo de inimigos receberam links aos destinos atuais. |
| O preparo completo da despedida estava depois do catálogo inteiro de ideias | Antes que o trem parta passou para logo depois dos métodos de preparo, antes de 3.6. A explicação agora desemboca no exemplo preenchido. |
| Quem só queria preparar rapidamente precisava atravessar todo o capítulo | A introdução aponta para Quando há pouco tempo e para a folha curta. A seção curta também leva ao exemplo preenchido. |
| A entrada do catálogo repetia a apresentação da seção 3.6 | A introdução foi encurtada e recebeu atalhos para situações, pessoas, lugares, complicações e as duas combinações completas. |
| Frases abstratas dificultavam entender a orientação | Foram simplificados o preparo de uma pessoa para confronto, a escolha das falas da despedida e o registro de contatos combinados. |

O histórico tem **17 registros**, sendo 16 substituições e a mudança de posição do exemplo. Quatro fontes foram alteradas: capítulos 1 e 2, capítulo 3 e seu complemento. A abertura foi mantida, pois seus caminhos de leitura, a referência ao Livro de Regras 1.0 e o uso em guilda ou campanha fechada já estão claros. Não foi necessário reescrevê-la para uniformizar a quantidade de mudanças.

## O que foi preservado e por quê

A primeira missão continua acompanhando conversa, investigação, combate, socorro e escolhas de retirada. O capítulo 2 amplia o mundo sem exigir a trama de Jujutsu Kaisen. O capítulo 3 usa a despedida para ensinar preparo sem tornar todo encontro uma tarefa perigosa. São funções diferentes; a retomada breve do anexo e de Helena ajuda a ligar os ensinamentos.

Os três começos curtos de 3.6 continuam mostrando que tipos de preparo cada ideia pede. O catálogo seguinte oferece peças para combinar e dois preparos mais detalhados. Seus novos atalhos permitem consultar uma parte sem percorrer todas as listas. O complemento continua incluído uma única vez em 3.6, antes de 3.7; o preparo da despedida agora vem antes desse conjunto.

A nomenclatura das regras continua quando é necessária: Classe, Integridade, Insistir, Sequela, Doma e as Origens não foram trocadas por sinônimos imprecisos. O mestre continua interpretando a presença do Receptáculo mediante acordo com o jogador, com as alternativas já aprovadas. O sistema segue apresentado com foco em guilda e uso possível em campanha fechada.

## Conferência

A conferência independente reproduz os 17 registros a partir das cópias anteriores e compara as 99 fontes da edição. As tabelas e o conjunto de números permanecem iguais, inclusive no exemplo mudado de lugar. A sequência numérica bruta do capítulo 3 muda por causa da movimentação do bloco; seus horários e parâmetros não foram alterados.

Foram refeitas as contas da demonstração: dano inicial de 24, vida do Amontoado em 48 → 36 → 22 → 10 → 0; tratamento 5 + 3 = 8; saldos finais de 2, 4 e 6 PE. O tratamento necessário e a contagem da janela continuam de acordo com Vida a zero e Socorro. Na travessia, a distância continua 4,5 m, com 9 m para natação comum e 7,5 m para impulso e salto da ficha apresentada. Os resultados são exemplos explicativos, sem declaração nova de equilíbrio.

A verificação de arquivos percorre os documentos HTML, seus destinos e âncoras, as imagens e as fontes Markdown. Também exige que as âncoras anteriores dos três capítulos continuem acessíveis, para não quebrar referências que vêm de outros casos. A primeira execução encontrou dois destinos novos que usavam títulos anteriores; ambos foram corrigidos para as seções atuais e conferidos novamente. A contagem e o resultado final ficam em `conferencia.json`.

Esta é uma entrega textual. Não foi criado outro PDF parcial, nem foi alegada inspeção visual do HTML no navegador. A restrição de abertura de arquivos locais registrada no lote anterior continua respeitada. O novo PDF completo e sua revisão de colunas, espaços e quebras vêm depois da leitura das demais partes. A prova de sete páginas do registro 136 e o PDF integrado anterior continuam preservados.

## Continuidade

A edição vigente permanece nas pastas `edicao-integrada-136`; o nome da pasta identifica sua origem, enquanto este registro e seu gerador identificam a revisão atual. As 99 fontes do estado anterior foram copiadas para `apoio-leitura-137/antes/`. Os arquivos históricos do registro 136 não foram regravados. Seu preparador de fontes não deve ser reaplicado sobre a edição atual, pois reconstruiria o estado anterior aos ajustes deste lote. Para atualizar a leitura, use o gerador deste registro, até que o próximo lote o substitua.

O salvamento é local, com atualização do manifesto por união a partir das 4.402 entradas anteriores. As alterações previstas fora do apoio novo são quatro fontes, três páginas HTML e nove arquivos de continuidade. Os demais textos, mapas, fontes tipográficas e provas anteriores ficam preservados.

**Próxima tarefa: leitura contínua dos capítulos 4–5 e dos exemplos usados por eles. Modelo: GPT-6.1 Sol; esforço alto.** Conferir descrição, testes, ritmo, combate, encerramento de sessão e passagem das missões à campanha. Depois, seguir pelos capítulos 6–10 e consultas, compor o PDF completo e revisar visualmente todas as suas páginas. A comparação final com o livro base e os demais guias continua pendente.
''')
config=json.loads((R/'04 - Planejamento/apoio-integracao-136/arquivos-do-lote.json').read_text())
config.update(registro=137,base_manifesto=4402,relatorio=report.relative_to(R).as_posix(),fontes_alteradas=[(T/n).relative_to(R).as_posix() for n in core[1:]],html_alterados=[(E/f'capitulo-0{n}.html').relative_to(R).as_posix() for n in [1,2,3]])
config.pop('preservacao',None)
save(A/'arquivos-do-lote.json',config)
for rel in config['controles']:
 p=R/rel;b=A/'antes'/rel
 if not b.exists():b.parent.mkdir(parents=True,exist_ok=True);b.write_bytes(p.read_bytes())
 s=p.read_text()
 if '**Fila vigente - registro 137,' in s:continue
 s=s.replace('**Fila vigente - registro 136,','**Fila histórica - registro 136,',1)
 url=os.path.relpath(report,p.parent)
 banner=f'> **Fila vigente - registro 137, 30/10/2026:** leitura contínua da abertura e dos capítulos 1–3 concluída, com exemplos e folhas conferidos. [Registro e edição atual](<{url}>). Preparo da despedida aproximado das instruções; atalhos de consulta e termos revistos; tabelas e números preservados. **Próximo: capítulos 4–5 e exemplos citados; GPT-6.1 Sol, esforço alto.** Depois, demais capítulos, PDF completo e revisão visual global. O gerador vigente está no apoio deste registro; não reaplicar o preparador de fontes 136 sobre a edição atual.\n\n'
 first=s.index('\n\n');s=s[:first+2]+banner+s[first+2:]
 if rel.endswith('revisao-98/LEIA-ME.md'):
  s=re.sub(r'(?m)^\*\*Próxima tarefa:\*\* leitura contínua da cópia integrada,.*?\*\*GPT-6\.1 Sol, esforço alto\.\*\*', '**Próxima tarefa:** leitura contínua dos capítulos 4–5 da cópia integrada e de seus exemplos. Depois, demais partes e revisão visual do PDF completo. **GPT-6.1 Sol, esforço alto.**',s)
 p.write_text(s)
print('Registro 137 e continuidade atualizados; nenhuma regra nova.')
