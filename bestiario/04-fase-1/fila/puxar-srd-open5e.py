import json, subprocess, time

def get(url):
    for attempt in range(4):
        p = subprocess.run(["curl","-sL","--max-time","120",url], capture_output=True, text=True)
        if p.returncode == 0 and p.stdout.strip().startswith("{"):
            return json.loads(p.stdout)
        print("retry", attempt, p.returncode, p.stdout[:200])
        time.sleep(3)
    raise SystemExit("failed " + url)

for doc in ["srd-2024", "srd-2014"]:
    out = []
    url = f"https://api.open5e.com/v2/creatures/?document__key={doc}&limit=50"
    while url:
        d = get(url)
        out.extend(d["results"])
        url = d.get("next")
        print(doc, len(out), "/", d.get("count"), flush=True)
    with open(f"{doc}.json", "w") as f:
        json.dump(out, f)
    print("SAVED", doc, len(out))
