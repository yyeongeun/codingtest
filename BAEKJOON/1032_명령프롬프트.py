#1032번 명령프롬프트
#https://www.acmicpc.net/problem/1032

n=int(input())
a=list(input())
a_len=len(a)
for i in range(n-1):
  b=list(input())
  for j in range(a_len):
    if a[j]!=b[j]:
      a[j]='?' 
print(''.join(a))
