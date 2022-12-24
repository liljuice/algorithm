n, m = map(int, input().split())
t = []
for _ in range(n):
  t.append(int(input()))

t.sort()
answer = 0
start = 0
end = t[0] * m  #최대 대기할 시간(최소 시간 심사대*인원)

while start <= end:
  mid = (start + end) // 2
  judged = 0
  
  for i in t:
    judged += mid // i
      
  if judged >= m:
    end = mid - 1
    answer = mid
  else:
    start = mid + 1


print(answer)
    
    
"""
시간 기준으로 몇명을 수용할 수 있을까?

7 10
1초 : 0 0 -> 0(start)
21초 : 3 2 -> 5명
26초 : 3 2 -> 5명
27초 : 3 2 -> 5명
28초 : 4 2 -> 6명
29초 : 4 2 -> 6명
32초 : 4 3 -> 7명
42초 : 6 4 -> 10명(end)
"""
