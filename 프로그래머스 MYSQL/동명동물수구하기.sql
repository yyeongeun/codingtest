-- 프로그래머스 lv 2 동명 동물 수 찾기
-- https://school.programmers.co.kr/learn/courses/30/lessons/59041

SELECT NAME, COUNT(ANIMAL_ID) AS COUNT
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) > 1
ORDER BY NAME
