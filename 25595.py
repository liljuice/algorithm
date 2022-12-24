n = int(input())
bp = []
region = []
for i in range(n):
  s = input().split()
  for j in range(n):
    if s[j] == '1':
      region.append(5*i+j)
    if s[j] == '2':
      shin = 5*i+j

if shin % 2 == 0: #shin의 위치가 짝수면 region의 위치가 홀수에 있어야 처치
  for r in region:
    if r % 2 == 0:
      print("Kiriya")
      exit(0)
else:
  for r in region:
    if r % 2 == 1:
      print("Kiriya")
      exit(0)
print("Lena")
