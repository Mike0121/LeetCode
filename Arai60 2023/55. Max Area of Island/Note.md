1:△ 23.Dec.2023
解法への発想:
ほぼすべて思いついた。最初、dfsが行われた回数(島の回数)をカウントしていた。
dfsが行われていた回数をカウントする書き方は、基本は覚える。



1. dfsが行われた回数を数える
(i)もし何も行われなかった場合は0を返す。 (if ~ return 0)1回にはカウントしない。
(ii)seen(この場合はgrid)を更新する際に、countを変数とし、4方向のdfsが行われた回数分を加算して返す。
(iii)各関数で返すのは、count。(return count)
```
def dfs(h, w):

		if h < 0 or H <= h or w < 0 or W <= w or grid[h][w] == 0:
				return 0

		grid[h][w] = 0
		count = 1

		count += dfs(h+1, w)
		count += dfs(h-1, w)
		count += dfs(h, w+1)
		count += dfs(h, w-1)

		return count
```
