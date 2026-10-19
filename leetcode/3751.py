import unittest


class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        output = 0

        for num in range(num1, num2 + 1):
            less_than_three_digits = num < 100
            if less_than_three_digits:
                continue

            str_num = str(num)

            for i, digit in enumerate(str_num):
                if i == 0:
                    continue

                if i == len(str_num) - 1:
                    continue

                value = int(digit)

                digit_is_peak = value > int(str_num[i - 1]) and value > int(
                    str_num[i + 1]
                )
                if digit_is_peak:
                    output += 1

                digit_is_valley = value < int(str_num[i - 1]) and value < int(
                    str_num[i + 1]
                )
                if digit_is_valley:
                    output += 1

        return output


class TestTotalWaviness(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.totalWaviness(120, 130), 3)

    def test_2(self):
        self.assertEqual(self.solver.totalWaviness(198, 202), 3)

    def test_3(self):
        self.assertEqual(self.solver.totalWaviness(4848, 4848), 2)


if __name__ == "__main__":
    unittest.main()
