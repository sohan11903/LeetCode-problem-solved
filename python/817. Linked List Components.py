# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def numComponents(self, head, nums):
        """
        :type head: ListNode
        :type nums: List[int]
        :rtype: int
        """
        s=''
        while head:
            if head.val in nums:
                s+=str(head.val)
            else: 
                s+=' '
            head=head.next
        f=s.split()
        return len(f)