class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x=0
        row=len(grid)
        col=len(grid[0])
        for i in range(0,row):
            for j in range(0,col):
                if(grid[i][j]<0):
                    x=x+1
        return x