# 프로그래머스 lv 1 [1차] 비밀지도
# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    new1 = []
    new2 = []
    
    # bin 함수로 이진법으로 바꾸기
    for i in range(n):
        # 앞의 '0b' 없애주기 [2:]
        new1.append(bin(arr1[i])[2:])
        new2.append(bin(arr2[i])[2:])
        # 0으로 길이 n개 채워주기
        new1[i] = ('0'*(n-len(new1[i]))) + new1[i]
        new2[i] = ('0'*(n-len(new2[i]))) + new2[i]

    # 암호 해독
    answer = []
    for i in range(n):
        c = ''
        for j in range(n):
            if new1[i][j] == '0' and new2[i][j] == '0':
                c += ' '
            elif new1[i][j] == '1' or new2[i][j] == '1':
                c += '#'
        answer.append(c)

    return answer
