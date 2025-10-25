from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        for i in range(len(words)):
            for char in allowed:
                words[i] = words[i].replace(char, "")

        return words.count("")
