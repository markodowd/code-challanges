class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        answer: list[str] = [""] * len(s)
        index = 0

        for char in s:
            answer[indices[index]] = char
            index += 1

        return "".join(answer)
