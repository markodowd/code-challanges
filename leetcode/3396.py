import unittest


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        ops = 0

        while len(nums) > 0 and len(set(nums)) != len(nums):
            nums = nums[3:]
            ops += 1

            if len(nums) == len(set(nums)):
                break

        return ops


class TestMinimumOperations(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.minimumOperations([1, 2, 3, 4, 2, 3, 3, 5, 7]), 2)

    def test_2(self):
        self.assertEqual(self.solver.minimumOperations([4, 5, 6, 4, 4]), 2)

    def test_3(self):
        self.assertEqual(self.solver.minimumOperations([6, 7, 8, 9]), 0)


if __name__ == "__main__":
    unittest.main()
