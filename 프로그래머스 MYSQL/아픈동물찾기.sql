-- 프로그래머스 lv 1 아픈 동물 찾기
-- https://school.programmers.co.kr/learn/courses/30/lessons/59036#fn1

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
