# 프로그래머스 lv1 옹알이(2)
# https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling):
    count = 0
    baby = ["aya","ye","woo","ma"]
    
    for i in babbling:
        for j in baby:
            if j*2 not in i:
                i = i.replace(j," ")
        if i.strip() == "":
            count += 1
    
    return count
