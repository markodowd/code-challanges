class Solution:
    def reverseWords(self, s: str) -> str:
        output = ""

        for word in s.split():
            output += f" {word[::-1]}"

        return output.strip()
