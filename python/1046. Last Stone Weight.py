class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones)>1:
            x=max(stones)
            stones.remove(x)
            y=max(stones)
            stones.remove(y)
            if x!=y:
                stones.append(x-y)
        return stones[0] if stones else 0
            