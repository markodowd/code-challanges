import unittest


class Solution:
    def largest_digits(self, nums: list[int]) -> list[int]:
        largest_digits = []

        for num in nums:
            largest = 0

            for digit in str(num):
                largest = max(largest, int(digit))

            largest_digits.append(largest)

        return largest_digits

    def count_digits(self, nums: list[int]):
        count = {}

        for num in nums:
            if num in count:
                count[num] = count[num] + 1
            else:
                count[num] = 1

        return count

    def find_doubles(self, digits_count) -> list[int]:
        doubles = []

        for digit, val in digits_count.items():
            if val >= 2:
                doubles.append(digit)

        return doubles

    def calculate_max_sum(
        self, nums: list[int], largest_digits: list[int], doubles: list[int]
    ) -> int:
        max_sum = -1

        for d in doubles:
            matching_nums = [
                nums[i] for i in range(len(nums)) if largest_digits[i] == d
            ]

            if len(matching_nums) >= 2:
                matching_nums.sort(reverse=True)
                current_sum = matching_nums[0] + matching_nums[1]
                max_sum = max(max_sum, current_sum)

        return max_sum

    def maxSum(self, nums: list[int]) -> int:
        largest_digits = self.largest_digits(nums)

        digits_count = self.count_digits(largest_digits)

        doubles = self.find_doubles(digits_count)

        if len(doubles) == 0:
            return -1

        return self.calculate_max_sum(nums, largest_digits, doubles)


class TestMaxSum(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.maxSum([112, 131, 411]), -1)

    def test_2(self):
        self.assertEqual(self.solver.maxSum([2536, 1613, 3366, 162]), 5902)

    def test_3(self):
        self.assertEqual(self.solver.maxSum([51, 71, 17, 24, 42]), 88)


if __name__ == "__main__":
    unittest.main()
