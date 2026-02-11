class Solution:
    def countAsterisks(self, s: str) -> int:
        count = 0

        counting = True

        for char in s:
            if char == '|':
                counting = not counting
            
            if counting and char == '*':
                count += 1

        return count
