1:✖ 12.Oct.2023

1. ヒント
dp: 各amountにおいて必要なコインの最小量
for: 各コインが、そのdpのamountを作るのに最短経路となる場合に更新
高速化:コインを降順にならべて、breakを書くことで・・・。

2.
#dp[a]: これまでに見つかった金額aを作るための最小コイン数
#なぜ、a-c=0ではなく、a-c>=0なのか？
#coins=[1000], amount=1の場合、そもそもifに入らない。
#coins=[1], amount=1000の場合、1000回ループが繰り返され、dp[1000]にたどり着くまで
#都度、1が加算されていく。最終的にdp[1000]=1000になる。

#elseを通るのは、amountを既に超えていて、
#それ以降のコインを試す必要がない場合 (ただの高速化要素であり本質ではない)