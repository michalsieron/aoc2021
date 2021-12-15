with open("test_data.txt", "r") as fd:
    data = fd.read().splitlines()

caves = {}
for line in data:
    c1, c2 = line.split("-")
    caves.setdefault(c1, []).append(c2)
    caves.setdefault(c2, []).append(c1)


def dfs(edges, current, repeated):
    ret = 0
    for c in caves[current[-1]]:
        if c == "end":
            ret += 1
        elif c.isupper() or c not in current:
            ret += dfs(caves, [*current, c], repeated)
        elif not repeated and c != "start":
            ret += dfs(caves, [*current, c], True)

    return ret


print(dfs(caves, ["start"], False))
