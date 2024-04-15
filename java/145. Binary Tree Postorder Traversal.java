class Solution {
    public static void postOrder(TreeNode root, List<Integer> result){
        if(root == null){
            return;
        }
        postOrder(root.left,result);
        postOrder(root.right,result);
        result.add(root.val);
        
    }
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> result = new ArrayList<>();
        postOrder(root,result);
        return result;
    }
}