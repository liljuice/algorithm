v, e = map(int, input().split())
parent = [i for i in range(v + 1)]
edge = []
for _ in range(e):
  edge.append(list(map(int, input().split())))  #가중치, 정점1, 정점2
edge.sort(key=lambda x : x[2])  #가중치 기준으로 오름차순 정렬


def find(parent, x):  #x번 정점의 부모노드 찾기
  if parent[x] != x:  #부모노드(parent[x])와 자식노드(x)가 다른 경우 다른 부모노드가 존재.
    parent[x] = find(parent, parent[x])
    #부모노드 배열에 parent[x]의 부모노드를 찾아 갱신
  return parent[x]


def union(parent, x, y):
  x = find(parent, x)
  y = find(parent, y)
  if x > y:
    parent[x] = y
  else:
    parent[y] = x
  #작은 번호의 부모노드가 다른 노드의 부모로 관계 갱신


ans = 0
for ed in edge:
  if find(parent, ed[0]) != find(parent, ed[1]):
    #부모노드가 다르면 사이클이 없음->union시켜서 최소 스패닝 트리에 넣기.
    union(parent, ed[0], ed[1])
    ans += ed[2]

print(ans)
