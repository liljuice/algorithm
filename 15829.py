L = int(input())
S = input()
alpha = {}
result = 0

for i in range(L):
  result += (ord(S[i]) - 96) * (31**i) # * 1234567891 -> 마지막 연산에서 1234567890 + 1이 되면 오답이 나옴.

print(result % 1234567891)
