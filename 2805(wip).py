import bisect

n, m = list(map(int, input().split()))
trees = list(map(int, input().split()))

trees = sorted(trees, reverse=True)  #내림차순 정렬

#46 42 40 26 4
#0 4 8 50
#trees[] 요소를 골라서 그 기준으로 값 비교

#trees[2] = 40
#treesCut = 8
#m과 treesCut 비교

trees.append(0)  #trees.top보다 작은 값의 H

li = [0]
asc = 0
temp = 0
for i in range(trees[0], 0, -1):
  for tree in trees:
    if i == tree:
      asc = asc + 1
  #if i in trees:
  #  asc = asc + 1
  temp += asc
  li.append(temp)

res = bisect.bisect_left(li, m)
res = trees[0] - res

print(res)
#

#min = trees[bisect.bisect(li, n)]
#max = trees[bisect.bisect(li, n) + 1]
