# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def get_intersection_node(headA, headB):
    p, q = headA, headB
    pp, qq = headA, headB
    
    while p and q:
        p = p.next
        q = q.next
    
    while p:
        p = p.next
        pp = pp.next
    while q:
        q = q.next
        qq = qq.next
    
    while pp and qq and pp != qq:
        pp = pp.next
        qq = qq.next
    return pp
