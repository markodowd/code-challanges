# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs_post(self, root):
        if root.left is None and root.right is None:
            return root.val == 1

        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)

        if root.val == 2:
            return left_val or right_val
        else:
            return left_val and right_val

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return self.dfs_post(root)
