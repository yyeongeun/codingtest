# 프로그래머스 lv 1 직사각형 별찍기
# https://school.programmers.co.kr/learn/courses/30/lessons/12969

n,m = map(int,input().rstrip().split(' '))
for i in range(m):
    print("*"*n)
