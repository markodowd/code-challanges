available_ingredients = 0

with open("./input.txt", "r") as f:
    content = f.read()
    parts = content.strip().split("\n\n")
    ingredient_ranges = parts[0].split("\n")
    ingredients = parts[1].split("\n")

for num in ingredients:
    found = False

    for id_range in ingredient_ranges:
        low, high = id_range.split("-")

        low_num = int(low)
        high_num = int(high)

        if not found and low_num <= int(num) <= high_num:
            found = True
            available_ingredients += 1


print(available_ingredients)
