// Remontagem da ficha escolhida por Mizuki. Não reutiliza a escala histórica.
const fs = require('fs'), path = require('path'), assert = require('assert');
const root = path.resolve(__dirname, '../..');
const read = p => fs.readFileSync(path.join(root,p),'utf8');
const C = require('../../sistema/05-material/gerador-inimigo/conta.js');
const p26 = read('sistema/03-mecanica/26-bestiario.md');
const p11 = read('sistema/03-mecanica/11-aptidoes-e-refino.md');
const fund = read('sistema/05-material/livro/manual/40-fundamento.md');
const num = s => Number(s.replace(',','.'));
function anchor(text,re,label) { const m=text.match(re); assert(m,`Âncora mudou: ${label}`); return m; }
function value(text,re,label) { return num(anchor(text,re,label)[1]); }
const nivel=30, n=6, atributos={Força:2,Destreza:4,Constituição:4,Inteligência:6,Essência:6};
const f=C.X.FAIXAS.find(x=>x[1]<=nivel && nivel<=x[2]), dg=C.degrau('Calamidade'), L=dg[1];
const cls=[...fund.matchAll(/^\| \*\*(\d)\*\* \| (\d+) \| (\d+) \| (\d+) \| (\d+) \| (\d+) \|/gm)].map(m=>m.slice(1).map(Number));
assert(cls.length,'Tabela de Classes não lida');
const maiorClasse=Math.max(...cls.filter(x=>x[1]<=nivel).map(x=>x[0]));
const cambio=value(p26,/`1` PE por rodada = `([\d,]+)` da cota/,'câmbio');
const domain=value(p26,/vida crua dele se divide por `([\d,]+)`/,'domínio');
const multExt=value(p11,/de pé, ela custa `([\d,]+) × a sua maior Classe`/,'Extensão');
const multCirc=value(p11,/teto por uso da sua `Energia Reversa` sobe para `([\d,]+) ×/,'Circulação');
const multRec=value(p26,/cada alvo leva `([\d,]+) ×` o golpe/,'Recarga');
const perSpell=value(p26,/orçamento de feitiço de uma ação é o golpe dela dividido por `([\d,]+)`/,'feitiço');
anchor(p26,/mantenha as frações até arredondar o resultado para baixo/,'PV-base sem arredondamento intermediário');
anchor(p26,/use os PV-base da célula, antes dos ajustes de papel, atributos e recursos/,'PV-base');
anchor(p26,/disparos = 1 \+ \(rodadas − 1\) ÷ 3/,'recarga 5–6');
anchor(p26,/disparos × 1,25/,'área da Recarga');
const base=L*n*f[4]/4, golpe=C.golpeAlvo(f,dg), derivadas=C.derivada(nivel);
const refino=derivadas[4], defesa=10+atributos.Destreza+C.protecao(refino);
const defesaFator=(50-5*(defesa-derivadas[1]))/50;
const circDados=Math.floor(multCirc*maiorClasse), curaReacao=circDados*2.5;
const shots=1+(L-1)/3, recFator=(shots*(multRec/2)+(L-shots))/L;
const circFator=1/(1-curaReacao/(n*f[4]/4));
const fatores={papel:C.fatorPapel('Artilheiro',dg,n).vida,defesa:defesaFator,dominio:domain,recarga:recFator,circulacao:circFator,intervencao:C.precoIntervencao(dg,n)};
const pv=C.arred(base*fatores.papel*fatores.defesa/fatores.dominio/fatores.recarga/fatores.circulacao/fatores.intervencao);
const reconstruido=pv*fatores.dominio*fatores.recarga*fatores.circulacao*fatores.intervencao/(fatores.papel*fatores.defesa);
assert(Math.abs(reconstruido-base)<=0.5000001*fatores.dominio*fatores.recarga*fatores.circulacao*fatores.intervencao/(fatores.papel*fatores.defesa),"PV não recompõem a célula dentro do arredondamento");
const quota=n*golpe, custoExt=Math.ceil(multExt*maiorClasse)*cambio+maiorClasse*cambio/L, custoReg=circDados*cambio;
const especial=(strike)=>{
 const budget=strike/perSpell, cl=cls.filter(x=>x[2]<=budget).at(-1);
 if(!cl) return {orcamento:budget,classe:null};
 assert(!cls.some(x=>x[0]>cl[0] && x[2]<=budget),'Não foi usada a maior Classe que cabe');
 return {orcamento:budget,classe:cl[0],leve:cl[3],media:cl[4],pesada:cl[5],clivarDados:Math.floor(budget-cl[5]+cl[4]),teiaDados:Math.floor(budget-2*cl[3])};
};
function recarga(target){
 target=Math.floor(target); let best;
 for(let k=1;k<=200;k++){const fix=target-k*6.5;if(fix<0||!Number.isInteger(fix))continue;
 const err=Math.abs(k*6.5-target*2/3); if(!best||err<best.err)best={err,dados:k,fixo:fix};}
 assert(best); return {media:target,expressao:`${best.dados}d12 + ${best.fixo}`};
}
const modes=[['normal',0],['Extensão',custoExt],['Regravação',custoReg],['ambas',custoExt+custoReg]].map(([nome,custo])=>{
 const hit=C.arred((quota-custo)/n);return {nome,custo,cota:quota-custo,golpe:hit,dados:C.dado(hit),tecnica:especial(hit)};
});
const S={nivel,n,categoria:dg[0],rodadas:L,atributos,refino,defesa,acerto:atributos.Essência+C.maestria(nivel),acertoCorpo:atributos.Força+C.maestria(nivel),cd:derivadas[3],base,fatores,pv,integridade:Math.floor(pv/2),golpe,dados:C.dado(golpe),curaAcao:Math.floor(base/L/n),braco:Math.floor(base/L*2/n),curaReacao,circDados,maiorClasse,cambio,custoExt,custoReg,quota,marcas:Math.floor(atributos.Inteligência/2)+Math.floor(C.maestria(nivel)/2),especial:especial(golpe),chama:recarga(golpe*multRec),intervencao:{media:C.arred(golpe*C.X.INTERVENCAO_EXTRA),dados:C.dado(C.arred(golpe*C.X.INTERVENCAO_EXTRA))},modos:modes};
// Prova construtiva da distribuição: não é uma ficha nova de jogador.
const criacao=[2,2,1,2,3], livres=[[4],[4,4],[1],[3],[2],[3],[3]], rei=[0,1,2,1,0];
const final=criacao.map((v,i)=>v+livres.flat().filter(x=>x===i).length+rei[i]);
assert.deepStrictEqual(final,Object.values(atributos)); assert.equal(criacao.reduce((a,b)=>a+b),10);
assert(final.every(x=>x<=6)); assert.equal(S.curaAcao,Math.floor(f[4]/4)); assert.equal(S.braco,Math.floor(f[4]/2));
assert.equal(C.media(S.dados),golpe);assert(C.temIntervencao(dg,n));
S.provaAtributos={criacao,livres,rei,final,aptidoes:{18:'Energia Reversa',22:'Circulação, escolha com refino',26:'Regravação',30:'Extensão'}};
// Débito corrente aprovado por Mizuki: nem estorno, nem dívida futura.
// O chamador informa ações LEGALMENTE disponíveis; o modelo não cria janelas.
function cobrar(saldos,custo) {
 assert(custo>=0 && saldos.every(x=>x>=0));
 const total=saldos.reduce((a,b)=>a+b,0);
 if(!saldos.length || total+1e-9<custo) return {permitido:false,saldos:[...saldos]};
 const fator=total? (total-custo)/total:0;
 const novos=saldos.map(x=>Math.max(0,x*fator));
 assert(Math.abs(novos.reduce((a,b)=>a+b,0)-(total-custo))<1e-8);
 return {permitido:true,saldos:novos,golpes:novos.map(x=>C.arred(x))};
}
const provas=[];
function caso(nome,saldos,custo,permitido) {
 const antes=JSON.stringify(saldos), r=cobrar(saldos,custo);
 assert.equal(JSON.stringify(saldos),antes,'consulta alterou entrada');
 assert.equal(r.permitido,permitido,nome);
 if(!permitido)assert.deepStrictEqual(r.saldos,saldos,'falha alterou cota');
 provas.push({nome,antes:saldos,custo,...r});return r;
}
caso('Regravação antes de agir',Array(n).fill(golpe),custoReg,true);
caso('Regravação depois de três ações',Array(n-3).fill(golpe),custoReg,true);
caso('Extensão depois de gastar tudo',[],custoExt,false);
caso('Extensão em janela externa com cota e requisitos fornecidos',[golpe],custoExt,true);
caso('Cota insuficiente',[golpe/2],custoReg,false);
caso('Dois braços destruídos antes de cobrar',Array(n-2).fill(golpe),custoReg,true);
const ambos=caso('Duas aptidões na mesma rodada',Array(n).fill(golpe),custoExt+custoReg,true);
const ext=caso('Primeira ativação de Extensão',Array(n).fill(golpe),custoExt,true);
caso('Nova ativação, novo débito de erguer',ext.saldos,maiorClasse*cambio/L,true);
const perda=ext.saldos.slice(1);
assert.equal(perda.length,n-1);assert(perda.every(x=>x===ext.saldos[0]));
provas.push({nome:'Perder braço depois do débito não estorna preço',antes:ext.saldos,depois:perda});
const reg=cobrar(Array(n).fill(golpe),custoReg);
const chamaPos=recarga(C.arred(reg.saldos[0])*multRec);
provas.push({nome:'Regravação seguida de Chama, todas as ações disponíveis',chama:chamaPos,acoesConsumidas:n,saldosDepois:[]});
assert.equal(cobrar([],custoReg).permitido,false);
provas.push({nome:'Nova rodada não recebe dívida',novaCota:quota,divida:0});
S.ensaioDebito=provas;
const fmt=x=>String(x).replace('.',',');
const dice=(count)=>`${Math.floor(count*4.5)} (${count}d8)`;
const e=S.especial;
const md=`# Sukuna — ficha integrada à grade vigente\n\n28/09/2026. Remontagem técnica da escolha autoral: Calamidade ×6, nível 30, Artilheiro. Substitui a ficha de v0.229–v0.242 para consulta de números. Não certifica equilíbrio. A política de débito corrente foi aprovada por Mizuki; aplicação e limites estão no relatório ao lado.\n\n**Defesa ${defesa} · PV ${pv} · Integridade ${S.integridade} · Refino ${refino} · CD ${S.cd}**\n\n**Força 2 · Destreza 4 · Constituição 4 · Inteligência 6 · Essência 6.** Maldição Média; deslocamento 9 m. Físico e Espírito treinados. Ocultismo, Intimidação e Percepção. Sem resistências, imunidades ou vulnerabilidades próprias declaradas.\n\n**Pacto — Chama Divina:** exige ter usado Desmembrar e Clivar; fora do Santuário só pode ser usada quando houver um único oponente na área. Não é um desconto adicional.\n\n## Traços e cura\n\n**Quatro Braços.** Dois braços fazem o Selo enquanto os outros lutam; a boca no abdômen recita. São ${n} ações por turno no total. Cada braço é alvo com Defesa ${defesa} e ${S.braco} PV. Destruir um tira uma ação, pela regra de partes destrutíveis. O traço não concede ações além dessas seis.\n\n**Rei das Maldições.** Quatro pontos de atributo adicionais, já incluídos.\n\n**Energia Reversa.** No lugar de uma ação, recupera ${S.curaAcao} PV próprios.\n\n**Circulação.** Como sua Reação, quando sofre dano, recupera ${curaReacao} (${circDados}d4) PV próprios. Compete com os demais usos da mesma Reação.\n\n**Regravação.** Durante o Rescaldo, uma Ação Bônus encerra o Rescaldo, sem curar PV, e debita ${fmt(custoReg)} da cota de dano daquela rodada. Cada uso deixa uma marca até o descanso longo; com ${S.marcas} marcas, não abre Expansão.\n\n## Ações\n\n**Ações Múltiplas.** Seis ações, reduzidas pelas partes destruídas. Escolhe Desmembrar, Clivar, Teia de Aranha ou troca uma ação por Energia Reversa. No máximo uma Teia por rodada. Chama Divina ocupa as ações múltiplas do turno, sem consumir Bônus, Reação ou Intervenção.\n\n**Desmembrar.** Ataque de conjuração +${S.acerto}, alcance 18 m, um alvo: **${golpe} (${S.dados}) de dano Cortante**. Alcança coisas com ou sem energia amaldiçoada.\n\n**Clivar.** Ataque de conjuração +${S.acerto}, alcance 1,5 m, um alvo com energia amaldiçoada: **${dice(e.clivarDados)} de dano Cortante**, e Impedido. Use o término e os testes da condição nas regras gerais; não foi criada duração própria para o Sukuna.\n\n**Teia de Aranha.** TR Físico CD ${S.cd}, criaturas numa Esfera de raio 3 m a partir do chão tocado: **${dice(e.teiaDados)} de dano de Concussão e Derrubado** na falha; metade do dano e não cai no sucesso.\n\n**Chama Divina (Recarga 5–6).** Exige Desmembrar e Clivar anteriores. TR Físico CD ${S.cd}: **${S.chama.media} (${S.chama.expressao}) de dano de Fogo** na falha; metade no sucesso. Fora do Santuário, Esfera de raio 3 m num ponto a até 18 m, com apenas um oponente na área. Dentro, alcança cada criatura no raio do Santuário. Começa disponível; depois de usada, só volta com 5 ou 6 no d6 no começo do turno.\n\n## Intervenções\n\nTrês por luta, cada uma uma vez; no máximo uma por rodada, logo depois do turno de outra criatura.\n\n**1. Desmembrar Dobrado.** Ataque de conjuração +${S.acerto}, alcance 18 m, um alvo: **${S.intervencao.media} (${S.intervencao.dados}) de dano Cortante**. O nome é preservado; o dano é o da primeira Intervenção vigente, 0,75 de um golpe, e não uma ação integral adicional.\n\n**2. Santuário Malévolo.** Abre a Expansão sem Barreiras com centro fixo no ponto de abertura, raio 200 m, por ${Math.floor(refino/2)} rodadas. Desmembrar e Clivar acertam sem rolagem nem TR em quem estiver dentro; Clivar dispensa o alcance. Sair do raio retira o alvo do Acerto. Aplicam-se disputa, concentração e demais regras de Expansão. Encerrada a Expansão, entra em Rescaldo pelo resto da cena: não usa as ações de técnica, inclusive Chama; preserva a cota em golpes de corpo +${S.acertoCorpo}, alcance 1,5 m, dano de Concussão. Regravação pode encerrar o Rescaldo.\n\n**3. Extensão de Domínio.** Envolve o corpo numa camada de domínio sem técnica por até ${refino} rodadas. Nada que uma Expansão faz o alcança, seja completa, incompleta ou sem barreiras; a barreira ainda o prende e os benefícios do dono permanecem. Anula técnica de contato até Classe ${C.protecao(refino)}; acima desse teto, recebe três quartos do dano. Não cai por golpe. Enquanto ativa, não usa feitiço nem Manejo. Expansão própria já aberta continua; abrir outra derruba a Extensão. Não concede acerto automático aos golpes. A ativação comum da aptidão continua seguindo Bônus no próprio turno ou Reação quando uma Expansão abre; a Intervenção aqui preserva a entrada específica da ficha escolhida.\n\n## Cota com aptidões\n\nA cota normal é ${quota} por rodada (${n} × ${golpe}). Regravação consome ${fmt(custoReg)} na rodada em que é usada. Extensão consome ${fmt(custoExt)} por rodada ligada na montagem com uma ativação por luta: manutenção mais ativação repartida pelas ${L} rodadas de referência. O inimigo não ganhou uma reserva de PE.\n\nEsta tabela é o cálculo de **seis ações ainda disponíveis**, com o custo repartido igualmente antes dos golpes. Não permite pagar retroativamente com ataques já resolvidos.\n\n| Situação | Cota após custo, antes do arredondamento | Golpe simples por ação |\n|---|---:|---|\n${modes.map(m=>`| ${m.nome} | ${fmt(Number(m.cota.toFixed(3)))} | ${m.golpe} (${m.dados}) |`).join('\n')}\n\nCom Extensão, os golpes são de corpo +${S.acertoCorpo}, alcance 1,5 m, dano de Concussão. O arredondamento segue o golpe do gerador; a tabela não é autorização para usar seis ações depois de perder braços. **Débito corrente, aprovado:** cobrar somente das ações ainda legalmente disponíveis naquela rodada. Ações resolvidas não mudam; sem cota suficiente, a aptidão não é ativada naquela janela. Não há dívida para a rodada seguinte. Essa restrição também vale fora do turno: ter Reação ou Intervenção não fornece cota de dano. A cobrança não conserva ações expiradas nem autoriza ações fora de sua janela.\n\nMantenha a cota exata, antes do arredondamento do golpe. Cada ação resolvida consome sua parcela orçada, independentemente de erro, bloqueio, dano rolado ou de ter sido usada para curar. Destruir um braço retira uma das ações ainda disponíveis quando cabível, sem desfazer uma resolução nem devolver custos. Aplique o custo às parcelas restantes; só depois arredonde o golpe e recalcule os preços da técnica. Perder uma ação depois do débito perde também a parcela que ela carregava, sem reembolso.\n\nNova ativação paga novamente a parcela de erguer da montagem (${fmt(maiorClasse*cambio/L)}); ela não ganha isenção por ter sido desligada. A manutenção da Extensão permanece cobrada nas rodadas ligadas, pela fórmula de montagem já declarada. Amortização é método de precificação, não dívida de uma rodada para outra.\n\n**Exemplos derivados:** Regravação antes de seis ações deixa golpe ${modes[2].golpe}; depois de três ações normais, as três restantes ficam em ${C.arred((3*golpe-custoReg)/3)}. Com dois braços destruídos antes da cobrança, as quatro restantes ficam em ${C.arred((4*golpe-custoReg)/4)}. Com a cota toda gasta, Extensão é recusada naquela janela. Se Regravação preceder Chama e todas as ações múltiplas ainda estiverem disponíveis, a Chama usa o golpe recalculado: ${chamaPos.media} (${chamaPos.expressao}); ela ocupa todas essas ações, não sucede ataques múltiplos já usados no turno.\n\nO ensaio em SAIDA-sukuna-grade.json confere a cobrança e a ausência de devolução/dívida. Não é playtest nem mede a dificuldade real do encontro.\n`;
const files={'SAIDA-sukuna-grade.json':JSON.stringify(S,null,2)+'\n','SUKUNA-GRADE-ATUAL.md':md};
if(process.argv.includes('--check')){
 for(const [name,body] of Object.entries(files))assert.equal(fs.readFileSync(path.join(__dirname,name),'utf8'),body,`${name} diverge dos donos; regenere e revise`);
 console.log('Sukuna: fontes lidas, PV/cura/partes/técnicas/atributos reproduzidos; arquivos sincronizados. Não é teste de equilíbrio.');
}else if(process.argv.includes('--json')) console.log(JSON.stringify(S,null,2));
else { for(const [name,body] of Object.entries(files))fs.writeFileSync(path.join(__dirname,name),body); console.log(JSON.stringify(S,null,2)); }
