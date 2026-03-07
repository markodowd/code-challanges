from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        modify = head.next
        next_sum = head.next

        while next_sum:
            running_total = 0

            while next_sum.val != 0:
                running_total += next_sum.val
                next_sum = next_sum.next

            modify.val = running_total
            next_sum = next_sum.next
            modify.next = next_sum
            modify = modify.next

        return head.next
