import unittest


class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        valid_words = []

        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"

        row_tracker = None

        for word in words:
            add_word = True

            lower_word = word.lower()
            first_char = lower_word[0]

            if first_char in first_row:
                row_tracker = 1
            elif first_char in second_row:
                row_tracker = 2
            else:
                row_tracker = 3

            for i in range(1, len(lower_word)):
                if row_tracker == 1 and lower_word[i] not in first_row:
                    add_word = False
                    break
                elif row_tracker == 2 and lower_word[i] not in second_row:
                    add_word = False
                    break
                elif row_tracker == 3 and lower_word[i] not in third_row:
                    add_word = False
                    break

            if add_word:
                valid_words.append(word)

        return valid_words


class TestFindWords(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(
            self.solver.findWords(["Hello", "Alaska", "Dad", "Peace"]),
            ["Alaska", "Dad"],
        )

    def test_2(self):
        self.assertEqual(self.solver.findWords(["omk"]), [])

    def test_3(self):
        self.assertEqual(self.solver.findWords(["adsdf", "sfd"]), ["adsdf", "sfd"])


if __name__ == "__main__":
    unittest.main()
