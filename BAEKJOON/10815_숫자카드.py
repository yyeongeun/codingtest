# 백준 10815번 숫자 카드
# 이분 탐색 알고리즘
# https://www.acmicpc.net/problem/10815

import sys
input = sys.stdin.readline

n = int(input()) # 숫자카드 개수
arr_n = sorted(list(map(int,input().split()))) # 숫자카드
m = int(input()) # 구해야할 정수
arr_m = list(map(int,input().split()))

for num in arr_m:
    s = 0
    e = n-1
    flag = False
    
    while s <= e: # 교차되지 않았다면
        mid = (s+e)//2
        if arr_n[mid] == num : # answer
            flag = True
            break
        elif arr_n[mid] > num : # up
            e = mid-1            
        else: # down
            s = mid+1
    if flag:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
