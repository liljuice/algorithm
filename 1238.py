import heapq as hq

n, m, x = map(int, input().split())
inf = int(1e9)
route = [[] for _ in range(n + 1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  route[a].append((b, c))


def dijkstra(start, end):
  dist = [inf] * (n + 1)
  queue = []
  hq.heappush(queue, (0, start))
  dist[start] = 0

  while queue:
    distance, node = hq.heappop(queue)
    if distance > dist[node]:
      continue
    for next in route[node]:
      cost = dist[node] + next[1]
      if cost < dist[next[0]]:
        dist[next[0]] = cost
        hq.heappush(queue, (cost, next[0]))

  return dist[end]


result = [0] * (n + 1)

for i in range(1, n + 1):
  result[i] += dijkstra(i, x)
  result[i] += dijkstra(x, i)

print(max(result))
