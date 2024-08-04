class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        d=set(nums)
        ans=[]
        for i in d:
            ans.append([nums.count(i),i])
        ans.sort()
        return (ans[len(d)-1][1])
        