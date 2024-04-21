class Solution {
    public static void countNode(TreeNode root){
        countNode(root);
    }
    public int countNodes(TreeNode root) {
        
        if(root == null){
            return 0;
        }
        int lN = countNodes(root.left);
        int rN = countNodes(root.right);
        return lN + rN + 1;
    }
}