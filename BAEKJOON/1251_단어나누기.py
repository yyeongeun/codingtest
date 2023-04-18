# 백준 1251번 단어 나누기
# https://www.acmicpc.net/problem/1251

word = list(input())
answer = []
tmp = []

for i in range(1,len(word)+1):
    for j in range(i+1,len(word)):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        tmp.append(a+b+c)

for a in tmp:
    answer.append(''.join(a))
    
print(sorted(answer)[0])
