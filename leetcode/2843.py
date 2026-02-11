class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for val in range(low, high + 1):
            if val < 10:
                continue

            str_val = str(val)

            if len(str_val) % 2 != 0:
                continue

            str_half_len = len(str_val) // 2

            val_left = str_val[:str_half_len]
            val_right = str_val[str_half_len:]

            val_left_total = sum(int(digit) for digit in val_left)
            val_right_total = sum(int(digit) for digit in val_right)

            if val_left_total == val_right_total:
                count += 1

        return count
