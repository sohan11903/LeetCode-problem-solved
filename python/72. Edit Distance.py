class Solution(object):
    def minDistance(self, a, b):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m=len(a)+1
        n=len(b)+1
        mat=[[0 for _ in range(m)] for _ in range(n)]
        for i in range(m):
            mat[0][i]=i
        for i in range(n):
            mat[i][0]=i
        for i in range(1,n):
            for j in range(1,m):
                if(b[i-1]==a[j-1]):
                    mat[i][j]=mat[i-1][j-1]
                else:
                    mat[i][j]=(min(mat[i-1][j-1],mat[i][j-1],mat[i-1][j])+1)
                
        return (mat[n-1][m-1])