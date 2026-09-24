import unittest


class Solution:
    def smallestIndex(self, nums: list[int]) -> int:
        for i, num in enumerate(nums):
            digit_sum = 0

            while num > 0:
                digit_sum += num % 10
                num //= 10

            if i == digit_sum:
                return i

        return -1


class TestSmallestIndex(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.smallestIndex([1, 3, 2]), 2)

    def test_2(self):
        self.assertEqual(self.solver.smallestIndex([1, 10, 11]), 1)

    def test_3(self):
        self.assertEqual(self.solver.smallestIndex([1, 2, 3]), -1)


if __name__ == "__main__":
    unittest.main()
