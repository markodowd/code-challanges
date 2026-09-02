import unittest


class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        left = min(min_index, max_index)
        right = max(min_index, max_index)

        front_only = right + 1
        back_only = n - left
        both_ends = (left + 1) + (n - right)

        return min(front_only, back_only, both_ends)


class TestMinimumDeletions(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.minimumDeletions([2, 10, 7, 5, 4, 1, 8, 6]), 5)

    def test_2(self):
        self.assertEqual(self.solver.minimumDeletions([0, -4, 19, 1, 8, -2, -3, 5]), 3)

    def test_3(self):
        self.assertEqual(self.solver.minimumDeletions([101]), 1)


if __name__ == "__main__":
    unittest.main()
