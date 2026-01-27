total = 0

with open("./input.txt", "r") as file:
    for line in file:
        largest_primary = 0
        largest_secondary = 0

        l_ptr = 0

        for i in range(len(line) - 2):
            value = int(line[i])

            if value > largest_primary:
                largest_primary = value
                l_ptr = i

        for i in range(l_ptr + 1, len(line) - 1):
            value = int(line[i])

            if value > largest_secondary:
                largest_secondary = value

        total += int(str(largest_primary) + str(largest_secondary))


print(total)
