import sys

input = sys.stdin.readline

n = int(input())
paper = []
for _ in range(n):
  paper.append(list(map(int, input().split())))

answer = {-1: 0, 0: 0, 1: 0}


def solution(x, y, size):  #size : 종이 가로 길이
  if size == 1:
    answer[paper[x][y]] += 1
    return

  first = paper[x][y]
  for i in range(x, x + size):
    for j in range(y, y + size):
      if paper[i][j] != first:
        solution(x, y, size // 3)
        solution(x + size // 3, y, size // 3)
        solution(x + 2 * size // 3, y, size // 3)
        solution(x, y + size // 3, size // 3)
        solution(x, y + 2 * size // 3, size // 3)
        solution(x + size // 3, y + size // 3, size // 3)
        solution(x + size // 3, y + 2 * size // 3, size // 3)
        solution(x + 2 * size // 3, y + size // 3, size // 3)
        solution(x + 2 * size // 3, y + 2 * size // 3, size // 3)
        return
  answer[first] += 1
  return


solution(0, 0, n)
print(answer[-1])
print(answer[0])
print(answer[1])
