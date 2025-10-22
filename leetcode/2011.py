operations_dict = {"++X": 1, "X++": 1, "--X": -1, "X--": -1}


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0

        for operation in operations:
            result += operations_dict[operation]

        return result
