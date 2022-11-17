n, r, c = map(int, input().split())

# n = 5까지 보자면
# 0,1 -> 1 / 1,0 -> 2 / 1,1 -> 3 2의 0승 n = 1
# 0,2 -> 4 / 2,0 -> 8 / 2,2 -> 12 2의 2승 n = 2
# 0,4 -> 16 / 4,0 -> 32 / 4,4 -> 48 2의 4승 n = 3
# 0,8 -> 64 / 8,0 -> 128 / 8,8 -> 192 2의 6승 n = 4 좌푯값 2의3승
# 0,16 -> 256 2**8
# 0,32 -> 1024 2**10
# ... n = 15일떄 0,16384 -> 2**24까지 필요 (좌푯값 2의14승)

# 예를 들어 5, 6을 찾는다면, 4,4 + 1,2 = 4,4 + 0,2 + 1,0
# =54 = 48+4+2
# 예를 들어 7, 3을 찾는다면, 4,0 + 3,3 = 4,0 + 2,2 + 1,1
# =32+12+3 = 47

# r과 c를 2의 제곱수 단위로 쪼개서 각 값을 더한다. (2**(14~0))
# 7, 3 -> 4의 나머지 -> 3, 3 -> 2의 나머지 -> 1, 1
# 26, 18 -> 16의 나머지 -> 10, 2 -> 8의 나머지 -> 2,2 -> 2의 나머지 -> 0, 0

numeric = [[0] * 2 for _ in range(16)]  # 방문차례값
squares = [2**x for x in reversed(range(0, 15))]  # 좌표값

numeric[0] = [1, 2]
for i in range(1, 16):
  numeric[i][0] = numeric[i - 1][0] * 4
  numeric[i][1] = numeric[i][0] * 2
#numeric = [1,2 / 4,8 / 16,32 / 64,128 ..]
rowSquare = []
colSquare = []

for i in range(0, 15):
  if r % squares[i] != r:  #행/열값이 설정된 좌표값보다 큼
    r = r % squares[i]  #나머지만 두고..
    rowSquare.append(14 - i)  #좌표값 저장

  if c % squares[i] != c:
    c = c % squares[i]
    colSquare.append(14 - i)

sum = 0
for rS in rowSquare:
  sum += numeric[rS][1]
for cS in colSquare:
  sum += numeric[cS][0]

print(sum)
