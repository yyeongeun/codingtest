# 백준 1138번 한 줄로 서기
# https://www.acmicpc.net/problem/1138

n = int(input()) #사람수
arr = list(map(int,input().split())) #왼쪽에 있는 자기보다 큰 사람수
answer = [0]*n #모두 비어있는 자리

for i in range(n):
    cnt = 0 #왼쪽에 있는 키 큰 사람 수
    for j in range(n):
        # 왼쪽에 있는 키 큰 사람수가 arr[i]와 같고, 현재 자리에 아무도 없다면
        if cnt == arr[i] and answer[j] == 0:
            answer[j] = i+1
            break
        elif answer[j] == 0:
            cnt += 1
            
print(" ".join(map(str,answer)))
