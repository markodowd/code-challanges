class Solution:
    def minCosts(self, cost: list[int]) -> list[int]:
        answer = [cost[0]]
        min_so_far = cost[0]

        for val in cost[1:]:
            min_so_far = min(min_so_far, val)
            answer.append(min_so_far)

        return answer

