class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse_linked_list(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next      # store next node
            curr.next = prev     # reverse pointer
            prev = curr          # move prev forward
            curr = nxt           # move curr forward
        return prev
