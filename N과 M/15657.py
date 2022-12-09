n, m = map(int, input().split())
num = list(map(int, input().split()))

num.sort()
s = []


def dfs(least):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(least, n):
    s.append(num[i])
    dfs(i)
    s.pop()
  return


dfs(0)
