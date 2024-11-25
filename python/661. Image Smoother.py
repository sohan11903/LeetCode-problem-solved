class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        row=len(img)
        col=len(img[0])
        ans=[[0 for _ in range(col)] for _ in range(row)]
        for i in range(row):
            for j in range(col):
                neigh = 1
                tot=img[i][j]
                if i>0 and j>0:
                    tot+=img[i-1][j-1]
                    neigh+=1
                if i>0 and j<col-1:
                    tot+=img[i-1][j+1]
                    neigh+=1
                if i<row-1 and j>0:
                    tot+=img[i+1][j-1]
                    neigh+=1
                if i<row-1 and j<col-1:
                    tot+=img[i+1][j+1]
                    neigh+=1
                if i>0:
                    tot+=img[i-1][j]
                    neigh+=1
                if i<row-1:
                    tot+=img[i+1][j]
                    neigh+=1
                if j>0:
                    tot+=img[i][j-1]
                    neigh+=1
                if j<col-1:
                    tot+=img[i][j+1]
                    neigh+=1
                ans[i][j]=tot//neigh
        return ans