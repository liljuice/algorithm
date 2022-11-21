n = int(input())
deck = list(map(int, input().split()))
m = int(input())
cmp = list(map(int, input().split()))
result = []
deck.sort()


def binSearch(target):
  start = 0
  end = n - 1
  while start <= end:
    mid = (start + end) // 2

    if target > deck[mid]:
      start = mid + 1
    elif target < deck[mid]:
      end = mid - 1
    elif target == deck[mid]:
      return 1

  return 0


for card in cmp:
  result.append(binSearch(card))

for i in range(m):
  print(result[i], end=' ')
