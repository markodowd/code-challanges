function minSteps(s: string, t: string): number {
  const sMap = new Map<string, number>()
  const tMap = new Map<string, number>()

  // Generate a map counting the occurances of each character in s
  for (let char of s) {
    sMap.set(char, (sMap.get(char) || 0) + 1)
  }

  // Generate a map counting the occurances of each character in t
  for (let char of t) {
    tMap.set(char, (tMap.get(char) || 0) + 1)
  }

  let steps = 0

  // Iterate through each character in t
  for (let [character, count] of tMap) {
    const sMapCharacterCount = sMap.get(character) || 0 // If the character does not exist in s, the number of occurances in s is 0

    // If t has more occurances of a character than s, then a step is required to make the counts equal
    if (count > sMapCharacterCount) {
      steps += count - sMapCharacterCount
    }
  }

  return steps
}
