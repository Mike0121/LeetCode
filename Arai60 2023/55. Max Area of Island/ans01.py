class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        H, W = len(grid), len(grid[0])

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

        
        ans = 0

        for i in range(H):
            for j in range(W):
                if grid[i][j] == 1:

                    ans = max(dfs(i, j), ans)
                    
        return ans
