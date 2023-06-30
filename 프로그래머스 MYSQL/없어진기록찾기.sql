-- 프로그래머스 lv 3 없어진 기록 찾기
-- https://school.programmers.co.kr/learn/courses/30/lessons/59042

SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_INS AS I
RIGHT JOIN ANIMAL_OUTS AS O
ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE I.ANIMAL_ID IS NULL
ORDER BY O.ANIMAL_ID;
