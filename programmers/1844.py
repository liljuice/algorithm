from collections import deque

def solution(maps):
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  n = len(maps)
  m = len(maps[0])

  def bfs():
    queue = deque()
    queue.append((0, 0))

    while queue:
      x, y = queue.popleft()
      for i in range(4):
        ix = x + dx[i]
        iy = y + dy[i]
        if ix >= 0 and ix < n and iy >= 0 and iy < m:
          if maps[ix][iy] == 1:
            maps[ix][iy] = maps[x][y] + 1
            queue.append((ix, iy))

    return maps[n - 1][m - 1]

  answer = bfs()
  if answer == 1:
    answer = -1

  return answer
