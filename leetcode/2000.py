class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)

        if index >= 0:
            new_word = ""
            new_word += word[index::-1]
            new_word += word[index + 1 :]
            return new_word
        else:
            return word
