
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        dummy.next = head
        slow = dummy 
        fast = dummy

        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        #remove node 
        slow.next = slow.next.next
        return dummy.next
