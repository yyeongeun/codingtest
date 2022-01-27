# 8958번 OX퀴즈
## https://www.acmicpc.net/problem/8958
### try 3 times

n = int(input())

for _ in range(n):
  ox_list = list(input())
  score = 0
  sum = 0
  
  for ox in ox_list:
    if ox == 'O':
      score += 1
      sum += score
    else:
      scroe = 0
      
  print(sum)
