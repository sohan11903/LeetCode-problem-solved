class Solution {
    public List<Integer> getRow(int rowIndex) {
        int[][] a = new int[100][100];
        List<Integer> list = new ArrayList<Integer>();
        for(int i=0;i<=rowIndex;i++){
            for(int j=0;j<=i;j++){
                if((j==0) || (i==j)){
                    a[i][j]=1;
                }
                else{
                    a[i][j]=a[i-1][j-1]+a[i-1][j];
                }
            }
        }
        for(int i=0;i<=rowIndex;i++){
            list.add(a[rowIndex][i]);
        }
        return list;
    }
}