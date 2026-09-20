import unittest


class Solution:
    def get_reversed_value(self, char: str) -> int:
        char = char.lower()

        return ord("z") - ord(char) + 1

    def reverseDegree(self, s: str) -> int:
        total = 0

        for i in range(len(s)):
            total += self.get_reversed_value(s[i]) * (i + 1)

        return total


class TestReverseDegree(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.reverseDegree("abc"), 148)

    def test_2(self):
        self.assertEqual(self.solver.reverseDegree("zaza"), 160)


if __name__ == "__main__":
    unittest.main()
