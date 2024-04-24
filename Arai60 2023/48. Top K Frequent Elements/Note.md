1:△ 05.Oct.2023


1.   dictを"valueの値"で"降順"にソートし、"k番目まで"の"keyの値"を取得する。
計算量: O(n log n) + O(k) (sorted関数がO(nlong))
```
 sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
 return [item[0] for item in sorted_d[:k]]
```