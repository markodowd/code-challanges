class Solution:
    def balancedStringSplit(self, s: str) -> int:
        output = 0

        tracker = 0

        for char in s:
            if char == 'L':
                tracker += 1
            else:
                tracker -= 1

            if tracker == 0:
                output += 1

        return output
