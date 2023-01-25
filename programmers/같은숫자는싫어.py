# 프로그래머스 lv 1
# 같은 숫자는 싫어
# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def soultion(arr):
  answer = []
  answer.append(arr[0])
  
  for num in arr[1:]:
    if arr[-1] != num:
      answer.append(num)
      
  return answer
