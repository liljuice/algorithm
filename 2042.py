n, m, k = map(int, input().split())
tree = [0] * (2 * n)

for i in range(n, 2 * n):
  tree[i] = int(input())

for i in range(n - 1, 0, -1):
  tree[i] = tree[i * 2] + tree[i * 2 + 1]

def query(left, right):
  result = 0
  left = left+n
  right = right+n

  while left < right:
    if left % 2 == 1: #부모노드가 구간에 포함되지 않는 경우
      result += tree[left]
      left += 1
    if right % 2 == 1:
      result += tree[right - 1]
      right -= 1
    left //= 2
    right //= 2
    
  return result    


def update(index, num):
  index = index + n
  tree[index] = num

  while index>1:
    tree[index >> 1] = tree[index] + tree[index ^ 1]
    #i>>1 : 2로 나눔(1버림), i^1 : 1과의 XOR 연산 -> 2의 배수면 +1 아니면 -1
    index >>= 1

for _ in range(m+k):
  a, b, c = map(int, input().split())

  if a == 1:
    update(b-1, c)
  else:
    print(query(b-1, c))
