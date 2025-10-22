from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isMirror(node_a, node_b):
            if not node_a and not node_b:
                return True

            if not node_a or not node_b:
                return False

            return (
                node_a.val == node_b.val
                and isMirror(node_a.left, node_b.right)
                and isMirror(node_a.right, node_b.left)
            )

        return isMirror(root, root)
