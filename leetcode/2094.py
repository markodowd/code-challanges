import unittest


class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        output = set()
        limit = len(digits)

        for i in range(limit):
            if digits[i] == 0:
                continue

            for j in range(limit):
                if j == i:
                    continue

                for k in range(limit):
                    if k == i or k == j:
                        continue

                    if digits[k] % 2 != 0:
                        continue

                    value = digits[i] * 100 + digits[j] * 10 + digits[k]
                    output.add(value)

        return sorted(output)


class TestFindEvenNumbers(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(
            self.solver.findEvenNumbers([2, 1, 3, 0]),
            [102, 120, 130, 132, 210, 230, 302, 310, 312, 320],
        )


if __name__ == "__main__":
    unittest.main()
