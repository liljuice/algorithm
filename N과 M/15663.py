n, m = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
s = []
printing = []
visited = [False] * n #방문한 인덱스

def dfs():
  if len(s) == m:
    temp = ' '.join(map(str, s))
    if temp not in printing:
      printing.append(temp)
    return

  for i in range(0, n):
    if visited[i] == True:
      continue
    s.append(num[i])
    visited[i] = True
    dfs(i)
    s.pop()
    visited[i] = False
  return


dfs()
for i in range(len(printing)):
  print(printing[i])
