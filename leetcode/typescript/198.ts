function rob(nums: number[]): number {
  const cache: number[] = []

  cache[0] = 0
  cache[1] = nums[0]

  for (let i = 1; i < nums.length; i++) {
    cache[i + 1] = Math.max(cache[i], cache[i - 1] + nums[i])
  }

  return cache[nums.length]
}
