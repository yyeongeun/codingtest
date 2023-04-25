# 프로그래머스 lv 1 기사단원의 무기
# https://school.programmers.co.kr/learn/courses/30/lessons/136798

def solution(number, limit, power):
    # number 안의 약수 개수 = 공격력 무기
    num = []
    for i in range(1,number+1):
        cnt = 0
        for j in range(1,int(i**(1/2))+1):
            if i % j == 0:
                cnt += 1
                if j**2 != i:
                    cnt += 1
        num.append(cnt)
    
    answer = 0
    for i in range(len(num)): # 공격력이 limit 초과한 경우 power
        if num[i] > limit :
            num[i] = power
        answer += num[i]
            
    return answer
