class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        if mat == target :
            return True
        for x in range (3):
            rm = []
            for i in range(0,len(mat)):
                d=[]
                for j in range(0,len(mat[0])):
                    d.append(mat[len(mat)-1-j][i])
                rm.append(d)
            mat = rm
            if mat == target :
                return True
        return False