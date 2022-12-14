import heapq as hq
import sys

input = sys.stdin.readline

n = int(input())
neg = []
pos = []
for _ in range(n):
  com = int(input())
  if com < 0:
    hq.heappush(neg, -com)
  elif com > 0:
    hq.heappush(pos, com)
  else:  #com == 0
    if not neg and not pos:
      print("0")
    elif not neg:
      print(hq.heappop(pos))
    elif not pos:
      print(-1 * hq.heappop(neg))
    else:
      if neg[0] <= pos[0]:
        print(-1 * hq.heappop(neg))
      else:
        print(hq.heappop(pos))

"""
tuple을 push하는 방법도 있다.
hq.heappush(queue, (abs(com), com)) # 절댓값 기준으로 정렬하고
print(hq.heappop(queue)[1]) # 원래값을 출력한다.
"""
