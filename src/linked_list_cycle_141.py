# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next):
        self.val = x
        self.next = next


class Solution(object):
    def has_cycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        if head == head.next:
            return True

        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if not fast or slow == fast:
                break
        return True if slow == fast else False


if __name__ == '__main__':
    o = Solution()
    head = ListNode(1, ListNode(2, None))
    ret = o.has_cycle(head)
    print(ret)