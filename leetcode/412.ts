// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

function fizzBuzz(n: number): string[] {
  const result: string[] = []

  for (let i = 1; i <= n; i++) {
    // Check if number is divisible by 3 or 5
    const divisibleBy3 = i % 3 === 0
    const divisibleBy5 = i % 5 === 0

    if (divisibleBy3 && divisibleBy5) {
      result.push('FizzBuzz')
      continue // Go to the next iteration
    }

    if (divisibleBy3) {
      result.push('Fizz')
      continue // Go to the next iteration
    }

    if (divisibleBy5) {
      result.push('Buzz')
      continue // Go to the next iteration
    }

    result.push(i.toString())
  }

  return result
}
