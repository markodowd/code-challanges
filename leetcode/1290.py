# Author: Mark O'Dowd
# Email: contact@markodowd.dev
# LeetCode: https://leetcode.com/u/markodowd

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def list_binary(self, node):
        binary = "0b"

        current = node

        while current:
            binary += str(current.val)
            current = current.next

        return binary

    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        return int(self.list_binary(head), 2)
