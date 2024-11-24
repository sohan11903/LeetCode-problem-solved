class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        ans=[]
        x=len(nums)//3
        for i in d:
            if d[i]>x:
                ans.append(i)
        return ans