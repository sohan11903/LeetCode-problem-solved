class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d={}
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i] += 1
        x=sorted(d.items(),key= lambda k: (-k[1],k[0]),reverse=True)
        res=[]
        for i in range(len(x)):
            for j in range(x[i][1]):
                res.append(x[i][0])
        return res      