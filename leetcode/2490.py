import unittest


class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        words_len = len(words)

        for i in range(words_len):
            current_word = words[i]

            if i == words_len - 1:
                next_word = words[0]
            else:
                next_word = words[i + 1]

            if current_word[-1] != next_word[0]:
                return False

        return True


class TestIsCircularSentence(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(
            self.solver.isCircularSentence("leetcode exercises sound delightful"), True
        )

    def test_2(self):
        self.assertEqual(self.solver.isCircularSentence("eetcode"), True)

    def test_3(self):
        self.assertEqual(self.solver.isCircularSentence("Leetcode is cool"), False)


if __name__ == "__main__":
    unittest.main()
