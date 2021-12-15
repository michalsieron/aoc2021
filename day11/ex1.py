with open("test_data.txt", "r") as fd:
    data = [
        [int(o) for o in line]
        for line in fd.read().splitlines()
    ]
    data = [
        [float("-inf"), *row, float("-inf")]
        for row in data
    ]
    data = [[float("-inf") for _ in data[0]]] + data + [[float("-inf") for _ in data[0]]]

flashes = 0
STEPS = 100

for row in data:
    for x in row:
        print(x if x >= 0 else "X", end=" ")
    print()

for _ in range(STEPS):
    for y, row in enumerate(data):
        for x, v in enumerate(row):
            data[y][x] += 1

    is_flashing = [
        [v > 9 for v in row]
        for row in data
    ]

    while any(any(row) for row in is_flashing):
        for y, row in enumerate(data):
            for x, v in enumerate(row):
                if is_flashing[y][x]:
                    is_flashing[y][x] = False
                    flashes += 1
                    for i in (-1, 0, 1):
                        for j in (-1, 0, 1):
                            data[y+i][x+j] += 1
                            if data[y+i][x+j] == 10:
                                is_flashing[y+i][x+j] = True
    

    for y, row in enumerate(data):
        for x, v in enumerate(row):
            data[y][x] = 0 if v > 9 else v


print(flashes)
