class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row=len(grid)
        col=len(grid[0])

        x=0
        if(row==1 and col==1):
            if grid[row-1][col-1]==1:
                x=4
            else:
                x=0
        else:
            for i in range(0,row):
                for j in range(0,col):
                    if(grid[i][j]==1):
                        
                        if(j+1>col-1 or grid[i][j+1]==0):
                            x=x+1
                        if(grid[i][j-1]==0 or j-1==-1):
                            x=x+1
                        if(grid[i-1][j]==0 or i-1==-1):
                            x=x+1
                        if(i+1>row-1 or grid[i+1][j]==0):
                            x=x+1
        return x
        