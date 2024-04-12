class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        x=""
        s=[]
        for i in (digits):
            x=x+str(i)
        y=int(x)+1
        z=str(y)
        r=len(z)
        for i in range(0,r):
            w=int(int(z)%10)
            s.append(w)
            z=int(z)/10
        return s[::-1]