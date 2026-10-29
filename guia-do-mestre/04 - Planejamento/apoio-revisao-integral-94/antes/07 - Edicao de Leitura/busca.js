(() => {
  'use strict';
  const form = document.getElementById('busca');
  const input = document.getElementById('consulta');
  const dialog = document.getElementById('resultados');
  const list = document.getElementById('lista-resultados');
  const summary = document.getElementById('resumo-busca');
  const normalize = value => value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const data = (window.CM_SEARCH || []).map(item => ({...item, haystack:normalize(item.id+' '+item.grupo+' '+item.titulo+' '+item.texto), title:normalize(item.titulo)}));
  document.getElementById('fechar-busca').addEventListener('click', () => dialog.close());
  dialog.addEventListener('close', () => input.focus());
  form.addEventListener('submit', event => {
    event.preventDefault();
    const raw = input.value.trim();
    const terms = normalize(raw).split(/\s+/).filter(Boolean);
    list.replaceChildren();
    if (!terms.length || raw.length < 2) {
      summary.textContent = 'Digite pelo menos dois caracteres para buscar títulos e trechos.';
      if (!dialog.open) dialog.showModal();
      return;
    }
    const matches = data.filter(item => terms.every(term => item.haystack.includes(term))).sort((a,b) => {
      const score = item => terms.reduce((sum,term) => sum+(item.title.includes(term)?10:0),0);
      return score(b)-score(a) || a.grupo.localeCompare(b.grupo) || a.titulo.localeCompare(b.titulo,'pt-BR');
    });
    summary.textContent = matches.length ? `${matches.length} consultas encontradas para “${raw}”. ${matches.length>30?'Exibindo as primeiras 30.':''}` : `Nenhuma consulta encontrada para “${raw}”. Tente um termo mais curto ou outra palavra do assunto.`;
    for (const item of matches.slice(0,30)) {
      const li = document.createElement('li');
      const group = document.createElement('span');group.className='grupo-resultado';group.textContent=item.grupo+' · '+item.id.replace(/^s0*/,'Consulta ');
      const link = document.createElement('a');link.href=(window.CM_ROOT || '')+item.url;link.textContent=item.titulo;
      const normalizedText=normalize(item.texto);const index=normalizedText.indexOf(terms[0]);const start=Math.max(0,index-70);
      const snippet=document.createElement('p');snippet.textContent=(start?'…':'')+item.texto.slice(start,start+230)+(start+230<item.texto.length?'…':'');
      li.append(group,link,snippet);list.append(li);
    }
    if (!dialog.open) dialog.showModal();
  });
})();
