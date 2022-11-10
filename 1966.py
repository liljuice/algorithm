t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  queue = list(map(int, input().split()))
  index = list(range(0, n))  # index : 문서 번호, queue : 문서의 중요도
  printOrder = 0

  while queue:  # 시행 최대 횟수는 n 이상임..
    # 맨 앞 문서의 중요도 비교 후 재배치
    if queue[0] == max(queue):  # 맨 앞 문서의 중요도가 가장 높은 경우
      queue.pop(0)
      printOrder += 1
      if index.pop(0) == m:
        print(printOrder)
        break

    else:
      queue.append(queue.pop(0))
      index.append(index.pop(0))
