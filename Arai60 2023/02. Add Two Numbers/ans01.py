# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        new_node = ListNode((l1.val + l2.val) % 10)
        carry_over = (l1.val + l2.val) // 10

        #new_linked_listの命名は、new_linked_list_headのほうが絶対にわかりやすい。
        #(詳しくはNote1.参照)
        new_linked_list = new_node
        current = new_linked_list

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

        while l1 or l2 or carry_over:
            #l1, l2のいずれかがNoneだった場合に0を入れるよう、v1,v2を用意。
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sub_total = v1 + v2 + carry_over

            new_node = ListNode((sub_total)%10)
            #print(new_node.val)
            current.next = new_node
            current = current.next


            carry_over = sub_total // 10
        
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return new_linked_list
