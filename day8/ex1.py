with open("test_data.txt", "r") as fd:
    data = fd.read().split()


answer = sum(
    int(len(pattern) in (2, 3, 4, 7))
    for pattern in data
) - data.count("|") * 4

print(answer)
