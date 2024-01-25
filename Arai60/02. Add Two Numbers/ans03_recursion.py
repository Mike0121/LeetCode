class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def add_two_numbers(l1, l2, carry):
            if not l1 and not l2 and carry == 0:
                return None

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            node = ListNode(total % 10)
            carry = total // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            upper_digits = addtwonumbers(l1, l2, carry)
            node.next = upper_digits

            return node

        return add_two_numbers(l1, l2, 0)

        