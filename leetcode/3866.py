from collections import Counter
import unittest


class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        counts = Counter(num for num in nums if num % 2 == 0)

        for num in nums:
            if num % 2 == 0 and counts[num] == 1:
                return num

        return -1


class TestFirstUniqueEven(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.firstUniqueEven([3, 4, 2, 5, 4, 6]), 2)

    def test_2(self):
        self.assertEqual(self.solver.firstUniqueEven([4, 4]), -1)

    def test_3(self):
        self.assertEqual(self.solver.firstUniqueEven([8, 2]), 8)


if __name__ == "__main__":
    unittest.main()
