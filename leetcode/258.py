import unittest


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0

        while num > 9:
            num = sum(int(digit) for digit in str(num))

        return num


class TestAddDigits(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def test_example_1(self):
        self.assertEqual(self.solver.addDigits(38), 2)

    def test_example_2(self):
        self.assertEqual(self.solver.addDigits(0), 0)


if __name__ == "__main__":
    unittest.main()
