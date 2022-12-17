n = int(input())
elsie = []
for _ in range(n):
  elsie.append(int(input()))
bessie = [i for i in range(1, 2 * n + 1) if i not in elsie]
#bessie = fullDeck - elsie 차집합, 오름차순 정렬
elsie.sort()

count = 0
indexB = 0
indexE = 0

while indexE < n and indexB < n:
  if bessie[indexB] > elsie[indexE]:
    indexB += 1
    indexE += 1
    count += 1
  else:
    indexB += 1

print(count)
