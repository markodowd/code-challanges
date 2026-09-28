class Solution:
    def maxDepth(self, s: str) -> int:
        depth_max = 0
        depth_count = 0

        for char in s:
            if char == "(":
                depth_count += 1
                depth_max = max(depth_max, depth_count)
            if char == ")":
                depth_count -= 1

        return depth_max
