class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        root_count = [[0] * n for _ in range(m)]

        root_count[0][0] = 1
        moves = [(1, 0), (0, 1)]
        
        for row in range(m):
            root_count[row][0] = 1

        for column in range(n):
            root_count[0][column] = 1

        for row in range(1, m):
            for column in range(1, n):
                root_count[row][column] += root_count[row - 1][column] + root_count[row][column - 1]

        return root_count[m - 1][n - 1]