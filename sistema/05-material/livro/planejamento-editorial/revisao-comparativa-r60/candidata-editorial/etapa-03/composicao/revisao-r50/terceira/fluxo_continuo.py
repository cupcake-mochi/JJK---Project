"""Composição por colunas contínuas; largura inteira só para estruturas largas."""
import re
from functools import lru_cache

class Fluxo:
    def __init__(self, ns):
        self.n = ns
        self.section_log = []
        self.flow_log = []
        self.context_heights = {}
        self.opening_log = []

    def atoms_for(self, parts, group):
        from copy import copy
        n=self.n;Unit=n['Unit'];heads={'h1','h2','h3','major','marker'}
        atoms=[];pending=[];heading=group;sid=0
        def emit(ps,wide=False):
            if not ps:return
            unit=Unit(ps);aw=unit.measure(n['AW'])[0];cw=unit.measure(n['CW'])[0]
            if cw>n['CAP']:wide=True
            assert aw<=n['CAP'] and (wide or cw<=n['CAP']),(ps[0].block,aw,cw)
            cfg=n['hierarquia'].get(ps[0].block,{})
            atoms.append({'unit':unit,'key':(next((x.key for x in ps if x.key),ps[0].block) or group)+f'--r38-{len(atoms)}',
                'section':sid,'group':group,'context':getattr(ps[0],'context',None) or cfg.get('contexto',group),
                'wide':wide,'aw':aw,'cw':cw,'continuation_title':heading if ps[0].kind not in heads else None})
        for part in parts:
            if part.kind in heads:
                heading=part.text;sid+=1;pending.append(part);continue
            if part.kind in {'cost','small'} and pending:
                pending.append(part);continue
            if part.kind=='table':
                # A category label plus a one-line description is not a useful
                # table opening alone. Keep its first two data rows with it.
                if not pending and atoms:
                    lead=atoms[-1]['unit'].parts
                    if (lead[-1].block==part.block and lead[-1].kind=='body'
                            and any(x.kind in heads for x in lead)):
                        q=copy(part);q.text=part.text[:3]
                        width=n['AW'] if n['tabela_larga'](part) or any(x.kind=='major' for x in lead) else n['CW']
                        if Unit(lead+[q]).measure(width)[0]<=n['CAP']-20:
                            pending=atoms.pop()['unit'].parts
                rows=part.text;wide=n['tabela_larga'](part) or any(x.kind=='major' for x in pending)
                # R48: tabelas realmente curtas permanecem inteiras; tabelas
                # longas seguem divisíveis, com o cabeçalho repetido.
                width=n['AW'] if wide else n['CW']
                if Unit([part]).measure(width)[0]<=n['CAP']*.30 and Unit(pending+[part]).measure(width)[0]<=n['CAP']-20:
                    emit(pending+[part],wide);pending=[];continue
                start=1;segments=[]
                while start<len(rows):
                    stop=min(start+2,len(rows))
                    if len(rows)-stop==1:stop=len(rows)
                    if stop<len(rows) and all(not x for x in rows[stop-1][1:]):stop+=1
                    q=copy(part);q.text=[rows[0]]+rows[start:stop];q.r38_original=part
                    q.r38_table_id=id(part);q.r38_row_start=start;q.r38_row_stop=stop
                    if start>1:q.key=None;q.aliases=[]
                    segments.append(q);start=stop
                for i,q in enumerate(segments):
                    emit(pending+[q] if i==0 else [q],wide or any(x.kind=='major' for x in pending))
                    pending=[]
                continue
            emit(pending+[part],part.kind=='esquema' or any(x.kind=='major' for x in pending));pending=[]
        assert not pending,('Título sem parágrafo',pending)
        # R40: uma introdução terminada em dois-pontos abre a lista junto
        # do primeiro item, em vez de anunciar conteúdo só na página seguinte.
        joined=[]
        for atom in atoms:
            if joined:
                previous=joined[-1];left=previous['unit'].parts;right=atom['unit'].parts
                if (left[-1].kind=='body' and str(left[-1].text).rstrip().endswith(':')
                    and right[0].kind=='body' and str(right[0].text).startswith('• ')
                    and left[-1].block==right[0].block):
                    u=Unit(left+right);aw=u.measure(n['AW'])[0];cw=u.measure(n['CW'])[0]
                    if cw<=n['CAP'] and not previous['wide'] and not atom['wide']:
                        previous.update(unit=u,aw=aw,cw=cw)
                        self.opening_log.append({'bloco':left[-1].block,'introducao':left[-1].text,'primeiro_item':right[0].text,'motivo':'R40: introdução e primeiro item da lista na mesma coluna.'})
                        continue
            joined.append(atom)
        # R40: a abertura de uma Trilha sem ilustração acompanha sua tabela
        # curta e o começo da primeira habilidade, quando cabem numa coluna.
        result=[];i=0
        while i<len(joined):
            a=joined[i];ps=a['unit'].parts;doc=ps[0].doc
            if ps[0].kind=='h1' and doc in {'bastiao','vanguarda','guia','emanador','evocador','incursor'}:
                end=i+1;found=False
                while end<len(joined):
                    parts=joined[end]['unit'].parts
                    if any(p.kind in {'h1','major'} for p in parts):break
                    if any(getattr(p,'editorial_style',None)=='entrada' for p in parts):found=True;end+=1;break
                    end+=1
                options=[end] if found else []
                table_start=next((j for j in range(i+1,end) if any(p.kind=='table' for p in joined[j]['unit'].parts)),None)
                if table_start is not None:
                    table_end=table_start+1
                    while table_end<end and self.table_join(joined[table_end-1],joined[table_end],n['CW']):table_end+=1
                    options.append(table_end)
                kept=False
                for target in options:
                    if any(x['wide'] for x in joined[i:target]):continue
                    u=self.joined_unit(joined[i:target]);cw=u.measure(n['CW'])[0];aw=u.measure(n['AW'])[0]
                    if cw<=n['CAP']-20:
                        a=dict(a);a.update(unit=u,cw=cw,aw=aw)
                        self.opening_log.append({'bloco':ps[0].block,'titulo':ps[0].text,'motivo':'R40: abertura da Trilha junto da progressão e, quando cabe, do começo da primeira habilidade.'})
                        result.append(a);i=target;kept=True;break
                if kept:continue
            result.append(a);i+=1
        # R44: exemplos curtos de pacto conservam a troca completa na mesma
        # coluna; "Dá" não fica separado de "Recebe" por uma virada de página.
        compact=[];i=0
        while i<len(result):
            a=result[i];ps=a['unit'].parts
            if ps[0].block=='ritual--pacto-exemplos' and ps[0].kind in heads and re.match(r'^\d+\.',str(ps[0].text)):
                end=i+1
                while end<len(result):
                    nxt=result[end]['unit'].parts
                    if nxt[0].block!='ritual--pacto-exemplos' or nxt[0].kind in heads:break
                    end+=1
                u=self.joined_unit(result[i:end]);cw=u.measure(n['CW'])[0]
                if cw<=n['CAP']/2 and not any(x['wide'] for x in result[i:end]):
                    a=dict(a);a.update(unit=u,cw=cw,aw=u.measure(n['AW'])[0])
                    compact.append(a);i=end;continue
            compact.append(a);i+=1
        # R45: catálogos e clãs não anunciam escolhas numa coluna sem
        # mostrar ao menos a primeira entrada e seu parágrafo inicial.
        connected=[];i=0
        while i<len(compact):
            a=compact[i];ps=a['unit'].parts
            label=str(ps[0].text)
            if ps[0].doc=='origens' and ps[0].kind in heads and (label.startswith('Menores d') or label in {'Zenin','Kamo','Gojo','Inumaki'}):
                stop=i+1
                while stop<len(compact):
                    nxt=compact[stop]['unit'].parts
                    if nxt[0].doc!='origens' or any(p.kind in {'h1','major'} for p in nxt):break
                    if any(p.kind in heads for p in nxt):
                        stop+=1
                        u=self.joined_unit(compact[i:stop]);cw=u.measure(n['CW'])[0]
                        if cw<=n['CAP']-20 and not any(x['wide'] for x in compact[i:stop]):
                            a=dict(a);a.update(unit=u,cw=cw,aw=u.measure(n['AW'])[0])
                            self.opening_log.append({'bloco':ps[0].block,'titulo':label,'motivo':'R45: catálogo/clã junto da primeira capacidade e seu primeiro parágrafo.'})
                            i=stop-1
                        break
                    stop+=1
            connected.append(a);i+=1
        # R48: a apresentação de uma categoria acompanha a primeira
        # entrada, quando a abertura combinada cabe numa coluna.
        anchored=[];i=0
        while i<len(connected):
            a=connected[i];ps=a['unit'].parts;first=ps[0]
            is_group=(getattr(first,'editorial_style',None)=='grupo' or first.kind=='h1' or first.text=='Especiais com preparação prolongada')
            if is_group and sum(p.kind in heads for p in ps)==1 and not a['wide']:
                stop=i+1
                while stop<len(connected):
                    ns=connected[stop]['unit'].parts
                    if ns[0].doc!=first.doc or connected[stop]['wide']:break
                    hs=[p for p in ns if p.kind in heads]
                    if hs:
                        child=hs[0]
                        subordinate=(child.kind not in {'h1','major'} and getattr(child,'editorial_style',None)!='grupo')
                        if subordinate:
                            u=self.joined_unit(connected[i:stop+1]);cw=u.measure(n['CW'])[0]
                            limit=n['CAP']-20 if getattr(first,'editorial_style',None)=='grupo' or first.text=='Especiais com preparação prolongada' else n['CAP']*.58
                            if cw<=limit:
                                a=dict(a);a.update(unit=u,cw=cw,aw=u.measure(n['AW'])[0])
                                self.opening_log.append({'bloco':first.block,'titulo':first.text,'motivo':'R48: apresentação junto da primeira entrada e do início de sua regra.'})
                                i=stop
                        break
                    stop+=1
            anchored.append(a);i+=1
        # A ficha curta do equipamento não substitui o início do efeito.
        result=[];i=0
        while i<len(anchored):
            a=anchored[i];ps=a['unit'].parts
            if (i+1<len(anchored) and ps[0].doc=='equip' and any(p.kind in heads for p in ps)
                    and ps[-1].kind=='body' and 'Grau' in str(ps[-1].text) and 'Efeito' in str(ps[-1].text)):
                z=anchored[i+1];zs=z['unit'].parts
                if zs[0].block==ps[-1].block and zs[0].kind=='body' and not a['wide'] and not z['wide']:
                    u=self.joined_unit([a,z]);cw=u.measure(n['CW'])[0]
                    if cw<=n['CAP']-20:
                        a=dict(a);a.update(unit=u,cw=cw,aw=u.measure(n['AW'])[0]);i+=1
                        self.opening_log.append({'bloco':ps[0].block,'titulo':ps[0].text,'motivo':'R48: nome e metadados junto do primeiro parágrafo do efeito.'})
            result.append(a);i+=1
        # Uma conclusão breve depois de tabela larga acompanha as últimas
        # linhas, em vez de ocupar sozinha a página seguinte.
        final=[];i=0
        while i<len(result):
            a=result[i];ps=a['unit'].parts
            if a['wide'] and ps[-1].kind=='table' and i+1<len(result):
                j=i+1
                while j<len(result):
                    qs=result[j]['unit'].parts
                    if qs[0].block!=ps[-1].block or any(p.kind in heads or p.kind=='table' for p in qs):break
                    j+=1
                tail=result[i+1:j]
                if tail and sum(x['aw'] for x in tail)<=n['CAP']*.16:
                    u=self.joined_unit(result[i:j]);aw=u.measure(n['AW'])[0]
                    if aw<=n['CAP']*.65:
                        a=dict(a);a.update(unit=u,cw=u.measure(n['CW'])[0],aw=aw);i=j-1
                        self.opening_log.append({'bloco':ps[-1].block,'motivo':'R48: conclusão curta junto do fim da tabela larga.'})
            final.append(a);i+=1
        # Fechamentos localizados na revisão visual: o exemplo acompanha
        # a regra que demonstra, e a Bênção curta conserva suas condições.
        kept=[];i=0
        while i<len(final):
            a=final[i];ps=a['unit'].parts
            if (str(ps[0].text) in {'Sangue Frio','Leitura a Dois','Gambiarra'}
                    or (ps[0].block=='dano--zero' and ps[0].text=='Aguentar')):
                j=i+1
                while j<len(final) and final[j]['unit'].parts[0].block==ps[0].block and not any(p.kind in heads for p in final[j]['unit'].parts):j+=1
                u=self.joined_unit(final[i:j]);cw=u.measure(n['CW'])[0]
                if cw<=n['CAP']-20 and not any(x['wide'] for x in final[i:j]):
                    a=dict(a);a.update(unit=u,cw=cw,aw=u.measure(n['AW'])[0]);i=j-1
            if kept and ps[0].block in {'dano--temporarios','guia--guia-modelos'} and (ps[0].kind=='note' or str(ps[0].text).startswith('**Exemplo')):
                z=kept[-1];zs=z['unit'].parts
                if zs[-1].block==ps[0].block and zs[-1].kind=='body' and not z['wide'] and not a['wide']:
                    u=self.joined_unit([z,a]);cw=u.measure(n['CW'])[0]
                    if cw<=n['CAP']*.5:
                        z.update(unit=u,cw=cw,aw=u.measure(n['AW'])[0]);i+=1;continue
            kept.append(a);i+=1
        return kept

    def table_join(self,left,right,width):
        """Overhead removed when consecutive pieces of one table share a column."""
        a=left['unit'].parts[-1];b=right['unit'].parts[0]
        if not hasattr(a,'r38_table_id') or getattr(b,'r38_table_id',None)!=a.r38_table_id:return 0
        from copy import copy
        q=copy(a);q.text=[a.text[0]]
        return self.n['Unit']([q]).measure(width)[0]+self.n['DENSITY']['atom_gap']

    def joined_unit(self,batch):
        from copy import copy
        parts=[]
        for atom in batch:
            for p in atom['unit'].parts:
                if (parts and hasattr(p,'r38_table_id') and getattr(parts[-1],'r38_table_id',None)==p.r38_table_id):
                    q=copy(parts[-1]);q.text=q.text+p.text[1:];q.r38_row_stop=p.r38_row_stop;parts[-1]=q
                else:parts.append(p)
        return self.n['Unit'](parts)

    def joined_batches(self,batch):
        result=[];at=0
        while at<len(batch):
            stop=at+1
            while stop<len(batch) and self.table_join(batch[stop-1],batch[stop],self.n['AW']):stop+=1
            a=dict(batch[at]);u=self.joined_unit(batch[at:stop]);a.update(unit=u,aw=u.measure(self.n['AW'])[0],cw=u.measure(self.n['CW'])[0]);result.append(a);at=stop
        return result

    def add_atoms(self, ch, atoms):
        n=self.n; Unit=n['Unit']; Part=n['Part']; M=n['M']; CW=n['CW']; G=n['G']; AW=n['AW']
        page=None; y=n['TOP']; band=0; columns_used=False
        def fresh(a):
            nonlocal page,y,band,columns_used
            page=n['newpage'](ch,a['context']); y=n['TOP']; band=0; columns_used=False
        def context_part(a):
            ps=a['unit'].parts; cfg=n['hierarquia'].get(ps[0].block,{})
            if ps[0].kind in {'major','h1'} and not ps[0].generated:return None
            context=a['context']
            if a.get('continuation_title'):
                title=str(a['continuation_title']).replace(' (continuação)','')
                context=(context if context==title or context.endswith(' / '+title) else context+' / '+title)
            label=re.sub(r'\*|`','',str(ps[0].text))
            if label==context:return None
            if not context or context==ch['titulo']:return None
            return Part('small',context,doc=ps[0].doc,block=ps[0].block,generated=True)
        def ctx_height(a):
            p=context_part(a)
            if not p:return 0
            if p.text not in self.context_heights:self.context_heights[p.text]=Unit([p]).measure(CW)[0]
            return self.context_heights[p.text]
        def heights(batch):return sum(a['cw'] for a in batch)+self.n['DENSITY']['atom_gap']*max(0,len(batch)-1)
        at=0
        while at<len(atoms):
            a=atoms[at]
            if page is None:fresh(a)
            if a['wide']:
                extra=context_part(a) if y==n['TOP'] else None
                eh=Unit([extra]).measure(AW)[0] if extra else 0
                if a['aw']+eh>y-n['BOTTOM']+.01:
                    fresh(a);extra=context_part(a);eh=Unit([extra]).measure(AW)[0] if extra else 0
                if a['aw']+eh>n['CAP']:extra=None;eh=0
                stop=at+1
                # Consecutive rows share one header until the actual page break.
                while stop<len(atoms) and atoms[stop]['wide'] and self.table_join(atoms[stop-1],atoms[stop],AW):
                    if self.joined_unit(atoms[at:stop+1]).measure(AW)[0]+eh>y-n['BOTTOM']+.01:break
                    stop+=1
                bid=f'{page["numero"]}-{band}';band+=1
                if extra:y-=n['put'](page,Unit([extra]),M,y,AW,'contexto',bid)
                y-=n['put'](page,self.joined_unit(atoms[at:stop]),M,y,AW,'uma-coluna',bid,a['key']);y-=n['DENSITY']['atom_gap']
                at=stop;page['content_height']=n['TOP']-y;continue
            end=at
            while end<len(atoms) and not atoms[end]['wide']:end+=1
            # Brief prose leading directly to a wide table keeps one width.
            run=self.joined_batches(atoms[at:end]);lead_height=sum(x['aw'] for x in run)+n['DENSITY']['atom_gap']*max(0,len(run)-1)
            if (end<len(atoms) and lead_height<=n['CAP']
                    and lead_height+n['DENSITY']['atom_gap']+atoms[end]['aw']<=y-n['BOTTOM']):
                for item in run:
                    bid=f'{page["numero"]}-{band}';band+=1
                    y-=n['put'](page,item['unit'],M,y,AW,'uma-coluna',bid,item['key']);y-=n['DENSITY']['atom_gap']
                at=end;page['content_height']=n['TOP']-y;continue
            while at<end:
                # Before a wide table, use the remaining page as a single stream
                # when all remaining prose and the first rows fit. This avoids
                # an unnecessary column pair just before the table.
                remaining=self.joined_batches(atoms[at:end])
                lead_height=sum(x['aw'] for x in remaining)+n['DENSITY']['atom_gap']*max(0,len(remaining)-1)
                if (end<len(atoms) and lead_height+n['DENSITY']['atom_gap']+atoms[end]['aw']<=y-n['BOTTOM']):
                    for item in remaining:
                        bid=f'{page["numero"]}-{band}';band+=1
                        y-=n['put'](page,item['unit'],M,y,AW,'uma-coluna',bid,item['key']);y-=n['DENSITY']['atom_gap']
                    at=end;page['content_height']=n['TOP']-y
                    break
                if columns_used:fresh(atoms[at])
                available=y-n['BOTTOM']
                # Plan the complete remaining run before drawing. A greedy
                # page fill can strand one short paragraph on the final page.
                # Preserve order and indivisible openings, and distribute the
                # unavoidable end space across pages without adding pages.
                gap=n['DENSITY']['atom_gap'];origin=at
                prefix=[0]
                joins=[0]+[self.table_join(atoms[i-1],atoms[i],CW) for i in range(origin+1,end)]
                for j,item in enumerate(atoms[origin:end]):prefix.append(prefix[-1]+item['cw']+gap-joins[j])
                def span(i,j):return prefix[j-origin]-prefix[i-origin]-gap+joins[i-origin]+ctx_height(atoms[i])
                # R48: page balance must not strand the end of a rule.
                # A boundary inside a subsection is more costly when only a
                # short tail remains, or the entire subsection fits a column.
                @lru_cache(None)
                def split_cost(pos, page_break=True):
                    if pos<=origin or pos>=end:return 0
                    nxt=atoms[pos];prev=atoms[pos-1]
                    leftpart=prev['unit'].parts[-1];rightpart=nxt['unit'].parts[0]
                    table_id=getattr(leftpart,'r38_table_id',None)
                    if table_id is not None and getattr(rightpart,'r38_table_id',None)==table_id:
                        lo=pos-1;hi=pos+1
                        while lo>origin and getattr(atoms[lo-1]['unit'].parts[-1],'r38_table_id',None)==table_id:lo-=1
                        while hi<end and getattr(atoms[hi]['unit'].parts[0],'r38_table_id',None)==table_id:hi+=1
                        if span(lo,hi)<=n['CAP']-20:return n['CAP']**2*(2 if page_break else .7)
                    if (not nxt.get('continuation_title') or
                            prev['unit'].parts[-1].block!=nxt['unit'].parts[0].block):return 0
                    lo=pos-1
                    while lo>origin and atoms[lo].get('continuation_title') and atoms[lo-1]['unit'].parts[-1].block==nxt['unit'].parts[0].block:lo-=1
                    hi=pos+1
                    while hi<end and atoms[hi].get('continuation_title') and atoms[hi]['unit'].parts[0].block==nxt['unit'].parts[0].block:hi+=1
                    whole=span(lo,hi);tail=span(pos,hi)
                    if page_break:
                        return n['CAP']**2*(.10 + (.65 if tail<n['CAP']*.25 else 0) + (.25 if whole<n['CAP']*.85 else 0))
                    return n['CAP']**2*(.06 if whole<n['CAP']*.55 else .005)
                @lru_cache(None)
                def next_complete_height(pos):
                    # Uma entrada curta inteira pode ocupar o espaço restante;
                    # nunca preencher o rodapé apenas com seu título.
                    hi=pos+1
                    while hi<end and atoms[hi].get('continuation_title') and atoms[hi]['unit'].parts[0].block==atoms[pos]['unit'].parts[0].block:hi+=1
                    return span(pos,hi)-ctx_height(atoms[pos])
                @lru_cache(None)
                def plan(i,room):
                    if i==end:return (0,0,[])
                    candidates=[]
                    for stop in range(i+1,end+1):
                        choices=[]
                        if stop==i+1:
                            left=span(i,stop)
                            if left>room and atoms[i]['cw']<=room:left=atoms[i]['cw']
                            if left<=room:choices.append((stop,left,0))
                        for cut in range(i+1,stop):
                            left=span(i,cut);right=span(cut,stop)
                            if max(left,right)<=room:choices.append((cut,left,right))
                        if not choices:
                            if prefix[stop-origin]-prefix[i-origin]-gap>2*room:break
                            continue
                        # Keep room for the following full-width element.
                        # Continuity preference must not add a table-only page
                        # when another valid split fits that element here.
                        if stop==end and end<len(atoms):
                            fits_next=[v for v in choices if max(v[1],v[2])+atoms[end]['aw']+gap<=room+.01]
                            if fits_next:choices=fits_next
                        if stop==end or y<n['TOP']:cut,left,right=min(choices,key=lambda x:split_cost(x[0],False)+abs(x[1]-x[2])*30)
                        else:
                            cut,left,right=min(choices,key=lambda x:split_cost(x[0],False)+(room-x[1])*100)
                            # With little text on this page, filling the left
                            # column first can leave only one paragraph on the
                            # right. Balance that pair without adding a region.
                            if right < .4*room:
                                cut,left,right=min(choices,key=lambda x:split_cost(x[0],False)+abs(x[1]-x[2])*30)
                        rest=plan(stop,n['CAP'])
                        # Reservar espaço para a tabela larga que vem depois das
                        # colunas evita uma página final quase vazia.
                        extra_page=0
                        if stop==end and end<len(atoms):
                            next_height=atoms[end]['aw']+gap
                            extra_page=int(max(left,right)+next_height>room+.01)
                        # Tiny final pages are the strongest visual penalty;
                        # normal end-of-section whitespace remains acceptable.
                        used=left+right
                        low=max(0,.9*n['CAP']-used)**2 if room>=n['CAP']-.1 else 0
                        ragged=(2*room-used)**2*.04
                        cost=rest[1]+((2*room-used)**2 if stop<end else max(0,.65*n['CAP']-used)**2*10)+abs(left-right)*.05+split_cost(stop)+split_cost(cut,False)
                        if stop<end and split_cost(stop) and right and right+atoms[stop]['cw']+gap-self.table_join(atoms[stop-1],atoms[stop],CW)<=room:
                            cost+=n['CAP']**2
                        # Evitar uma página quase vazia, intermediária ou final.
                        # Não transferir o vão para outra página da sequência.
                        if (stop<end or end==len(atoms)) and room>=n['CAP']-.1:
                            cost+=max(0,n['CAP']*.95-used)**2*40
                        if stop<end and right:
                            next_h=next_complete_height(stop)
                            free=room-right-gap
                            if next_h<=free+.01:
                                cost+=n['CAP']**2*3
                        candidates.append((rest[0]+1+extra_page,cost,[(stop,cut,left,right)]+rest[2]))
                    return min(candidates,key=lambda x:(x[0],x[1])) if candidates else (10**6,10**12,[])
                sequence=plan(at,available)[2]
                chosen=sequence[0] if sequence else None
                if chosen is None:
                    if y==n['TOP']:
                        # Context is optional; content itself must always fit.
                        assert atoms[at]['cw']<=available,(atoms[at]['key'],atoms[at]['cw'],available)
                        chosen=(at+1,at+1,atoms[at]['cw'],0)
                    else:fresh(atoms[at]);continue
                stop,cut,lh,rh=chosen; bid=f'{page["numero"]}-{band}';band+=1
                for start,finish,x in [(at,cut,M),(cut,stop,M+CW+G)]:
                    if start==finish:continue
                    yy=y;extra=context_part(atoms[start])
                    if extra and span(start,finish)<=available:
                        yy-=n['put'](page,Unit([extra]),x,yy,CW,'contexto',bid)
                    i=start
                    while i<finish:
                        j=i+1
                        while j<finish and self.table_join(atoms[j-1],atoms[j],CW):j+=1
                        yy-=n['put'](page,self.joined_unit(atoms[i:j]),x,yy,CW,'duas-colunas',bid,atoms[i]['key'])
                        if j<finish:yy-=n['DENSITY']['atom_gap']
                        i=j
                columns_used=True
                self.flow_log.append({'pagina':page['numero'],'capitulo':ch['numero'],'faixa':bid,
                    'primeiro':atoms[at]['key'],'ultimo':atoms[stop-1]['key'],
                    'altura_esquerda':round(lh,2),'altura_direita':round(rh,2),
                    'motivo':'Leitura contínua: coluna esquerda inteira, depois coluna direita inteira.'})
                y-=max(lh,rh)+self.n['DENSITY']['atom_gap'];at=stop
                if at<end:fresh(atoms[at])
            page['content_height']=n['TOP']-y
