class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        val = num ** 0.5
        if val == int(val):
            return True
        return False