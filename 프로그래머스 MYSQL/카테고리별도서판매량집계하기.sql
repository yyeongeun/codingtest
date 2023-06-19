-- 프로그래머스 lv 3 카테고리 별 도서 판매량 집계하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/144855

SELECT B.CATEGORY, SUM(S.SALES) AS TOTAL_SALES
FROM BOOK_SALES AS S
JOIN BOOK AS B
ON S.BOOK_ID = B.BOOK_ID
WHERE S.SALES_DATE LIKE "2022-01%"
GROUP BY B.CATEGORY
ORDER BY B.CATEGORY;
