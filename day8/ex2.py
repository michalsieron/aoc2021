with open("test_data.txt", "r") as fd:
    data = fd.read().splitlines()

answer = 0
for line in data:
    input_patterns, output_patterns = line.split(" | ")
    input_patterns = input_patterns.split()
    output_patterns = output_patterns.split()

    mapping = [None for n in range(10)]
    
    for pattern in input_patterns:
        pattern_set = set(pattern)

        if len(pattern) == 2:
            mapping[1] = pattern_set
        elif len(pattern) == 3:
            mapping[7] = pattern_set
        elif len(pattern) == 4:
            mapping[4] = pattern_set
        elif len(pattern) == 7:
            mapping[8] = pattern_set

    for pattern in input_patterns:
        pattern_set = set(pattern)

        common_bd = len(pattern_set & (mapping[4] - mapping[1]))
        common_cf = len(pattern_set & mapping[1])

        if len(pattern) == 5:
            if common_cf == 2:
                mapping[3] = pattern_set
            elif common_bd == 2:
                mapping[5] = pattern_set
            else:
                mapping[2] = pattern_set
        elif len(pattern) == 6:
            if common_bd == 1:
                mapping[0] = pattern_set
            elif common_cf == 1:
                mapping[6] = pattern_set
            else:
                mapping[9] = pattern_set

    reverse_mapping = {frozenset(mapping[i]): i for i in range(10)}

    answer += int("".join(
        str(reverse_mapping[frozenset(pattern)])
        for pattern in output_patterns
    ))

print(answer)
