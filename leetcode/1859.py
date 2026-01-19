class Solution:
    def sortSentence(self, s: str) -> str:
        word_arr = s.split()
        arr_len = len(word_arr)
        arr = [None] * arr_len

        for word in word_arr:
            text = word[:-1]
            number = word[-1]
            
            arr[int(number) - 1] = text

        return ' '.join(arr)
