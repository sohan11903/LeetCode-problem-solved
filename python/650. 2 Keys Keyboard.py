class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        current=1
        count=0
        buffer=0
        while(current<n):
            rest=n-current
            if rest % current == 0:
                buffer=current
                current+=buffer
                count+=2
            else:
                current+=buffer
                count+=1  
        return count