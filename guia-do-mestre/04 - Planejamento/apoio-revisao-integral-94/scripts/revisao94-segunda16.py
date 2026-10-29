from revisar_guia94 import *
edit(source(41),[('Essa é uma regra específica publicada. Não o transforme','Esse Pacto tem uma regra própria. Não o transforme')],'Segundo pente-fino, página 238')
p=R/source(47)
for old in re.findall(r'A \[exemplo[^\n]*?\)',p.read_text()):edit(source(47),[(old,'O'+old[1:])],'Segundo pente-fino, página 242: concordância')
for n in [48,49]:
 t=(R/source(n)).read_text()
 for pat in [r' A \[comparação 47\]\([^\n]+?\) reúne as decisões de criação\.',r'O \[planejamento 52\]\([^\n]+?\) reúne as decisões de criação\.',r'A \[comparação 47\]\([^\n]+?\) detalha os casos\. Esse registro']:
  for m in re.finditer(pat,t):edit(source(n),[(m.group(),'O registro' if m.group().endswith('Esse registro') else '')],'Segundo pente-fino: retirar remissão de bastidores')
edit(source(48),[('Nara gasta a Padrão e os 3 PE já comprometidos e impede a aplicação inteira.','Nara gasta a Padrão e os 3 PE já comprometidos, mas o Pacto impede a aplicação inteira.')],'Segundo pente-fino, página 244: identificar quem impede a aplicação')
