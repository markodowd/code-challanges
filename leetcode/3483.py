import unittest


class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        valid_values = set()
        digits_len = len(digits)

        for i in range(digits_len):
            first_number = digits[i]

            if first_number == 0:
                continue

            first_value = str(first_number)

            for j in range(digits_len):
                if j == i:
                    continue

                second_number = digits[j]
                second_value = first_value + str(second_number)

                for k in range(digits_len):
                    if k == i or k == j:
                        continue

                    third_number = digits[k]
                    third_value = int(second_value + str(third_number))

                    if third_value % 2 == 0:
                        valid_values.add(third_value)

        return len(valid_values)


class TestTotalNumbers(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.totalNumbers([1, 2, 3, 4]), 12)

    def test_2(self):
        self.assertEqual(self.solver.totalNumbers([0, 2, 2]), 2)

    def test_3(self):
        self.assertEqual(self.solver.totalNumbers([6, 6, 6]), 1)

    def test_4(self):
        self.assertEqual(self.solver.totalNumbers([1, 3, 5]), 0)


if __name__ == "__main__":
    unittest.main()
