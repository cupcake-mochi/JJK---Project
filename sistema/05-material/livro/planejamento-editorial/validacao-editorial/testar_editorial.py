from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch
import hashlib,json,unittest
import conferir_editorial as v
REG=[{'termo':'Malabarista','donos':['incursor']},{'termo':'Movimento Acrobático','donos':['incursor']},{'termo':'Carregar','donos':['fundamento'],'somente_nome_marcado':True}]
class Editorial(unittest.TestCase):
 def codes(self,s,domain='geral',blocks=()):return {i['codigo'] for i in v.scan(s,domain,REG,blocks)}
 def test_atx(self):self.assertIn('E001',self.codes('## Como ler uma arma'))
 def test_case(self):self.assertIn('E001',self.codes('### COMO LER AS TABELAS'))
 def test_inline_format(self):self.assertIn('E001',self.codes('## **Como ler** uma arma'))
 def test_setext(self):self.assertIn('E001',self.codes('Como ler uma arma\n----'))
 def test_html(self):self.assertIn('E001',self.codes('<h2>Como ler uma arma</h2>'))
 def test_numbered_heading(self):self.assertIn('E001',self.codes('## 3. Como ler uma arma'))
 def test_nonheading(self):self.assertNotIn('E001',self.codes('O parágrafo menciona como ler um mapa.'))
 def test_valid_title(self):self.assertFalse(self.codes('## Características das armas'))
 def test_code_is_not_heading(self):self.assertFalse(self.codes('```text\n## Como ler\n```'))
 def test_wrong_owner(self):self.assertIn('E002',self.codes('O Malabarista recebe outra manipulação.'))
 def test_own_owner(self):self.assertFalse(self.codes('O Malabarista recebe outra manipulação.','incursor'))
 def test_accent_normalization(self):self.assertIn('E002',self.codes('Use Movimento Acrobatico.'))
 def test_linebreak_name(self):
  # Important: wrapping must not bypass the check.
  self.assertIn('E002',self.codes('Use Movimento\nAcrobático.'))
 def test_markup_name(self):self.assertIn('E002',self.codes('Use **Movimento Acrobático**.'))
 def test_link_label(self):self.assertIn('E002',self.codes('Veja [Movimento Acrobático](#dono).'))
 def test_path_not_prose(self):self.assertFalse(self.codes('Veja [a tabela](../Malabarista.md).'))
 def test_common_verb(self):self.assertFalse(self.codes('Carregar uma mochila ocupa Volume.'))
 def test_named_verb(self):self.assertIn('E002',self.codes('A restrição **Carregar** tem custo.'))
 def test_copy_without_name(self):
  prose=' '.join('palavra'+str(i) for i in range(30))
  self.assertIn('E003',self.codes(prose,blocks=[('incursor','classe.md',prose)]))
 def test_copy_in_owner(self):
  prose=' '.join('palavra'+str(i) for i in range(30))
  self.assertFalse(self.codes(prose,'incursor',[('incursor','classe.md',prose)]))
 def test_export_gate(self):
  with TemporaryDirectory() as d:
   p=Path(d)/'REGRA.md';p.write_text('# Equipamento\nTexto próprio.\n')
   with patch.object(v,'configuration',return_value=(REG,[{'arquivo':str(p),'dominio':'geral'}],[])):
    with self.assertRaises(RuntimeError):v.assert_exportable(p)
    ev=p.parent/'evidencias';ev.mkdir();r=ev/'LOCALIZACAO-EDITORIAL.json'
    r.write_text(json.dumps({'sha256_texto':hashlib.sha256(p.read_bytes()).hexdigest(),'titulos_revisto':True,'sem_explicacao_alheia':True,'revisor':'teste','vocabulario_revisto':True}))
    v.assert_exportable(p)
    p.write_text('# Como ler uma arma\nO Malabarista aparece.\n')
    with self.assertRaises(RuntimeError):v.assert_exportable(p)
 def test_unknown_file(self):
  with TemporaryDirectory() as d:
   p=Path(d)/'REGRA.md';p.write_text('# Teste')
   with patch.object(v,'configuration',return_value=(REG,[],[])):
    self.assertEqual(v.check_file(p)[0]['codigo'],'E000')
