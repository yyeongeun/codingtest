#1193번
#https://www.acmicpc.net/problem/1193

X = int(input())
line = 0

while X > line:
  X -= line
  line += 1
  
if line%2 == 0:
  a = X
  b = line-X+1
else:
  a = line-X+1
  b = X
  
print(a,"/",b,sep='')
