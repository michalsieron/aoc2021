with open("test_data.txt", "r") as fd:
    data = fd.read().splitlines()

window_size = 1
answer = sum(a < b for a, b in zip(data, data[window_size:]))
print("answer:", answer)
