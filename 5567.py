from collections import deque

n = int(input())
m = int(input())
friend = [[] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
  a, b = map(int, input().split())
  friend[a].append(b)
  friend[b].append(a)


def bfs():
  queue = deque()
  queue.append((1, 0))
  visited[1] = True
  count = 0
  while queue:
    person, dist = queue.popleft()
    if dist <= 2:
      count += 1
    for f in friend[person]:
      if not visited[f]:
        visited[f] = True
        queue.append((f, dist + 1))
  return count - 1


print(bfs())
