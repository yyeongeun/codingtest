# 지능형 기차 2
## https://www.acmicpc.net/problem/2460
### try 1 time

num = 0 # 현재 기차에 있는 사람 수
result = [] # 정거장당 사람 수 리스트로 저장하기

for i in range(1,11):
    down, up = list(map(int,input().split()))
    num = num - down + up # 내리고 타기
    result.append(num)

result.sort()
print(result[-1]) # 가장 많았던 사람수
