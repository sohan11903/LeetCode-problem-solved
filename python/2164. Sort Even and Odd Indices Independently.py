class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        odd=[]
        even=[]
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        o,e=0,0
        for i in range(len(nums)):
            if i%2==0:
                nums[i]=even[e]
                e+=1
            else:
                nums[i]=odd[o]
                o+=1
        return nums