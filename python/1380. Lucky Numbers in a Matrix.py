class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        c = []
        d = []
        min =[]
        max = []
        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                c.append(matrix[i][j])
            s = sorted(c)
            max.append(s[len(matrix) - 1])
            c = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                c.append(matrix[i][j])
            s =sorted(c)
            if s[0] in max:
                d.append(s[0])
                return d
                break
            else:
                c=[]