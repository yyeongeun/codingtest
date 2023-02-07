# 프로그래머스 lv 4
# 징검다리
# https://school.programmers.co.kr/learn/courses/30/lessons/43236

def solution(distance, rocks, n):
    answer = 0
    start,end = 1,distance
    rocks.sort()
    
    while start <= end:
        mid = (start+end)//2
        del_stone = 0
        pre_stone = 0
        for rock in rocks:
            if rock-pre_stone < mid:
                del_stone += 1
            else:
                pre_stone = rock
            if del_stone > n:
                break
        if del_stone > n:
            end = mid-1
        else:
            answer = mid
            start = mid+1
            
    return answer
