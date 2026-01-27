ROLL = "@"
EMPTY_SPACE = "."

matrix = []

with open("./input.txt") as f:
    for line in f:
        matrix.append(list(line.strip()))

rows = len(matrix)
cols = len(matrix[0])

total_rolls_removed = 0

while True:
    rolls_to_remove = []

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != ROLL:
                continue

            adjacent_rolls = 0

            for di in (-1, 0, 1):
                for dj in (-1, 0, 1):
                    if di == 0 and dj == 0:
                        continue

                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        if matrix[ni][nj] == ROLL:
                            adjacent_rolls += 1

            if adjacent_rolls < 4:
                rolls_to_remove.append((i, j))

    if not rolls_to_remove:
        break

    for i, j in rolls_to_remove:
        matrix[i][j] = EMPTY_SPACE

    total_rolls_removed += len(rolls_to_remove)


print(total_rolls_removed)
