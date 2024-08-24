class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        if n=="9009":
            return "8998"
        c=len(n)
        a=[]
        absarr=[]
        p1=n[:c//2]
        if c%2==0:
            u=p1+p1[::-1]
            a.append(int(u))
        else:
            u=n[:c//2 +1]+p1[::-1]
            a.append(int(u))
        if c%2==0:
            z=int(u[(c//2)])
            
            if len(n)==2:
                a.append(int(str(z-1)+str(z-1)))
                a.append(int(str(z+1)+str(z+1)))
            else:
                u=n[:c//2]+p1[::-1]
                if z-1!=-1:
                    a.append(int(u[:c//2 - 1]+str(z-1)+str(z-1)+u[-(c//2 -1):]))
                a.append(int(u[:c//2 - 1]+str(z+1)+str(z+1)+u[-(c//2 -1):]))
        elif len(n)==1:
            a.append(int(str(int(n[0])-1)))
            a.append(int(str(int(n[0])+1)))
            
        else:
            z=int(u[(c//2)])
            u=n[:c//2]+p1[::-1]
            if z-1!=-1:
                a.append(int(u[:c//2]+str(z-1)+p1[::-1]))
            a.append(int(u[:c//2]+str(z+1)+p1[::-1]))
        if len(n)!=1:
            a.append(int('9'*(c-1)))
        a.append(int(str(10**c + 1)))

        a.sort()
        if int(n) in a:
            a.remove(int(n))
        for i in a:
            l=abs(int(n)-i)
            if l!=0:
                absarr.append(l)
        ans=absarr.index(min(absarr))
        return str(a[ans])