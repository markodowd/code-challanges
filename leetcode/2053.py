class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        count_map = {}

        for s in arr:
            count_map[s] = count_map.get(s, 0) + 1
        
        distinct_count = 0
        
        for s in arr:
            if count_map[s] == 1:
                distinct_count += 1
                if distinct_count == k:
                    return s
        
        return ""
