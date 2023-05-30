# 프로그래머스 lv 1 [1차] 다트 게임
# https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    # 해당 점수 마이너스
    score = []
    for i in range(1,len(dartResult)):
        d = dartResult[i]
        dd = dartResult[i-1]      
        
        # S D T 점수계산
        if d == 'S' and dd.isdigit():
            # 숫자가 10인 경우
            if dd == '0' and dartResult[i-2].isdigit(): 
                dd = 10  
            score.append(int(dd)**1)
        elif d == "D" and dd.isdigit():
            # 숫자가 10인 경우
            if dd == '0' and dartResult[i-2].isdigit(): 
                dd = 10  
            score.append(int(dd)**2)
        elif d == "T" and dd.isdigit():
            # 숫자가 10인 경우
            if dd == '0' and dartResult[i-2].isdigit(): 
                dd = 10  
            score.append(int(dd)**3)
        
        # 옵션 *, #
        elif d == "*":
            if len(score) == 1:
                score[0] *= 2
            elif len(score) >= 2:
                score[-1] *= 2
                score[-2] *= 2
        elif d == "#":
            score[-1] *= -1
            
    print(score)
    
    return sum(score)
