import unittest
import random


class Solution:
    def getRandomLetter(self, exclude1: str = "", exclude2: str = "") -> str:
        letter = chr(random.randint(97, 122))
        while letter == exclude1 or letter == exclude2:
            letter = chr(random.randint(97, 122))
        return letter

    def modifyString(self, s: str) -> str:
        output = list(s)
        n = len(output)

        for idx in range(n):
            if output[idx] == "?":
                left = output[idx - 1] if idx > 0 else ""
                right = output[idx + 1] if idx < n - 1 else ""
                output[idx] = self.getRandomLetter(left, right)

        return "".join(output)


class TestModifyString(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def assertValid(self, s: str):
        output = self.solver.modifyString(s)

        self.assertEqual(len(output), len(s))
        self.assertNotIn("?", output)

        for idx, char in enumerate(s):
            if char == "?":
                self.assertTrue(output[idx].islower() and output[idx].isalpha())
            else:
                self.assertEqual(output[idx], char)

        for left, right in zip(output, output[1:]):
            self.assertNotEqual(left, right)

        return output

    def test_1(self):
        self.assertValid("?zs")

    def test_2(self):
        self.assertValid("ubv?w")

    def test_consecutive_question_marks(self):
        self.assertValid("??")

    def test_all_question_marks(self):
        self.assertValid("?" * 100)

    def test_single_question_mark(self):
        self.assertValid("?")

    def test_no_question_marks(self):
        self.assertEqual(self.solver.modifyString("abc"), "abc")

    def test_repeated_runs_stay_valid(self):
        # the replacement letter is random, so run it enough times to catch
        # a bad branch that only shows up for some draws
        for _ in range(200):
            self.assertValid("a?b?c??d")


if __name__ == "__main__":
    unittest.main()
