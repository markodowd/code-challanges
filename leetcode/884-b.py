# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        from collections import Counter

        # Combine both sentences and split into words
        combined_words = s1.split() + s2.split()

        # Count occurrences of each word
        word_count = Counter(combined_words)

        # Return words that appear exactly once
        return [word for word, count in word_count.items() if count == 1]
