class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in nums:
            c=[]
            while i>0:
                x=i%10
                c.append(x)
                i=i//10
            c=c[::-1]
            for i in c:
                a.append(i)
        return a