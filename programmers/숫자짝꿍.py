# 프로그래머스 lv1 숫자 짝꿍
# https://school.programmers.co.kr/learn/courses/30/lessons/131128#

def solution(X,Y):
    answer = ''
    for i in range(9,-1,-1):
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))
    if answer == '':
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else:
        return answer
