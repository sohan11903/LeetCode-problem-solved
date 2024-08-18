class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        d={}
        ans=[[],[]]
        for i in matches:
            d[i[0]]=0 
            d[i[1]]=0
        for i in matches:
            d[i[0]]+=0 
            d[i[1]]+=1
        for i in d:
            if d[i]==0:
                ans[0].append(i)
            if d[i]==1:
                ans[1].append(i)
        ans[0].sort()
        ans[1].sort()
        return ans