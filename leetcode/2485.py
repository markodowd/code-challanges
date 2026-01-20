class Solution:
    def pivotInteger(self, n: int) -> int:
        x = -1

        lPoint = 1
        rPoint = n

        leftTotal = 1
        rightTotal = n * (n + 1) // 2

        while lPoint <= rPoint:
            currentRight = rightTotal - leftTotal + lPoint
            
            if leftTotal < currentRight:
                lPoint += 1
                leftTotal += lPoint
            elif leftTotal > currentRight:
                rPoint -= 1
            else:
                x = lPoint
                break
        
        return x
