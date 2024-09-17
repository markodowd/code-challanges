# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"TreeNode({self.val}, {self.left}, {self.right})"


class Solution:
    def sumRootToLeaf(self, root: any) -> int:
        print("root: ", root)

        def dfs(node, current_sum):
            print("node: ", node)

            if not node:
                return 0

            print("current_sum PRE bit shift: ", current_sum)
            current_sum = (current_sum << 1) | node.val
            print("current_sum POST bit shift: ", current_sum)

            if not node.left and not node.right:  # Leaf node
                return current_sum

            return dfs(node.left, current_sum) + dfs(node.right, current_sum)

        return dfs(root, 0)


node0 = TreeNode(0)
node1 = TreeNode(1)

test_case = TreeNode(
    1,
    TreeNode(0, TreeNode(0), TreeNode(1)),
    TreeNode(1, TreeNode(0), TreeNode(1)),
)

test_answer = Solution().sumRootToLeaf(test_case)
print(test_answer)
