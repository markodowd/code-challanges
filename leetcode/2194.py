class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        output = []

        col_start = s[0]
        row_start = int(s[1])
        col_end = s[3]
        row_end = int(s[4])

        for i in range(ord(col_start), ord(col_end) + 1):
            for j in range(row_start, row_end + 1):
                output.append(chr(i) + str(j))
        
        return output

