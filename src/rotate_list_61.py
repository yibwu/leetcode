# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next 


class Solution:
    def rotate_right(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        k = k % self.get_lens(head)
        if k == 0:
            return head

        # separate linklist by k, then rotate two linklist separatly
        last_k = self.go_last_k_element(head, k)
        list_1 = self.rotate_list(head)
        list_2 = self.rotate_list(last_k)

        # concat two separate linklist
        p = list_1
        while p and p.next:
            p = p.next
        p.next = list_2

        # rotate whole list
        new_head = self.rotate_list(list_1)
        return new_head

    def print_list(self, head):
        while head is not None:
            print(head.val)
            head = head.next

    def rotate_list(self, head):
        if head is None:
            return head
        else:
            tail, p = None, head
            while p and p.next:
                t = p.next
                p.next = tail
                tail = p
                p = t
            p.next = tail
            return p
    
    def go_last_k_element(self, head, k):
        pre = head
        fast, slow = head, head
        for _ in range(k):
            fast = fast.next
        
        while fast is not None:
            fast = fast.next
            pre = slow
            slow = slow.next
        pre.next = None
        return slow

    def get_lens(self, head):
        count = 0
        while head is not None:
            count += 1
            head = head.next
        return count


if __name__ == '__main__':
    o = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))) 
    ret = o.rotate_right(head, 2)
    o.print_list(ret)
