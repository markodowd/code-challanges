class Solution:
    def hasSameDigits(self, s: str) -> bool:
        current = s
        temp = ""

        while len(current) > 2:
            for i in range(len(current) - 1):
                val = (int(current[i]) + int(current[i+1])) % 10
                temp += str(val)
            
            current = temp
            temp = ""
        
        return int(current[0]) == int(current[1])
