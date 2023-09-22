# https://www.acmicpc.net/problem/1407
# 백준 1407번 2로 몇 번 나누어질까

A,B = map(int,input().split())

A -= 1
tmp_A = 0
# 1로 나누었을 때의 값 더해주기 175//1 = 175
tmp_A += A
# 2의 배수로 나누었을 때의 값 더해주기
for i in range(1,99):  
    tmp_A += (A//(2**i))*((2**i)-(2**(i-1)))

tmp_B = 0
tmp_B += B
for i in range(1,99):
    tmp_B += (B//(2**i))*((2**i)-(2**(i-1)))

print(tmp_B-tmp_A)
