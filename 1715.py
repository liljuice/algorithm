"""
"묶을 때마다" 작은 묶음 두 개부터 묶는다
10 20 30 40 50 60
102030405060
3030405060
60405060
609060
12090
30+ 30+30 + 40+50 + 60+60 + 120+90 = 510
최소힙!
"""
import heapq as hq

n = int(input())
deck = []
answer = 0
for _ in range(n):
  hq.heappush(deck, int(input()))

while len(deck) > 1:
  temp1 = hq.heappop(deck)
  temp2 = hq.heappop(deck)
  answer += (temp1 + temp2)
  hq.heappush(deck, temp1+temp2)
print(answer)
