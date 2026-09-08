import unittest


class Solution:
    def semiOrderedPermutation(self, nums: list[int]) -> int:
        nums_len = len(nums)

        if nums[0] == 1 and nums[-1] == nums_len:
            return 0

        start_idx = 0
        end_idx = 0

        for i in range(nums_len):
            if nums[i] == 1:
                start_idx = i

            if nums[i] == (nums_len - 1):
                end_idx = i

        return start_idx + (nums_len - end_idx)


class TestSemiOrderedPermutation(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.semiOrderedPermutation([2, 1, 4, 3]), 2)

    def test_2(self):
        self.assertEqual(self.solver.semiOrderedPermutation([2, 4, 1, 3]), 3)

    def test_3(self):
        self.assertEqual(self.solver.semiOrderedPermutation([1, 3, 4, 2, 5]), 0)

    def test_4(self):
        self.assertEqual(self.solver.semiOrderedPermutation([2, 1]), 1)


if __name__ == "__main__":
    unittest.main()
