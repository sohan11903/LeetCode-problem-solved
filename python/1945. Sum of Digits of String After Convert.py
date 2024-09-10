class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ans=""
        new=""
        l=[]
        for i in s:
            c=str((ord(i)-ord('a'))+1)
            new+=c
        for i in range(k):
            new=str(sum(int(f) for f in new))
        return int(new)