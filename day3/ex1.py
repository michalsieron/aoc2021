with open("test_data.txt", "r") as fd:
    data = fd.read().splitlines()


epsilon = "".join(
    max("1", "0", key=column.count)
    for column in zip(*data)
)
gamma = epsilon.translate({ord("0"): "1", ord("1"): "0"})

print(int(epsilon, 2) * int(gamma, 2))

# minified version
# e="".join(max("10",key=c.count)for c in zip(*open("data.txt")))[:-1]
# print(int(e,2)*int(e.translate({48:49,49:48}),2))
