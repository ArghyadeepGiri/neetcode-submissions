# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        temp1 = head.next
        temp2 = head.next.next
        while temp1 != temp2:
            try:
                temp1 = temp1.next
                temp2 = temp2.next.next
            except:
                return False
        return True
        