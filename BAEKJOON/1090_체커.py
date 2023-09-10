# https://www.acmicpc.net/problem/1090
# 백준 플레니텀4 100번 체커

n = int(input())
arr = []
x,y = [], []
answer = [-1]*n

for _ in range(n):
    a,b = map(int,input().split())
    arr.append([a,b])
    x.append(a)
    y.apend(b)

# 만날 수 있는 모든 경우의 수 = 모든 체커의 x좌표와 y좌표
for nx in x:
    for ny in y:
        # 각 체커와의 이동 횟수(거리)를 계산
        dist = []
        for ex,ey in arr:
            # x의 이동 횟수 + y의 이동 횟수
            d  = abs(ex - nx) + abs(ey - ny)
            dist.append(d)
        
        # 이동 횟수 적은 것부터 정렬
        dist.sort()
        tmp = 0
        for i in range(len(dist)):
            d = dist[i]
            tmp += d
            # 이동횟수가 작은 값부터 tmp에 더해주고, answer[i]에 입력한다.
            if answer[i] == -1:
                answer[i] = tmp
            else:
                # tmp = dist[0] + dist[1] + dist[2]
                # answer[1] = dist[0] + dist[1]
                # answer[i]는 최소 i+1개 이상의 체커와 같은 칸에 모인 경우이다.
                # # tmp와 answer[i]중 더 작은 값으로 업데이트한다.
                answer[i] = min(tmp,answer[i])
print(*answer)
