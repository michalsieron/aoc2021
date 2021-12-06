with open("test_data.txt", "r") as fd:
    data = list(map(int, fd.read().strip().split(",")))
    fish_count = [data.count(d) for d in range(9)]

days = 18
for _ in range(days):
    fish_count = fish_count[1:] + fish_count[:1]
    fish_count[6] += fish_count[8]

print("answer:", sum(fish_count))
