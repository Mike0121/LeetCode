1:✖ 25.Nov.2023

1. listのlistを、内部のlistの1つ目の値をkeyとして並び替える
list.sort(key = lambda i : i[0])
※i[0] が同じである内部リスト間では、元の順序（安定ソート）が保持される。
※破壊的、計算量: O(NlogN)

0番目の要素に基づいてソートした後、1番目の要素に基づいてさらにソートするには:
list.sort(key=lambda i: (i[0], i[1]))