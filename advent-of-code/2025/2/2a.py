invalid_sum = 0

with open("./input.txt", "r") as file:
    ranges = file.read().strip().split(",")

    for num_range in ranges:
        low, high = num_range.split("-")

        for num in range(int(low), int(high) + 1):
            num_str = str(num)
            num_len = len(num_str)

            if num_len % 2 == 0:
                num_mid = num_len // 2
                if num_str[:num_mid] == num_str[num_mid:]:
                    invalid_sum += num

print(invalid_sum)
