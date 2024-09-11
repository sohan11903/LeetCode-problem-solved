class Solution(object):
    def minBitFlips(self, s, g):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        s=list(bin(s)[2:])
        g=list(bin(g)[2:])
        c=0
        if len(s)!=len(g):
            for i in range(abs(len(s)-len(g))):    
                if len(s)>len(g):
                    g.insert(0,'0')
                else:
                    s.insert(0,'0')
        for i in range(len(s)):
            if s[i]!=g[i]:
                c+=1
        return c
