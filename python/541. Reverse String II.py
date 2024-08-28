class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        p=[]
        i=0
        while i<=len(s):
            p.append(s[i:i+k])
            i+=k
        for i in range(0,len(p),2):

            p[i]=p[i][::-1]
        return "".join(p)
        
