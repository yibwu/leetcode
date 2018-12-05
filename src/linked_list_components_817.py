# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next):
        self.val = x
        self.next = next


class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        len = self.len_link_list(head)
        arr = [0 for _ in range(len)]
        matrix = [arr for _ in range(len)]
        print(matrix)
        self.init_graph(head, matrix)
        print(matrix)

        # res = self.get_components(head, G)
        # return res

    def init_graph(self, head, matrix):
        count = 0
        while head and head.next:
            print(count, count+1)
            matrix[count][count + 1] = 1
            count += 1
            head = head.next


    def len_link_list(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def get_components(self, head, G):
        G.sort()
        p = head
        changed = False
        count = 0
        i = 0
        while i < len(G):
            while p and i < len(G) and p.val == G[i]:
                i += 1
                p = p.next
                changed = True
            if changed:
                count += 1
                changed = False
            if p:
                p = p.next
        return count


if __name__ == '__main__':
    # head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4, None)))))
    # G = [0, 3, 1, 4]
    # head = ListNode(0, ListNode(1, ListNode(2, None)))
    # G = [1, 0]
    head = ListNode(0, ListNode(2, ListNode(4, ListNode(3, ListNode(1, None))))) # [0, 2, 4, 3, 1]
    G = [3, 2, 4]
    o = Solution()
    o.numComponents(head, G)
    # o.walk_link_list(head)
    # ret = o.get_components(head, G)
    # print(ret)