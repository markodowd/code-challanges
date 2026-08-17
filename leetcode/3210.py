import unittest


class Solution:
    def calculateIndex(self, idx: int, k: int, s_len: int) -> int:
        while k > 0:
            idx += 1

            if idx == s_len:
                idx = 0

            k -= 1

        return idx

    def getEncryptedString(self, s: str, k: int) -> str:
        result = ""
        s_len = len(s)

        for i in range(s_len):
            idx = self.calculateIndex(i, k, s_len)
            result += s[idx]

        return result


class TestCalculateIndex(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.calculateIndex(0, 3, 4), 3)

    def test_2(self):
        self.assertEqual(self.solver.calculateIndex(1, 3, 4), 0)

    def test_3(self):
        self.assertEqual(self.solver.calculateIndex(2, 4, 4), 2)


class TestGetEncryptedString(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.getEncryptedString("dart", 3), "tdar")

    def test_2(self):
        self.assertEqual(self.solver.getEncryptedString("aaa", 1), "aaa")


if __name__ == "__main__":
    unittest.main()
