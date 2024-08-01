class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        a = [[0] * n for _ in range(n)]
        x=1
        m=n-1
        right=m
        bottom=m
        left=0
        top=0
        
        ans=[]
        while(top<=bottom and left<=right):
            for i in range(left,right+1):
                a[top][i]=x
                x+=1
            top+=1
            for i in range(top,bottom+1):
                a[i][right]=x
                x+=1
            right-=1
            if(top<=bottom):
                for i in range(right,left-1,-1):
                    a[bottom][i]=x
                    x+=1
                bottom-=1
            if(left<=right):
                for i in range(bottom,top-1,-1):
                    a[i][left]=x
                    x+=1
                left+=1
            
        return a