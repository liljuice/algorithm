import heapq as hq

n, k = map(int, input().split())
inf = int(1e9)
cost = [inf] * 100001
cost[n] = 0

def dijkstra():
  queue = []
  hq.heappush(queue, (0, n))

  while queue:
    dist, node = hq.heappop(queue)
    nextNode = [node - 1, node + 1, node * 2]
    #각 노드의 다음 노드 : node-1, node+1, node*2
    for i in range(3):
      if 0 <= nextNode[i] <= 100000:
        if i == 2 and cost[nextNode[i]] > dist:
          cost[nextNode[i]] = dist  #0초 소모
          hq.heappush(queue, (cost[nextNode[i]], nextNode[i]))
        elif 0 <= i <= 1 and cost[nextNode[i]] > dist:
          cost[nextNode[i]] = dist + 1  #1초 소모
          hq.heappush(queue, (cost[nextNode[i]], nextNode[i]))


dijkstra()
print(cost[k])
