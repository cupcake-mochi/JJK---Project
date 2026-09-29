#!/usr/bin/env python3
"""Conta as rodadas de cada combate do FIREBALL (Zhu et al., ACL 2023, CC-BY-4.0).

O FIREBALL e o registro de ~25 mil combates reais de D&D 5e jogados no Discord com o
bot Avrae (ago-nov 2022). Cada evento `combat_state_update` traz o numero da rodada e a
lista de combatentes (tipo `player`, `monster` ou `group`).

Este script le o tarball publico em fluxo (sem salvar os 7,7 GB), e para cada combat_id
guarda: a maior rodada, quantos `player` com ficha (PJ) e quantos monstros apareceram,
a soma do PV maximo dos monstros, se houve evento `combat_end`, o numero de acoes
automatizadas (`automation_run`) e o tempo de relogio entre o 1o e o ultimo evento.

Saida: fireball-combates.csv (uma linha por combate), na mesma pasta deste script.

Uso:  python3 conta-fireball-rodadas.py [URL-ou-arquivo-local]
"""
import csv
import gzip
import io
import json
import os
import subprocess
import sys
import tarfile

URL = "https://datasets.mechanus.zhu.codes/fireball-anonymized-nov-28-2022-kfdjl.tar.gz"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fireball-combates.csv")


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else URL
    if src.startswith("http"):
        proc = subprocess.Popen(["curl", "-s", src], stdout=subprocess.PIPE)
        stream = proc.stdout
    else:
        stream = open(src, "rb")
    tf = tarfile.open(fileobj=stream, mode="r|gz")
    C = {}
    nfiles = 0
    for m in tf:
        if not (m.isfile() and "/data/" in m.name and m.name.endswith(".jsonl.gz")):
            continue
        f = tf.extractfile(m)
        raw = f.read()
        nfiles += 1
        try:
            lines = gzip.decompress(raw).decode("utf-8", "replace").splitlines()
        except Exception:
            continue
        for line in lines:
            if not line:
                continue
            try:
                e = json.loads(line)
            except Exception:
                continue
            cid = e.get("combat_id")
            if cid is None:
                continue
            et = e.get("event_type")
            ts = e.get("timestamp")
            c = C.get(cid)
            if c is None:
                c = C[cid] = {"maxr": 0, "pcs": set(), "mons": {}, "ended": 0,
                              "acts": 0, "t0": ts, "t1": ts, "upd": 0}
            if isinstance(ts, (int, float)):
                if c["t0"] is None or ts < c["t0"]:
                    c["t0"] = ts
                if c["t1"] is None or ts > c["t1"]:
                    c["t1"] = ts
            if et == "combat_end":
                c["ended"] = 1
            elif et == "automation_run":
                c["acts"] += 1
            elif et == "combat_state_update":
                d = e.get("data") or {}
                c["upd"] += 1
                try:
                    r = int(d.get("round") or 0)
                except Exception:
                    r = 0
                if r > c["maxr"]:
                    c["maxr"] = r
                cs = d.get("combatants") or []
                if isinstance(cs, str):
                    try:
                        cs = json.loads(cs)
                    except Exception:
                        cs = []
                stack = list(cs)
                while stack:
                    x = stack.pop()
                    if not isinstance(x, dict):
                        continue
                    t = x.get("type")
                    if t == "group":
                        stack.extend(x.get("combatants") or [])
                    elif t == "player" and x.get("character_id") is not None:
                        c["pcs"].add(x.get("id"))
                    elif t == "monster":
                        hp = x.get("max_hp")
                        c["mons"][x.get("id")] = hp if isinstance(hp, (int, float)) else 0
        if nfiles % 200 == 0:
            print(f"{nfiles} arquivos, {len(C)} combates", file=sys.stderr, flush=True)
    with open(OUT, "w", newline="") as fo:
        w = csv.writer(fo)
        w.writerow(["combat_id", "max_round", "n_pc", "n_monsters", "monster_hp_total",
                    "ended_event", "automation_runs", "state_updates", "wallclock_s"])
        for cid, c in C.items():
            dur = (c["t1"] - c["t0"]) if isinstance(c["t0"], (int, float)) and isinstance(c["t1"], (int, float)) else ""
            w.writerow([cid, c["maxr"], len(c["pcs"]), len(c["mons"]), sum(c["mons"].values()),
                        c["ended"], c["acts"], c["upd"], dur])
    print(f"FIM: {nfiles} arquivos, {len(C)} combates -> {OUT}", file=sys.stderr)


if __name__ == "__main__":
    main()
