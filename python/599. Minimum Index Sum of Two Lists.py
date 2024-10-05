class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d=list(set(list1) & set(list2))
        f=[]
        if len(d)==1:
            return d
        for i in d:
            f.append(list1.index(i)+list2.index(i))
        minv=min(f)
        ans=[]
        for i in range(len(f)):
            if f[i]==minv:
                ans.append(d[i])
        return ans