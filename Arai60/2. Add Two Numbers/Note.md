1:✖ 10.Dec.2023

1. new_linked_listとcurrentの違いを答えよ。
new_linked_list と current の違いは、それぞれがリンクリスト内で異なる役割を果たすことにあります。new_linked_list は新しいリンクリストの先頭ノード（ヘッド）を常に指しています。これはリンクリストの最初のノードであり、リンクリスト全体への入り口となります。一方、current は新しいリンクリストの最後のノードを指し、新しいノードがリンクリストに追加されるたびに更新されます。この current ポインタを使用することで、リンクリストの末尾に新しいノードを効率的に追加することができます。new_linked_list は全体のリンクリストへの参照を保持し続け、current は新しいノードの追加場所を追跡します。

2. 何度やっても
下記を各箇所を間違える。
```
l1 = l1.next if l1 else None
l2 = l2.next if l2 else None
```

3. よくある間違え
下記のコードの何がダメかを指摘してみよう。
```
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        new_node = ListNode((l1.val + l2.val) % 10)
        carry_over = (l1.val + l2.val) // 10

        new_linked_list = new_node

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

        while l1 or l2 or carry_over:
            #l1, l2のいずれかがNoneだった場合に0を入れるよう、v1,v2を用意。
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sub_total = v1 + v2 + carry_over

            new_node = ListNode((sub_total)%10)
            #print(new_node.val)
            new_linked_list.next = new_node
            new_linked_list = new_linked_list.next

            carry_over = sub_total // 10
        
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return new_linked_list
```