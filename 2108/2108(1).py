import math
from collection import Counter

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
  count = Counter(numbers).most_common()

  if len(count) > 1:
    if count[0][1] == count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
  else:
      print(count[0][0])


def domain():
  ret = numbers[-1] - numbers[0]
  print(ret)


mean()
median()
mode()
domain()
