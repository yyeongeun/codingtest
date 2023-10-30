# 백준 2503번 숫자 야구
# 재귀함수로 풀기
# https://www.acmicpc.net/problem/2503

import sys
# 파이썬 천번정도 반복하면 멈추기 때문에, 더 돌리기
sys.setrecursionlimit(9999999) 

def checker(hint_idx,number):
    _number = hint[hint_idx][0]
    _strike = hint[hint_idx][1]
    _ball = hint[hint_idx][2]
    
    strike = 0
    ball = 0
    
    # 정답 백의자리, 십의자리, 일의자리
    _A = _number // 100
    _B = (_number - (_A*100)) // 10
    _C = _number % 10
    
    # 비교값 백의자리, 십의자리, 일의자리
    A = number // 100
    B = (number - (A*100)) // 10
    C = number % 10
    
    if A == 0 or B == 0 or C == 0: # 1부터 9까지의 숫자임
        return False
    if A == B or A == C or B == C: # 각 숫자는 겹치지 않음
        return False
    
    # 스트라이크 개수 세기
    if A == _A:
        strike += 1
    if B == _B:
        strike += 1
    if C == _C:
        strike += 1
    # 볼 개수 세기
    if A == _B or A == _C:
        ball += 1
    if B == _A or B == _C:
        ball += 1
    if C == _A or C == _B:
        ball += 1
        
    # 스트라이크, 볼 개수 맞다면, 힌트 모두 통과한 경우!
    if strike == _strike and ball == _ball:
        return True
    return False
        
def recur(hint_idx,number):
    global answer
    
    if hint_idx == n:
        answer += 1
        recur(0,number+1) #number 바꿔주고 다시 힌트 0부터 돌리기
        return
    if number == 1000: # 끝
        return
    
    # 만약에 힌트에 통과했다면(스트라이크, 볼 카운트가 동일하다면)
    if checker(hint_idx,number):
        # 같은 number에서 다른 힌트도 통과하는지 보기
        recur(hint_idx+1,number)
    # 만약에 힌트에 통과하지 않았다면,
    else:
        recur(0,number+1) #number 바꿔주고 다시 힌트 0부터 돌리기
        
n = int(input())
hint = [list(map(int,input().split())) for _ in range(n)]
answer = 0
recur(0,100)
print(answer)
