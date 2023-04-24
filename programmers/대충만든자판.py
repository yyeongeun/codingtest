# 프로그래머스 lv 1 대충 만든 자판
# https://school.programmers.co.kr/learn/courses/30/lessons/160586

def check(keylist, character):
    return keylist.index(character)+1

def solution(keymap, targets):
    answer = []
    
    for target in targets:
        tmp_list = []
        
        for idx in range(len(target)):
            character = target[idx]
            cur = 101
            for keylist in keymap:
                if character in set(keylist):
                    cur = min(cur, check(keylist,character))
            tmp_list.append(cur)

        if 101 in tmp_list:
            answer.append(-1)
        else:
            answer.append(sum(tmp_list))

    return answer
