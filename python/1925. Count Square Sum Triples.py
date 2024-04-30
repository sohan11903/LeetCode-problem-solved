class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums=[]
        count = 0
        for i in range (0,n):
            nums.append((i+1)*(i+1))

        for i in range(0,n):
            for j in range(i+1,n):
                if(nums[i]+nums[j] in nums):
                    count+=1
        return (count*2)