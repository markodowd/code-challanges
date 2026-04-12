class Solution:
    def reverseByType(self, s: str) -> str:
        answer = ""
        special_chars = "!@#$%^&*()"

        alpha = []
        special = []

        for char in s:
            if char in special_chars:
                special.append(char)
            else:
                alpha.append(char)

        for char in s:
            if char in special_chars:
                answer += special.pop()
            else:
                answer += alpha.pop()

        return answer
