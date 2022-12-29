#1157번 단어 공부
#https://www.acmicpc.net/problem/1157

word = input().upper()
unique_word = list(set(word))
cnt_list = []

for i in range(unique_word):
  cnt = word.count(i)
  cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) >= 2:
  print("?")
else:
  max_index = cnt_list.index(max(cnt_list))
  print(unique_word[max_index])
