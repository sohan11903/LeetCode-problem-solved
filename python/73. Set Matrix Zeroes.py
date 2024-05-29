class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        p = len(matrix)
        q = len(matrix[0])
        t=[]
        for i in range(p):      
            for j in range(q):
                k=[]
                if(matrix[i][j] == 0):
                    k=[i,j]
                    t.append(k)
        for i in range(len(t)):
            s=t[i][0]
            d=t[i][1]
            for w in range (q):
                matrix[s][w] = 0
            for x in range (p):
                matrix[x][d] = 0
        return matrix