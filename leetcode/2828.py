class Solution:
    def isAcronym(self, words: list[str], s: str) -> bool:
        s_len = len(s)

        if s_len != len(words):
            return False

        for i in range(s_len):
            if s[i] == words[i][0]:
                continue
            else:
                return False

        return True
