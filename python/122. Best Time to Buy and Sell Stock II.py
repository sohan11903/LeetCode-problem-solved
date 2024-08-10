class Solution(object):
    def maxProfit(self, p):
        """
        :type prices: List[int]
        :rtype: int
        """
        cost = 0
        for i in range(1,len(p)):
            if(p[i]>p[i-1]):
                cost+=p[i]-p[i-1]
        return cost
        