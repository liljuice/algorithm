n = input()
m = int(input())
err = []
if m:
  err = list(input().split())
if n == 100:
  print("0")
  exit(0)

answer = abs(int(n)-100)
for i in range(0, 1000000):
  target = str(i)
  for t in target:
    if t in err:
      break
  else:
    answer = min(answer, len(target)+abs(i-int(n)))
print(answer)
