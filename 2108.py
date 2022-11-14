import math

n = int(input())  #odd-number

numbers = []

for i in range(n):
  numbers.append(int(input()))

numbers = sorted(numbers)


def mean():
  ret = math.fsum(numbers) / n
  print(round(ret))


def median():
  print(numbers[math.ceil(n / 2) - 1])


def mode():
  count = {}
  for num in numbers:
    if num not in count:
      count[num] = 1
    else:
      count[num] = count[num] + 1

  maxKey = [
    key for key, value in count.items() if max(count.values()) == value
  ]

  if len(maxKey) > 1:
    print(maxKey[1])
  else:
    print(maxKey[0])


def domain():
  ret = numbers[-1] - numbers[0]
  print(ret)


mean()
median()
mode()
domain()
