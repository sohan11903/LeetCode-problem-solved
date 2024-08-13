import math
class Solution(object):
    def pickGifts(self, gifts, k):
        """
        :type gifts: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(k):
            ma = gifts.index(max(gifts))
            gifts[ma]=math.floor(math.sqrt(gifts[ma]))
        return int(sum(gifts))
        