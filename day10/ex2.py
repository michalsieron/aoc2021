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

rev_brace_points = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

points = []
for line in data:
    stack = []
    for brace in line:
        if brace in brace_pairs.keys():
            stack.append(brace)
        elif brace in brace_pairs.values():
            popped = stack.pop()
            if brace_pairs[popped] != brace:
                break
    else:
        if len(stack) > 0:
            line_points = 0
            for unclosed in reversed(stack):
                line_points *= 5
                line_points += rev_brace_points[unclosed]
            points.append(line_points)

print(sorted(points)[len(points) // 2])
