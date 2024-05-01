class Solution(object):
    def minimumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        s=[]
        for i,j,k in combinations(nums,3):
            if(i<j and j>k):
                ans=i+j+k
                s.append(ans)   
        if len(s) == 0:
            return -1   
        return min(s)