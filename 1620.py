n, m = map(int, input().split())
dogam = {}
rdogam = {}
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range(n):
  dogam[i + 1] = input().rstrip()
  rdogam[dogam[i + 1]] = i + 1

for j in range(m):
  quiz = input().rstrip()
  if quiz[0] in nums:
    quiz = int(quiz)
    print(dogam[quiz])
  else:
    print(rdogam[quiz])
