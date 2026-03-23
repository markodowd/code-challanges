class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.total_sum = 0

        def traverse(node):
            if not node:
                return

            traverse(node.right)

            self.total_sum += node.val
            node.val = self.total_sum

            traverse(node.left)

        traverse(root)
        return root
