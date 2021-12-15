with open("data.txt", "r") as fd:
    data = [
        [int(h) for h in line]
        for line in fd.read().splitlines()
    ]
    data = [
        [9, *row, 9]
        for row in data
    ]
    data = [[9 for _ in data[0]]] + data + [[9 for _ in data[0]]]


answer = 0
for y, row in enumerate(data[1:-1], 1):
    for x, h in enumerate(row[1:-1], 1):
        neighbours = [data[y-1][x], data[y][x-1], data[y][x+1], data[y+1][x]]
        if min(h, *neighbours) == h and neighbours.count(h) == 0:
            answer += h + 1

print(answer)
