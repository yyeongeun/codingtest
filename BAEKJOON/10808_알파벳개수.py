# 10808번 알파벳개수
## https://www.acmicpc.net/problem/10808

n = input()
lst = [0]*26

for i in range(n):
    lst[ord(i)-97] += 1
for i in lst:
    print(i, end=' ')
