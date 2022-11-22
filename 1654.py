k, n = map(int, input().split())
lan = []
for _ in range(k):
  lan.append(int(input()))


def getLan(length):
  temp = 0
  for i in range(k):
    if length:
      temp += lan[i] // length
  return temp


def binSearch(count):
  start = 1
  end = max(lan)
  while start <= end:
    mid = (start + end) // 2
    iGot = getLan(mid)
    if iGot >= count:
      start = mid + 1
    else:
      end = mid - 1

  return end


print(binSearch(n))
"""
lan = [457 539 743 802]
start = 0, end = 802
mid = 402 -> 1 + 1 + 1 + 1 = 4 
원하는 랜선 갯수보다 적음 

start = 0, end = 401
mid = 200 -> 2 + 2 + 3 + 4 = 11
원하는 랜선 갯수와 같음!
"최대 길이"인지 확인이 필요함.

start = 201, end = 401
mid = 301 -> 1 + 1 + 2 + 2 
start = 201, end = 301
...
...
..
start = 201, end = 201 -> 10

mid = 201 -> 2 + 2 + 3 + 3 = 10
길이를 늘려 수가 바뀌는 지점을 찾자
"""
