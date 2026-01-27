ENTRY = "S"
SPLITTER = "^"

total = 0
valid_indicies = set()

with open("./input.txt", "r") as file:
    content = file.readlines()

    valid_indicies.add(content[0].index(ENTRY))

    for i in range(1, len(content)):
        charet_indicies = [i for i, c in enumerate(content[i]) if c == SPLITTER]

        if len(charet_indicies) == 0:
            continue

        for val in charet_indicies:
            if val in valid_indicies:
                total += 1

                valid_indicies.remove(val)

                valid_indicies.add(val - 1)
                valid_indicies.add(val + 1)


print(total)
