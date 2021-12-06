with open("test_data.txt", "r") as fd:
    data = []
    for line in fd.read().splitlines():
        p1, p2 = line.split(" -> ")
        x1, y1 = map(int, p1.split(","))
        x2, y2 = map(int, p2.split(","))

        data.append((x1, y1, x2, y2))


size = max(max(l) for l in data) + 1
field = [[0 for _ in range(size)] for _ in range(size)]

for x1, y1, x2, y2 in data:
    if y1 == y2: # row
        sx, gx = sorted((x1, x2))
        for x in range(sx, gx + 1):
            field[y1][x] += 1
    elif x1 == x2: # column
        sy, gy = sorted((y1, y2))
        for y in range(sy, gy + 1):
            field[y][x1] += 1


answer = sum(sum(1 for v in row if v > 1) for row in field)
print(answer)
