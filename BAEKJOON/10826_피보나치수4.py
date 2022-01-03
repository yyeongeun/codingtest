# 10826번 피보나치 수 4
## 10870번 피보나치 수 5 관련 문제
## https://www.acmicpc.net/problem/10826
### try 1 time

n = int(input())

fibonacci = [0,1]
for i in range(2,n+1): # 범위 : 2부터 n까지
    data = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(data)
    
print(fibonacci[n])
