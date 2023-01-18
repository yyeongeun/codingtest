#2339번 석판 자르기 골드1
#https://www.acmicpc.net/problem/2339

def f(sx, sy, ex, ey, hv):
    noise = [] #불순물
    dia = 0 #보석결정체
    
    for i in range(sx, ex):
        for j in range(sy, ey):
            if stones[i][j] == 1:
                noise.append([i, j])
            elif stones[i][j] == 2:
                dia += 1

    if dia == 1 and len(noise) == 0: 
        return 1 #다이아만 한개 -> 한개로만 나뉨
    if dia == 0 or len(noise) == 0:
        return 0 #둘다 없으면 -> 나눌게 없음 0

    count = 0 #자르는 횟수

    if hv != 1:
        for nx, ny in noise: #불순물의 x,y 좌표
            can_cut = True #자를 수 있는 여부
            for i in range(sy, ey):
                if stones[nx][i] == 2: #불순물이 있는 x줄(nx)에 있는 y 중 다이아가 있는 경우 
                    can_cut = False
                    break #다이아 있는 줄은 자를 수 없기 때문
            if can_cut: #nx줄에 있는 y 중 다이아가 없는 경우
                count += (f(sx, sy, nx, ey, 1) * f(nx + 1, sy, ex, ey, 1)) 
                # ex를 nx로 업데이트해준다. sx를 nx+1로 업데이트해준다.
                # x는 검토를 완료했으니, hv를 1로 바꾸어 2가 아닌 밑의 if문을 검사해서 y줄을 검사해준다.
                # 총 count = 왼쪽 석판에서 나온 count * 오른쪽 석판에서 나온 count

    if hv != 2:
        for nx, ny in noise:
            can_cut = True
            for i in range(sx, ex):
                if stones[i][ny] == 2: #불순물이 있는 y줄(ny)에 있는 x 중 다이아가 있는 경우
                    can_cut = False
                    break
            if can_cut: #ny줄에 있는 x 중 다이아가 없는 경우
                count += (f(sx, sy, ex, ny, 2) * f(sx, ny + 1, ex, ey, 2))
                # ey를 ny로 업데이트해준다. sy를 ny+1로 업데이트해준다.

    return count


n = int(input())

stones = [list(map(int, input().split())) for _ in range(n)]

result = f(0, 0, n, n, 0)

print(result if result != 0 else -1)
