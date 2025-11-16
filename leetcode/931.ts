// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

function minFallingPathSum(matrix: number[][]): number {
  // The criteria indicates that the matrix will be a square so we can use the length for the rows and columns
  const matrixLength: number = matrix.length

  let prevRow: number[] = [...matrix[0]] // Initialize with the first row

  for (let row: number = 1; row < matrixLength; row++) {
    const currRow: number[] = []

    for (let col: number = 0; col < matrixLength; col++) {
      const currentValue: number = matrix[row][col]

      // Calculate the sum of the current value and the previous row
      const middle: number = currentValue + prevRow[col]
      const left: number = currentValue + (prevRow[col - 1] || Infinity) // If the previous row index is out of bounds, use Infinity
      const right: number = currentValue + (prevRow[col + 1] || Infinity) // If the previous row index is out of bounds, use Infinity

      currRow[col] = Math.min(middle, left, right)
    }

    prevRow = [...currRow] // Update the previous row with the current row
  }

  return Math.min(...prevRow)
}
