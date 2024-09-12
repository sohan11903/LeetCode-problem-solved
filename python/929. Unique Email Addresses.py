class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        ans=set()
        for i in emails:
            x,y=i.split('@')
            x=x.split('+')[0]
            x=x.replace('.','')
            ans.add(x+"@"+y)
        return len(ans)