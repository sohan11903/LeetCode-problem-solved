class Solution(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i,j,k,l in combinations(nums, 4):
            if i+j+k == l:
                count += 1
        return count
        