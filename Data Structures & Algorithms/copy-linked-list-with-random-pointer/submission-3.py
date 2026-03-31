"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head):

        if not head:
            return

        #create hashmap
        copy = {}
        dummy = head
        while dummy:
            copy[dummy] = Node(dummy.val)
            dummy = dummy.next

        temp = head
        while temp:
            if temp.next:
                copy[temp].next = copy[temp.next]
            if temp.random:
                copy[temp].random = copy[temp.random]
            temp = temp.next
        
        return copy[head]
        