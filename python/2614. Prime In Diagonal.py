class Solution:
    def diagonalPrime(self, nums):
        x=[]
        
        for i in range(len(nums)):
            x.append(nums[i][i])
            x.append(nums[i][len(nums)-1-i])
        answer=0
        for i in range(len(x)):
                for j in range(2,int(sqrt(x[i]))+1):
                    if x[i]%j==0:
                        break
                else:
                    if x[i]>answer:
                        answer=x[i]
        if answer==1:
            return 0
        return answer