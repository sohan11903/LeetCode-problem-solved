class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=set(nums)
        nums.discard(0)
        return len(nums)