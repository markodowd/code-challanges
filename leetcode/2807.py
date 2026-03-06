from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def find_gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        current = head

        while current and current.next:
            gcd_val = self.find_gcd(current.val, current.next.val)

            new_node = ListNode(gcd_val, current.next)

            current.next = new_node

            current = new_node.next

        return head
