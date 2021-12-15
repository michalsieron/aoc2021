with open("test_data.txt", "r") as fd:
    data = fd.read().splitlines()

template = data[0]
counter = {e: template.count(e) for e in template}

polymer = {}
for a, b in zip(template, template[1:]):
    polymer[(a, b)] = polymer.get((a, b), 0) + 1

rules = {}
for line in data[2:]:
    pair, new = line.split(" -> ")
    rules[tuple(pair)] = new

steps = 10
for s in range(steps):
    new_polymer = {}
    for (a, b), ab_count in polymer.items():
        c = rules[(a, b)]

        new_polymer[(a, c)] = new_polymer.get((a, c), 0) + ab_count
        new_polymer[(c, b)] = new_polymer.get((c, b), 0) + ab_count
        counter[c] = counter.get(c, 0) + ab_count

    polymer = new_polymer


most = max(counter.values())
least = min(counter.values())
print(most - least)
