class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def dfs(i, j, grid):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return dfs(i, j+1, grid) + dfs(i+1, j, grid) + dfs(i-1,j,grid) + dfs(i,j-1,grid) + 1
                
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                count = max(count, dfs(i,j,grid))
                    
        return count
