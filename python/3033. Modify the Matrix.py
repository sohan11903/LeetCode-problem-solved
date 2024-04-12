class Solution(object):
    def modifiedMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        c=[]
        max=[]
        for j in range(len(matrix[0])):     
            for i in range(len(matrix)):
                c.append(matrix[i][j])
                s=sorted(c)
            max.append(s[len(matrix)-1])
            c=[]

     

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j]==-1):
                    matrix[i][j]=max[j]
                    
        return matrix