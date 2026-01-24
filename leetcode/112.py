from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        path_sums = []

        def dfs(node, current_sum):
            if not node:
                return

            current_sum += node.val

            if not node.left and not node.right:
                path_sums.append(current_sum)
                return

            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

        dfs(root, 0)

        if target_sum in path_sums:
            return True

        return False

