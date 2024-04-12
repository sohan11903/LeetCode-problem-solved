class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        y=len(s)
        one=0
        ans=""
        for i in range(0,y):
            if(s[i]=='1'):
                one=one+1
        for i in range(1,one):
            ans=ans+"1"
        for i in range(y-one):
            ans=ans+"0"
        return  ans+"1"
       