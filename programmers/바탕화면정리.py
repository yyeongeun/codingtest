# 프로그래머스 lv 1 바탕화면 정리
# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    x, y = [], []

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                x.append(j)
                y.append(i)
                
    return [min(y),min(x),max(y)+1,max(x)+1]
