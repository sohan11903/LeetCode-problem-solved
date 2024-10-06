class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        ans=''
        first=strs[0]
        last=strs[-1]
        for i in range(min(len(first),len(last))):
            if first[i]==last[i]:
                ans+=first[i]
            else:
                return ans
        return ans