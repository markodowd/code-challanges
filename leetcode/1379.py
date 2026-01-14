class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(node, target):
            if not node:
                return None

            if node.val == target.val:
                return node

            left_result = dfs(node.left, target)
            if left_result:
                return left_result

            return dfs(node.right, target)

        return dfs(cloned, target)
