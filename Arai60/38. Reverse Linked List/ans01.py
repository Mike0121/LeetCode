# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list_head = None
        curr = head 

        while curr:
            
            #2⇒3⇒4⇒5を一旦tmpに保存
            tmp = curr.next

            #1⇒new_list_head
            curr.next = new_list_head

            #new_listの最後尾をcurrに移動
            new_list_head = curr

            curr = tmp

        return new_list_head
