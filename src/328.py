# Definition for singly-linked list.
class ListNode:

    def __init__(self, x, next):
        self.val = x
        self.next = next 


class Solution:

    def oddEvenList(self, head):
        p = head
        prev, tail = None, None
        cnt = 0
        while p:
            cnt += 1
            prev = tail
            tail = p
            p = p.next
        if cnt % 2 == 0:
            tail = prev
        
        prev, p = None, head
        odd = True
        end = tail
        while p and p != end:
            q = p.next
            p.next = None
            if odd:
                if not prev:
                    prev = p
                else:
                    prev.next = p
                    prev = p
                odd = False
            else:
                p.next = tail.next
                tail.next = p
                tail = p
                odd = True
            p = q
        if prev:
            prev.next = p 
        return head

    def print_linked_list(self, head):
        while head:
            print(head.val)
            head = head.next
                
            
if __name__ == '__main__':
    obj = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    h = obj.oddEvenList(head)
    obj.print_linked_list(h)
