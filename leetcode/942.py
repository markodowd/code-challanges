class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        answer = []

        low = 0
        high = len(s)

        for val in s:
            if val == "I":
                answer.append(low)
                low += 1
            else:
                answer.append(high)
                high -= 1

        answer.append(low)

        return answer
