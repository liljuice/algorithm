#1339.py

# 예제
# AGCDE BFADE EBA
# 우선순위 배정법
# 자릿수 단위로 간다. 00000000 -> A:10000 B:10000
# 모든 자리를 더한다면, A 10101 B 10010 -> A가 더 큼.

n = int(input())
altoNum = {}
alpha = []
sum = 0
for _ in range(n):
  alpha.append(input())
#alpha.sort(key=len, reverse=True)

for a in alpha:
  for i in range(len(a)):
    dig = len(a) - i - 1  # 자릿수
    if a[i] not in altoNum:
      altoNum[a[i]] = 10**dig
    else:
      altoNum[a[i]] += 10**dig

prior = dict(sorted(altoNum.items(), key=lambda x: x[1], reverse=True))
prior = list(prior.keys())

for i in range(len(prior)):
  altoNum[prior[i]] = 9 - i

for a in alpha:
  for i in range(len(a)):
    dig = len(a) - i - 1
    sum += altoNum[a[i]] * 10**dig

print(sum)
