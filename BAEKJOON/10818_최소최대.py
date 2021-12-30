# 최소, 최대
## https://www.acmicpc.net/problem/10818
### try 1 time

N = int(input()) # 정수의 개수 N
numbers = list(map(int,input().split())) # N개의 정수들

print(min(numbers),max(numbers),end=' ')
