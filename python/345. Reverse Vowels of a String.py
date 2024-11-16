class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        f=['a','e','i','o','u','A','E','I','O','U']
        l=0
        r=len(s)-1
        d=list(s)
        while l < r:
            while l<r and s[l] not in f :
                l+=1
            while r>l and s[r] not in f :
                r-=1
            d[l],d[r]=d[r],d[l]
            l+=1
            r-=1
        return ''.join(d)

        
        # x=[]
        # for i in s:
        #     if i in f :
        #         x.append(i)
        # l = len(x)-1
        # s=list(s)
        # for i in range(len(s)):
        #     if s[i] in f:
        #         s[i]=x[l]
        #         l-=1
        # return ''.join(s)
        