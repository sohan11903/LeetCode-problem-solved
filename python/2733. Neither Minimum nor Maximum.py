class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if len(nums)<3:
            return -1
        s=len(nums)//2
        if len(nums)%2!=0:
            return nums[s]
        return nums[s-1]