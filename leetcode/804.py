MORSE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--.."
}

class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse_concat_words = set()

        for word in words:
            temp_morse = ""

            for char in word:
                temp_morse += MORSE[char.upper()]

            morse_concat_words.add(temp_morse)
        
        return len(morse_concat_words)
