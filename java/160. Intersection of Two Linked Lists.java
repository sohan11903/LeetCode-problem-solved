public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ArrayList<ListNode> a1 = new ArrayList<>();
        ArrayList<ListNode> a2 = new ArrayList<>();
        while(headA!=null){
            a1.add(headA);
            headA = headA.next;
        }
        while(headB!=null){
            a2.add(headB);
            headB = headB.next;
        }
        int x=a1.size();
        int y=a2.size();
        for(int i=0;i<Math.min(x,y);i++){
            if(x>y){
                if(a1.contains(a2.get(i))){
                    return a2.get(i);
                }
            }
            else{
                if(a2.contains(a1.get(i))){
                    return a1.get(i);
                }
            }
        }
        return null;
    }
}