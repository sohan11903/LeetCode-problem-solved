class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
       
        valid = set([i+1 for i in range(len(matrix))])
        for i in range(len(matrix)):
            if(set(matrix[i])!=valid):
                return False
        for j in range(len(matrix)):
            if set([matrix[i][j] for i in range(len(matrix))]) != valid:
                return False
        return True
            