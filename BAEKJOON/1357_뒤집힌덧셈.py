# 1357번
# https://www.acmicpc.net/problem/1357

#내 정답
X,Y = input().split()

dev Rev(X):
  ans = 0
  x = 1
  for i in range(len(X)):
    xx = int(x[i])*x
    ans += xx
    x *= 10
  return ans

print(Rev(str(Rev(X)+Rev(Y))))

#보통 정답
X,Y = input().split()

def Rev(X):
  ans = int(X[::-1])
  return ans

print(Rev(str(Rev(X)+Rev(Y))))
