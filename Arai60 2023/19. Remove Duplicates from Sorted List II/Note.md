1:✖ 15.Dec.2023 (難)
解法への発想:
この問題の肝は、確実に**while文後の"場合分け"**である。
2パターンの追加があり得ることに気付けるかどうか。
while文でfastを 動かした後、下記の2パターンが考えらえれる。

(i) while fast.val == fast.next.valを通過した場合:
A(slow) ⇒ B(slow.next) ⇒ C(fast) ⇒ E(fast.next)のようになり、
BとCは同じ値であり(slow.next != fast)、Cはスキップしなくてはならない。
そのため、slow.next = fast.nextにする。

(ii) while fast.val == fast.next.valを通過しなかった場合:
A(slow) ⇒ B(slow.next, fast) ⇒ C(fast.next)のようになり、
AとBが異なる値であり(while文を通過していない)、slow.next == fastとなる。
この場合は、slowを次に進めるだけ。

1. ノードの値の比較
val で比較するのを忘れない。

2. 本問のノードの更新方法
少し今回の解法のノードの更新方法はややこしいため、注意が必要。
最終的には、新しく作成したdummyを、prevで更新して返すが、
while内では、**curのポインタを都度更新し、必要があればprev(prev.nextではなく)をcurに直接置き換える**
方法を取っている

また、prev.nextとcurは、値ではなく直接ノードを比較していることに注意。