class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        output = 0

        for i in range(len(words)):
            for j in range(i+1, len(words) - 1):
                if words[i] == words[j][::-1]:
                    output += 1

        return output
