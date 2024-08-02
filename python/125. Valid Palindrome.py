class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c=''
        for i in s:
            if i.isalpha() or i.isdigit():
                c=c+i 
        n=c.lower()
        
        if n != n[::-1]:
            return False
        return True