#1259번
#https://www.acmicpc.net/problem/1259

# 보통 방식
# while True:
#   n = input()
#   if (n == '0'):
#     break
    
#   if n == n[::-1]:
#     answer = 'yes'
#   else:
#     answer = 'no'
#   print(answer)

#내 풀이과정(복잡)
yesno = []

while True:
  n = input()
  if (n == '0'):
    break
    
  answer = []
  for i in range(len(n)):
    if n[0+i] == n[-1-i]:
      answer.append('yes')
      
  if len(answer) == len(n):
    yesno.append('yes')
  else:
    yesno.append('no')
    
print('\n'.join(yesno))
