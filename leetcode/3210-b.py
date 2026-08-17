import unittest


class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        s_len = len(s)
        return "".join(s[(i + k) % s_len] for i in range(s_len))


class TestGetEncryptedString(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.getEncryptedString("dart", 3), "tdar")

    def test_2(self):
        self.assertEqual(self.solver.getEncryptedString("aaa", 1), "aaa")


if __name__ == "__main__":
    unittest.main()
