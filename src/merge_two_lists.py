# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_lists_recursive(l1, l2):
    if not l1 or not l2:
        return l1 if not l2 else l2
    elif l1.val <= l2.val:
        if not l1.next:
            l1.next = l2
        elif l2.val <= l1.next.val:
            l1_next = l1.next
            l1.next = l2
            l2.next = merge_two_lists_recursive(l1_next, l2.next)
        else:
            l1.next = merge_two_lists_recursive(l1.next, l2)
        return l1
    else:
        return merge_two_lists_recursive(l2, l1)


def merge_two_lists_iter(l1, l2):
    if not l1 or not l2:
        return l1 if not l2 else l2

    head = l1 if l1.val < l2.val else l2
    cur = head

    while l1 and l2:
        if cur == l1:
            if not l1.next:
                cur.next = l2
                break
            elif l2.val < l1.next.val:
                l1_next = l1.next
                cur.next = l2
                cur = l2
                l1 = l1_next
            else:
                l1 = l1.next
                cur = l1
        else:
            l1, l2 = l2, l1
    return head


if __name__ == '__main__':
    nums1 = [-9, -5, -3, -2, -2, 3, 7]
    l1 = [ListNode(n) for n in nums1]
    i = 0
    while i < len(l1) - 1:
        l1[i].next = l1[i + 1]
        i += 1

    nums2 = [-10, -8, -4, -3, -1, 3]
    l2 = [ListNode(n) for n in nums2]
    i = 0
    while i < len(l2) - 1:
        l2[i].next = l2[i + 1]
        i += 1

    #head = merge_two_lists_recursive(l1[0], l2[0])
    head = merge_two_lists_iter(l1[0], l2[0])
    while head:
        print(head.val)
        head = head.next
