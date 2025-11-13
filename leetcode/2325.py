class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        ALPHABET = "abcdefghijklmnopqrstuvwxyz"
        sub_table = {}
        answer = ""

        for char in key:
            if char == " ":
                continue

            if char not in sub_table:
                sub_table[char] = ALPHABET[0]
                ALPHABET = ALPHABET[1:]

        for char in message:
            if char == " ":
                answer += " "
                continue

            answer += sub_table[char]

        return answer
