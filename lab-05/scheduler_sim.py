#!/usr/bin/env python3
import collections

# Базовий набір процесів
procs = [
    {"id": 1, "arrival": 0, "burst": 5},
    {"id": 2, "arrival": 1, "burst": 3},
    {"id": 3, "arrival": 2, "burst": 1},
    {"id": 4, "arrival": 4, "burst": 2},
]

def report(name, sched):
    print(name)
    sched = sorted(sched, key=lambda p: p["id"])
    ws, ts, rs = [], [], []
    for p in sched:
        w = p["finish"] - p["arrival"] - p["burst"]
        t = p["finish"] - p["arrival"]
        r = p["start"] - p["arrival"]
        ws.append(w)
        ts.append(t)
        rs.append(r)
        print(f'  P{p["id"]}: start={p["start"]} finish={p["finish"]}  '
              f'W={w} T={t} R={r}')
    n = len(sched)
    print(f'  Середнє: W={sum(ws) / n:.2f}  T={sum(ts) / n:.2f}  '
          f'R={sum(rs) / n:.2f}')

def fcfs(proc_list=None):
    if proc_list is None:
        proc_list = procs
    out, time = [], 0
    for p in sorted(proc_list, key=lambda x: x["arrival"]):
        time = max(time, p["arrival"])
        out.append({
            "id": p["id"],
            "arrival": p["arrival"],
            "burst": p["burst"],
            "start": time,
            "finish": time + p["burst"]
        })
        time += p["burst"]
    report("FCFS", out)

def sjf(proc_list=None):
    if proc_list is None:
        proc_list = procs
    left = list(proc_list)
    out, time = [], 0
    while left:
        ready = [p for p in left if p["arrival"] <= time]
        if not ready:
            time = min(p["arrival"] for p in left)
            ready = [p for p in left if p["arrival"] <= time]
        p = min(ready, key=lambda x: (x["burst"], x["arrival"], x["id"]))
        out.append({
            "id": p["id"],
            "arrival": p["arrival"],
            "burst": p["burst"],
            "start": time,
            "finish": time + p["burst"]
        })
        time += p["burst"]
        left.remove(p)
    report("SJF (невитискальний)", out)

def rr(q=2, proc_list=None):
    if proc_list is None:
        proc_list = procs
    p_sorted = sorted(proc_list, key=lambda x: x["arrival"])
    out = {p["id"]: {"id": p["id"], "arrival": p["arrival"], "burst": p["burst"]} for p in p_sorted}
    rem = {p["id"]: p["burst"] for p in p_sorted}
    start = {}
    finish = {}
    queue = collections.deque()
    arrived = 0
    time = 0
    done = set()

    while len(done) < len(p_sorted):
        while arrived < len(p_sorted) and p_sorted[arrived]["arrival"] <= time:
            queue.append(p_sorted[arrived])
            arrived += 1
        if not queue:
            time = p_sorted[arrived]["arrival"]
            continue
        p = queue.popleft()
        if p["id"] not in start:
            start[p["id"]] = time
        run = min(rem[p["id"]], q)
        rem[p["id"]] -= run
        time += run
        while arrived < len(p_sorted) and p_sorted[arrived]["arrival"] <= time:
            queue.append(p_sorted[arrived])
            arrived += 1
        if rem[p["id"]] == 0:
            finish[p["id"]] = time
            done.add(p["id"])
        else:
            queue.append(p)

    sched = []
    for p in p_sorted:
        out[p["id"]]["start"] = start[p["id"]]
        out[p["id"]]["finish"] = finish[p["id"]]
        sched.append(out[p["id"]])
    report(f"Round-Robin (q={q})", sched)

if __name__ == "__main__":
    print("=== БАЗОВИЙ НАБІР (4 ПРОЦЕСИ) ===")
    fcfs()
    sjf()
    rr(q=2)

    print("\n=== ВПЛИВ КВАНТА (Q=1, Q=2, Q=4) ===")
    rr(q=1)
    rr(q=2)
    rr(q=4)

    print("\n=== НАБІР ІЗ 5 ПРОЦЕСАМИ (ДОДАНО P5) ===")
    procs5 = list(procs) + [{"id": 5, "arrival": 3, "burst": 4}]
    fcfs(procs5)
    sjf(procs5)
    rr(q=2, proc_list=procs5)
