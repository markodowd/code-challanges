import unittest


class Solution:
    def findNonMinOrMax(self, nums: list[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)

        for num in nums:
            if num != min_num and num != max_num:
                return num

        return -1


class TestFindNonMinOrMax(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertIn(self.solver.findNonMinOrMax([3, 2, 1, 4]), [2, 3])

    def test_2(self):
        self.assertEqual(self.solver.findNonMinOrMax([1, 2]), -1)

    def test_3(self):
        self.assertEqual(self.solver.findNonMinOrMax([2, 1, 3]), 2)


if __name__ == "__main__":
    unittest.main()
