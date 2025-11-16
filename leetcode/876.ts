// Author: Mark O'Dowd
// Email: contact@markodowd.dev
// LeetCode: https://leetcode.com/u/markodowd

class ListNode {
  val: number
  next: ListNode | null
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val
    this.next = next === undefined ? null : next
  }
}

function middleNode(head: ListNode | null): ListNode | null {
  // If there is no head return null
  if (!head) {
    return null
  }

  // If there is only one node can just return it
  if (!head.next) {
    return head
  }

  // Two pointers
  let middleNode = head
  let endNode = head

  // Iterate through the list until the endNode reaches the end (endNode === null)
  while (endNode && endNode.next) {
    // Move the middleNode one step forward
    if (middleNode.next) {
      middleNode = middleNode.next
    }
    // Move the endNode two steps forward
    if (endNode.next.next) {
      endNode = endNode.next.next
    }
  }

  return middleNode
}
