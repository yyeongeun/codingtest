# 약수 구하기
## https://www.acmicpc.net/problem/2501

answer = []
N, k = list(map(int,input().split()))

for i in range(1,N+1):
    if N % i == 0:
        answer.append(i)

# answer.sort() -> 굳이 할 필요 없다.
if len(answer) < k:
    result = 0
else:
    result = answer[k-1]

print(result)
