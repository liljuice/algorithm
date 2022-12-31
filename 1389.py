n, m = map(int, input().split())
inf = int(1e6)
net = [[inf]*(n+1) for _ in range(n+1)]
dist = [[inf]*(n+1) for _ in range(n+1)]
for _ in range(m):
  a, b = map(int, input().split())
  net[a][b] = 1
  net[b][a] = 1

for k in range(1, (n+1)):
  for i in range(1, (n+1)):
    for j in range(1, (n+1)):
      if net[i][j] > net[i][k] + net[k][j]:
        net[i][j] = net[i][k] + net[k][j]
temp = inf
for i in range(1,(n+1)):
  if temp > sum(net[i])-inf:
    temp = sum(net[i])-inf
    ans = i

print(ans)
  
