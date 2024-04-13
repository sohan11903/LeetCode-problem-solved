class Solution {
    public ListNode removeElements(ListNode head, int val) {
        if(head == null){
            return head;
        }
        while(head != null && head.val == val){
            head = head.next;
            if(head == null){
                return null;
            }
        }
        
        ListNode snode = head;
        while(snode.next!=null){
            if(snode.next.val == val){
                snode.next = snode.next.next;
            }
            else{
                snode = snode.next;
            }
            
        }
        return head; 
    }
}