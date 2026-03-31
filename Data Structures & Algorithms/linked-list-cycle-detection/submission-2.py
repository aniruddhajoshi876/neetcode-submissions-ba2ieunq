 #Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head):
        slow=head
        fast=head
        cycle = False
        while not cycle and fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast == slow:
                cycle = True
            if not fast:
                break
        return cycle



        