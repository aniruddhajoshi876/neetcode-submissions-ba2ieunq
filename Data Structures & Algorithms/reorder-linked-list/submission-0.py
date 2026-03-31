#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head):

        #splitting
        node = head
        slow = node
        fast = node

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        l1 = head
        l2 = slow.next
        slow.next = None

        #reverse

        current = l2
        previous = None
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        #merge
        l2 = previous

        while l1 and l2:
            temp1 = l1.next
            l1.next = l2
            l1 = temp1
            temp2 = l2.next
            l2.next = temp1
            l2=temp2
            
        