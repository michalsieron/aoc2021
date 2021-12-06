with open("test_data.txt", "r") as fd:
    data = fd.read().splitlines()


def ex2(arr, op):
    left = list(arr)
    i = 0
    while len(left) > 1:
        c = str(int(op(sum({"0": -1, "1": 1}[l[i]] for l in left), 0)))
        left = [l for l in left if l[i] == c]
        i += 1

    return left[0]


oxygen = ex2(data, lambda a, b: a >= b)
co2 = ex2(data, lambda a, b: a < b)

print(int(oxygen, 2) * int(co2, 2))
