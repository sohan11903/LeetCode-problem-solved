title = "Ewn R H HOg O Omi oGl"
class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        arr=title.split(" ")
        ans=[]
        for i in arr:
            if len(i)<=2:
                ans.append(i.lower())
                
            else:
                ans.append(i.capitalize())
        return ' '.join(ans)
       
