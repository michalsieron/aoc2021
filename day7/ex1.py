with open("test_data.txt", "r") as fd:
    data = list(map(int, fd.read().strip().split(",")))

median = sorted(data)[len(data) // 2]
answer = sum(abs(p - median) for p in data)
print(answer)
