from typing import List


class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        result: List[int] = []

        for num in order:
            if num in friends:
                result.append(num)

        return result

