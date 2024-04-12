class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x=0
        for i in nums:
            nums[x]=i*i
            x=x+1

        ans = sorted(nums)

        return ans