class Vocabulary(unittest.TestCase):
 def test_legal_requires_context(self):self.assertEqual(v.scan_vocabulary('Uma combinação legal.')[0]['codigo'],'E005')
 def test_plural(self):self.assertEqual(v.scan_vocabulary('Combinações legais.')[0]['termo'],'legais')
 def test_plain_equivalent(self):self.assertEqual(v.scan_vocabulary('Uma combinação permitida pelas regras.'),[])
 def test_term_system_not_banned(self):self.assertEqual(v.scan_vocabulary('Maestria limita as perícias beneficiadas.'),[])
 def test_ignore_code_url_and_comment(self):self.assertEqual(v.scan_vocabulary('```\nlegal\n```\n[regra](legal.md)\n<!-- legal -->'),[])
 def test_unfamiliar(self):self.assertEqual(v.scan_vocabulary('No turno subsequente.')[0]['termo'],'subsequente')
 def test_context_exception_and_expiry(self):
  with TemporaryDirectory() as d:
   p=Path(d)/'REGRA.md';p.write_text('# Diálogo\n“Legal, você veio!”\n');ev=p.parent/'evidencias';ev.mkdir();r=ev/'LOCALIZACAO-EDITORIAL.json'
   with patch.object(v,'configuration',return_value=([],[{'arquivo':str(p),'dominio':'geral'}],[])):
    review={'sha256_texto':hashlib.sha256(p.read_bytes()).hexdigest(),'titulos_revisto':True,'sem_explicacao_alheia':True,'vocabulario_revisto':True,'revisor':'teste','excecoes_vocabulario':[{'termo':'legal','linha':2,'justificativa':'Diálogo usa o sentido cotidiano de aprovação.'}]}
    r.write_text(json.dumps(review));v.assert_exportable(p)
    p.write_text('# Regra\nUma combinação legal.\n')
    self.assertIn('E005',{x['codigo'] for x in v.check_file(p,True)})
    self.assertIn('E006',{x['codigo'] for x in v.check_file(p,True)})

class InitialArticles(unittest.TestCase):
 def findings(self,text):return v.scan_title_articles(text)
 def test_four_articles(self):
  for title in ('A ação','O ataque','As armas','Os testes'):
   with self.subTest(title=title):self.assertEqual(self.findings('# '+title)[0]['codigo'],'E007')
 def test_case_and_format(self):
  self.assertEqual(self.findings('## **AS** armas ##')[0]['titulo'],'AS armas')
 def test_linked_title(self):self.assertEqual(self.findings('## [O turno](#turno)')[0]['termo'],'O')
 def test_setext(self):self.assertEqual(self.findings('As armas\n---')[0]['formato'],'setext')
 def test_html(self):self.assertEqual(self.findings('<h2 class="capitulo">O ataque</h2>')[0]['formato'],'html')
 def test_multiline_html(self):
  self.assertEqual(self.findings('Texto\n<h2>\nA ação\n</h2>')[0]['linha'],2)
 def test_numeric_prefix(self):
  for title in ('1. A ação','2.1 O ataque','3 — As armas'):
   with self.subTest(title=title):self.assertTrue(self.findings('# '+title))
 def test_preserve_accent(self):
  self.assertEqual(self.findings('# À distância\n## Às portas'),[])
 def test_article_word_only(self):
  self.assertEqual(self.findings('# Ação\n## Onda\n### Ataques\n#### Ordem'),[])
 def test_article_inside_title(self):self.assertEqual(self.findings('# Perder a concentração'),[])
 def test_prose_not_title(self):self.assertEqual(self.findings('O turno começa agora.'),[])
 def test_markdown_quote(self):
  self.assertEqual(self.findings('> # O turno\n> A ação\n> ---\n>> ## As armas'),[])
 def test_html_quote(self):self.assertEqual(self.findings('<blockquote>\n<h2>O turno</h2>\n</blockquote>'),[])
 def test_fenced_code(self):
  self.assertEqual(self.findings('```md\n# O turno\n```\n~~~\nAs armas\n---\n~~~'),[])
 def test_fence_length(self):
  self.assertEqual(self.findings('````md\n```\n# O turno\n````'),[])
 def test_indented_code(self):
  self.assertEqual(self.findings('    # O turno\n\t<h2>A ação</h2>\n    Os testes\n    ---'),[])
 def test_html_code(self):
  self.assertEqual(self.findings('<pre>\n<h2>O turno</h2>\n</pre>\n<code>\n# A ação\n</code>'),[])
 def test_comment(self):self.assertEqual(self.findings('<!--\n# O turno\n-->'),[])
 def test_returns_original_line(self):
  self.assertEqual(self.findings('```\n# Ignorado\n```\n\n# O turno')[0]['linha'],5)
 def test_connected_to_main_scan(self):
  self.assertIn('E007',{x['codigo'] for x in v.scan('# O turno','geral',[])})
 def test_export_blocks_even_with_current_review(self):
  with TemporaryDirectory() as d:
   p=Path(d)/'REGRA.md';p.write_text('# O turno\nTexto próprio.\n')
   ev=p.parent/'evidencias';ev.mkdir()
   (ev/'LOCALIZACAO-EDITORIAL.json').write_text(json.dumps({'sha256_texto':hashlib.sha256(p.read_bytes()).hexdigest(),'titulos_revisto':True,'sem_explicacao_alheia':True,'revisor':'teste','vocabulario_revisto':True}))
   with patch.object(v,'configuration',return_value=([],[{'arquivo':str(p),'dominio':'geral'}],[])):
    with self.assertRaisesRegex(RuntimeError,'E007'):v.assert_exportable(p)

