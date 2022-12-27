k = int(input())
choco = 1
cut = [1]

while choco < k:
  choco *= 2
  cut.append(choco)

for i in range(len(cut)-1, -1, -1):
  k %= cut[i]

  if k == 0:
    print(choco, len(cut)-i - 1)
    break
