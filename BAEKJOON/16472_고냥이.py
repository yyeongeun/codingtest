# 백준 16472번 고냥이
# 투포인터 알고리즘
# https://www.acmicpc.net/problem/16472
import sys
input = sys.stdin.readline

n = int(input()) # 번역기가 인식할 수 있는 알파벳 최대 개수
arr = list(input().rstrip()) # 문자열 알파벳 소문자

s = 0
e = 0
letters = []
letters.append(arr[s]) # 맨 앞 1개 인식하고 시작
dist = 0

while s < len(arr) and e < len(arr):
    dist = max(dist,e-s+1)
    if len(letters) <= n: # 인식할 수 있는 알파벳 개수라면
        e += 1 # 한 개 더 인식
        if e < len(arr) and arr[e] not in letters:
            letters.append(arr[e]) # 해당 알파벳 추가

    if len(letters) > n: # 인식할 수 없다면 리셋! 새롭게 시작
        s = s+1
        e = s
        letters = [arr[s]]
print(dist)
