# 프로그래머스 lv 2
# 모음사전
# https://school.programmers.co.kr/learn/courses/30/lessons/84512
# 정답1
from itertools import product

def solution(word):
    words = []
    for i in range(1,6):
        for c in product(['A','E','I','O','U'],repeat=i):
            words.append(''.join(list(c)))
    words.sort()
    answer = words.index(word) + 1
    
    return answer


# 정답2
def solution(word):
    char = {'A':0,'E':1,'I':2,'O':3,'U':4}
    re = (((5+1)*5+1)*5+1)*5+1
    answer = len(word)
    
    for i in word:
        answer += re*char[i]
        re = (re-1)//5
    
    return answer
