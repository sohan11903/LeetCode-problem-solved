class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        d={5:0 ,10:0 }
        for i in bills:
            if i==5:
                d[5]+=1
            elif i==10:
                if d[5]:
                    d[5]-=1
                    d[10]+=1
                else:
                    return False
            else:
                if d[5] and d[10]:
                    d[5]-=1
                    d[10]-=1
                elif d[5]>=3:
                    d[5]-=3
                else:
                    return False
        else:
            return True