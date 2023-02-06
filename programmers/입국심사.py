# 프로그래머스 lv 3
# 입국심사
# https://school.programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0
    start,end = min(times),max(times)*n
    
    while start<= end:
        people = 0
        mid = (start+end)//2
        
        for time in times:
            people += mid//time
            if people >= n:
                break
                
        if people >= n:
            answer = mid
            end = mid-1
        elif people < n:
            start = mid+1
    
    return answer
