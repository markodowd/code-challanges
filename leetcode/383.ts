// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

function canConstruct(ransomNote: string, magazine: string): boolean {
  const magazineMap = new Map<string, number>()

  // Create a map counting the number of each character in the magazine
  for (let char of magazine) {
    magazineMap.set(char, (magazineMap.get(char) ?? 0) + 1)
  }

  // Check if the ransom note can be constructed using the number of characters in the magazine
  for (let char of ransomNote) {
    if (!magazineMap.has(char)) {
      return false
    }

    const charCount = magazineMap.get(char) ?? 0

    if (!charCount) {
      return false
    }

    magazineMap.set(char, charCount - 1)
  }

  return true
}
