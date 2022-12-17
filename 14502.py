from itertools import combinations
from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
lab = []
clean = []
virus = []
for i in range(n):
  lab.append(list(map(int, input().split())))
  for j in range(m):
    if lab[i][j] == 0:
      clean.append((i, j))
    if lab[i][j] == 2:
      virus.append((i, j))

cases = list(combinations(clean, 3))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(lab, x, y):
  queue = deque()
  queue.append((x, y))
  #visited = []
  while queue:
    ix, iy = queue.popleft()
    for i in range(4):
      nx = ix + dx[i]
      ny = iy + dy[i]
      if nx >= 0 and nx < n and ny >= 0 and ny < m:
        if lab[nx][ny] != 1 and lab[nx][ny] != 3:  #and (nx, ny) not in visited:
          lab[nx][ny] = 3
          queue.append((nx, ny))
          #visited.append((nx, ny))
  return


result = []
for walls in cases:
  tempLab = deepcopy(lab)
  count = 0
  for w in walls:
    tempLab[w[0]][w[1]] = 1

  for v in virus:
    bfs(tempLab, v[0], v[1])

  for i in tempLab:
    for j in i:
      if j == 0:
        count += 1

  result.append(count)

print(max(result))
