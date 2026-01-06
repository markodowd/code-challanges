class Solution:
    def maximum69Number(self, num: int) -> int:
        maximum = list(str(num))

        for i in range(len(maximum)):
            if maximum[i] == "6":
                maximum[i] = "9"
                break

        return int("".join(maximum))
