# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None

        dummy_head = ListNode(0, head)
        slow = dummy_head
        fast = head

        while fast and fast.next:
            while fast.next and fast.val == fast.next.val:
                fast = fast.next
            
            if slow.next != fast:
                slow.next = fast.next
                
            else:
                slow = slow.next

            fast = fast.next


        return dummy_head.next