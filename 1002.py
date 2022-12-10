# 마린과의 거리를 반지름으로하고 각 터렛의 좌표를 중심으로 하는 원의 접점의 개수

import math
n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2) 
    if dist == 0 and r1 == r2 : #동심원
        print(-1)
    elif r1 + r2 == dist or abs(r1-r2) == dist: #외접 또는 내접
        print(1)
    elif abs(r1-r2) < dist < (r1+r2): #내접과 외접 사이...
        print(2)
    else:
        print(0) 
