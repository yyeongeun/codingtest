-- 프로그래머스 lv 3 저자 별 카테고리 별 매출액 집계하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/144856

SELECT A.AUTHOR_ID, AUTHOR_NAME, CATEGORY, SUM((SALES * PRICE)) AS TOTAL_SALES

FROM BOOK_SALES S
JOIN BOOK B ON S.BOOK_ID = B.BOOK_ID
JOIN AUTHOR A ON B.AUTHOR_ID = A.AUTHOR_ID

WHERE YEAR(S.SALES_DATE) = 2022 AND MONTH(S.SALES_DATE) = 1
GROUP BY CATEGORY, AUTHOR_ID
ORDER BY A.AUTHOR_ID, CATEGORY DESC
