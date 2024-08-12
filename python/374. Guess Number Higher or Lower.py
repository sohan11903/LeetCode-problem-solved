# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lef = 1
        rig = n
        while lef <= rig:
            mid = (lef + rig)//2
            res = guess(mid)
            if res == -1:
                rig = mid - 1
            elif res == 1:
                lef = mid + 1
            else :
                return mid    
     