n = int(input()) #1<=n<=10000 출력값 최대 101*103

nums = [True] * (104)
primes = []
specials = []
for i in range(2,104):
  if nums[i]:
    primes.append(i)
    for j in range(2*i, 104, i):
      nums[j] = False

for i in range(len(primes)-1):
  specials.append(primes[i]*primes[i+1])

for s in specials:
  if s>n:
    print(s)
    break

