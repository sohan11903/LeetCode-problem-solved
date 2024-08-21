class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        d=[]
        for i in range(len(heights)):
            ind=heights.index(max(heights))
            heights[ind]=-1
            d.append(names[ind])
        return d