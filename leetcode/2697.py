class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s_list = list(s)

        left = 0
        right = len(s_list) - 1

        while left < right:
            if ord(s_list[left]) < ord(s_list[right]):
                s_list[right] = s_list[left]
            else:
                s_list[left] = s_list[right]

            left += 1
            right -= 1

        return "".join(s_list)
