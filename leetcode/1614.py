class Solution:
    def maxDepth(self, s: str) -> int:
        max_output = 0
        output = 0

        for i in range(len(s)):
            if s[i] == '(':
                output += 1

                if output > max_output:
                    max_output = output
            
            if s[i] == ')':
                output -= 1
        
        return max_output
