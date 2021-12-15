def print_sheet(sheet):
    for line in sheet:
        for v in line:
            print("#" if v else " ", end="")
        print()


def transpose_sheet(sheet):
    return [list(column) for column in zip(*sheet)]
    

def fold_sheet_y(sheet, where):
    if where < len(sheet) / 2: # flip it
        sheet = sheet[::-1]
        where = len(sheet) - where - 1
    
    new_sheet = []
    for i, line_below in enumerate(sheet[where+1:]):
        line_above = sheet[where - i - 1]
        new_sheet.append([a or b for a, b in zip(line_above, line_below)])
    
    left = len(sheet) - 2 * len(new_sheet) - 1
    new_sheet.extend(sheet[:left][::-1])
    return new_sheet[::-1]


def fold_sheet(sheet, axis_where):
    axis, where = axis_where.split("=")
    where = int(where)

    if axis == "y":
        return fold_sheet_y(sheet, where)
    elif axis == "x":
        return transpose_sheet(fold_sheet_y(transpose_sheet(sheet), where))


with open("test_data.txt", "r") as fd:
    positions, folds = fd.read().split("\n\n")
    positions = positions.splitlines()
    folds = folds.splitlines()

for i, line in enumerate(positions):
    x, y = line.split(",")
    positions[i] = (int(x), int(y))

max_x = max(positions, key=lambda p: p[0])[0]
max_y = max(positions, key=lambda p: p[1])[1]
sheet = [
    [False for _ in range(max_x + 1)]
    for _ in range(max_y + 1)
]

for x, y in positions:
    sheet[y][x] = True

visible = sum(
    line.count(True)
    for line in fold_sheet(sheet, folds[0].split()[-1])
)
print(visible)

for fold in folds:
    axis_where = fold.split()[-1]
    sheet = fold_sheet(sheet, axis_where)

print()
print_sheet(sheet)
