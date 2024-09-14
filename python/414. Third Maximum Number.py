nums =[2,3,-2134]
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        s=nums[0]
        c=1
        for i in range(len(nums)):
            if nums[i]!=s:
                s=nums[i]
                c+=1
            if c==3:
                return nums[i]
        return max(nums)
    

