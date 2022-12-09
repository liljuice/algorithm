from collections import deque

n, m = map(int, input().split())
maze = []
for _ in range(n):
  maze.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs():
  queue = deque()
  queue.append((0, 0))

  while queue:
    x, y = queue.popleft()
    step = maze[x][y]
    for i in range(4):
      ix = x + dx[i]
      iy = y + dy[i]
      if ix >= 0 and ix < n and iy >= 0 and iy < m:
        if maze[ix][iy] == 1:
          queue.append((ix, iy))
          maze[ix][iy] = step + 1
  return


dfs()
print(maze[n - 1][m - 1])
