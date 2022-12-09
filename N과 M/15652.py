n, m = map(int, input().split())

s = []


def dfs(least):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(least, n + 1):
    s.append(i)
    dfs(i)
    s.pop()
  return


dfs(1)
