while True:
  string = input()
  stack = []
  flag = 0
  # LIFO -> 스택!
  if string == '.':
    break
    
  for word in string:
    if word == '.':
      break

    elif word == '(':
      stack.append(1)

    elif word == ')':
      if not stack or stack[-1] == 2:
        flag = 1
        break
      if stack[-1] == 1:
        stack.pop()
      else:
        flag = 1

    elif word == '[':
      stack.append(2)

    elif word == ']':
      if not stack or stack[-1] == 1:
        flag = 1
        break
      if stack[-1] == 2:
        stack.pop()
      else:
        flag = 1

  if not stack and flag == 0:
    print("yes")
  else:
    print("no")

