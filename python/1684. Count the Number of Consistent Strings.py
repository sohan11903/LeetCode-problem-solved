class Solution(object):
    def countConsistentStrings(self, a, w):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        c=0
        r=set(a)
        for i in w:
            if set(i).issubset(r):
                c+=1
        return c