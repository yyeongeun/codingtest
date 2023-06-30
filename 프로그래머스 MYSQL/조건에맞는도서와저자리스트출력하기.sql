-- 프로그래머스 lv 2 조건에 맞는 도서와 저자 리스트 출력하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/144854

SELECT BOOK_ID, AUTHOR_NAME, DATE_FORMAT(PUBLISHED_DATE,"%Y-%m-%d") AS PUBLISED_DATE
FROM BOOK AS B
JOIN AUTHOR AS A
ON B.AUTHOR_ID = A.AUTHOR_ID
WHERE CATEGORY = "경제"
ORDER BY PUBLISHED_DATE;
