class Solution:
    def kthCharacter(self, k: int) -> str:
        word = "a"

        while len(word) < k:
            gen_str = ""

            for char in word:
                gen_str += chr((ord(char) - ord("a") + 1) % 26 + ord("a"))

            word += gen_str

        return word[k - 1]
