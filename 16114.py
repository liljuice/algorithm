X, N = map(int, input().split())

if N == 1:
  if X < 0:
    print("INFINITE")
  else:
    print(0)
elif N % 2 == 1:
  print("ERROR")

else:
  if X <= 0:
    print(0)
  elif N == 0:
    print("INFINITE")
  else:
    desc = N / 2
    count = 0
    while X > 0:
      X = X - desc
      count += 1
    print(count - 1)
