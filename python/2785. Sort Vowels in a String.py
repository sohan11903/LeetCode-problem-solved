class Solution(object):
    def sortVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        x=[]
        f=['A','E','I','O','U','a','e','i','o','u']
        k={'A':0,'E':0,'I':0,'O':0,'U':0,'a':0,'e':0,'i':0,'o':0,'u':0}
        z=list(s)
        for i in s:
            if i in f:
                k[i]+=1
        ans=''
        l=0
        for i in s:
            if i in k:
                while k[f[l]]==0:
                    l+=1
                ans+=f[l]
                k[f[l]]-=1
            else:
                ans+=i
        return ans
                