class Solution(object):
    def categorizeBox(self, length, width, height, mass):
        """
        :type length: int
        :type width: int
        :type height: int
        :type mass: int
        :rtype: str
        """
        if (length >= 10**4 or width >=10**4 or height >= 10**4 or length * width * height >= 10**9) and mass >= 100:
            return 'Both'
        elif not (length >= 10**4 or width >=10**4 or height >= 10**4 or length * width * height >= 10**9) and not mass >= 100:
            return 'Neither' 
        elif mass >= 100: return 'Heavy'
        else: return 'Bulky'
    
        