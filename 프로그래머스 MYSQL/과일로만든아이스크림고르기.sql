-- 프로그래머스 lv 1 과일로 만든 아이스크림 고르기
-- https://school.programmers.co.kr/learn/courses/30/lessons/133025?language=mysql

SELECT A.FLAVOR
FROM FIRST_HALF A
INNER JOIN ICECREAM_INFO B
ON A.FLAVOR = B.FLAVOR
WHERE (A.TOTAL_ORDER > 3000) AND (B.INGREDIENT_TYPE LIKE 'fruit_based')
ORDER BY A.TOTAL_ORDER DESC;
