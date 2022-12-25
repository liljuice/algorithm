import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
  n = int(input())
  closet = {}
  for i in range(n):
    a, b = input().split()
    if b not in closet:
      closet[b] = 1
    else:
      closet[b] += 1
  result = 1
  for i, j in closet.items():
    result *= (j + 1)
  print(result - 1)
