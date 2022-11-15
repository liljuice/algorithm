from collections import deque


def cycle(queue):
  temp = queue.popleft()
  queue.append(temp)
  return


n, k = map(int, input().split())
seat = deque([x for x in range(1, n + 1)])
joseph = []
while seat:
  for _ in range(k - 1):
    cycle(seat)
  joseph.append(seat.popleft())

print('<', end='')
if n > 1:
  for i in range(n - 1):
    print(joseph[i], end=', ')
print(joseph[n - 1], end='>')
