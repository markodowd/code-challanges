import unittest


class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        output = 0
        counter = {}

        for char in chars:
            counter[char] = counter.get(char, 0) + 1

        for word in words:
            temp_counter = counter.copy()
            word_is_valid = True

            for char in word:
                if char not in temp_counter or temp_counter[char] == 0:
                    word_is_valid = False
                    break

                temp_counter[char] -= 1

            if word_is_valid:
                output += len(word)

        return output


class TestCountCharacters(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(
            self.solver.countCharacters(["cat", "bt", "hat", "tree"], "atach"), 6
        )

    def test_2(self):
        self.assertEqual(
            self.solver.countCharacters(
                ["hello", "world", "leetcode"], "welldonehoneyr"
            ),
            10,
        )


if __name__ == "__main__":
    unittest.main()
