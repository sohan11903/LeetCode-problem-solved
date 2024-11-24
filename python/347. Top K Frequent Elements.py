class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter, OrderedDict
        d=Counter(nums)
        z=OrderedDict(sorted(d.items(), key=lambda item:item[1],reverse=True))
        v=0
        ans=[]
        for i in z:
            ans.append(i)
            v+=1
            if v==k:
                return ans
        