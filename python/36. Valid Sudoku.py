class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = len(board)
        col = len(board[0])
        for i in range (row):
            for j in range(col):
                num = board[i][j]
                if(board[i][j] != "."):
                        for x in range (len(board)):
                            if(x==j):
                                x=x+1
                            if (x == len(board)):
                                break
                            if board[i][x] == str(num) :
                                return False

                        for x in range (len(board)):
                            if(x==i):
                                x=x+1
                            if(x==len(board)):
                                break
                            if board[x][j] == str(num) :
                                return False

                        b = int(math.sqrt(len(board)))
                        sr = i - (i % b)
                        sc = j - (j % b)
                        for p in range(b):
                            for q in range(b):
                                if((q+sc)==j):
                                    q=q+1
                                if ((q + sc) ==(sc+b)):
                                    break
                                if board[p+sr][q+sc] == str(num):
                                    return False
        return True
        