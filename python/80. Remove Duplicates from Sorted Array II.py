class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p=len(nums)
        s=set(nums)
        for a in s:
            i=0
            z=nums.count(a)
            if z>2:
                i=z-2
                for e in range(i):
                    nums.remove(a)
        return p