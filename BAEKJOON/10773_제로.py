# 10773번
# https://www.acmicpc.net/problem/10773

k = int(input())
stack = []

for i in range(k):
    num = int(input())
    if len(stack) >= 1 and num == 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))
