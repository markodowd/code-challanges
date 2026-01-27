total = 0

with open("./input.txt", "r") as file:
    for line in file:
        clean_line = line.strip()

        values = [0] * 12
        pointer = 0

        for i in range(len(values)):
            highest = 0

            for j in range(pointer, len(clean_line) - ((12 - 1) - i)):
                value = int(clean_line[j])

                if value > highest:
                    highest = value
                    pointer = j

            values[i] = highest
            pointer += 1

        total += int("".join(map(str, values)))

print(total)
