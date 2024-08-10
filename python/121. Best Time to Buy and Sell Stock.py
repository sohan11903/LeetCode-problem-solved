class Solution(object):
    def maxProfit(self, p):
        """
        :type prices: List[int]
        :rtype: int
        """
        mi=p[0]
        maxProf = 0
        for i in range(1,len(p)):
            cost=p[i]-mi
            maxProf=max(maxProf,cost)
            mi=min(mi,p[i])
        return maxProf