class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        ans=[-1,-1]
        j=len(nums)-1
        ri,rj=False,False
        while(ri != True or rj!=True) and i <= j :
            if nums[i]==target:
                ans[0]=i
                ri=True
            else:
                i+=1
            if nums[j]==target:
                ans[1]=j
                rj=True
            else:
                j-=1
        return ans
