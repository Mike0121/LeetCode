1:✖(for), ✖(sliding-window) 08.Oct.2023

Kadaneのアルゴリズム: O(n)
整数のリストの中で最大の連続する部分配列の和を効率的に見つけるためのアルゴリズム
基本的な考え方は、現在の要素を含む部分配列の最大和を計算し、それを以前の最大和と比較して更新する。もし現在の部分配列の和が0未満になった場合、その部分配列は最大和を持つ可能性がないので、和を0にリセットする。

1. 余計なテクニックの分類にとらわれない

2. 和がマイナスになった時点で、sum=0とすることでansをリセットする

Quiz.
Subaaryではなく、SubSequenceだった場合、どのように変更をするべきか？
スライディングウィンドウを用いた解き方で書き直す。
