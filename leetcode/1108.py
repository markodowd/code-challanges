# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
