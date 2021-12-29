# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        ans = self.recurse(head)
        head.next=None
        return ans
        
    def recurse(self,head):
        nxt = head.next
        if nxt is None:
            return head
        
        temp= self.recurse(nxt)
        head.next.next=head
        return temp