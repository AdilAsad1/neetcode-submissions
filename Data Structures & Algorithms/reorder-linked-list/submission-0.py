# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return 

        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        
        curr = head
        for i in range(len(stack)//2):
            a = curr.next
            tail = stack.pop()
            curr.next = tail
            tail.next = a
            curr = a
        curr.next = None

