import unittest


class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        seen = set()

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] in seen:
                return i // 3 + 1

            seen.add(nums[i])

        return 0


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
