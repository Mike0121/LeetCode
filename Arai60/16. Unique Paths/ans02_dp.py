class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path_count = [[0] * n for _ in range(m)]

        path_count[0][0] = 1
        moves = [(1, 0), (0, 1)]
        
        for row in range(m):
            path_count[row][0] = 1

        for column in range(n):
            path_count[0][column] = 1

        for row in range(1, m):
            for column in range(1, n):
                path_count[row][column] += path_count[row - 1][column] + path_count[row][column - 1]

        return path_count[m - 1][n - 1]