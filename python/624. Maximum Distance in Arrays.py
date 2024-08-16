class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        size=len(arrays)
        minEle=arrays[0][0]  
        maxEle=arrays[0][-1]
        ans=0
        for i in range(1,size):
            smin=arrays[i][0] 
            smax=arrays[i][-1] 
            x=abs(minEle-smax)
            y=abs(maxEle-smin)
            if minEle>smin: minEle=smin 
            else: minEle=minEle
            if maxEle<smax: maxEle=smax 
            else: maxEle=maxEle
            ans=max(ans,x,y)
        return ans