-- 프로그래머스 lv 3 조건에 맞는 사용자 정보 조회하기
-- https://school.programmers.co.kr/learn/courses/30/lessons/164670

SELECT USER_ID, NICKNAME, 
CONCAT(CITY," ",STREET_ADDRESS1," ",STREET_ADDRESS2) AS "전체주소", 
CONCAT(LEFT(TLNO,3),"-",SUBSTRING(TLNO,4,4),"-",RIGHT(TLNO,4)) AS "전화번호"

FROM USED_GOODS_BOARD AS A
JOIN USED_GOODS_USER AS B
ON A.WRITER_ID = B.USER_ID

GROUP BY USER_ID
HAVING COUNT(*) >= 3
ORDER BY USER_ID DESC;
