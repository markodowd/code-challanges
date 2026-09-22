import unittest


class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        output = []
        start = 0
        current_char = s[0]
        s_len = len(s)

        for i, val in enumerate(s):
            new_character = val != current_char
            last_index = i == s_len - 1

            if new_character or last_index:
                if new_character:
                    end = i - 1
                else:
                    end = i

                if end - start > 1:
                    output.append([start, end])

                if new_character:
                    current_char = val
                    start = i

        return output


class TestLargeGroupPositions(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.largeGroupPositions("abbxxxxzzy"), [[3, 6]])

    def test_2(self):
        self.assertEqual(self.solver.largeGroupPositions("abc"), [])

    def test_3(self):
        self.assertEqual(
            self.solver.largeGroupPositions("abcdddeeeeaabbbcd"),
            [[3, 5], [6, 9], [12, 14]],
        )


if __name__ == "__main__":
    unittest.main()
