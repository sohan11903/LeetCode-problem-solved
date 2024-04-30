class Solution {
    public List<List<Integer>> generate(int numRows) {
        int[][] a = new int[100][100];
        List<List<Integer>> list = new ArrayList<>();
        for(int i=0;i<=numRows-1;i++){
            for(int j=0;j<=i;j++){
                if((j==0) || (i==j)){
                    a[i][j]=1;
                }
                else{
                    a[i][j]=a[i-1][j-1]+a[i-1][j];
                }
            }
        }
        for(int i=0;i<=numRows-1;i++){
            List<Integer> list1 = new ArrayList<Integer>();
            for(int j=0;j<=i;j++){
                list1.add(a[i][j]);
            }
            list.add(list1);
        }
        return list;
    }
}