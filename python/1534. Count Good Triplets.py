class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        count = 0
        if set(arr) == 1:
            return 0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if(abs(arr[i] - arr[j])<= a ):
                    for k in range (j+1,len(arr)):
                        if(abs(arr[i] - arr[k]) <= c  and abs(arr[j] - arr[k]) <= b):
                            count+=1
        return count