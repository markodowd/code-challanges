function numberOfSteps(num: number): number {
  let steps = 0

  while (num > 0) {
    const numIsEven = num % 2 === 0

    if (numIsEven) {
      num /= 2
    } else {
      num -= 1
    }

    steps++
  }

  return steps
}
