class Solution(object):
    def spiralOrder(self, a):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n=len(a)-1
        m=len(a[0])-1
        right=m
        bottom=n
        left=0
        top=0
        
        ans=[]
        while(top<=bottom and left<=right):
            for i in range(left,right+1):
                ans.append(a[top][i])
            top+=1
            for i in range(top,bottom+1):
                ans.append(a[i][right])
            right-=1
            if(top<=bottom):
                for i in range(right,left-1,-1):
                    ans.append(a[bottom][i])
                bottom-=1
                
            if(left<=right):
                for i in range(bottom,top-1,-1):
                    ans.append(a[i][left])
                left+=1
            
        return ans