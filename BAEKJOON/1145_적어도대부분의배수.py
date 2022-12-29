#1145번 적어도 대부분의 배수
#https://www.acmicpc.net/problem/1145

a = list(map(int,input().split()))
a_min = min(a)

while True:
  cnt = 0
  for i in range(5):
    if a_min % a[i] == 0:
      cnt += 1
  if cnt >= 3:
    print(a_min)
    break
  a_min += 1
