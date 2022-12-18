from collections import deque

n = int(input())

node = [[] for _ in range(n + 1)]
whichnodeistheparent = [0] * (n + 1)
visited = [False] * (n + 1)
for _ in range(n - 1):
  a, b = map(int, input().split())
  node[a].append(b)
  node[b].append(a)


#[6] [4] [6, 5] [1, 2, 7] [3] [1, 3] [4]
def bfs():
  queue = deque()
  queue.append(1)
  visited[1] = True
  while queue:
    parent = queue.popleft()

    if node[parent]:
      for n in node[parent]:
        if not visited[n]:
          queue.append(n)
          whichnodeistheparent[n] = parent
          visited[n] = True


bfs()
for result in whichnodeistheparent:
  if result != 0:
    print(result)
