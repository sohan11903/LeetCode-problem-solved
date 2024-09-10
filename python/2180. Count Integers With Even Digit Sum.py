class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        c=0
        for i in range(1,num+1):
            z=0
            while i>0:
                    g=i%10
                    z+=g
                    i=i//10
            if z%2==0:
                    c+=1
        return c