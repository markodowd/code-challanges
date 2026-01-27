import re

#
# PART 1
#

results = []


def calculate_results(text) -> None:
    pattern = r"mul\(\d+,\d+\)"

    matches = re.findall(pattern, line)

    for match in matches:
        numbers = re.search(r"mul\((\d+),(\d+)\)", match)

        num1 = int(numbers.group(1))
        num2 = int(numbers.group(2))

        results.append(num1 * num2)


with open("input.txt", "r") as file:
    for line in file:
        calculate_results(line)


print("Total: ", sum(results))


#
# PART 2
#

conditional_results = []


def calculate_conditional_results(text) -> None:
    instructions_enabled = True

    enable = "do()"
    disable = "don't()"

    pattern = r"(do\(\)|don't\(\))|mul\((\d+),(\d+)\)"

    matches = re.findall(pattern, text)

    for match in matches:
        if match[0] == enable:
            instructions_enabled = True

        elif match[0] == disable:
            instructions_enabled = False

        else:
            if instructions_enabled:
                num1 = int(match[1])
                num2 = int(match[2])

                conditional_results.append(num1 * num2)


with open("input.txt", "r") as file:
    content = file.read()
    calculate_conditional_results(content)


print("Total Conditional: ", sum(conditional_results))

