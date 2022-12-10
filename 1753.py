import sys
import heapq as hq

input = sys.stdin.readline
inf = int(1e9)
v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]  #tree[n] n번 노드
dist = [inf] * (v + 1)  #dist[n] n번 노드까지의 최단 거리
dist[k] = 0
for _ in range(e):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))

def dijkstra():
  queue = []
  hq.heappush(queue, (0, k))

  while queue:
    distTemp, node = hq.heappop(queue) 
    if distTemp > dist[node]:
      continue
    for nextNode in graph[node]:
      cost = dist[node] + nextNode[1]
      if cost < dist[nextNode[0]]:
        dist[nextNode[0]] = cost
        hq.heappush(queue, (cost, nextNode[0])) # 중요 : cost를 기준으로 heapq를 구성해야함!! 최소 힙에서 cost가 낮은걸 먼저 pop해줘야 21~22 line으로 시간을 줄여준다.

dijkstra()

for i in range(1, v+1):
  if dist[i] == inf:
    print("INF")
  else:
    print(dist[i])
