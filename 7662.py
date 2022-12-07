import heapq as hq

t = int(input())
for _ in range(t):
  k = int(input())
  maxhq = []
  minhq = []
  avail = [True] * k
  for i in range(k):
    com, num = input().split()
    num = int(num)

    if com == 'I':
      hq.heappush(maxhq, (-1 * num, i))
      hq.heappush(minhq, (num, i))

    elif com == 'D':
      if num == -1:
        while minhq and not avail[minhq[0][1]]: #비활성 노드는 전부 pop
          hq.heappop(minhq)
        if minhq:
          val, k = hq.heappop(minhq)
          avail[k] = False
      elif num == 1:
        while maxhq and not avail[maxhq[0][1]]:
          hq.heappop(maxhq)
        if maxhq:
          val, k = hq.heappop(maxhq)
          avail[k] = False
  result = []
  for data in minhq:
    if avail[data[1]] == True:
      result.append(data[0])

  if result:
    print(max(result), min(result))
  else:
    print("EMPTY")
