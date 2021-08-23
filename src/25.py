# Definition for singly-linked list.
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        
        p = head
        t = k
        while p and t:
            p = p.next
            t -= 1
        if t > 0:
            return head
        
        newHead, tail = self.reverse(head, k)
        tail.next = self.reverseKGroup(p, k)
        return newHead
        
    def reverse(self, head, k):
        pre = None
        p = head
        while p and k:
            nxt = p.next
            p.next = pre
            pre = p
            p = nxt
            k -= 1
        return pre, head
            
