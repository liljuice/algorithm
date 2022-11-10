n, m = list(map(int, input().split()))
trees = list(map(int, input().split()))

start = 0
end = max(trees)

# Parametric Search
while start <= end:
  mid = (start + end) // 2
  wood = 0

  for tree in trees:
    if tree > mid:
      wood += tree - mid

  if wood < m:  # 가져갈 양보다 적게 얻은 경우 -> 절단기 높이를 낮추자
    end = mid - 1
  else:
    start = mid + 1

print(end)
