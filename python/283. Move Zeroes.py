class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        x = len(nums)
        while i < x:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                x=x-1
            else:
                i+=1
        return nums