import unittest


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0

        for num in range(low, high + 1):
            if num % 2 != 0:
                count += 1

        return count


class TestCountOdds(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.countOdds(3, 7), 3)

    def test_2(self):
        self.assertEqual(self.solver.countOdds(8, 10), 1)


if __name__ == "__main__":
    unittest.main()
