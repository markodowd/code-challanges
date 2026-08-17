import unittest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = {}

        for char in s:
            counter[char] = counter.get(char, 0) + 1

        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1

        return True


class TestIsAnagram(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def test_example_1(self):
        self.assertEqual(self.solver.isAnagram("anagram", "nagaram"), True)

    def test_example_2(self):
        self.assertEqual(self.solver.isAnagram("rat", "car"), False)


if __name__ == "__main__":
    unittest.main()
