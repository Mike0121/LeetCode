class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #DPによる解答
        #dpテーブルの作成
        #dpテーブルに加算するのは、
        #その道にたどり着くまでのルート
        dp = [[0]*(n) for _ in range(m)]


        #dpテーブルの初期化
        dp[0][0] = 1

        #重要
        #各列と行を1で初期化する
        #最初の1行の各セルに到達する方法は、常に左のセルからの移動のみ
        #したがって、最初の1行の各セルに到達するユニークなパスの数は1となります。
        for i in range(m):
            dp[i][0] = 1

        for i in range(n):
            dp[0][i] = 1
        
        for i in range(1, n):
            for j in range(1, m):
                dp[j][i] += dp[j-1][i] + dp[j][i-1]

        return dp[m-1][n-1]
        