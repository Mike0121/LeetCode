class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid_height = len(obstacleGrid)
        grid_width = len(obstacleGrid[0])
        path_count = [[0] * grid_width for _ in range(grid_height)]

        
        for height in range(grid_height):
            if obstacleGrid[height][0] == 1:
                break
            path_count[height][0] = 1

        for width in range(grid_width):
            if obstacleGrid[0][width] == 1:
                break
            path_count[0][width] = 1

        
        for height in range(1, grid_height):
            for width in range(1, grid_width):
                if obstacleGrid[height][width] == 1:
                    continue

                path_count[height][width] = path_count[height - 1][width] + path_count[height][width - 1]
        
        return path_count[height][width]