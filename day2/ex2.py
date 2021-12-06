with open("test_data.txt", "r") as fd:
    data = fd.read().splitlines()


horizontal = 0
depth = 0
aim = 0

for line in data:
    instruction, value_str = line.split()
    value = int(value_str)

    if instruction == "forward":
        horizontal += value
        depth += aim * value
    elif instruction == "down":
        aim += value
    elif instruction == "up":
        aim -= value


answer = horizontal * depth
print("answer:", answer)
