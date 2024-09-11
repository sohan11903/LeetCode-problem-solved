class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        d=str(n)
        ans=0
        for i in range(len(d)):
            z=int(d[i])
            if i%2==0:
                ans+=z
            else:
                ans-=z
        return ans