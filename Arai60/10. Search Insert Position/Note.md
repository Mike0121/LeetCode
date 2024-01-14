1:✖ 10.Dec.2023

NeetCode解説
https://www.youtube.com/watch?v=K-RYzDZkzCI

1. Pythonの//
Pythonの // は、「床除算（floor division）」を行い、割り算の結果を小数点以下を切り捨てた整数にする。
この演算子は、割り算の結果から小数部分を取り除き、最も近い小さい整数に丸める。
ex)  7 // 3 ⇒ 2 , -7 // 3 ⇒ -3 
小数点以下の部分がある場合でも、それを無視して最も近い小さい整数を返す。

2. 二分探索の注意点
・r = len(nums) としない
・r = mid - 1 or while l < r:のどちらかにする。
※基本的には、while l <= r, r = mid-1とする。

3.典型
下記のコードの誤りを、そしてなぜかを指摘してみよう。
```
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            mid = (l+r)//2
            
            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                l = mid + 1

            elif nums[mid] > target:
                r = mid - 1

        return l
```

A.
(i) r の初期値を len(nums) としていますが、これはリストの末尾の要素を指していません。len(nums) - 1 が正しい末尾のインデックスです。

(ii) r = mid - 1 とすることは不適切です。通常の2分探索では、r に mid をそのまま代入するべきです。これは、検索範囲を半分に減らす際に、中央値を含まないようにするためです。
               