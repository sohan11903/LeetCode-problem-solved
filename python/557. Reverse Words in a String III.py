class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=s.split(" ")
        x=[]
        for i in a:
            x.append(i[::-1])
        return " ".join(x)