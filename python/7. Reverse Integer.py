class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = ''
        sign = 1
        for i in str(x):
            if i=='-':
                sign = -1
            else:
                s += i
        s = sign * int(s[::-1])
        if s < -(2 ** 31) or s >(2**31 - 1):
            return 0
        return s