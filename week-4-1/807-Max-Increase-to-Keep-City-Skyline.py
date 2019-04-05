class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = map(max, grid)
        col = map(max, zip(*grid))
        after_increase = sum(min(i, j) for i in row for j in col)
        original = sum(map(sum, grid))

        return after_increase - original
        
       
        
