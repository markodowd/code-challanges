import unittest


class Solution:
    def minimumPushes(self, word: str) -> int:
        word_len = len(word)

        if word_len <= 8:
            return word_len

        if word_len <= 16:
            return 8 + ((word_len - 8) * 2)

        if word_len <= 24:
            return 24 + ((word_len - 16) * 3)

        return 48 + ((word_len - 24) * 4)


class TestMinimumPushes(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_word_less_than_9(self):
        self.assertEqual(self.solver.minimumPushes("abcde"), 5)

    def test_word_less_than_17(self):
        self.assertEqual(self.solver.minimumPushes("xycdefghij"), 12)

    def test_word_less_than_25(self):
        self.assertEqual(self.solver.minimumPushes("acolkxjbizfmhnrdq"), 27)

    def test_word_less_full_alphabet(self):
        self.assertEqual(self.solver.minimumPushes("abcdefghijklmnopqrstuvwxyz"), 56)


if __name__ == "__main__":
    unittest.main()
