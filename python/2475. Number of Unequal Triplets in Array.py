class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        if set(nums)==1:
            return 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]!=nums[j]):
                    for k in range (j+1,len(nums)):
                        if(nums[i]!=nums[k] and nums[j]!=nums[k]):
                            count+=1
        return count