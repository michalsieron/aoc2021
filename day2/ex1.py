with open("test_data.txt", "r") as fd:
    data = fd.read().splitlines()


final = {
    "forward": 0,
    "down": 0,
    "up": 0,
}

for line in data:
    instruction, value = line.split()
    final[instruction] += int(value)


horizontal = final["forward"]
depth = final["down"] - final["up"]

answer = horizontal * depth
print("answer:", answer)
