import unittest


class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0

        count = 0

        for num in range(1000, n + 1):
            if num < 1_000_000:
                count += 1
            else:
                count += 2

        return count


class TestCountCommas(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.countCommas(1002), 3)

    def test_2(self):
        self.assertEqual(self.solver.countCommas(998), 0)


if __name__ == "__main__":
    unittest.main()
