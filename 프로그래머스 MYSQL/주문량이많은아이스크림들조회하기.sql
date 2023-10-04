-- 프로그래머스 lv 4 주문량이 많은 아이스크림들 조회하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/133027?language=mysql

SELECT A.FLAVOR
FROM FIRST_HALF AS A
JOIN (SELECT FLAVOR, SUM(TOTAL_ORDER) AS TOTAL_ORDER
      FROM JULY
      GROUP BY FLAVOR
      ) AS B
ON A.FLAVOR = B.FLAVOR
ORDER BY (A.TOTAL_ORDER + B.TOTAL_ORDER) DESC
LIMIT 3;
