# https://www.acmicpc.net/problem/1978
# 백준 1978번 소수 찾기

n = int(input())
nums = map(int, input().split())
answer = 0

for num in nums:
    cnt = 0
    if num > 1:
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:
                cnt += 1 # 소수 아닌 경우
        if cnt == 0: 
            answer += 1
print(answer)
