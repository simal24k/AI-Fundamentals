#Beam Search
def h(n):
    return abs(20 - n)

ops = [lambda x: x + 2, lambda x: x + 3, lambda x: x * 2]

beam = [{"val": 1, "path": [1]}]
k    = 2
goal = 20

level = 0
while beam:
    print(f"Level {level}: {[s['val'] for s in beam]}")

    if any(s["val"] == goal for s in beam):
        found = next(s for s in beam if s["val"] == goal)
        print(f"\nGoal reached!")
        print(f"Path: {found['path']}")
        break

    next_states = []
    seen = set()
    for s in beam:
        for op in ops:
            nv = op(s["val"])
            if nv <= goal and nv not in seen:
                seen.add(nv)
                next_states.append({"val": nv, "path": s["path"] + [nv]})

    next_states.sort(key=lambda s: h(s["val"]))
    beam = next_states[:k]
    level += 1
