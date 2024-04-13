
class Solution {
    public ListNode reverseList(ListNode head) {
        if(head == null || head.next == null){
                return head;      
            }
        ListNode prev = head;
        ListNode curr = head.next;
        while (curr != null) {
           
            ListNode next = curr.next;
            curr.next = prev;
            //update
            prev = curr;
            curr = next;  
        }
        head.next = null;
        head = prev;
        return head;
    }  
}
