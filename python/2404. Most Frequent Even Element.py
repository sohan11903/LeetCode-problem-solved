from collections import Counter
class Solution(object):
    def mostFrequentEven(self, nums):
        e = []
        for i in nums:
            if i % 2 == 0:
                e.append(i)
        if not e:
            return -1
        e = sorted(e)
        ec = Counter(e)
        for i in e:
            if ec[i] == max(ec.values()):
                return i
        