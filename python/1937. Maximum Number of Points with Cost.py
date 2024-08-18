points = [[1,1,3],[1,5,1],[3,1,1]]
m = len(points)
n = len(points[0])
dp = [[0 for _ in range(n)] for _ in range(m)]
for i in range(n):
    dp[0][i] = points[0][i]
        
for i in range(1, m):
    dp[i][0] = dp[i-1][0]
    dp[i][-1] = dp[i-1][-1]
            
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]-1)
                
    for j in range(n-2, -1, -1):
        dp[i][j] = max(dp[i-1][j], dp[i][j+1]-1, dp[i][j])
            
    for j in range(0, n):
        dp[i][j] += points[i][j]
# print(max(dp[-1]))
print(dp)