class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        idx = 0

        while len(merged) < len(word1 + word2):
            if idx < len(word1):
                merged += word1[idx]
            
            if idx < len(word2):
                merged += word2[idx]
            
            idx += 1

        return merged
