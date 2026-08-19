import unittest


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        power = 0
        total = 0

        while total < n:
            total = 4**power
            power += 1

        return total == n


class TestIsPowerOfFour(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.isPowerOfFour(16), True)

    def test_2(self):
        self.assertEqual(self.solver.isPowerOfFour(5), False)

    def test_3(self):
        self.assertEqual(self.solver.isPowerOfFour(1), True)


if __name__ == "__main__":
    unittest.main()
