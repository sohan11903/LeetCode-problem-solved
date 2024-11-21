class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i=0
        j=len(height)-1
        max_water=0
        while(i<j):
            water=min(height[i],height[j])*abs(i-j)
            max_water=max(max_water,water)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max_water