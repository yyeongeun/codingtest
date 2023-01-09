#1356번
#https://www.acmicpc.net/problem/1356

N = int(input())
yes = 0

for i in range(1, len(N)):
  left = N[:i]
  right = N[i:]
  L = R = 1
  for j in left:
    L *= int(j)
  for k in right:
    R *= int(k)
  if L == R :
    yes = 1
    print("YES")
    break
    
if yes == 0:
  print("NO")
  
