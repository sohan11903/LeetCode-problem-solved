class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        x=0

        row = len(mat)
        col = len(mat[0])
        if(row%2!=0):
            for i in range(0, row):
                x=x+mat[i][i]+mat[i][col-1-i]

            x=x-mat[int(row/2)][int(row/2)]

        else:
            for i in range(0, row):
                x = x + mat[i][i] + mat[i][col - 1 - i]
        return x
