import unittest


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 1

        for num in range(2, min(a, b) + 1):
            if a % num == 0 and b % num == 0:
                count += 1

        return count


class TestCommonFactors(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.commonFactors(12, 6), 4)

    def test_2(self):
        self.assertEqual(self.solver.commonFactors(25, 30), 2)


if __name__ == "__main__":
    unittest.main()
