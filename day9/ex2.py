with open("data.txt", "r") as fd:
    data = [
        [-1 if h == '9' else 0 for h in line]
        for line in fd.read().splitlines()
    ]
    data = [
        [-1, *row, -1]
        for row in data
    ]
    data = [[-1 for _ in data[0]]] + data + [[-1 for _ in data[0]]]

basin = 1
basin_sizes = {1: 0}

while sum(row.count(0) for row in data):
    changed = False
    for y, row in enumerate(data[1:-1], 1):
        for x, h in enumerate(row[1:-1], 1):
            doesnt_belong_to_any_basin = h == 0
            is_current_basin_new = basin_sizes[basin] == 0
            neighbours_current_basin = basin in (data[y-1][x], data[y][x-1], data[y][x+1], data[y+1][x])
            if doesnt_belong_to_any_basin and (is_current_basin_new or neighbours_current_basin):
                data[y][x] = basin
                basin_sizes[basin] += 1
                changed = True

    if not changed:
        basin += 1
        basin_sizes[basin] = 0

max3_sizes = sorted(basin_sizes.values())[-3:]
answer = max3_sizes[0] * max3_sizes[1] * max3_sizes[2]
print(answer)
