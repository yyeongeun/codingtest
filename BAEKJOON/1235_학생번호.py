# 백준 1235번 학생 번호
# https://www.acmicpc.net/problem/1235

n = int(input())
num = []
for _ in range(n):
    num.append(str(input()))


for i in range(1,len(num[0])+1):
    answer = []
    for j in range(n):
        if num[j][-i:] in answer:
            break
        else:
            answer.append(num[j][-i:])
    if len(answer) == n:
        print(i)
        break
