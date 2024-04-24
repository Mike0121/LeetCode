1:✖(ビット演算)、✖(back tracking) 10.Dec.2023
解法への発想:
結果として、2^3通りの組み合わせ(各要素に関して入れるor入れない)が発生する。
recursiveにこの問題を解く場合、
i = 0が最初に入り、
j = 0 ~2でループが回る。**j=2でbacktracking関数に突入した場合それ以上のループは発生しない。**
j = 0(1) ⇒ j = 1(1, 2) ⇒ j = 2(1, 2, 3)
						⇒ j = 3(1, 3)
j = 1(2のみ) ⇒ j = 2(2,3)
j = 2(3のみ)
ポイントとして、この書き方をした場合、numsの同じインデックスの値が2度はいらないことである。



NeetCode解説:
https://www.youtube.com/watch?v=REOH22Xwdkk

類題:
https://leetcode.com/problems/permutations/?envType=list&envId=rbx9vwti

0. バックトラッキングの図示
おそらく、ツリー(樹形図)が一番わかりやすい。
ツリーをコードにできるようになると強そう。

1. ビット演算で2^Nの組み合わせを生成


例えば、N=3のとき、
for i in range(2^N) では、0~7 が生成される。
これは、2進数表現で、000 ~ 111 となる。

これと、j:0~3の2進数表現である、001, 010, 100 の&がTrueになるとき、
numsの中からjの対応するビットが立っているインデックスの値を追加する。

i & (1 << j) が True になるのは、i の対応する j 番目のビットが1である場合である。
例えば、i = 3 (011 と表される)の場合、j = 0 と j = 1 で True（011 & 001 と 011 & 010）。
(各bitのうち、一つでも同じ位置に1が立っていればTrueになる。(結果が0にならないため))

```
class Solution:
    def subsets(self, nums):
        N = len(nums)
        result = []

        for i in range(2 ** N):
            subset = []
            for j in range(N):
                if i & (1 << j):
                    subset.append(nums[j])
            result.append(subset)

        return result
```
