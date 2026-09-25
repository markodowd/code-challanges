import unittest


class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        prices = sorted(prices)

        first_min_cost = prices[0]
        second_min_cost = prices[1]

        leftover = money - (first_min_cost + second_min_cost)

        if leftover < 0:
            return money

        return leftover


class TestBuyChoco(unittest.TestCase):
    def setUp(self) -> None:
        self.solver = Solution()

    def test_1(self):
        self.assertEqual(self.solver.buyChoco([1, 2, 2], 3), 0)

    def test_2(self):
        self.assertEqual(self.solver.buyChoco([3, 2, 3], 3), 3)


if __name__ == "__main__":
    unittest.main()
