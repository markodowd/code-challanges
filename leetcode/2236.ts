// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

class TreeNode {
  val: number
  left: TreeNode | null
  right: TreeNode | null
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val
    this.left = left === undefined ? null : left
    this.right = right === undefined ? null : right
  }
}

function checkTree(root: TreeNode | null): boolean {
  // Check if root node exists and if not exit early
  if (!root) {
    return false
  }

  // Check if root node has left and right child nodes and if not exit early
  if (!root.left || !root.right) {
    return false
  }

  // Assign values of root and child nodes to variables
  const rootNodeValue = root.val
  const leftNodeValue = root.left.val
  const rightNodeValue = root.right.val

  // Calculate sum of child nodes
  const sumOfChildNodes = leftNodeValue + rightNodeValue

  // Check if root value equals sum of child nodes
  return rootNodeValue === sumOfChildNodes
}
