n, m = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
s = []
printing = []


def dfs(least):
  if len(s) == m:
    temp = ' '.join(map(str, s))
    if temp not in printing:
      printing.append(temp)
    return

  for i in range(least, n):
    s.append(num[i])
    dfs(i)
    s.pop()
  return


dfs(0)
for i in range(len(printing)):
  print(printing[i])
