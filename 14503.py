n, m = map(int, input().split())
r, c, d = map(int, input().split())
#0북 1동 2남 3서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
home = []
cleaned = [[False] * m for _ in range(n)]
for i in range(n):
  home.append(list(map(int, input().split())))

cleaned[r][c] = 1


def robotCleaner(r, c, d):
  #왼쪽 방향 == direction ++  // 북->서->남->동
  result = 0
  while True:
    succeed = False
    for i in range(4):
      if d == 0:
        next_d = 3
        d = 3
      else:
        next_d = d - 1
        d = d - 1
      next_r = r + dx[next_d]
      next_c = c + dy[next_d]

      #범위 밖이거나 벽 2-2.
      if next_r >= 0 or next_r < n or next_c >= 0 or next_c < m:
        #2-1.
        if cleaned[next_r][next_c] == False and home[next_r][next_c] == 0:
          r = next_r
          c = next_c
          cleaned[next_r][next_c] = True
          succeed = True
          result += 1
          break

    if not succeed:
      next_r = r - dx[d]
      next_c = c - dy[d]

      if home[next_r][next_c] == 1:
        break

      r = next_r
      c = next_c

  return result


print(robotCleaner(r, c, d) + 1) #처음 위치도 청소
