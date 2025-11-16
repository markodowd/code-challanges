// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

function halvesAreAlike(s: string): boolean {
  // Array of vowels
  const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

  // Split the string in half
  const firstHalf = s.slice(0, s.length / 2)
  const secondHalf = s.slice(s.length / 2)

  // Create two objects to store the vowel count for each half
  let firstHalfVowelCount = 0
  let secondHalfVowelCount = 0

  // Iterate through each half and count the vowels
  for (let char of firstHalf) {
    if (vowels.includes(char)) {
      firstHalfVowelCount++
    }
  }

  for (let char of secondHalf) {
    if (vowels.includes(char)) {
      secondHalfVowelCount++
    }
  }

  // Return true if the vowel counts are equal
  return firstHalfVowelCount === secondHalfVowelCount
}
