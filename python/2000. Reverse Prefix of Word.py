class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        n = word.find(ch)
        if(n==-1):
            return word
        ans = word[n::-1]+word[n+1:]
        return ans