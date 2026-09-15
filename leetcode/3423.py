import unittest


class Solution:
    def maxAdjacentDistance(self, nums: list[int]) -> int:
        max_distance = 0

        for i in range(len(nums) - 1):
            max_distance = max(max_distance, abs(nums[i] - nums[i + 1]))

        max_distance = max(max_distance, abs(nums[0] - nums[len(nums) - 1]))

        return max_distance


class TestMaxAdjacentDistance(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.maxAdjacentDistance([1, 2, 4]), 3)

    def test_2(self):
        self.assertEqual(self.solver.maxAdjacentDistance([-5, -10, -5]), 5)


if __name__ == "__main__":
    unittest.main()
