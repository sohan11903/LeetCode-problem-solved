class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for i in nums:
            if i<0:
                if i*-1 in nums:
                    return i*-1
        return -1