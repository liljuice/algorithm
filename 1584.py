from collections import deque

inf = int(1e6)
area = [[0] * 501 for _ in range(501)]
visited = [[False] * 501 for _ in range(501)]
dist = [[inf] * 501 for _ in range(501)]

# 0 : 안전, -1 : 죽음, 1 : 위험
n = int(input())
for _ in range(n):
  x1, y1, x2, y2 = map(int, input().split())
  xl = min(x1, x2)
  xr = max(x1, x2)
  yl = min(y1, y2)
  yr = max(y1, y2)
  for i in range(xl, xr + 1):
    for j in range(yl, yr + 1):
      area[i][j] = 1
m = int(input())
for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  xl = min(x1, x2)
  xr = max(x1, x2)
  yl = min(y1, y2)
  yr = max(y1, y2)
  for i in range(xl, xr + 1):
    for j in range(yl, yr + 1):
      area[i][j] = -1


def bfs():
  queue = deque()
  queue.append((0, 0))
  visited[0][0] = True
  dist[0][0] = 0
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      ix = x + dx[i]
      iy = y + dy[i]
      if ix < 0 or ix > 500 or iy < 0 or iy > 500:
        continue
      if area[ix][iy] != -1 and not visited[ix][iy]:
        if area[ix][iy] == 0:
          queue.appendleft((ix, iy))
          visited[ix][iy] = True
          dist[ix][iy] = dist[x][y]
        else:
          queue.append((ix, iy))
          visited[ix][iy] = True
          dist[ix][iy] = dist[x][y] + 1

  return


bfs()
ans = dist[500][500]
if ans == inf:
  print("-1")
else:
  print(ans)
