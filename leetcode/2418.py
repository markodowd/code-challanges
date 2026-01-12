class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        answer = []

        sorted_indices = sorted(
            range(len(heights)), key=lambda i: heights[i], reverse=True
        )

        for idx in sorted_indices:
            answer.append(names[idx])

        return answer
