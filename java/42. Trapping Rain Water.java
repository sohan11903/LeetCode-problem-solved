class Solution {
    public int trap(int[] height) {
        int max=0;
        int coun=0;
        int i=0;
        int j=height.length-1;
        int leftMax=height[i];
        int rightMax=height[j];
        while(i<j){
            if(leftMax<=rightMax){
                coun=coun+(leftMax - height[i]);
                i++;
                leftMax=Math.max(leftMax,height[i]);
            }else{
                coun=coun+(rightMax - height[j]);
                j--;
                rightMax=Math.max(rightMax,height[j]);
            }
        }
        return coun;
    }
}