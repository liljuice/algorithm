n = int(input())
graph = {}
for _ in range(n):
  root, left, right = input().split()
  graph[root] = [left, right]


def preOrder(result, root):
  if root != '.':
    result.append(root)
    preOrder(result, graph[root][0])
    preOrder(result, graph[root][1])


def inOrder(result, root):
  if root != '.':
    inOrder(result, graph[root][0])
    result.append(root)
    inOrder(result, graph[root][1])


def postOrder(result, root):
  if root != '.':
    postOrder(result, graph[root][0])
    postOrder(result, graph[root][1])
    result.append(root)


result = []
preOrder(result, 'A')
for i in result:
  print(i, end='')
print()
result = []
inOrder(result, 'A')
for i in result:
  print(i, end='')
print()
result = []
postOrder(result, 'A')
for i in result:
  print(i, end='')
print()
