def merge_intervals(ingredient_ranges):
    ranges = []

    for id_range in ingredient_ranges:
        start_str, end_str = id_range.split("-")
        start = int(start_str)
        end = int(end_str)
        ranges.append((start, end))

    ranges.sort()

    merged = [ranges[0]]

    for current_start, current_end in ranges[1:]:
        last_start, last_end = merged[-1]

        if current_start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, current_end))
        else:
            merged.append((current_start, current_end))

    return sum(end - start + 1 for start, end in merged)


with open("./input.txt", "r") as f:
    content = f.read()
    parts = content.strip().split("\n\n")
    ingredient_ranges = parts[0].split("\n")

print(merge_intervals(ingredient_ranges))
