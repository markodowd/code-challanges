class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        output = []

        for i in range(len(prices)):
            discount_found = False
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    output.append(prices[i] - prices[j])
                    discount_found = True
                    break

            if not discount_found:
                output.append(prices[i])

        return output

