n = int(input())
dp = [[0, []] for i in range(n+1)]
dp[1][1] += [1]

for i in range(2, n+1):
  dp[i][0] = dp[i-1][0] + 1 #최악의 경우.
  dp[i][1] = dp[i-1][1] + [i]
  if i % 3 == 0:
    if dp[i][0] > dp[i//3][0]+1:
       dp[i][0] = dp[i//3][0]+1
       dp[i][1] = dp[i//3][1] + [i]
  if i % 2 == 0:
    if dp[i][0] > dp[i//2][0]+1:
       dp[i][0] = dp[i//2][0]+1
       dp[i][1] = dp[i//2][1] + [i]

# while n > 0: 메모리초과
#   if n % 3 == 0:
#     if dp[n//3][0] > dp[n][0]+1:
#       dp[n//3][0] = dp[n][0] + 1
#       dp[n//3][1] = dp[n][1] + [n//3]
#   if n % 2 == 0:
#     if dp[n//2][0] > dp[n][0] + 1:
#       dp[n//2][0] = dp[n][0] + 1
#       dp[n//2][1] = dp[n][1] + [n//2]
#   if dp[n-1][0] > dp[n][0] + 1:
#       dp[n-1][0] = dp[n][0] + 1
#       dp[n-1][1] = dp[n][1] + [n-1]   
#   n -= 1

print(dp[n][0])
dp[n][1].reverse()
for i in dp[n][1]:
  print(i, end=' ')
