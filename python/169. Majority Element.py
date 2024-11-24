class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import Counter
        d=Counter(nums)
        x=len(nums)//2
        for i in d:
            if d[i]>x:
                return i