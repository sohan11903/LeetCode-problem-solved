class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        if word == word.upper():
            return 0
        l=sorted(set(word))
        i=0
        c=0
        while l[i] != l[i].lower():
            if l[i].lower() in l:
                c+=1
            i+=1
        return c
        