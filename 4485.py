import sys
import heapq as hq

input = sys.stdin.readline
inf = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dijkstra(graph, n):
  dist = [[inf] * n for _ in range(n)]
  visited = [[False] * n for _ in range(n)]
  dist[0][0] = graph[0][0]
  visited[0][0] = True
  queue = []
  hq.heappush(queue, (dist[0][0], (0, 0)))
  while queue:
    d, node = hq.heappop(queue)
    for i in range(4):
      nx = node[0] + dx[i]
      ny = node[1] + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
        continue
      if d > dist[node[0]][node[1]]:
        continue
      cost = dist[node[0]][node[1]] + graph[nx][ny]
      if cost < dist[nx][ny]:
        dist[nx][ny] = cost
        visited[nx][ny] = True
        hq.heappush(queue, (dist[nx][ny], (nx, ny)))
  return dist[n-1][n-1]

tc=0
while True:
  tc+=1
  n = int(input())
  if n == 0:
    break
  cave = [list(map(int, input().split())) for _ in range(n)]
  ans = dijkstra(cave, n)
  print("Problem {0}: {1}".format(tc, ans))
