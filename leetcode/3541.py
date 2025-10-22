class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {}
        consonants = {}

        for char in s:
            if char in "aeiou":
                if char in vowels:
                    vowels[char] = vowels[char] + 1
                else:
                    vowels[char] = 1
            else:
                if char in consonants:
                    consonants[char] = consonants[char] + 1
                else:
                    consonants[char] = 1

        max_vowel = vowels[max(vowels, key=vowels.get)] if vowels else 0
        max_consonants = (
            consonants[max(consonants, key=consonants.get)] if consonants else 0
        )

        print(max_vowel)
        print(max_consonants)

        return max_vowel + max_consonants
