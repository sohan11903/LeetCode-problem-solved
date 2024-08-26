class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans=[]
        s=""
        for i in num:
            s+=str(i)
        s=str(int(s)+k)
        for i in s:
            ans.append(int(i))
        return ans