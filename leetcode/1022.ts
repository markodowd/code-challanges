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

function sumRootToLeaf(root: TreeNode | null): number {
  const dfs = (node: TreeNode | null, currentAcc: number) => {
    if (!node) return 0

    currentAcc = (currentAcc << 1) | node.val

    if (!node.left && !node.right) {
      return currentAcc
    }

    return dfs(node.left, currentAcc) + dfs(node.right, currentAcc)
  }

  return dfs(root, 0)
}
