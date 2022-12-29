from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
area = []

for i in range(n):
  area.append(list(map(int, input().split())))
  for j in range(n):
    if area[i][j] == 9:
      baby = [i, j]
      area[i][j] = 0
s = 2
eaten = 0
# 아기상어 크기보다 작은 칸을 먹을 수 있고,
# 아기상어 크기보다 큰 칸을 지나갈 수 없다.

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def bfs(x, y, size):  # x,y: 아기상어 좌표 size : 아기상어 크기
  queue = deque()
  queue.append((x, y))
  visited = [[False] * n for _ in range(n)]
  dist = [[0] * n for _ in range(n)]
  temp = []
  while queue:
    nx, ny = queue.popleft()
    for i in range(4):
      ix = nx + dx[i]
      iy = ny + dy[i]
      if ix < 0 or ix >= n or iy < 0 or iy >= n:
        continue
      if not visited[ix][iy] and area[ix][iy] <= size:
        queue.append((ix, iy))
        visited[ix][iy] = True
        dist[ix][iy] = dist[nx][ny] + 1
        if 0 < area[ix][iy] < size:
          temp.append((dist[ix][iy],ix,iy))
  temp.sort(key=lambda x : (x[0],x[1],x[2]))
  if not temp:
    return False
  return temp[0]

ans = 0
while True:
  next = bfs(baby[0], baby[1], s)
  if not next:
    break
  ans += next[0]
  eaten += 1
  if eaten == s:
    s += 1
    eaten = 0

  area[next[1]][next[2]] = 0
  baby[0] = next[1]
  baby[1] = next[2]

print(ans)
