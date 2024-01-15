3:× 10.Dec.2023

1. Linked Listの構造における重要な勘違い
23, 54, 78, 90のLinked Listを考える。
(各メモリ番地は1000, 2000, 3000, ... とする。)

勘違い:
23|1000 (head) ⇒ 54|2000 ⇒ 78|3000 ⇒ 90|4000 (tail)

正解:
23|2000 (head) ⇒ 54|3000 ⇒ 78|4000 ⇒ 90|NULL (tail) (通常(Python)はこっち)
or
-|1000 (head) ⇒ 23|2000 ⇒ 54|3000 ⇒ 78|4000 ⇒ 90|NULL (tail) (明示的にheadを定義する場合)

あるノードに格納されるのは、そのノードの値(val)と、"次のノードの番地"であることに注意。

また、LinkedListにおいてnodeを指すというのは、ポインタを指すということ。
current = headとした場合、currentにheadのポインタを代入。
current.next は、リンクリストのノードの「次のノードへの参照（ポインタ）」を指す。
ex)current = 23|2000を指している場合、current.nextは54|3000 
(current.nextはcurrentが指す次の番地、2000を指すわけではないので注意)


2. 新しいLinked Listの作成方法
-空のLinkedListを作成
new_linked_list = None
※リンクリストが初期状態で何も含まれていないこと、またはリンクリストの末尾を示すためによく使われます。
(今回は末尾して作成している。)

-値が1のLinkedListを作成
new_linked_list = ListNode(1)

-ノードの追加
new_linked_list.next = ListNode(2)  # 2を値とする次のノードを追加