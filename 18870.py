n = int(input())
line = list(map(int, input().split()))
lineSorted = sorted(line)
linePrior = {}
result = []
comp = 0
for coor in lineSorted:
  if coor not in linePrior:
    linePrior[coor] = comp
    comp += 1

for coor in line:
  result.append(linePrior[coor])

for i in range(n):
  print(result[i], end=' ')
