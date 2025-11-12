class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        tracker = 0
        answer = ""
        primitive_decomposition = ""

        for char in s:
            primitive_decomposition += char

            if char == "(":
                tracker += 1
            else:
                tracker -= 1

            if tracker == 0:
                primitive_decomposition += " "

        split = primitive_decomposition.split(" ")

        for sub in split:
            answer += sub[1:-1]

        return answer
