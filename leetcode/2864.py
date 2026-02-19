class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s_copy = list(s)
        pointer = 0

        for i in range(len(s_copy)):
            if s_copy[i] == '1':
                s_copy[i] = s_copy[len(s_copy) - 1]
                s_copy[len(s_copy) - 1] = '1'
                break

        for i in range(len(s_copy) - 1):
            if s_copy[i] == '1':
                if s_copy[pointer] == '0':
                    s_copy[pointer] = '1'
                    s_copy[i] = '0'
                pointer += 1

        return ''.join(s_copy)
