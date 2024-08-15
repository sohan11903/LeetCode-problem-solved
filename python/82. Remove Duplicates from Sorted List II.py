# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            p1=p.next
            p2=p.next.next
            if p1.val == p2.val:
                temp=p2
                while (temp and p1.val == temp.val):
                    temp=temp.next
                p.next=temp
            else:
                p=p.next
        return dummy.next