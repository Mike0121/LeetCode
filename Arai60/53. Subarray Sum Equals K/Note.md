1:✖ 18.Dec.2023

1. TwoPointersでやろうとするも、うまくいかず。
配列に負の数が含まれる場合や、和が k になる部分配列が複数回にわたって継続する場合には、スライディングウィンドウだけでは不十分なことが多い。

2. countHashMap[0] = 1の理由
countHashMap[0] = 1に設定する理由は、左側にいきなりtargetを満たすsumが来た場合、1を加えたいから。
nums [2, 1, -1, 1, ...] k = 3の場合、[2. 1]にたどり着いた時点で、ans=1にするため、countHashMap[0] = 1にしておく。