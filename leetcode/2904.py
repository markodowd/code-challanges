import unittest


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        output = ""
        beautiful = []
        len_s = len(s)

        for i in range(len_s):
            if s[i] != "1":
                continue

            count = 1
            temp = "1"

            if count == k:
                beautiful.append(temp)
                continue

            for j in range(i + 1, len_s):
                val = s[j]
                temp += val

                if val == "1":
                    count += 1

                if count == k:
                    beautiful.append(temp)
                    break

        if len(beautiful) == 0:
            return output

        min_len = min(len(t) for t in beautiful)
        candidates = [t for t in beautiful if len(t) == min_len]

        return min(candidates)


class TestShortestBeautifulSubstring(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(
            self.solver.shortestBeautifulSubstring("100011001", 3), "11001"
        )

    def test_2(self):
        self.assertEqual(self.solver.shortestBeautifulSubstring("1011", 2), "11")

    def test_3(self):
        self.assertEqual(self.solver.shortestBeautifulSubstring("000", 1), "")

    def test_4(self):
        self.assertEqual(self.solver.shortestBeautifulSubstring("11000111", 1), "1")

    def test_5(self):
        self.assertEqual(
            self.solver.shortestBeautifulSubstring("001110101101101111", 10),
            "10101101101111",
        )


if __name__ == "__main__":
    unittest.main()
