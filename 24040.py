"""
넓이 n, 가로폭을 다 합치면 3의 배수
즉, 가로x와 세로y를 곱한 값이 n일때 x+y가 3의 배수여야 한다.

x+y = 3a * 3a = sum 6a / 3a+1 * 3a+2 = sum 6a+3
n = 9a^2 / 9a^2+9a+2
"""
t = int(input())
for _ in range(t):
  n = int(input())
  if n % 9 == 0 or n%3==2:
    print("TAK")
  else:
    print("NIE")
