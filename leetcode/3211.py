class Solution:
    def validStrings(self, n: int) -> list[str]:
        answer = []

        def backtrack(current_string):
            if len(current_string) == n:
                answer.append(current_string)
                return

            backtrack(current_string + "1")

            if not current_string or current_string[-1] != "0":
                backtrack(current_string + "0")

        backtrack("")

        return answer
