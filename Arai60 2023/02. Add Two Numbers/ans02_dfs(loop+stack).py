class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node_list = deque()
        carry = 0
        head = dummy = ListNode(0)

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            node = ListNode(total % 10)
            carry = total // 10

            node_list.append(node)

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        while node_list:
            next_node = node_list.popleft()
            dummy.next = next_node
            dummy = dummy.next

        return head.next


        