class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        
        return True
    
# Very funnny solution and this is medium question no wayyy....

# Other Solution
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        
        i=0
        j=len(piles)-1
        alice=0
        bob=0
        while(i<j):
            if piles[i] > piles[j]:
                alice+=piles[i]
                bob+=piles[j]
            else:
                alice+=piles[j]
                bob+=piles[i]
            i+=1
            j-=1
        return True if alice>bob else False
        