class DocumentedOwners(unittest.TestCase):
 def entry(self):
  return next(x for x in json.loads((v.B/'DONOS.json').read_text())['termos'] if x['termo']=='Mão Firme')
 def test_mao_firme_is_published_passive(self):
  source=v.R/'sistema/05-material/livro/manual/40-fundamento.md'
  self.assertIn('| `Mão Firme` | 1 |',source.read_text())
  self.assertIn('fundamento',self.entry()['donos'])
  self.assertNotIn('aptidoes',self.entry()['donos'])
 def test_mao_firme_allowed_in_its_catalogue(self):
  self.assertNotIn('E002',{x['codigo'] for x in v.scan('## Mão Firme\nTalento de Categoria 1.','fundamento',[self.entry()])})
 def test_mao_firme_still_blocked_outside_owners(self):
  self.assertIn('E002',{x['codigo'] for x in v.scan('## Mão Firme','geral',[self.entry()])})
 def test_mao_firme_reference_is_not_an_aptitude(self):
  self.assertIn('E002',{x['codigo'] for x in v.scan('## Mão Firme','aptidoes',[self.entry()])})
 def test_renamed_catalogue_entries_keep_owner(self):
  registry=json.loads((v.B/'DONOS.json').read_text())['termos']
  for name in ('Identificar Feitiço','Leitura de Feitiços'):
   entry=next(x for x in registry if x['termo']==name)
   self.assertEqual(entry['alias_historico'],'Aviso')
   self.assertEqual(v.scan('## '+name,'fundamento',[entry]),[])
   self.assertIn('E002',{x['codigo'] for x in v.scan('## '+name,'geral',[entry])})
 def test_shared_nominal_aliases_are_not_class_abilities(self):
  data=json.loads((v.B/'DONOS.json').read_text())
  aliases={x['atual'] for x in data['aliases_historicos'] if x.get('uso_compartilhado')}
  self.assertIn('Guarda Aberta',aliases)
  self.assertIn('Categoria de Efeito / CE',aliases)
  self.assertEqual(v.scan('Enquanto estiver com a Guarda Aberta, a regra se aplica.','geral',data['termos']),[])
class ContextualReferences(unittest.TestCase):
 def finding(self,code='E002'):
  return {'codigo':code,'termo':'Corpo Amaldiçoado','trecho':'Requisito: indisponível ao Corpo Amaldiçoado.'}
 def exception(self,**changes):
  e={'termo':'Corpo Amaldiçoado','trecho':self.finding()['trecho'],'papel':'requisito','justificativa':'Precisa identificar a rota sem explicar sua habilidade.','nao_reproduz_regra':True};e.update(changes);return e
 def filtered(self,e,code='E002'):
  return v.filter_location_references([self.finding(code)],{'excecoes_localizacao':[e]})
 def test_reviewed_exact_requirement(self):self.assertEqual(self.filtered(self.exception()),[])
 def test_changed_excerpt_is_blocked(self):self.assertTrue(self.filtered(self.exception(trecho='Outra frase.')))
 def test_changed_term_is_blocked(self):self.assertTrue(self.filtered(self.exception(termo='Bastião')))
 def test_missing_reason_is_blocked(self):self.assertTrue(self.filtered(self.exception(justificativa='')))
 def test_explication_not_permitted(self):self.assertTrue(self.filtered(self.exception(papel='explicacao')))
 def test_copy_not_permitted(self):self.assertTrue(self.filtered(self.exception(),'E003'))
 def test_title_not_permitted(self):self.assertTrue(self.filtered(self.exception(),'E007'))
 def test_unreviewed_copy_not_permitted(self):self.assertTrue(self.filtered(self.exception(nao_reproduz_regra=False)))
 def test_stale_review_not_permitted(self):
  with TemporaryDirectory() as d:
   p=Path(d)/'REGRA.md';p.write_text('# Aptidões\n'+self.finding()['trecho']+'\n')
   ev=p.parent/'evidencias';ev.mkdir()
   (ev/'LOCALIZACAO-EDITORIAL.json').write_text(json.dumps({'sha256_texto':'stale','excecoes_localizacao':[self.exception()]}))
   reg=[{'termo':'Corpo Amaldiçoado','donos':['origens']}]
   with patch.object(v,'configuration',return_value=(reg,[{'arquivo':str(p),'dominio':'aptidoes'}],[])):
    self.assertIn('E002',{x['codigo'] for x in v.check_file(p)})

class FullNamePrecedence(unittest.TestCase):
 def findings(self,text,domain='evocador'):
  reg=[{'termo':'Conduzir','donos':['vanguarda']},{'termo':'Conduzir a Especial','donos':['evocador']}]
  return [x for x in v.scan(text,domain,reg) if x['codigo']=='E002']
 def test_full_own_name(self):self.assertFalse(self.findings('# Conduzir a Especial'))
 def test_short_foreign_name_remains(self):self.assertEqual(len(self.findings('Conduzir a Especial e depois Conduzir.')),1)
 def test_foreign_full_name_remains(self):self.assertTrue(self.findings('# Conduzir a Especial','geral'))
 def test_wrapped_full_name(self):self.assertFalse(self.findings('Conduzir a\nEspecial'))
 def test_short_heading_not_exempt(self):self.assertTrue(self.findings('# Conduzir'))

if __name__=='__main__':unittest.main(verbosity=2)
