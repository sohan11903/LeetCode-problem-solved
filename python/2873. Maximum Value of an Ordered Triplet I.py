class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = []
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)):
                for k in range (j+1,len(nums)):
                    k=((nums[i]-nums[j])*nums[k])
                    ans.append(k)
        if max(ans)<0:
            return 0
        return max(ans)  