class Solution:
    def replaceDigits(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i].isdigit():
                char = chr(ord(s[i - 1]) + int(s[i]))
                stack.append(char)
            else:
                stack.append(s[i])

        return "".join(stack)
