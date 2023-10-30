# 백준 2961번 도영이가 만든 맛있는 음식
# https://www.acmicpc.net/problem/2961

def recur(idx, sin, sun, use):
    global answer
    
    if idx == n:
        if use > 0 : # 재료 무조건 1개 이상 사용
            answer = min(answer, abs(sin - sun))
        return
    # 재료 사용 O
    recur(idx+1, sin*ingre[idx][0], sun+ingre[idx][1], use+1)
    # 재료 사용 X
    recur(idx+1, sin, sun, use)

n = int(input()) # 재료의 개수
ingre = [list(map(int,input().split())) for _ in range(n)]
answer = 1e9
recur(0,1,0,0) # 초기값 신맛=1, 쓴맛=0
print(answer)
