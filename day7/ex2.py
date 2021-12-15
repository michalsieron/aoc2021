with open("test_data.txt", "r") as fd:
    data = list(map(int, fd.read().strip().split(",")))


def cost(f, t):
    diff = abs(f - t) + 1
    return int(diff * (diff - 1) / 2)


mean = round(sum(data) / len(data))
answer = min(
    sum(cost(p, mean + i) for p in data)
    for i in (-1, 0, 1)
)

print(answer)
