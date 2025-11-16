# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_count = {}

        # Combine both sentences and split into words
        for word in s1.split() + s2.split():
            word_count[word] = word_count.get(word, 0) + 1

        # Return words that appear exactly once
        return [word for word, count in word_count.items() if count == 1]
