#PyPy3로 제출한 결과 메모리 초과가 나옴.

import sys
input = sys.stdin.readline
S = set()
m = int(input())
for _ in range(m):
  command = input().split()
  if len(command) == 2:
    command[1] = int(command[1]) #숫자로 바꾸지 않으면, all 커맨드에서 오류 발생
  if command[0] == "add":
    S.add(command[1])
  elif command[0] == "remove":
    S.discard(command[1])
  elif command[0] == "check":
    if command[1] in S:
      print(1)
    else:
      print(0)
  elif command[0] == "toggle":
    if command[1] in S:
      S.discard(command[1])
    else:
      S.add(command[1])
  elif command[0] == "all":
    S = set([i for i in range(1, 21)])
  elif command[0] == "empty":
    S = set()
