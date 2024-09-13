class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        y=bin(int(date[:4]))[2:]
        m=bin(int(date[5:7]))[2:]
        d=bin(int(date[8:10]))[2:]
        return y+"-"+m+"-"+d