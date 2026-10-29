from pathlib import Path
import pymupdf as fitz
import json,hashlib
H=Path(__file__).resolve().parent;P=H.parent/'revisao-capitulo21/composicao/output/pdf';O=H/'composicao/output/pdf';V=H/'revisao';V.mkdir(exist_ok=True);reports=[]
for pal,suffix in [('claro',''),('noturno','-Noturno')]:
 a=fitz.open(P/f'Ciclo-Maldito-Revisao-Indice{suffix}.pdf');b=fitz.open(O/f'Ciclo-Maldito-Livro-de-Regras{suffix}.pdf');assert len(a)==len(b)==425;words_bad=[];pixels_bad=[]
 for n in range(len(a)):
  wa=a[n].get_text('words');wb=b[n].get_text('words')
  if len(wa)!=len(wb) or any(x[4]!=y[4] or max(abs(i-j) for i,j in zip(x[:4],y[:4]))>.01 for x,y in zip(wa,wb)):words_bad.append(n+1)
  pa=a[n].get_pixmap(matrix=fitz.Matrix(1,1),alpha=False);pb=b[n].get_pixmap(matrix=fitz.Matrix(1,1),alpha=False)
  if pa.width!=pb.width or pa.height!=pb.height or hashlib.sha256(pa.samples).digest()!=hashlib.sha256(pb.samples).digest():pixels_bad.append(n+1)
  if (n+1)%100==0:print(pal,n+1,flush=True)
 reports.append({'paleta':pal,'paginas':len(a),'paginas_com_texto_ou_posicao_diferentes':words_bad,'paginas_com_imagem_diferente':pixels_bad,'resolucao_imagem_dpi':72});print(pal,'concluído',flush=True)
r={'resultado':'aprovado' if all(not x['paginas_com_texto_ou_posicao_diferentes'] and not x['paginas_com_imagem_diferente'] for x in reports) else 'requer revisão','referencia':'Etapa 21 validada','comparacoes':reports};(V/'PROVA-REPRODUCAO.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n');print(json.dumps(r,ensure_ascii=False))
