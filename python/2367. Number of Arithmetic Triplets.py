class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        count=0
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)):
                if nums[j]-nums[i]==diff:
                    for k in range (j+1,len(nums)):
                        if nums[k] - nums[j] == diff:
                            count+=1
                            
        return count