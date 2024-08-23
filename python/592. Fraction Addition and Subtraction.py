
class Solution(object):
    def fractionAddition(self, exp):
        """
        :type expression: str
        :rtype: str
        """
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        num = 0
        denum = 1
        i = 0
        while i < len(exp):
            currNum = 0
            currdenum = 0
            neg = exp[i] == "-"
            if exp[i] == '+' or exp[i]=="-":
                i=i+1
            while(i<len(exp) and exp[i]!="/"):
                n=int(exp[i])
                currNum = currNum*10 + n
                i=i+1
            i=i+1
            if neg == True:
                currNum = -1*currNum
                
            while(i<len(exp) and exp[i]!="+" and exp[i] != "-"):
                m=int(exp[i])
                currdenum = currdenum*10 + m
                i=i+1
                
            num= num*currdenum + currNum*denum
            denum=denum*currdenum 
        t=abs(gcd(num,denum))
        return str(num//t)+"/"+str(denum//t)