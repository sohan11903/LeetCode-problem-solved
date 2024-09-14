class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()
        x=int(len(arr)*0.05)
        arr=arr[x:len(arr)-x]
        sum=0
        le=0
        for i in arr:
            sum+=i
            le+=1
        p=sum/float(le)
        return p