class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        x=len(matrix)
        y=len(matrix[0])
        for i in range(x):
            for j in range(y):
                if matrix[i][j]==target:
                    return True
        return False