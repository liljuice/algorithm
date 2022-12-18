from itertools import combinations

n, m = map(int, input().split())
city = []
chicken = []
home = []
for i in range(n):
  city.append(list(map(int, input().split())))
  for j in range(n):
    if city[i][j] == 2:
      chicken.append([i, j])
    elif city[i][j] == 1:
      home.append([i, j])

combi = list(combinations(chicken, len(chicken) - m))
result = []
for c in combi:
  after = [x for x in chicken if x not in c]
  chickenDist = 0
  for h in home:
    temp = 100000
    for a in after:
      dist = abs(h[0] - a[0]) + abs(h[1] - a[1])
      if temp > dist:
        temp = dist
    chickenDist += temp
  result.append(chickenDist)

print(min(result))
