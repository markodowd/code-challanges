from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.min_count: float = float("inf")
        self.dfs(root, 1)
        return int(self.min_count)

    def dfs(self, node: Optional[TreeNode], count: int) -> None:
        if not node or count >= self.min_count:
            return

        if not node.left and not node.right:
            self.min_count = min(self.min_count, count)
            return

        self.dfs(node.left, count + 1)
        self.dfs(node.right, count + 1)
