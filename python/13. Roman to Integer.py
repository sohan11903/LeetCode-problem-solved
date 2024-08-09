class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        keys = list(s) 
        c=d[keys[0]]
        for i in range(1,len(keys)):
            if d[keys[i]] > d[keys[i-1]]:
                c -= d[keys[i-1]]
                c += d[keys[i]] - d[keys[i-1]]  
            else:
                c += d[keys[i]] 
        return c