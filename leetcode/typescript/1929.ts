function getConcatenation(nums: number[]): number[] {
  const numsLength: number = nums.length
  const arr: number[] = []

  for (let j = 1; j <= 2; j++) {
    for (let i = 0; i < numsLength; i++) {
      arr.push(nums[i])
    }
  }

  return arr
}
