class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        con=0
        first = text.split()
        for i in first:
            c=True
            for j in i:
                if j in brokenLetters:
                    c=False
                    break
            if c:
                con+=1
        return con

            

                
 
            