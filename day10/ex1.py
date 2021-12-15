with open("test_data.txt", "r") as fd:
    data = fd.read().splitlines()

brace_pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

brace_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

points = 0
for line in data:
    stack = []
    for brace in line:
        if brace in brace_pairs.keys():
            stack.append(brace)
        elif brace in brace_pairs.values():
            popped = stack.pop()
            if brace_pairs[popped] != brace:
                points += brace_points[brace]
                break

print(points)
