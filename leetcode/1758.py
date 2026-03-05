class Solution:
    def minOperations(self, s: str) -> int:
        count_0 = 0
        count_1 = 0
        tracker_0 = '0'
        tracker_1 = '1'

        for i in range(len(s)):
            if s[i] == tracker_0:
                count_0 += 1
            
            if tracker_0 == '0':
                tracker_0 = '1'
            else:
                tracker_0 = '0'
        
        for i in range(len(s)):
            if s[i] == tracker_1:
                count_1 += 1
            
            if tracker_1 == '0':
                tracker_1 = '1'
            else:
                tracker_1 = '0'
            

        return min(count_0, count_1)
