n = int(input())
meeting = []
for i in range(n):
  meeting.append(list(map(int, input().split())))

meeting = sorted(meeting, key=lambda x: (x[1], x[0]))

end = meeting[0][1]
count = 1
if n > 1:
  for i in range(1, n):
    if meeting[i][0] >= end:
      end = meeting[i][1]
      count += 1

print(count)
"""
회의 종료시간 기점으로 그리디(짧은걸로!)하게 개수를 구해본다. 

1) 1234 회의 끝 이후 가장 짧은것 (567...) -> 4회
2) 345 회의 -> 3회
3) 0123456 회의 -> 3회
...
-> 가장 최솟값?

+
종료시간 기준 정렬 이후 시작시간 기준으로도 정렬해준다.
이유)
2
11
01
이 경우 정렬되지 않으면 11 회의로 결과값이 1이 된다.
시작시간 정렬 시 01 -> 11 회의로 결과값이 2가 된다.
"""
