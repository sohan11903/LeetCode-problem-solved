class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        arr=[]
        ans=0
        while(num>0):
            arr.append(num%2)
            num=num//2
        for i in range(len(arr)):
            if arr[i]==0:
                arr[i]=1
                ans+=1*(2**i)
            else:
                arr[i]=0
        return ans