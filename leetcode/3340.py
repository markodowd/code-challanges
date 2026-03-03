class Solution:
    def isBalanced(self, num: str) -> bool:
        even_total = 0
        odd_total = 0

        for i in range(len(num)):
            if i % 2 == 0:
                even_total += int(num[i])
            else:
                odd_total += int(num[i])
        
        return even_total == odd_total

