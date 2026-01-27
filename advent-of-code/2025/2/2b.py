invalid_sum = 0

with open("./input.txt", "r") as file:
    ranges = file.read().strip().split(",")

    for num_range in ranges:
        low, high = num_range.split("-")

        for num in range(int(low), int(high) + 1):
            num_str = str(num)
            num_len = len(num_str)

            is_repeating = False

            for pattern_len in range(1, num_len // 2 + 1):
                if num_len % pattern_len == 0:
                    pattern = num_str[:pattern_len]
                    repetitions = num_len // pattern_len

                    if pattern * repetitions == num_str:
                        is_repeating = True
                        break

            if is_repeating:
                invalid_sum += num

print(invalid_sum)
