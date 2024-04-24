class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        H = len(grid) #4
        W = len(grid[0]) #5
        #seen = [[]*W for _ in range(H)] #直接gridを更新するので不要
        moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        #※重要な考え方
        #すべての'1'からdfsを行い、dfsで通った点を'0'にする。
        #dfsが行われた点の数が、隣接するの数。

        def dfs(h, w):
            #移動先がない場合
            #※注意: 0~H-1, 0~W-1の範囲でseenを用意し、探索しているので、
            #        h = Hの場合は範囲外
            if h > H-1 or h < 0 or w > W-1 or w < 0 or grid[h][w] == '0':
                return 

            #if visit the place, mark the island. 
            #seen[h][w] = '0'
            grid[h][w] = '0'
            
            for move in moves:
                #h, w = h+move[0], w+move[1] #h,wの値は直接更新しない
                dfs(h+move[0], w+move[1])

        count = 0
        for i in range(H):
            for j in range(W):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
            
        