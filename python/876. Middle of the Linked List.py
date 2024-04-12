
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast,slow=head,head
        ans=[]
        while(fast!=None and fast.next!=None):
            slow, fast = slow.next, fast.next.next
        return slow
        