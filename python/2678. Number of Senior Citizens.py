class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """
        c=0
        for i in details:
            age=i[11:13]
            if int(age)>60:
                c+=1
        return c