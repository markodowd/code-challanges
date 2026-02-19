class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        output = 0

        words = text.split()

        for word in words:
            broken = False
            for char in word:
                if char in brokenLetters:
                    broken = True
                    break
            if not broken:
                output += 1

        return output

