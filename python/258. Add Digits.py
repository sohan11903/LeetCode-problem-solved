class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """      
        token=None
        sum = 0
        while (int(num) > 0):
            val = num % 10
            sum=sum+val
            num = int(num/10)

            if(num <= 0):
                token=True
            if(sum>9 and token==True):
                num=sum
                sum=0
        return sum
       
       
    