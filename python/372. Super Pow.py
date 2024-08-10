class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if a==1:
            return 1
        x=int("".join(map(str,b)))
        return pow(a,x,1337)
        