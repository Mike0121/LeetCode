class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        H, W = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [[0] * W for _ in range(H)]
        
        for h in range(H):
            if obstacleGrid[h][0] == 1:
                break

            dp[h][0] = 1


        for w in range(W):
            if obstacleGrid[0][w] == 1:
                break

            dp[0][w] = 1

        for h in range(1, H):
            for w in range(1, W):
                if obstacleGrid[h][w] == 1:
                    continue

                dp[h][w] = dp[h-1][w] + dp[h][w-1]

        return dp[H-1][W-1]
        