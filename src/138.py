# Definition for a Node.
class Node:

    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    
    def copyRandomList(self, head):
        p = head
        while p:
            q = p.next
            newNode = Node(p.val, p.next, p.random)
            p.next = newNode
            p = q
            
        oldNode = head
        while oldNode:
            newNode = oldNode.next
            if newNode.random:
                newNode.random = newNode.random.next
            oldNode = newNode.next
        
        if head:
            newNode = head.next
            while newNode and newNode.next:
                newNode.next = newNode.next.next
                newNode = newNode.next
            return head.next
        else:
            return None
