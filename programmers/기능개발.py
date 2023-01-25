# 프로그래머스 lv 2
# 기능개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586

# 내 정답
import math
def solution(progresses, speeds):
  answer = []
  
  finishday = []
  for i in range(speeds):
    finishday.append(math.ceil((100-progresses[i])/speeds[i]))
    
  stack = []
  stack.append(finishday[0])
  
  for f in finishday[1:]:
    if f > max(stack):
      answer.append(len(stack))
      stack = []
    stack.append(f)
  answer.append(len(stack))


# 다른 사람의 풀이
def soultion(progresses, speeds):
  Q = []
  
  for p,s in zip(progresses,speeds):
    if len(Q) == 0 or Q[-1][0] < -((p-100)//s):
      Q.append([-((p-100)//s), 1]
    else:
      Q[-1][1] += 1
 
  return [q[1] for q in Q]
