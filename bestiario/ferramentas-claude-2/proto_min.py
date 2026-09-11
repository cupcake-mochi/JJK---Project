import re, os, math, docx
_R = '/media/mizuki/HD Externo II/Claude/Claude 2'
def _mb(x): return math.ceil(x - 0.5) if abs(x % 1 - 0.5) < 1e-9 else round(x)
_MAN = {}
for _t in docx.Document(os.path.join(_R, 'manual/Fundamento-MANUAL-v7.docx')).tables:
    _cab = [c.text.strip() for c in _t.rows[0].cells]
    if _cab and _cab[0].startswith('Nível do grupo') and 'Chefe: dano' in _cab:
        for _r in _t.rows[1:]:
            _v = [c.text.strip() for c in _r.cells]; _vd = _v[2].split(' a ')
            _MAN[int(_v[0])] = (float(_v[1].replace('~', '')), (int(_vd[0]) + int(_vd[-1])) / 2, float(_v[3]))
        break
_CAM = re.findall(r'\|\s*\*\*(\w+)\*\*\s*\|\s*d(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|', open(os.path.join(_R, 'sistema/03-mecanica/01-atributos-acerto-defesa.md'), encoding='utf-8').read())
_V1 = sum(int(c[2]) for c in _CAM) / 5; _VN = sum(int(c[3]) for c in _CAM) / 5
def simula(saida, corpos):
    vs = [list(c) for c in corpos]; rod = 0; cob = 0.0
    while vs and rod < 100:
        cob += sum(c[1] for c in vs); sobra = saida
        while sobra > 0 and vs:
            if vs[0][0] <= sobra: sobra -= vs.pop(0)[0]
            else: vs[0][0] -= sobra; sobra = 0
        rod += 1
    return rod, cob
S30, CV30, CD30 = _MAN[30]; KV30, KD30 = math.floor(S30 / 4), _mb(CD30 * 0.25); VG30 = 4 * (_V1 + _VN * 29 + 3 * 30)
