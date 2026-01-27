MULTIPLY_OPERATOR = "*"
ADDITION_OPERATOR = "+"
total = 0


def clean_rows(lines):
    cleaned_rows = []

    for i in range(5):
        cleaned = [item for item in lines[i].split(" ") if item != ""]
        cleaned_rows.append(cleaned)

    return cleaned_rows


with open("./input.txt", "r") as file:
    rows = file.read().splitlines()
    rows = clean_rows(rows)

    operators = rows[-1]

    for i in range(len(rows[0])):
        running_total = 0
        operator = operators[i]

        for j in range(len(rows) - 1):
            if j == 0:
                running_total = int(rows[j][i])
                continue

            if operator == MULTIPLY_OPERATOR:
                running_total *= int(rows[j][i])

            if operator == ADDITION_OPERATOR:
                running_total += int(rows[j][i])

        total += running_total
        running_total = 0


print(total)
