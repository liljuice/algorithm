n = int(input())  #수열의 길이

numbers = []  #입력된 수열
stack = []
stackPush = 0  #스택 리스트에 push할 값
isPossible = True  #수열을 만들 수 있는가?
calc = []  #연산 출력

for i in range(n):
  numbers.append(int(input()))

for num in numbers:
  while num:
    if len(stack) == 0:  #스택이 비어있을 때
      calc.append('+')
      stackPush += 1
      stack.append(stackPush)
      if stackPush > num:
        isPossible = False
        break

    if stack[-1] < num:  #stack[-1]은 리스트 stack의 마지막 요소 값
      if stackPush > num:
        isPossible = False
        break
      calc.append('+')
      stackPush += 1
      stack.append(stackPush)  #stack의 top값이 찾는 값보다 작다면 다음 값 push
    else:
      calc.append('-')
      if stack.pop() == num:  #stack에서 pop하는 동시에 찾는 값과 비교
        break

if isPossible:
  for cal in calc:
    print(cal)
else:
  print('NO')
