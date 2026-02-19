class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        output = ""

        for word in words:
            word_sum = 0

            for char in word:
                word_sum += weights[ord(char) - ord("a")]

            word_modulo = word_sum % 26

            char = ord("z") - word_modulo
            output += chr(char)

        return output
