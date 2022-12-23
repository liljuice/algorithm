inf = int(1e9)
n = int(input())
m = int(input())

route = [[inf] * (n + 1) for _ in range(n + 1)]
#route[i][j] -> 도시 i에서 j로 가는 노선의 비용(입력값)
cost = [[inf] * (n + 1) for _ in range(n + 1)]
#cost[i][j] -> 도시 i에서 j로 가는 최소비용(결과값)

for _ in range(m):
  a, b, c = map(int, input().split())
  if route[a][b] > c:
    route[a][b] = c
    cost[a][b] = c


def floydWarshall():
  for k in range(1, n + 1):  # 거쳐가는 지점!
    for i in range(1, n + 1):
      for j in range(1, n + 1):
        if cost[i][j] > cost[i][k] + cost[k][j]:
          cost[i][j] = cost[i][k] + cost[k][j]


floydWarshall()

for i in range(1, n + 1):
  for j in range(1, n + 1):
    if i == j or cost[i][j] == inf:
      print(0, end=' ')
    else:
      print(cost[i][j], end=' ')
  print()
