import unittest


class Solution:
    def cycle_sum(self, idx: int, nums: list[int], k: int) -> int:
        total = 0
        n = len(nums)

        if k > 0:
            current_idx = idx
            for _ in range(k):
                current_idx += 1
                if current_idx == n:
                    current_idx = 0
                total += nums[current_idx]
        else:
            current_idx = idx
            for _ in range(abs(k)):
                current_idx -= 1
                if current_idx < 0:
                    current_idx = n - 1
                total += nums[current_idx]

        return total

    def decrypt(self, code: list[int], k: int) -> list[int]:
        n = len(code)
        result = [0] * n

        if k == 0:
            return result

        for i in range(n):
            result[i] = self.cycle_sum(i, code, k)

        return result


class TestDecrypt(unittest.TestCase):
    def setUp(self):
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.decrypt([5, 7, 1, 4], 3), [12, 10, 16, 13])

    def test_2(self):
        self.assertEqual(self.solver.decrypt([1, 2, 3, 4], 0), [0, 0, 0, 0])

    def test_3(self):
        self.assertEqual(self.solver.decrypt([2, 4, 9, 3], -2), [12, 5, 6, 13])


if __name__ == "__main__":
    unittest.main()
