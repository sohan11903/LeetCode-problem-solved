class Solution {
    public int[] createTargetArray(int[] nums, int[] index) {
        ArrayList<Integer> arr1 = new ArrayList<Integer>();
        for(int i=0;i<nums.length;i++){
            arr1.add(index[i],nums[i]);
        }
        int [] ans = new int[nums.length];
        for(int i=0;i<nums.length;i++){
            ans[i] = arr1.get(i);
        }
        return ans;
    }
}