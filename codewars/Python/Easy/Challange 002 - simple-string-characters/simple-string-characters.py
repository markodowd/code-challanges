def solve(s):
    upper = []
    lower = []
    numbers = []
    special = []

    for char in s:
        if char.isupper():
            upper.append(char)
        elif char.islower():
            lower.append(char)
        elif char.isnumeric():
            numbers.append(char)
        else:
            special.append(char)

    return [len(upper)] + [len(lower)] + [len(numbers)] + [len(special)]
