class Solution {
    public int differenceOfSum(int[] nums) {
        int sum1=0;
        int sum2=0;
        int s=0;
        for(int i=0;i<nums.length;i++){
            sum1=sum1+nums[i];
        }
        for(int i=0;i<nums.length;i++){
            if (nums[i]>9){
                int a=nums[i];
                while(a>0){
                    s = a%10;
                    sum2 = sum2 + s;
                    a=a/10;
                }
            }
            else{
                sum2 = sum2+nums[i];
            }
            
        }

        int ans = sum1-sum2;
        return ans;
    }
}