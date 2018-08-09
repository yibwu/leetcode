# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next):
        self.val = x
        self.next = next


class Solution(object):
    def merge_k_lists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = None if not lists else self.merge_sort(0, len(lists) - 1, lists)
        return head

    def merge(self, left, right):
        if not left or not right:
            return left if left else right
        else:
            if left.val < right.val:
                head = left
                left = left.next
            else:
                head = right
                right = right.next

        t, p, q = head, left, right
        while p and q:
            if p.val < q.val:
                t.next = p
                t = p
                p = p.next
            else:
                t.next = q
                t = q
                q = q.next
        while p:
            t.next = p
            t = p
            p = p.next
        while q:
            t.next = q
            t = q
            q = q.next
        return head

    def merge_sort(self, left, right, lists):
        if left < right:
            pivot = left + (right - left) // 2
            head_left = self.merge_sort(left, pivot, lists)
            head_right = self.merge_sort(pivot + 1, right, lists)
            head = self.merge(head_left, head_right)
            return head
        else:
            return lists[left]


if __name__ == '__main__':
    o = Solution()
    list1 = ListNode(1, ListNode(4, ListNode(5, None)))
    list2 = ListNode(1, ListNode(3, ListNode(4, None)))
    list3 = ListNode(2, ListNode(6, None))
    lists = [list1, list2, list3]
    ret = o.merge_k_lists(lists)
    while ret:
        print(ret.val)
        ret = ret.next