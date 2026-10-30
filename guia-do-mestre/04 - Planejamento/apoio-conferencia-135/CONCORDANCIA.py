"""Concordância por regra: reúne, de todo o conjunto revisto, as frases que afirmam algo sobre cada regra,
para ler lado a lado e achar contradição entre capítulos, casos e consultas."""
from pathlib import Path
import re, json
A = Path(__file__).resolve().parent; S = A.parents[1] / '06 - Redacao do Guia/revisao-98'
files = sorted([p for p in S.glob('*.md') if p.name != 'LEIA-ME.md'] + list((S/'casos').glob('*.md')) + list((S/'consultas').glob('*.md')))
T = {
 'Insistir/Aguentar': r'\bInsist|\bAguent', 'Estabilizar': r'Estabiliz', 'Janela de socorro': r'janela|\bSequela',
 'Bloquear/Aparar/Brecha': r'\bBloque|\bApar[ae]r?\b|\bBrecha', 'Iniciativa e empate': r'iniciativa',
 'Desengajar/oportunidade': r'Desengaj|ataque de oportunidade', 'Cobertura': r'[Cc]obertura',
 'Estudar/Ler o Ambiente': r'\bEstudar\b|Ler o Ambiente', 'Teste em grupo/Ajudar': r'teste em grupo|\bAjudar\b|travessia coletiva',
 'Dedicação 28 horas': r'28 horas|horas novas|ciclo de sete dias|saldo', 'XP e recompensa': r'\bXP\b|experiência semanal|remunera',
 'Descanso': r'descanso (curto|longo)', 'Doma': r'\bDoma\b|domar|domad', 'Promessa': r'Promessa', 'Overtime': r'Overtime',
 'Integridade': r'Integridade', 'Energia Reversa/cura': r'Energia Reversa', 'Cortina': r'\bCortina\b',
 'Patente/Grau': r'\bGrau [0-9]|patente', 'Morte permanente': r'morte permanente|morte automática',
 'Queda/salto': r'\bqueda\b|\bsalt[oa]', 'Carga/Volume': r'\bVolume\b|\bCarga\b', 'Reação': r'\bReaç(ão|ões)\b',
 'Selo': r'\bSelo\b', 'Classe do feitiço/PE': r'Classe [0-9][^.]{0,40}\b[0-9]+ PE',
}
sent = lambda t: [s.strip() for s in re.split(r'(?<=[.!?])\s+|\n+', re.sub(r'\]\(<?[^)]*\)', ']', t)) if s.strip()]
out = {}
for k, rx in T.items():
    out[k] = [(p.relative_to(S).as_posix(), s) for p in files for s in sent(p.read_text()) if re.search(rx, s)]
(A / 'concordancia.json').write_text(json.dumps(out, ensure_ascii=False, indent=0))
for k, v in out.items(): print(k, len(v), len({f for f, _ in v}))
