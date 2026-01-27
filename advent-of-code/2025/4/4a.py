ROLL = "@"

matrix: list[str] = []
accessable_rolls = 0

with open("./input.txt", "r") as file:
    for line in file:
        matrix.append(line.strip())


rows = len(matrix)
cols = len(matrix[0])

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] != ROLL:
            continue

        adjacent_rolls = 0

        for di in [-1, 0, 1]:
            for dj in [-1, 0, 1]:
                if di == 0 and dj == 0:
                    continue

                ni, nj = i + di, j + dj

                if 0 <= ni < rows and 0 <= nj < cols:
                    if matrix[ni][nj] == ROLL:
                        adjacent_rolls += 1

        if adjacent_rolls < 4:
            accessable_rolls += 1


print(accessable_rolls)
