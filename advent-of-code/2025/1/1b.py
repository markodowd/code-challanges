count = 0
position = 50

with open("./input.txt", "r") as file:
    for line in file:
        instruction = line.strip()
        direction = instruction[0]
        rotation = int(instruction[1:])

        while rotation > 0:
            if direction == "L":
                position -= 1

            if direction == "R":
                position += 1

            if position == 100:
                position = 0

            if position == 0:
                count += 1

            if position == -1:
                position = 99

            rotation -= 1


print(count)
