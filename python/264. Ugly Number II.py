class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[]
        for i in range(n):
            dp.append(0)
        dp[0]=1
        p1=0
        p2=0
        p3=0
        for i in range(1,n):
            twomul=dp[p1]*2
            threemul=dp[p2]*3
            fifthmul=dp[p3]*5
            dp[i]=min(twomul,threemul,fifthmul)
            if dp[i]==twomul: p1+=1
            if dp[i]==threemul: p2+=1
            if dp[i]==fifthmul: p3+=1
        return dp[n-1]
        