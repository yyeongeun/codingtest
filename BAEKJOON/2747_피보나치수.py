# 2747번 피보나치 수
## 10870번 피보나치 수 5 관련 문제
## https://www.acmicpc.net/problem/2747
### try 1 time

n = int(input())

fibonacci = [0,1]
for i in range(2, n+2):
    data = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(data)

print(fibonacci[n])
