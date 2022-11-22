s = input().split('-')
for i in range(len(s)):
  s[i] = list(map(int, s[i].split('+')))
  s[i] = sum(s[i])

res = s[0]
for i in range(1, len(s)):
  res -= s[i]

print(res)
