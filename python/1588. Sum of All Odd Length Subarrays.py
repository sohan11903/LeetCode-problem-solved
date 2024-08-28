class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n=1
        s=0
        ind=0
        while n<=len(arr):
            x=n
            ind=0
            while(n<=len(arr)):
                s += sum(arr[ind:n])
                ind+=1
                n+=1
            n=x
            n+=2
        return s