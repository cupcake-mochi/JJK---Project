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
                            and len(lead[-1].text.split())<=30
                            and any(x.kind in heads for x in lead)):
                        pending=atoms.pop()['unit'].parts
                rows=part.text;wide=n['tabela_larga'](part) or any(x.kind=='major' for x in pending)
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
        return result

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
                context=(context if context==title or context.endswith(' / '+title) else context+' / '+title)+' (continuação)'
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
                        if stop==end or y<n['TOP']:cut,left,right=min(choices,key=lambda x:abs(x[1]-x[2]))
                        else:
                            cut,left,right=max(choices,key=lambda x:x[1])
                            # With little text on this page, filling the left
                            # column first can leave only one paragraph on the
                            # right. Balance that pair without adding a region.
                            if right < .4*room:
                                cut,left,right=min(choices,key=lambda x:abs(x[1]-x[2]))
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
                        cost=rest[1]+((2*room-used)**2 if stop<end else max(0,.65*n['CAP']-used)**2*10)+abs(left-right)*.05
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
