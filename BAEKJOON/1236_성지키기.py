#1236번
#https://www.acmicpc.net/problem/1236

n,m = map(int,input().split())
array = []

for _ in range(n):
  array.append(input())
  
a,b = 0,0
for i in range(n):
  if "X" not in array[i]:
    a += 1
for j in range(m):
  if "X" not in [array[i][j] for i in range(n)]:
    b += 1
    
print(max(a,b))
